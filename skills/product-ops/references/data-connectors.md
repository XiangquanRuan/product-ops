# Data Connectors / 数据连接器

Standard interface for fetching operational data from any platform. The skill defines **what data it needs**; connectors handle **how to get it**.

## Language

Check for `[Language: 中文]` or `[Language: English]` in context. Default to 中文 if user writes in Chinese.

---

## Architecture

```
┌─────────────────────────────────────────────────┐
│                 product-ops skill                │
│                                                 │
│  Workflow needs data (e.g., weekly-report)      │
│       │                                         │
│       │ Step A: Check context.json              │
│       │   → tools.analytics                     │
│       │   → metrics.data_sources                │
│       │                                         │
│       │ Step B: Determine connector path        │
│       ▼                                         │
│  ┌──────────┬──────────┬──────────┬──────────┐ │
│  │  manual  │  lark-   │  csv/    │ custom   │ │
│  │          │  sheets  │  pandas  │ MCP      │ │
│  └────┬─────┴────┬─────┴────┬─────┴────┬─────┘ │
│       │          │          │          │       │
│       ▼          ▼          ▼          ▼       │
│  Standardized DataResponse → inject into output │
└─────────────────────────────────────────────────┘
```

---

## Standard Data Formats

### DataRequest (skill → connector)

What the skill asks for:

```json
{
  "workflow": "weekly-report | daily-brief | monthly-review | funnel-analysis | experiment-review | custom",
  "period": {
    "type": "range | last_n_days | this_week | this_month | last_month",
    "start": "2026-06-22",
    "end": "2026-06-28"
  },
  "metrics": [
    {
      "key": "dau",
      "label": "日活跃用户数",
      "required": true
    },
    {
      "key": "new_users",
      "label": "新增用户",
      "required": true
    },
    {
      "key": "retention_d7",
      "label": "D7 留存率",
      "required": true
    },
    {
      "key": "revenue",
      "label": "收入",
      "required": false
    },
    {
      "key": "conversion",
      "label": "核心转化率",
      "required": true
    },
    {
      "key": "crash_rate",
      "label": "崩溃率",
      "required": false
    }
  ],
  "filters": {
    "platform": "web | ios | android | all",
    "segment": "string | null",
    "version": "string | null"
  },
  "context_hints": {
    "analytics_tool": "amplitude | mixpanel | shenCe | lark-sheets | googleAnalytics | csv | manual | other",
    "sheets_url": "string | null",
    "dashboard_url": "string | null"
  }
}
```

### DataResponse (connector → skill)

What the connector returns:

```json
{
  "status": "ok | partial | failed",
  "source": "lark-sheets | csv-file | manual-input | amplitude-api | ...",
  "source_detail": "飞书表格「运营看板」/ 工作表「周报数据」",
  "period": {
    "start": "2026-06-22",
    "end": "2026-06-28"
  },
  "fetched_at": "2026-06-28T09:00:00+08:00",
  "metrics": {
    "dau": {
      "value": 12500,
      "previous_value": 12100,
      "change_pct": 3.3,
      "unit": "users",
      "status": "ok"
    },
    "new_users": {
      "value": 2450,
      "previous_value": 2300,
      "change_pct": 6.5,
      "unit": "users",
      "status": "ok"
    },
    "retention_d7": {
      "value": 25.3,
      "previous_value": 26.1,
      "change_pct": -3.1,
      "unit": "%",
      "status": "ok"
    },
    "revenue": {
      "value": null,
      "previous_value": null,
      "change_pct": null,
      "unit": "CNY",
      "status": "not_available",
      "note": "未配置飞书表格中的收入列"
    }
  },
  "anomalies": [
    {
      "metric": "retention_d7",
      "severity": "warning",
      "note": "较上周下降 0.8pp，低于近5周均值 27.1%"
    }
  ],
  "warnings": [
    "revenue 数据不可用：飞书表格中未找到对应列"
  ]
}
```

---

## Built-in Connector Paths

### Path 1: `manual` — 手动输入（永远可用的兜底方案）

Always available. No setup needed.

**What the skill does**:
1. Generate a fill-in form with all required metrics
2. User pastes numbers (from any source)
3. Parse and validate
4. Return DataResponse

**User experience**:
```
📊 请提供本周数据（直接粘贴数字即可）：

DAU: ______ (上周: ______)
新增用户: ______ (上周: ______)
D7 留存率: ______% (上周: ______%)
收入: ______ (上周: ______)
崩溃率: ______%

或直接说「跳过」使用占位符。
```

### Path 2: `lark-sheets` — 飞书表格自动读取

Uses the installed `/lark-sheets` skill.

**Prerequisites**:
- `/lark-sheets` skill installed
- User has configured `metrics.data_sources.sheets_url` in context.json

**What the skill does**:
1. Read context.json → get `metrics.data_sources.sheets_url`
2. Call `/lark-sheets` to read the spreadsheet
3. Map spreadsheet columns to metric keys using definitions from context
4. Calculate period-over-period changes
5. Return DataResponse

**Spreadsheet convention** (recommended layout):
```
| 日期       | DAU   | 新增用户 | D7留存 | 收入    | 转化率 |
|-----------|-------|---------|--------|--------|-------|
| 2026-06-22| 12500 | 2450    | 25.3%  | 84000  | 12.5% |
| 2026-06-21| 12400 | 2380    | 25.8%  | 83500  | 12.3% |
```

### Path 3: `csv-pandas` — CSV/Excel 文件处理

Uses the installed `/pandas-data-analysis` skill.

**Prerequisites**:
- `/pandas-data-analysis` skill installed
- User provides CSV/Excel file

**What the skill does**:
1. Ask user to provide file path or drag-drop
2. Call `/pandas-data-analysis` to read and process
3. Map columns to metrics
4. Calculate changes
5. Return DataResponse

---

## Connector Decision Flow

```
DataRequest generated
        │
        ▼
Check context.json tools.analytics:
        │
        ├─ "lark-sheets" + sheets_url set → Try Path 2 (lark-sheets)
        │   └─ fails? → Fall back to Path 1 (manual)
        │
        ├─ "amplitude" / "mixpanel" / "shenCe" / "googleAnalytics"
        │   └─ No built-in connector exists → 
        │       Tell user: "📊 {tool} 暂不支持自动读取。请将数据导出为 CSV 后在对话中提供，或手动粘贴数字。"
        │       → Fall back to Path 3 or Path 1
        │
        └─ null / "manual" → Path 1 (manual)
```

**Important rule**: Never block on data. If auto-fetch fails, always fall back to manual input. Show what failed and why.

---

## Metrics Key Registry

Standard metric keys used across all workflows. Connectors should map their data source columns to these keys.

| Key | Label (zh) | Label (en) | Unit | Used In |
|-----|-----------|------------|------|---------|
| `dau` | 日活跃用户数 | DAU | users | daily, weekly, monthly |
| `mau` | 月活跃用户数 | MAU | users | monthly |
| `new_users` | 新增用户 | New Users | users | daily, weekly, monthly |
| `retention_d1` | D1 留存率 | D1 Retention | % | daily |
| `retention_d7` | D7 留存率 | D7 Retention | % | weekly, monthly |
| `retention_d30` | D30 留存率 | D30 Retention | % | monthly |
| `revenue` | 收入 | Revenue | varies | daily, weekly, monthly |
| `conversion` | 核心转化率 | Core Conversion | % | daily, weekly, monthly |
| `crash_rate` | 崩溃率 | Crash Rate | % | daily, weekly |
| `pay_rate` | 付费率 | Pay Rate | % | weekly, monthly |
| `arpu` | 人均收入 | ARPU | varies | weekly, monthly |
| `cac` | 获客成本 | CAC | varies | monthly |
| `ltv` | 用户生命周期价值 | LTV | varies | monthly |
| `churn` | 流失率 | Churn Rate | % | monthly |
| `nps` | 净推荐值 | NPS | score | monthly |
| `csat` | 客户满意度 | CSAT | score | monthly |
| `engagement` | 参与度 | Engagement | varies | weekly |

---

## How Data Flows Into Output

Once the DataResponse is obtained, the workflow injects values into the report template:

```
Before (v0.2):                      After (v0.3 with connector):
                               
| DAU | {填写} | {填写} |       | DAU | 12,500 | 12,100 | +3.3% |
                               
📈 关键趋势:                       📈 关键趋势:
(空白，等用户填)                   • DAU 连续第3周增长，本周 +3.3%
                                • D7 留存率 25.3%，低于5周均值 27.1% ⚠️
                                • 数据来源: 飞书表格「运营看板」
```

---

## Adding a New Connector (Community)

To add a connector for a new platform (e.g., Amplitude, Mixpanel, 神策):

### Option A: Skill-Based Connector
Create a file at `connectors/{platform-name}/SKILL.md` with:
1. How to authenticate
2. How to map the platform's data model to standard metric keys
3. How to call the platform's API

### Option B: MCP-Based Connector
Create an MCP server configuration at `connectors/{platform-name}/mcp.json`

### Option C: Script-Based Connector
Create a Python/Node script at `connectors/{platform-name}/fetch.py`

See `connectors/CONTRIBUTING.md` for detailed instructions.

---

## Per-Workflow Data Requirements

### daily-brief
```
Required: dau, new_users, revenue, crash_rate
Optional: retention_d1, conversion
Period: yesterday (single day)
```

### weekly-report
```
Required: dau, new_users, retention_d7, conversion, revenue
Optional: crash_rate, pay_rate, arpu, nps
Period: this week (Monday–Sunday)
```

### monthly-review
```
Required: mau, new_users, retention_d7, retention_d30, revenue, pay_rate, churn
Optional: arpu, ltv, cac, nps, csat
Period: this month (1st–last day)
```

### funnel-analysis
```
Required: conversion (each stage)
Optional: all session metrics
Period: user-specified range
```

### experiment-review
```
Required: conversion (control), conversion (variant)
Optional: all guardrail metrics
Period: experiment duration
```
