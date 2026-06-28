# Competitive Intelligence / 竞品情报与市场分析

Systematic competitor tracking, feature benchmarking, and market signal monitoring for product operations.

## Language

Check for `[Language: 中文]` or `[Language: English]` in context. Default to 中文 if user writes in Chinese.

## Context Injection

If `context.json` is loaded, inject these fields into every output in this file:

| Placeholder | Context Path | Fallback |
|-------------|-------------|----------|
| `{Product Name}` | `company.product_name` | "我们" |
| `{Direct Competitors}` | `competitors.direct[*].name` | (ask user) |
| `{Indirect Competitors}` | `competitors.indirect[*].name` | (omit) |
| `{Our Differentiation}` | `competitors.our_differentiation` | (omit) |
| `{Industry}` | `company.industry` | (omit) |
| `{Competitor details}` | `competitors.direct[*].strength/weakness` | (omit) |

**Rule**: Never fabricate context. If a field is null/absent, use the fallback. If the fallback is "(ask user)", ask the user for competitor names before proceeding.

---

## 1. Competitor Tracking Framework / 竞品追踪框架

### Competitor Tiers

```
Tier 1: 直接竞品 Direct Competitors (same product, same target)
    → Track: every release, pricing change, positioning shift
Tier 2: 间接竞品 Indirect Competitors (alternative solutions)
    → Track: major releases, strategy shifts
Tier 3: 潜在竞品 Potential Threats (adjacent products that could expand)
    → Track: funding, hiring, market entry signals
```

### What to Track

For each competitor, maintain:

| Dimension | What to Track | Frequency |
|-----------|-------------|-----------|
| **Product** | New features, UI/UX changes, platform expansion | Weekly |
| **Pricing** | Pricing model, plan changes, promotions | Weekly |
| **Positioning** | Website messaging, pitch changes, new verticals | Monthly |
| **Marketing** | Content strategy, ad campaigns, social presence | Weekly |
| **GTM** | Partnerships, integrations, enterprise deals | Monthly |
| **Team** | Key hires, departures, team size signals | Monthly |
| **Funding** | Funding rounds, valuation, investor updates | As news breaks |
| **Metrics** | Public numbers, estimates, app store data | Monthly |

---

## 2. Competitive Scan Workflow / 竞品扫描流程

### Weekly Scan (5 min per competitor)

Quick weekly check of competitor activity:

```
🔍 竞品周扫描 | Weekly Competitive Scan — {Date}

━━━━━━━━━━━━━━━━━━━━━━━

竞品 A — {name}:
• 产品更新 Product: {any new features / changes this week?}
• 市场动作 Market: {any campaigns / announcements / PR?}
• 用户信号 User Signal: {app store review trends / social sentiment shift?}
• 关注点 What to Watch: {1 thing to pay attention to}

竞品 B — {name}:
...

竞品 C — {name}:
...

━━━━━━━━━━━━━━━━━━━━━━━

📊 本周竞品动态总结 Weekly Summary:
• 最重要的变化 Biggest change: {what happened}
• 对我们的影响 Impact on us: {low / medium / high}
• 建议行动 Recommended action: {what we should do}

🏷 标签 Tags: #{competitor} #{market} #{weekly-scan}
```

### Monthly Deep-Dive (30 min)

Once a month, do a deeper competitive review. For deep positioning analysis → route to `/pmprompt:positioning-canvas`.

---

## 3. Feature Comparison Matrix / 功能对标矩阵

### Building a Feature Matrix

Work with the user to identify key feature dimensions, then map competitors:

```
📋 功能对标矩阵 | Feature Comparison Matrix
📅 Updated: {Date}

| 功能 Feature | 我们 Us | 竞品A | 竞品B | 竞品C |
|-------------|--------|-------|-------|-------|
| {Feature 1} | ✅ / 🟡 / ❌ | ✅ | 🟡 | ❌ |
| {Feature 2} | ✅ | ✅ | ✅ | ✅ |
| {Feature 3} | 🟡 | ❌ | ❌ | ✅ |
| {Feature 4} | ❌ | ✅ | ❌ | ❌ |
| {Feature 5} | ✅ | ❌ | ❌ | ❌ |

图例 Legend: ✅ = 有/好 Has/Good | 🟡 = 部分/一般 Partial/Average | ❌ = 无/差 Missing/Poor

📊 分析 Insights:
• 我们领先 Where we lead: {features}
• 我们落后 Where we lag: {features}
• 差异化机会 Differentiation opportunity: {gap in market}
• 需要补齐的 Must-have gaps: {features we need to build}
```

---

## 4. Market Signal Monitoring / 市场信号监控

### Signals to Watch

| Signal Type | Where to Monitor | Tool |
|-------------|-----------------|------|
| Product launches | Product Hunt, 36Kr, TechCrunch | RSS, Twitter |
| Funding news | Crunchbase, IT桔子, 36Kr | Google Alerts |
| Pricing changes | Competitor websites | Manual check |
| Key hires | LinkedIn | LinkedIn alerts |
| User sentiment shifts | App Store reviews, Reddit, 小红书 | Manual / review tools |
| Patent filings | Patent databases | Google Patents |
| Regulatory changes | Industry news, government announcements | News monitoring |

### Setting Up Google Alerts (Suggested)

For each competitor:
- `"{competitor name}" product launch`
- `"{competitor name}" funding`
- `"{competitor name}" review`
- `"{industry keyword}" market`

---

## 5. Competitive Battle Cards / 竞品对战卡

One-page summary for each key competitor — useful for sales enablement and internal alignment:

```
🃏 竞品对战卡 | Competitive Battle Card — {Competitor Name}

概览 Overview:
• 公司名称 Company: {name}
• 成立年份 Founded: {year}
• 总部 HQ: {location}
• 融资 Funding: {total raised, latest round}
• 团队规模 Team Size: {estimated employees}
• 目标客户 Target: {ICP description}

产品 Product:
• 核心功能 Core Features: {3-5 key features}
• 差异化 Differentiator: {what they claim as unique}
• 弱点 Weaknesses: {where they fall short}
• 定价 Pricing: {starting price, model}

市场 Market:
• 市场定位 Positioning: {tagline / elevator pitch}
• GTM 策略 GTM Motion: {PLG / sales-led / hybrid}
• 主要渠道 Channels: {how they acquire users}

对我们意味着什么 What This Means for Us:
• 竞争威胁 Threat Level: 🔴🟡🟢
• 我们如何赢 How We Win: {our advantages}
• 需要注意的 Watch Out For: {their advantages or moves}
• 话术应对 Objection Handling: {how to respond when customers bring them up}
```

---

## 6. Market & Industry Analysis / 市场与行业分析

For broader market analysis (TAM, trends, industry shifts):

### Quick Market Assessment

```
📈 市场分析快照 | Market Snapshot — {Market/Industry}

市场规模 Market Size:
• TAM: {total addressable market estimate}
• SAM: {serviceable addressable market}
• SOM: {serviceable obtainable market}
• 增长率 Growth Rate: {CAGR}%

市场趋势 Trends:
• {trend 1}: {description + implication for us}
• {trend 2}: {description + implication for us}
• {trend 3}: {description + implication for us}

竞争格局 Competitive Landscape:
• 市场集中度 Concentration: {fragmented / moderate / consolidated}
• 主要玩家 Key Players: {list with market share estimates}
• 新进入者 New Entrants: {notable recent entrants}
• 替代威胁 Substitutes: {alternative solutions}
```

For comprehensive market research → route to `/money-strategy`

---

## 7. External Skill Routing

| Need | Route To |
|------|----------|
| Competitive positioning canvas | `/pmprompt:positioning-canvas` |
| Full business strategy + competitive analysis | `/money-strategy` |
| SEO competitive analysis | `/money-seo` |
| Social media competitive monitoring | `/money-social` |
| Deep market research | `/deep-research` |
| SWOT analysis | Handled directly in this skill or `/money-strategy` |

---

## 8. Competitive Intel Cadence

| Frequency | Activity | Owner |
|-----------|----------|-------|
| Daily | Quick scan of competitor social + Product Hunt | Product Ops |
| Weekly | Feature changes, pricing, App Store reviews | Product Ops |
| Monthly | Battle card updates, deep-dive on one competitor | Product Ops + PM |
| Quarterly | Full competitive review, positioning refresh | PM + Strategy |

For setting up recurring scans → use `/loop` or weekly operations workflow in `weekly-operations.md`
