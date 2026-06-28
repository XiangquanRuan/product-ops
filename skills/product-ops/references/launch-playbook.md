# Product Launch Playbook / 产品发布运营手册

Complete product launch operations playbook: pre-launch checklist, launch day coordination, post-launch monitoring, and go-to-market coordination.

## Language

Check for `[Language: 中文]` or `[Language: English]` in context. Default to 中文 if user writes in Chinese.

## Context Injection

If `context.json` is loaded, inject these fields into every output in this file:

| Placeholder | Context Path | Fallback |
|-------------|-------------|----------|
| `{Product Name}` | `company.product_name` | "产品" |
| `{platforms}` | `product.platforms` | "Web" |
| `{release cadence}` | `releases.typical_cadence` | "weekly" |
| `{feature flag tool}` | `releases.feature_flag_tool` | (omit) |
| `{rollout strategy}` | `releases.rollout_strategy` | (omit) |
| `{rollback procedure}` | `releases.rollback_procedure` | (omit) |
| `{comms tool}` | `tools.communication` | "Slack" |
| `{monitoring tool}` | `tools.monitoring` | (omit) |
| `{cicd tool}` | `tools.cicd` | (omit) |
| `{eng lead}` | `team.key_contacts.engineering_lead` | (omit) |
| `{pm}` | `team.key_contacts.pm` | (omit) |

**Rule**: Never fabricate context. If a field is null/absent, use the fallback. If the fallback is "(omit)", remove that line/section entirely.

---

## Phase 0: Launch Classification / 发布分级

Not all launches are equal. Classify the launch first:

| Level | Scope | Example | Ceremony |
|-------|-------|---------|----------|
| 🔴 **Major Launch** | New product, major version, platform expansion | v2.0, iOS launch, new market | Full playbook |
| 🟡 **Feature Launch** | Significant new feature | New payment method, AI feature | Light playbook |
| 🟢 **Minor Release** | Improvements, bug fixes | Weekly release | Minimal process |
| ⚪ **Hotfix** | Emergency fix | Critical bug fix | Expedited process |

---

## Phase 1: Pre-Launch Checklist / 上线前检查清单

### T-7 Days (一周前)

**Product Readiness**:
- [ ] 功能验收 Feature sign-off: PM has verified all features work as expected
- [ ] 设计验收 Design QA: Designer has verified UI/UX matches specs
- [ ] 测试通过 QA sign-off: All test cases passed, no P0/P1 bugs open
- [ ] 性能测试 Performance: Load test passed, P99 latency within target
- [ ] 安全检查 Security review: No critical vulnerabilities → route to `/money-quality` for comprehensive quality gates

**Operational Readiness**:
- [ ] 监控配置 Monitoring: Dashboards and alerts configured for new features
- [ ] 数据分析埋点 Analytics: All tracking events verified and documented
- [ ] 帮助文档 Help docs: New feature documentation ready (in-app, help center)
- [ ] 客服培训 Support training: Support team briefed on new features, FAQ ready
- [ ] 降级方案 Rollback plan: Documented and tested rollback procedure

**Communications Readiness**:
- [ ] 发布公告 Release notes: Drafted and reviewed (see `content-operations.md`)
- [ ] 应用商店文案 App Store copy: Updated screenshots, description (if applicable)
- [ ] 社交媒体 Social media: Post drafts ready for launch day
- [ ] 用户通知 User notification: Push/email/in-app message ready
- [ ] 内部通告 Internal announcement: Team briefed on launch details

### T-3 Days (三天前)

- [ ] 预发布环境验证 Staging verification: Full regression on staging
- [ ] 灰度方案 Feature flag/Rollout plan: % rollout scheduled, criteria for full rollout defined
- [ ] 客服话术 Support scripts: Support team has response templates for expected issues
- [ ] 关键人到位 Key people confirmed: Engineers, PM, Designer on standby for launch day

### T-1 Day (一天前)

- [ ] Launch readiness meeting (30 min): Final go/no-go decision
- [ ] 值班安排 On-call schedule: Who's on-call for the next 24h/72h?
- [ ] 沟通渠道确认 Comms channel: Where will the team coordinate during launch? (Lark group, Slack channel)
- [ ] 回滚流程确认 Rollback rehearsal: Everyone knows how to roll back and who can authorize it

---

## Phase 2: Launch Day / 上线当天

### Launch Day Timeline

```
⏰ 上线日流程 | Launch Day Timeline

T-2h: 上线前确认 Pre-Launch Check
• 值班人员到位 On-call team online
• 监控面板打开 Monitoring dashboards open
• 沟通渠道测试 Comms channel test message
• 发布流程确认 Release process walkthrough

T-1h: 代码冻结 Code Freeze
• 最后确认最后一次构建 Last build verified
• 发布说明最终检查 Release notes final review
• 灰度配置确认 Feature flag configs verified

T-0: 发布 Launch!
• 按灰度方案逐步放量 Roll out per plan: 1% → 5% → 25% → 100%
• 每个阶段停留观察 Wait and observe at each stage
• 实时监控 Real-time monitoring:
  - 崩溃率 Crash rate
  - 错误率 Error rate  
  - 核心流程转化 Core funnel conversion
  - 加载时间 Page load time
  - 用户反馈 User feedback (social, reviews, tickets)

T+1h: 第一次检查点 First Checkpoint
• 所有监控指标正常? All metrics green?
• 有用户反馈异常? Any user reports of issues?
• ✅ 继续放量 Continue rollout / ⏸ 暂停 Pause / 🔙 回滚 Rollback

T+4h: 第二次检查点 Second Checkpoint
• 全量发布完成? Full rollout complete?
• 关键指标稳定? Key metrics stable?
• 客服工单有异常? Support ticket spike?

T+24h: 发布后24小时确认 24h Post-Launch
• 24h 数据报告 24h data review
• 是否有regression? Any regressions detected?
• 用户反馈汇总 User feedback summary
```

### Launch Day Communication

**Internal Launch Announcement** (at T-0):
```
🚀 {Feature/Version} 已上线 | Now Live!

已按 {X}% 灰度发布中 Rolling out at {X}%.

📊 监控看板 Monitoring Dashboard: {link}
🐛 问题反馈 Report Issues: {channel/link}
📝 发布说明 Release Notes: {link}

值班 On-call: @{name} (eng), @{name} (pm)
```

**Launch Complete Announcement** (at 100% rollout):
```
✅ {Feature/Version} 全量发布完成 | Fully Rolled Out

📊 上线数据 Launch Metrics (24h):
• 崩溃率 Crash Rate: {value}% (正常 Normal)
• 新功能使用 New Feature Usage: {n} users
• 用户反馈 User Feedback: {sentiment summary}

🔗 发布说明 Release Notes: {link}
📝 复盘文档 Post-mortem Doc: {link} (to be filled)
```

---

## Phase 3: Post-Launch Monitoring / 上线后监控

### Monitoring Schedule

| Checkpoint | When | What to Check |
|-----------|------|---------------|
| 1-hour | T+1h | Crash rate, error rate, core funnel |
| 4-hour | T+4h | Full rollout metrics, support tickets |
| 24-hour | T+24h | Full day metrics, user feedback, revenue impact |
| 72-hour | T+72h | Stabilization check, delayed issues, adoption rate |
| 1-week | T+7d | Weekly impact review, retention of new feature users |

### Post-Launch Data Review Template

```
📊 上线后数据回顾 | Post-Launch Data Review
🚀 {Feature/Version} — {Launch Date}

━━━━━━━━━━━━━━━━━━━━━━━

⏰ {Timeframe} Check-in:

📈 核心指标 Core Metrics:
| 指标 Metric | 上线前 Before | 当前 Current | 变化 Change | 状态 |
|------------|-------------|------------|-----------|------|
| 崩溃率 Crash Rate | {v}% | {v}% | {+/-}pp | 🟢🟡🔴 |
| 错误率 Error Rate | {v}% | {v}% | {+/-}pp | 🟢🟡🔴 |
| 核心转化 Conversion | {v}% | {v}% | {+/-}pp | 🟢🟡🔴 |
| 加载时间 Load Time | {v}ms | {v}ms | {+/-}ms | 🟢🟡🔴 |

🎯 新功能使用 New Feature Adoption:
• 使用用户 Users: {n}
• 使用率 Adoption Rate: {n}%
• 留存 Retention: {D1/D7 if available}

💬 用户反馈 User Feedback:
• 反馈量 Volume: {n} items
• 情感 Sentiment: 正向 {p}% / 中性 {n}% / 负向 {n}%
• 主要话题 Top Themes: {list}

⚠️ 问题与异常 Issues:
• {issue} — 状态: {open/in progress/resolved}
• {issue} — 状态: {open/in progress/resolved}

🎯 决策 Decision:
• ✅ 继续 Continue as planned / ⏸ 暂停观察 Pause and monitor / 🔙 回滚 Rollback
```

---

## Phase 4: Post-Launch Retro / 上线复盘

### After 1 Week

Schedule a 30-45 minute launch retrospective with the team:

**Agenda**:
1. What went well? (10 min)
2. What could have gone better? (10 min)
3. What should we do differently next time? (10 min)
4. Action items (5 min)

**Retro Output**:

```
🔄 上线复盘 | Launch Retrospective — {Feature/Version}

📊 上线数据总结 Launch Metrics Summary:
• {key metric}: target {t} → actual {a} (达成 Achieved / 未达成 Missed / 超越 Exceeded)
• {key metric}: target {t} → actual {a}

✅ 做得好的 What Went Well:
• {item}
• {item}

📈 可以改进的 What Could Be Better:
• {item} → 改进建议 Suggestion: {action}
• {item} → 改进建议 Suggestion: {action}

📋 行动项 Action Items:
• {action} — Owner: @{name} — Due: {date}
• {action} — Owner: @{name} — Due: {date}

💡 关键学习 Key Learnings:
• {learning to apply to next launch}
```

---

## Phase 5: Go-to-Market Coordination / 市场推广协同

For major launches, coordinate with marketing:

### GTM Checklist

- [ ] Blog post / 公众号文章 published
- [ ] Social media posts across channels (X, LinkedIn, 小红书, etc.)
- [ ] Email newsletter sent to user base
- [ ] Product Hunt launch (if applicable)
- [ ] Press outreach / media coverage
- [ ] Influencer / KOL coordination
- [ ] Paid promotion setup (if budgeted)
- [ ] Community announcement (Discord, Slack, Reddit)
- [ ] App Store Optimization (new screenshots, description)

For content creation → `/money-content`
For social media strategy → `/money-social`
For SEO → `/money-seo`

---

## External Skill Routing

| Need | Route To |
|------|----------|
| Pre-launch quality gates | `/money-quality` |
| Release notes writing | `content-operations.md` or `/money-content` |
| Social media launch posts | `/money-social` |
| Content for GTM | `/money-content` |
| SEO for launch page | `/money-seo` |
| Meeting minutes for retro | `/lark-minutes` |
| Task tracking for action items | `/lark-task` |
| Team communication | `/lark-im` |
| Stakeholder update post-launch | `/pmprompt:stakeholder-update-generator` |

---

## Templates

- Launch checklist: `assets/launch-checklist.md`
