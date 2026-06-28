---
name: connector-http-api
description: "Generic HTTP API data connector. Fetches operational data from any REST API by configuring endpoint URLs, auth, and JSON field mappings. Use when connecting product-ops to Amplitude, Mixpanel, 神策, GrowingIO, or custom analytics backends."
---

# HTTP API Data Connector

A universal connector that fetches operational data from **any REST API**. Configure once, then all `product-ops` workflows can auto-pull data.

## Prerequisites

- The target platform exposes a REST API
- You have an API key, token, or credentials
- The API returns JSON

## Setup

### Step 1: Create a Connector Config

In `~/.product-ops/projects/{slug}/connectors/http-api.json`:

```json
{
  "name": "my-analytics",
  "base_url": "https://api.amplitude.com/3",
  "auth": {
    "type": "basic | bearer | header | query",
    "key": "YOUR_API_KEY",
    "secret": "YOUR_SECRET_KEY (basic auth only)",
    "header_name": "Authorization (header auth only)",
    "query_param": "api_key (query auth only)"
  },
  "endpoints": {
    "metrics": {
      "method": "GET | POST",
      "path": "/api/v2/projects/{project_id}/metrics",
      "body_template": {
        "start": "{{start_date}}",
        "end": "{{end_date}}"
      }
    }
  },
  "field_mapping": {
    "dau": {
      "jsonpath": "data.metrics.active_users",
      "type": "number",
      "transform": "none | divide_by_100 | multiply_by_1000"
    },
    "new_users": {
      "jsonpath": "data.metrics.new_users",
      "type": "number"
    },
    "retention_d7": {
      "jsonpath": "data.metrics.retention.day7",
      "type": "percentage"
    },
    "revenue": {
      "jsonpath": "data.metrics.revenue.total",
      "type": "number"
    },
    "conversion": {
      "jsonpath": "data.metrics.conversion_rate",
      "type": "percentage"
    }
  },
  "previous_period": {
    "strategy": "second_api_call | single_response_contains_both",
    "offset_days": 7
  }
}
```

### Step 2: Test the Connection

```bash
python connectors/http-api/scripts/fetch.py \
  --config ~/.product-ops/projects/myapp/connectors/http-api.json \
  --workflow weekly-report \
  --start 2026-06-22 \
  --end 2026-06-28
```

Expected output: a valid DataResponse JSON.

### Step 3: Set in Context

Update `context.json`:
```json
{
  "metrics": {
    "data_sources": {
      "analytics_tool": "http-api",
      "connector_config": "~/.product-ops/projects/myapp/connectors/http-api.json"
    }
  }
}
```

Now `product-ops` will use this connector automatically.

---

## Field Mapping Reference

### jsonpath

Dot-notation path to the metric value in the API response JSON.

Examples:
- `data.metrics.dau` → `{"data": {"metrics": {"dau": 12500}}}`
- `results[0].values.active` → `{"results": [{"values": {"active": 12500}}]}`
- `metrics.retention.day7` → `{"metrics": {"retention": {"day7": 0.253}}}`

### type

How to interpret the raw value:
- `number` — integer or float, used as-is
- `percentage` — if value is 25.3, treated as 25.3%; if value is 0.253, use `transform: multiply_by_100`
- `currency` — number, unit from context

### transform

Optional post-processing:
- `none` — no transform
- `divide_by_100` — for percentage values stored as 0-100
- `multiply_by_100` — for decimal values (0.253 → 25.3)
- `multiply_by_1000` — for k-unit values

---

## Supported Auth Methods

| Type | Use For | Config Fields |
|------|---------|--------------|
| `bearer` | Most modern APIs | `key` (the token) |
| `basic` | Older APIs | `key` (username), `secret` (password) |
| `header` | Custom header auth | `header_name`, `key` |
| `query` | API key in URL | `query_param`, `key` |

**Security**: Never commit the config file. It's stored in `~/.product-ops/`, which is `.gitignore`'d.

---

## Platform-Specific Examples

### Amplitude

```json
{
  "base_url": "https://amplitude.com/api/3",
  "auth": {"type": "basic", "key": "YOUR_API_KEY", "secret": "YOUR_SECRET_KEY"},
  "endpoints": {
    "metrics": {
      "method": "GET",
      "path": "/charts/daily_active_users"
    }
  },
  "field_mapping": {
    "dau": {"jsonpath": "data.series[0]", "type": "number"}
  }
}
```

### 神策 (Sensors Analytics)

```json
{
  "base_url": "https://YOUR_INSTANCE.sensorsdata.cn",
  "auth": {"type": "bearer", "key": "YOUR_API_TOKEN"},
  "endpoints": {
    "metrics": {
      "method": "POST",
      "path": "/api/v2/analysis/event",
      "body_template": {
        "measures": [{"event_name": "$pageview", "aggregator": "COUNT"}],
        "unit": "day",
        "start_date": "{{start_date}}",
        "end_date": "{{end_date}}"
      }
    }
  },
  "field_mapping": {
    "dau": {"jsonpath": "rows[0].value", "type": "number"}
  }
}
```

### GrowingIO

```json
{
  "base_url": "https://www.growingio.com/api",
  "auth": {"type": "header", "header_name": "X-API-Key", "key": "YOUR_API_KEY"},
  "endpoints": {
    "metrics": {
      "method": "POST",
      "path": "/v2/projects/{project_id}/analytics",
      "body_template": {
        "metrics": ["active_users", "new_users", "revenue"],
        "date_range": ["{{start_date}}", "{{end_date}}"]
      }
    }
  }
}
```

---

## Error Handling

| Error | Behavior |
|-------|----------|
| Auth failed (401/403) | Show: "API 认证失败。请检查 http-api.json 中的 API key。" |
| Rate limited (429) | Show: "API 请求被限流。请稍后重试或降低请求频率。" |
| Network error | Fall back to manual input |
| Field not found in response | Mark metric as `not_available`, show which jsonpath failed |
| Response not valid JSON | Show raw response snippet, suggest checking endpoint config |

---

## Usage Example

```
User: 本周周报
product-ops:
  → context.json says analytics_tool = "http-api"
  → Loads connector config from http-api.json
  → Calls scripts/fetch.py with workflow=weekly-report, dates=2026-06-22/2026-06-28
  → Script calls Amplitude API, maps response fields via jsonpath
  → Returns DataResponse with real DAU, retention, revenue values
  → Report generated with live data
```

## Script

The Python implementation is at `connectors/http-api/scripts/fetch.py`.
