---
name: connector-lark-sheets
description: "Data connector for 飞书表格 (Lark Sheets). Fetches operational data from Feishu spreadsheets for product-ops workflows."
---

# 飞书表格 Data Connector

Fetches product operations data from 飞书多维表格 or 电子表格.

## Prerequisites

- `/lark-sheets` skill installed in Claude Code
- Feishu app with Sheets permission enabled
- A spreadsheet with weekly/daily operational data

## Setup

1. Create a 飞书表格 with this recommended layout:

```
| 日期       | DAU   | 新增用户 | D7留存 | 收入    | 转化率 | 崩溃率 |
|-----------|-------|---------|--------|--------|-------|--------|
| 2026-06-22| 12500 | 2450    | 25.3%  | 84000  | 12.5% | 0.05%  |
| 2026-06-21| 12400 | 2380    | 25.8%  | 83500  | 12.3% | 0.04%  |
| ...       | ...   | ...     | ...    | ...    | ...   | ...    |
```

2. Copy the spreadsheet URL

3. In `product-ops`, run setup:
```
/product-ops 配置
```
When asked "数据在哪看？", paste the spreadsheet URL.

## How It Works

1. `product-ops` skill reads `context.json` → `metrics.data_sources.sheets_url`
2. When a workflow needs data (e.g., weekly report), the skill:
   a. Calls `/lark-sheets` to read the spreadsheet
   b. Finds the column that matches each metric key
   c. Extracts current period and previous period values
   d. Calculates period-over-period changes
   e. Returns a DataResponse
3. The skill injects real values into the report

## Column Name Mapping

The connector auto-detects columns by these keywords (case-insensitive, supports Chinese and English):

| Metric Key | Recognized Column Names |
|-----------|------------------------|
| `dau` | DAU, 日活, 日活跃, Daily Active, 活跃用户 |
| `new_users` | 新增, New Users, 新用户, 新增用户 |
| `retention_d7` | D7, 7日留存, 次日留存7, Day7, 七天留存, D7留存 |
| `retention_d30` | D30, 30日留存, Day30, 三十天留存, D30留存 |
| `revenue` | 收入, Revenue, 营收, GMV, 流水, MRR |
| `conversion` | 转化, Conversion, 转化率, CVR |
| `crash_rate` | 崩溃, Crash, 闪退, 崩溃率 |
| `pay_rate` | 付费率, Pay Rate, 付费转化 |
| `arpu` | ARPU, 人均收入, 客单价 |
| `churn` | 流失, Churn, 流失率 |

If a column name doesn't match any known pattern, the connector will ask: "飞书表格中的「{column name}」列对应哪个指标？"

## Error Handling

- **Sheet not found** → Show the configured URL; let user verify it's correct
- **Column not found** → Show available columns; ask user to map or add the column
- **No data for this period** → Show the date range found in the sheet; ask user to update
- **Permission error** → Remind user to authorize the Lark Sheets app

## Usage Example

```
User: 本周周报
product-ops:
  → Connector reads 飞书表格「运营数据看板」
  → Finds columns: DAU, 新增用户, D7留存, 收入, 转化率
  → Extracts week 2026-06-22 to 2026-06-28
  → Calculates changes vs week 2026-06-15 to 2026-06-21
  → Returns DataResponse with real values
  → Report generated with actual numbers
```
