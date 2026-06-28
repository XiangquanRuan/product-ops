# Monthly Operations / 月度运营

Monthly business review (月报), OKR tracking, feature adoption review, and next-month planning for product operations.

## Language

Check for `[Language: 中文]` or `[Language: English]` in context. Default to 中文 if user writes in Chinese.

## Context Injection

If `context.json` is loaded, inject these fields into every output in this file:

| Placeholder | Context Path | Fallback |
|-------------|-------------|----------|
| `{Product Name}` | `company.product_name` | "产品" |
| `{Company}` | `company.name` | (omit if null) |
| `{DAU/MAU label}` | `metrics.definitions.dau.name` | "DAU/MAU" |
| `{Revenue label}` | `metrics.definitions.revenue.name` | "收入" |
| `{Retention label}` | `metrics.definitions.retention_d7.name` | "留存率" |
| `{analytics tool}` | `metrics.data_sources.analytics_tool` | (omit) |
| `{competitor names}` | `competitors.direct[*].name` | (omit) |
| `{OKR tool}` | `tools.documentation` | (omit) |
| `{target users}` | `product.target_users_icp` | (omit) |

**Rule**: Never fabricate context. If a field is null/absent, use the fallback. If the fallback is "(omit)", remove that line/section entirely.

---

## 1. Monthly Business Review / 月度经营分析 (月报)

The monthly review is more strategic than the weekly report — it covers what we learned and what we're changing.

### Pre-Work: Data Collection

Before writing the monthly report, gather:

**Product Metrics** (月度):
- MAU trend (3-6 months to show trajectory)
- New users (total, by channel, CAC by channel)
- Retention (D1/D7/D30, cohort view)
- Revenue (total, by plan/segment, vs target)
- Key feature adoption (new features, core features)
- Quality metrics (uptime, crash rate, P99 latency)

**Operational Metrics** (月度):
- Experiments run/concluded
- User feedback volume & sentiment
- Content published & performance
- Support tickets & resolution
- Team velocity (features shipped, bugs fixed)

**Business Metrics** (月度):
- Burn rate / runway
- Customer acquisition cost trends
- LTV trends
- Churn rate (voluntary vs involuntary)

### Monthly Report Structure

```
📊 {Product Name} 月度经营分析 | Monthly Business Review
📅 {Month} {Year}

━━━━━━━━━━━━━━━━━━━━━━━
一、月度概览 Executive Summary

本月 {2-3 sentence high-level summary of the month}
• 最重要的事 Biggest thing that happened: {event}
• 最大的变化 Biggest change: {metric shift or strategic pivot}
• 最大的风险 Biggest risk: {risk}

━━━━━━━━━━━━━━━━━━━━━━━
二、核心指标 Core Metrics

📈 用户增长 User Growth:

| 指标 | 本月 | 上月 | 环比 MoM | 目标 Target | 达成 |
|------|-----|-----|----------|------------|-----|
| MAU | {v} | {v} | {+/-}% | {v} | 🟢🟡🔴 |
| 新增 New Users | {v} | {v} | {+/-}% | {v} | 🟢🟡🔴 |
| D7 留存 D7 Retention | {v}% | {v}% | {+/-}pp | {v}% | 🟢🟡🔴 |
| D30 留存 D30 Retention | {v}% | {v}% | {+/-}pp | {v}% | 🟢🟡🔴 |

💰 收入 Revenue:

| 指标 | 本月 | 上月 | 环比 MoM | 目标 Target | 达成 |
|------|-----|-----|----------|------------|-----|
| MRR | {v} | {v} | {+/-}% | {v} | 🟢🟡🔴 |
| ARPU | {v} | {v} | {+/-}% | {v} | 🟢🟡🔴 |
| 付费率 Pay Rate | {v}% | {v}% | {+/-}pp | {v}% | 🟢🟡🔴 |
| 月流失率 Churn | {v}% | {v}% | {+/-}pp | {v}% | 🟢🟡🔴 |

🔧 产品健康 Product Health:

| 指标 | 本月 | 上月 | 阈值 |
|------|-----|-----|-----|
| 崩溃率 Crash Rate | {v}% | {v}% | < {t}% |
| 可用性 Uptime | {v}% | {v}% | > {t}% |
| P99 延迟 Latency | {v}ms | {v}ms | < {t}ms |

📈 MAU 趋势图 MAU Trend (6 months):
```
{Month-5}: ████████ {v}
{Month-4}: █████████ {v}
{Month-3}: ██████████ {v}
{Month-2}: ███████████ {v}
{Month-1}: ████████████ {v}
{Current}: ██████████████ {v}
```

━━━━━━━━━━━━━━━━━━━━━━━
三、本月重点成果 Key Results

✅ 已发布 Releases:
• {feature/initiative} — 对指标的影响 Impact: {metric change}
• {feature/initiative} — 对指标的影响 Impact: {metric change}

🔬 实验结论 Experiments:
• {n} experiments run | {n} shipped | {n} killed | {n} still running
• 最大的结论 Biggest learning: {key insight}

📝 内容与运营 Content & Ops:
• 发布内容 {n} pieces | 总阅读 {n} | 最佳: {title}
• 用户反馈收集 {n} 条 | 已处理 {n} 条

━━━━━━━━━━━━━━━━━━━━━━━
四、OKR 进展 OKR Progress

Objective 1: {objective}
• KR1: {key result} — 当前: {current} / 目标: {target} ({progress}%) 🟢🟡🔴
• KR2: {key result} — 当前: {current} / 目标: {target} ({progress}%) 🟢🟡🔴

Objective 2: {objective}
• KR1: {key result} — 当前: {current} / 目标: {target} ({progress}%) 🟢🟡🔴
• KR2: {key result} — 当前: {current} / 目标: {target} ({progress}%) 🟢🟡🔴

月度 OKR 总结 Summary:
• 进展良好 On track: {KRs}
• 有风险 At risk: {KRs} — 原因: {reasons}
• 需要调整 Needs adjustment: {any KRs that should be changed}

For formal OKR setting/review → `/pmprompt:okrs`

━━━━━━━━━━━━━━━━━━━━━━━
五、用户洞察 User Insights

💬 本月用户反馈:
• 总反馈 {n} 条 | 正向 {p}% | 负向 {n}%
• 热议功能 Most discussed: {feature}
• 痛点 Top pain points: {1-2}

🔍 关键发现 Key User Findings:
• {finding 1} — 行动 Action: {what we're doing}
• {finding 2} — 行动 Action: {what we're doing}

━━━━━━━━━━━━━━━━━━━━━━━
六、竞品与市场 Competitive & Market

• 竞品重大更新 Major competitor moves: {1-2 key items}
• 市场变化 Market shifts: {any trends or news}
• 对我们的影响 Implication: {what this means for us}

For detailed competitive analysis → `competitive-intel.md`

━━━━━━━━━━━━━━━━━━━━━━━
七、问题与风险 Issues & Risks

| 风险 Risk | 可能性 Prob. | 影响 Impact | 缓解措施 Mitigation | 负责人 |
|----------|------------|------------|-------------------|--------|
| {risk} | 高/中/低 | 高/中/低 | {action} | {owner} |
| {risk} | 高/中/低 | 高/中/低 | {action} | {owner} |

━━━━━━━━━━━━━━━━━━━━━━━
八、下月计划 Next Month Plan

🎯 下月目标 Next Month Goals:
1. {goal} — 成功标准 Success: {metric target}
2. {goal} — 成功标准 Success: {metric target}
3. {goal} — 成功标准 Success: {metric target}

📋 重点事项 Key Initiatives:
• {initiative} — ETA: {date} — Owner: {person}
• {initiative} — ETA: {date} — Owner: {person}
• {initiative} — ETA: {date} — Owner: {person}

🔮 关注事项 Watch Items:
• {item to monitor}
• {item to monitor}

💡 本月最大的收获 Key Learning from This Month:
{one important lesson learned}
```

---

## 2. Feature Adoption Review / 功能使用回顾

Monthly review of how features are performing:

```
🔧 功能使用月度回顾 | Feature Adoption Review

新功能 New Features (launched this quarter):

| 功能 Feature | 上线日 Launch | 日活用户 DAU | 目标达成 vs Target | 留存 Retention |
|-------------|------------|------------|-------------------|---------------|
| {feature} | {date} | {n} ({n}%) | {status} | {D7/D30}% |
| {feature} | {date} | {n} ({n}%) | {status} | {D7/D30}% |

核心功能 Core Features:

| 功能 Feature | 本月使用 Usage | 上月 Usage | 趋势 Trend |
|-------------|-------------|----------|-----------|
| {feature} | {n} ({n}%) | {n} ({n}%) | ↗↘→ |
| {feature} | {n} ({n}%) | {n} ({n}%) | ↗↘→ |

📊 分析 Insights:
• 增长最快的功能 Fastest growing: {feature} (+{X}%)
• 下降最多的功能 Biggest decliner: {feature} (-{X}%)
• 未达预期 Below expectations: {features} — 原因与计划: {analysis}
```

---

## 3. Monthly Team Retro / 月度团队复盘

For a team-level retrospective → route to `/money-retro` for evidence-based retro format.

Quick version in this skill:

```
🔄 月度复盘 | Monthly Retro — {Month}

做得好 What went well:
• {item}
• {item}

可以改进 What could be better:
• {item} — 改进建议 Suggestion: {action}
• {item} — 改进建议 Suggestion: {action}

下月行动 Action Items:
• {action} — Owner: {person}
• {action} — Owner: {person}
```

---

## 4. Monthly Ops Schedule / 月度运营节奏

Recommended monthly cadence:

| Day | Activity | Duration |
|-----|----------|----------|
| 1st | Data pull — all monthly metrics | 2 hours |
| 1st-3rd | Draft monthly report | 3 hours |
| 3rd | OKR progress update | 1 hour |
| 5th | Monthly business review meeting | 1 hour |
| 7th | Content performance review | 1 hour |
| 14th | Strategy / roadmap check-in | 1 hour |
| 21st | Competitive deep-dive | 2 hours |
| 28th | Next month planning | 2 hours |

---

## Templates

- Monthly report template: `assets/monthly-report-template.md`

## External Skill Routing

| Need | Route To |
|------|----------|
| Deep retro | `/money-retro` |
| OKR setting/review | `/pmprompt:okrs` |
| Strategy review | `/money-strategy` |
| Financial deep-dive | `/money-finance` |
| Stakeholder presentation | `/pmprompt:stakeholder-update-generator` |
