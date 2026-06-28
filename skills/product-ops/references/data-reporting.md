# Data Analysis & Reporting / 数据分析与报表

Data analysis and reporting workflows for product operations: KPI dashboards, funnel analysis, cohort analysis, anomaly detection, and report generation.

## Language

Check for `[Language: 中文]` or `[Language: English]` in context. Default to 中文 if user writes in Chinese.

---

## 1. KPI Dashboard Design / KPI看板设计

Help the user define what to track, how to visualize, and how to set up monitoring.

### Step 1: Identify the Product's North Star

Ask the user:
- What is the one metric that best captures the value users get from your product?
- Examples: DAU (social), GMV (ecommerce), messages sent (messaging), tasks completed (productivity)

### Step 2: Design the KPI Hierarchy

```
Level 1: North Star Metric (北极星指标)
    ├── Level 2: Input Metrics (驱动指标)
    │   ├── Acquisition: new users, CAC, channel mix
    │   ├── Activation: % users reaching "aha moment"
    │   ├── Engagement: DAU/MAU, session length, feature depth
    │   ├── Retention: D1/D7/D30 retention
    │   ├── Revenue: ARPU, LTV, conversion rate
    │   └── Referral: viral coefficient, invite send rate
    └── Level 3: Operational Metrics (运营指标)
        ├── Content: posts published, CTR, engagement rate
        ├── Support: ticket volume, CSAT, resolution time
        └── Quality: crash rate, load time, error rate
```

### Step 3: Build the Dashboard

For each metric, define:
- **Definition**: How is it calculated?
- **Source**: Where does the data come from? (database, analytics tool, sheets)
- **Frequency**: How often is it updated? (realtime, hourly, daily)
- **Target**: What's the goal/threshold?
- **Alert**: At what value should someone be notified?

### Output Format

```
📊 KPI Dashboard — {Product Name}

🎯 北极星指标 North Star:
• {metric name}: {current value} | Target: {target} | Status: 🟢🟡🔴

📈 增长指标 Growth:
• 新增用户 New Users: {value} | Target: {target}
• 获客成本 CAC: {value} | Benchmark: {benchmark}
• 激活率 Activation: {value}% | Target: {target}%

👥 参与度 Engagement:
• DAU: {value} | WoW: {change}%
• DAU/MAU: {value}% | Industry avg: {benchmark}%
• 人均使用时长 Avg Session: {value} min

🔄 留存 Retention:
• D1: {value}% | D7: {value}% | D30: {value}%

💰 收入 Revenue:
• 总收入 Total: {value} | Target: {target}
• ARPU: {value} | LTV: {value}
• 付费转化率 Pay Conversion: {value}%

🛡 质量 Quality:
• 崩溃率 Crash Rate: {value}% | Threshold: {threshold}%
• P99 加载时间: {value}ms | Threshold: {threshold}ms
```

---

## 2. Funnel Analysis / 漏斗分析

Step-by-step conversion analysis to identify where users drop off.

### Workflow

1. **Define the funnel stages** with the user
2. **Get the data** (user provides numbers, or pull from tools)
3. **Calculate drop-off rates** between each stage
4. **Identify the biggest leak** — where's the largest absolute and relative drop?
5. **Suggest diagnosis** — route to `/money-diagnose` for deep root cause

### Common Funnels by Product Type

**Acquisition Funnel**:
```
Impression → Click → Landing Page → Sign Up → Onboarding → Activated
```

**Purchase Funnel (E-commerce)**:
```
Visit → Product View → Add to Cart → Checkout → Purchase
```

**Content Funnel**:
```
Impressions → Click → Read (50%) → Read (100%) → Share/Save → Subscribe
```

### Output Format

```
🔍 漏斗分析 Funnel Analysis — {Funnel Name}

| 阶段 Stage | 用户数 Users | 阶段转化 Step Conv. | 总体转化 Overall |
|-----------|-------------|-------------------|----------------|
| {stage 1} | {n} | — | 100% |
| {stage 2} | {n} | {step%}% | {overall%}% |
| {stage 3} | {n} | {step%}% | {overall%}% |
| {stage 4} | {n} | {step%}% | {overall%}% |

🚨 最大流失点 Biggest Drop-off:
• {stage A} → {stage B}: {loss%}% 用户流失 (lost {n} users)
• 可能原因 Likely Causes: {suggestions}
• 建议动作 Recommended: {actions}

📊 与上周对比 vs Last Week:
• 整体转化 Overall: {current}% → {previous}% ({change}pp)
• 最大改善 Most Improved: {stage}
• 最大恶化 Most Declined: {stage}
```

---

## 3. Cohort Analysis / 同期群分析

Track how specific user groups behave over time.

### Types of Cohorts

1. **Time-based cohorts**: Users who signed up in the same week/month
2. **Behavior-based cohorts**: Users who performed a specific action
3. **Acquisition channel cohorts**: Users from different sources

### Retention Cohort Table Format

```
📅 留存同期群 Retention Cohort — {Cohort Type}

Week 0 = sign-up week (100%)

| Cohort | W0 | W1 | W2 | W3 | W4 | W5 | W6 | W7 | W8 |
|--------|----|----|----|----|----|----|----|----|----|
| 2026-W22 | 100% | 45% | 32% | 28% | 25% | 22% | 20% | 19% | 18% |
| 2026-W23 | 100% | 42% | 30% | 26% | 23% | 21% | 19% | — | — |
| 2026-W24 | 100% | 48% | 35% | 31% | 28% | — | — | — | — |
| 2026-W25 | 100% | 50% | 38% | — | — | — | — | — | — |

📊 分析 Insights:
• D7 retention is {trend} — {improving/declining/stable}
• 第{cwk}周后留存趋稳 at ~{rate}%
• 最佳同期群 Best cohort: {cohort} — 可能原因: {reason}
```

### Ask the User for Data

If the user doesn't have the data ready:
1. Explain what a cohort table looks like
2. Ask them to provide sign-up week + weekly active data
3. Offer to process CSV/Excel data via `/lark-sheets` or `/pandas-data-analysis`

---

## 4. Anomaly Detection / 异常检测

When a metric looks off, help the user diagnose.

### Detection Checklist

1. **Is it real?** Check data pipeline, timezone, sampling, tracking bugs
2. **How big?** Calculate deviation from expected (z-score, % change vs baseline)
3. **When did it start?** Narrow down the time window
4. **What else changed?** Check releases, campaigns, competitor moves, external events
5. **Is it isolated?** Does it affect all users or a specific segment/region/platform?

### Output Format

```
⚠️ 指标异常 Metric Anomaly Detected

📉 异常指标 Anomalous Metric:
• {metric name}: {current} vs baseline {baseline} ({deviation}% deviation)

⏰ 时间线 Timeline:
• 异常开始 Detected: {datetime}
• 最近发布 Recent Release: {version} at {datetime}
• 最近活动 Recent Campaign: {campaign} at {datetime}

🔬 影响范围 Scope:
• 总用户影响 Overall: {affected%}% of users
• 平台 Platform: {iOS affected / Android normal / Web normal}
• 地区 Region: {region breakdown}
• 版本 Version: {version breakdown}

💡 建议下一步 Suggested Next Steps:
1. {immediate action}
2. Route to /money-diagnose for deep root cause analysis
3. {monitoring plan}
```

For deep root cause analysis → `/money-diagnose`

---

## 5. Automated Report Generation

### Setting Up Periodic Reports

**Weekly report** → see `weekly-operations.md`
**Monthly report** → see `monthly-operations.md`

### Ad-Hoc Data Requests

When user asks "帮我看看这个数据" or "analyze this data":

1. Ask what data they have (format: CSV, Excel, screenshots, raw numbers, database query)
2. Determine what question they're trying to answer
3. Process the data:
   - **CSV/Excel** → `/pandas-data-analysis` for Python analysis
   - **Lark sheets** → `/lark-sheets` to read directly
   - **Raw numbers** → process directly in conversation
   - **Screenshots** → ask user to read out key numbers
4. Produce analysis with clear findings and recommendations
5. **Offer visualization** → `/chart-visualization` or `/plotly`

---

## Integration Notes

- **Python analysis**: For complex data processing, route to `/pandas-data-analysis`
- **Lark Sheets**: For users with data in Feishu, route to `/lark-sheets` to read/write directly
- **Charts**: Route to `/chart-visualization` for AntV/G2 charts, `/plotly` for interactive plots
- **DOCX output**: Per user preference, offer to save reports as `.docx` via `/document-skills:docx`
