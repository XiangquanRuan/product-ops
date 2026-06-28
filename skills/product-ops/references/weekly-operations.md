# Weekly Operations / 周度运营

Weekly product operations: data report (周报), user feedback digest, competitive scan, and growth review. The weekly report is the single most important recurring output for product ops.

## Language

Check for `[Language: 中文]` or `[Language: English]` in context. Default to 中文 if user writes in Chinese.

## Context Injection

If `context.json` is loaded, inject these fields into every output in this file:

| Placeholder | Context Path | Fallback |
|-------------|-------------|----------|
| `{Product Name}` | `company.product_name` | "产品" |
| `{company}` | `company.name` | (omit if null) |
| `{industry}` | `company.industry` | (omit if null) |
| `{DAU label}` | `metrics.definitions.dau.name` | "DAU" |
| `{Revenue label}` | `metrics.definitions.revenue.name` | "收入" |
| `{Retention label}` | `metrics.definitions.retention_d7.name` | "D7 留存率" |
| `{Conversion label}` | `metrics.definitions.conversion.name` | "核心转化率" |
| `{analytics tool}` | `metrics.data_sources.analytics_tool` | (omit) |
| `{data dashboard}` | `metrics.data_sources.dashboard_url` | (omit) |
| `{competitor names}` | `competitors.direct[*].name` | (omit) |
| `{differentiation}` | `competitors.our_differentiation` | (omit) |
| `{brand tone}` | `brand.tone` | "professional" |
| `{primary channels}` | `brand.primary_channels` | (omit) |
| `{target users}` | `product.target_users_icp` | (omit) |

**Rule**: Never fabricate context. If a field is null/absent, use the fallback. If the fallback is "(omit)", remove that line/section entirely.

---

## 1. Weekly Data Report (周报) — Core Workflow

The weekly report answers: **What happened this week? What did we learn? What's next?**

### Data to Collect (before writing)

Ask the user for data or help them pull it:

**Product Metrics** (本周数据):
- DAU/MAU — trend vs last week
- New users — acquisition volume & cost
- Retention — D1/D7/D30, trend
- Core funnel conversion — each step's conversion rate
- Revenue — total & by channel
- Key feature usage — top features, new feature adoption
- Crash rate, bug count, response time

**Operational Metrics** (运营数据):
- Content published — articles, posts, push notifications, count & performance
- User feedback — new feedback count, sentiment ratio
- Experiments — active experiments, results concluded
- Tickets/cases closed — CS response time, resolution rate
- Shipments — features released, hotfixes deployed

### Report Structure

Produce a structured weekly report:

```
📊 {Product Name} 周报 | Weekly Report
📅 {Date Range}

━━━━━━━━━━━━━━━━━━━━━━━

一、核心数据 Core Metrics

| 指标 Metric | 本周 This Week | 上周 Last Week | 环比 WoW |
|------------|---------------|---------------|----------|
| DAU | {value} | {value} | {+/-}% |
| 新增用户 New Users | {value} | {value} | {+/-}% |
| 留存率 Retention D7 | {value}% | {value}% | {+/-}pp |
| 核心转化 Conversion | {value}% | {value}% | {+/-}pp |
| 收入 Revenue | {value} | {value} | {+/-}% |

📈 关键趋势 Key Trends:
• {describe 1-2 important trends}
• {describe any anomalies}

━━━━━━━━━━━━━━━━━━━━━━━

二、本周重点成果 Key Results

✅ 已上线 Shipped:
• {feature/change} — 对用户的影响: {impact}
• {feature/change} — 对用户的影响: {impact}

🔬 实验结论 Experiments Concluded:
• {experiment name} — 结果: {result} — 决策: {ship/kill/iterate}
• {experiment name} — 结果: {result} — 决策: {ship/kill/iterate}

━━━━━━━━━━━━━━━━━━━━━━━

三、用户反馈与洞察 User Insights

💬 本周反馈概况:
• 收到反馈 {count} 条 | 正向 {pos}% | 中性 {neu}% | 负向 {neg}%
• 主要话题 Top Themes:
  1. {theme} ({count} mentions)
  2. {theme} ({count} mentions)
  3. {theme} ({count} mentions)

🔍 值得关注的反馈:
• "{user quote or summary}" — 影响面: {how many users affected}
• "{user quote or summary}" — 影响面: {how many users affected}
• → 建议行动 Recommended Actions: {what to do}

━━━━━━━━━━━━━━━━━━━━━━━

四、问题与风险 Issues & Risks

⚠️ 线上问题 Production Issues:
• {issue} — 影响: {impact scope} — 状态: {fixed/in progress/monitoring}
• {issue} — 影响: {impact scope} — 状态: {fixed/in progress/monitoring}

🔴 风险项 Risks:
• {risk} — 可能性: {probability} — 影响: {impact} — 缓解: {mitigation}

━━━━━━━━━━━━━━━━━━━━━━━

五、下周计划 Next Week Plan

🎯 重点目标 Key Objectives:
1. {objective 1}
2. {objective 2}
3. {objective 3}

📋 具体事项 Tasks:
• {task} — 预计完成: {date} — 负责人: {owner}
• {task} — 预计完成: {date} — 负责人: {owner}
• {task} — 预计完成: {date} — 负责人: {owner}

❓ 需要支持 Needs Help:
• {what} — 需要谁: {who}

━━━━━━━━━━━━━━━━━━━━━━━

六、本周思考与收获 Learnings

💡 {1-2 key learnings or observations from this week}
```

### Post-Report Actions

After generating the report:
1. **Offer to save** — save as `.md` or `.docx` file
2. **Offer to share** — draft Lark IM / Slack message with key highlights
3. **Route to retro** — if user wants deeper reflection → `/money-retro`
4. **Route to stakeholder update** — if user needs leadership summary → `/pmprompt:stakeholder-update-generator`

---

## 2. User Feedback Weekly Digest

For a focused feedback-only weekly review:

1. **Collect**: Ask user for feedback sources (app store reviews, support tickets, NPS, user interviews, social media)
2. **Synthesize**: Identify themes, severity, frequency
3. **Prioritize**: What needs action this week?
4. **Route**: For deep analysis → `/pmprompt:user-feedback-synthesizer`

Output as a section within the weekly report or standalone.

---

## 3. Competitive Weekly Scan

Quick weekly competitor check (not full deep-dive — that's `competitive-intel.md`):

- **3 competitors to watch**: Any feature launches, pricing changes, positioning shifts?
- **Market signals**: Any funding news, acquisition, key hires?
- **What we should know**: 1-2 things that might affect our product decisions

Output as a short section within the weekly report.

---

## 4. Growth Metrics Weekly Review

For growth-focused teams:

| Metric | This Week | Target | Status |
|--------|-----------|--------|--------|
| New user acquisition | {value} | {target} | 🟢🟡🔴 |
| Activation rate | {value}% | {target}% | 🟢🟡🔴 |
| D7 retention | {value}% | {target}% | 🟢🟡🔴 |
| Revenue / Monetization | {value} | {target} | 🟢🟡🔴 |
| Referral / viral coefficient | {value} | {target} | 🟢🟡🔴 |

For deep growth loop analysis → `/pmprompt:growth-loops`

---

## 5. Setting Up Recurring Weekly Ops

### Via `/loop` Command
```
/loop 168h /product-ops 生成周报
```
Triggers weekly report generation every 168 hours (7 days).

### Best Day/Time
- **Friday afternoon** (16:00-17:00) — wrap-up the week
- **Monday morning** (09:00-10:00) — review last week, plan this week

---

## Templates

- Weekly report template: `assets/weekly-report-template.md`
