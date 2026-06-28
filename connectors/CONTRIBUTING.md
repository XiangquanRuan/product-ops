# Contributing a Data Connector

A data connector tells `product-ops` how to fetch operational data from a specific platform. This document explains how to build one.

---

## What a Connector Does

```
DataRequest (standard format) → [Your Connector] → DataResponse (standard format)
```

The skill defines what data it needs. Your connector handles **how to get it** from one specific platform.

---

## Quick Start: 3 Files to Create

```
connectors/{platform-name}/
├── SKILL.md          # Required: How to use this connector
├── fetch.py          # Optional: Script to call API / parse files
└── README.md         # Optional: Platform setup instructions for users
```

## Step 1: Fork and Create

```bash
git checkout -b connector-{platform-name}
mkdir -p connectors/{platform-name}
```

## Step 2: Write SKILL.md

Use this template:

```markdown
---
name: connector-{platform-name}
description: "Data connector for {Platform Name}. Fetches operational data (DAU, revenue, retention, etc.) for product-ops workflows."
---

# {Platform Name} Data Connector

Fetches product operations data from {Platform Name}.

## Prerequisites

- {Account type needed}
- {API key / OAuth / token setup}
- {Any specific permissions}

## Setup

1. {Step 1}
2. {Step 2}

## Data Mapping

Map {Platform Name}'s data model to standard `product-ops` metric keys:

| {Platform} Field | Standard Metric Key | Notes |
|------------------|-------------------|-------|
| {field name} | `dau` | {mapping notes} |
| {field name} | `new_users` | {mapping notes} |
| {field name} | `retention_d7` | {mapping notes} |
| {field name} | `revenue` | {mapping notes} |

## Usage

In `product-ops`, set `context.json`:
```json
{
  "metrics": {
    "data_sources": {
      "analytics_tool": "{platform-slug}",
      "sheets_url": "{your data URL or resource ID}"
    }
  }
}
```

Then any workflow that needs data will use this connector.

## Implementation

{Describe how the connector works:
- API calls? Which endpoints?
- File parsing? What format?
- How to handle auth?
- How to handle errors / missing data?}

## Standard DataResponse Format

Your connector must return data in the DataResponse format defined in `skills/product-ops/references/data-connectors.md`. Key fields:

```json
{
  "status": "ok | partial | failed",
  "source": "{platform-slug}",
  "source_detail": "{human-readable source description}",
  "metrics": {
    "dau": {
      "value": 12500,
      "previous_value": 12100,
      "change_pct": 3.3,
      "unit": "users",
      "status": "ok | not_available"
    }
    // ... all requested metrics
  },
  "anomalies": [],
  "warnings": []
}
```

## Error Handling

- If auth fails → `status: "failed"`, tell the user to re-authenticate
- If a specific metric is unavailable → set `status: "not_available"` for that metric only, `status: "partial"` overall
- Never throw errors that block the workflow — always return a best-effort DataResponse

## Testing

Test your connector against the `weekly-report` workflow:
```bash
/product-ops 生成周报
```

Verify:
- [ ] Data is fetched from {Platform Name}
- [ ] Metrics are correctly mapped to standard keys
- [ ] Previous period values are correctly computed
- [ ] Missing metrics don't break the report
- [ ] Anomalies are detected when values deviate >10%
```

## Step 3: Submit a Pull Request

1. Push your connector branch
2. Create a PR against `main`
3. In the PR description, include:
   - What platform does this connect?
   - What data can it fetch?
   - Setup instructions for users
   - A screenshot of a successful weekly report using this connector

---

## Connector Design Guidelines

- **One platform per connector** — Don't bundle multiple platforms
- **Best-effort always** — Return partial data rather than failing completely
- **No secrets in code** — Use environment variables or context.json for tokens
- **Document the mapping** — Users need to understand how their data maps to standard keys
- **Handle rate limits** — If the API rate-limits, tell the user rather than retrying silently
- **Fall back gracefully** — If the connector fails, the skill always falls back to manual input
