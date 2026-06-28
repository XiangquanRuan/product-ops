# Daily Operations / 日常运营

Daily product operations workflows: morning check-in, standup, and end-of-day summary. This is the most frequently used workflow in product operations.

## Language

Check for `[Language: 中文]` or `[Language: English]` in context. Default to 中文 if user writes in Chinese. All output must be in the chosen language.

---

## 1. Morning Check-in / 晨间检查 (10 min)

Start every day with a structured check-in. Ask the user or fetch from connected tools:

### Check Items

1. **Core KPIs snapshot** (昨天数据):
   - DAU/MAU — any unusual change (±5%)?
   - Revenue — on track vs daily target?
   - Conversion rate — any dip in key funnels?
   - Crash rate / error rate — any spikes?
   - Key feature adoption — usage up or down?

2. **Alerts & Incidents** (告警与事故):
   - Any P0/P1 alerts overnight?
   - Any customer complaints escalated?
   - Any ongoing incidents?
   - Anything broken in production?

3. **Today's Calendar** (今日日程):
   - Meetings? Who, when, topic?
   - Deadlines? What's due today?
   - Launches or changes? Anything going live?
   - Key dependencies? Who needs what from you?

4. **Yesterday's Completion** (昨日完成):
   - What was planned yesterday?
   - What actually got done?
   - What was blocked and why?

5. **Today's Priorities** (今日重点):
   - Top 3 must-do items
   - Any important but not urgent items to watch
   - Blockers to escalate

### Output Format

```
📊 产品运营晨报 | Product Ops Daily Brief — {Date}

【核心数据 Core Metrics】
• DAU: {value} ({change}% vs yesterday)
• 收入 Revenue: {value} ({change}%)
• 主流程转化率 Key Conversion: {value} ({change}%)
• 崩溃率 Crash Rate: {value}
• 功能使用 Top Feature: {feature} ({usage})

【告警状态 Alerts】
• 活跃告警 Active: {count} | P0: {count} P1: {count}
• 事故 Incident: {status}

【今日日程 Today's Calendar】
• {time} — {event} ({attendees})
• {time} — {event} ({attendees})

【昨日回顾 Yesterday】
• 完成 Done: {items}
• 未完成 Blocked: {items} — 阻塞原因: {reason}

【今日重点 Today's Priorities】
1. {priority 1}
2. {priority 2}
3. {priority 3}
⚠️ 关注 Watch: {items}
```

### If Connected Tools Available

- **Lark/Feishu sheets**: Pull KPI data automatically via `/lark-sheets`
- **Lark/Feishu calendar**: Pull today's schedule via `/lark-calendar`
- **Lark/Feishu task**: Pull open tasks via `/lark-task`
- **Monitoring tools**: Ask user to share screenshot or dashboard URL if data not accessible programmatically

---

## 2. Daily Standup Report / 每日站报 (5 min)

Generate a structured standup update for team sync (async or live).

### Template

**Async standup post** (Slack / Lark IM / DingTalk):

```
👋 {Name} | 今日站报 | {Date}

✅ 昨日完成 Yesterday:
• {item} — {brief outcome}
• {item} — {brief outcome}

🔨 今日计划 Today:
• {item} [预计 {hours}h]
• {item} [预计 {hours}h]

🚧 阻塞项 Blockers:
• {blocker} — 需要 @{person/team} 协助

💡 备注 Notes:
• {any context, insights, or asks}
```

### For Standup Meetings

If running a live/voice standup, keep it to 90 seconds per person:
1. What did I do yesterday?
2. What will I do today?
3. What's blocking me?

---

## 3. End-of-Day Summary / 日终总结 (5 min)

Wrap up the day with a quick summary for yourself and the team.

### Check Items

1. **Today's accomplishments** — what shipped, what made progress
2. **Decisions made** — any key decisions and their rationale
3. **Issues surfaced** — new bugs, user complaints, process problems
4. **Carry-over to tomorrow** — what didn't get done
5. **Wins to celebrate** — anything worth sharing, no matter how small

### Output Format

```
🌙 日终总结 | EOD Summary — {Date}

【今日成果 Today's Results】
• 已发布 Shipped: {items}
• 有进展 Progress: {items}
• 已决策 Decided: {items}

【问题与风险 Issues & Risks】
• {issue} — 处理状态: {status}
• {risk} — 缓解措施: {mitigation}

【明日待办 Carry-over】
• {item}
• {item}

【今日亮点 Win of the Day】
🌟 {one thing worth celebrating}
```

---

## 4. Setting Up Recurring Daily Ops / 设置自动化日运营

For users who want automated daily operations:

### Via `/loop` Command
```
/loop 24h /product-ops 每日晨报
```
This triggers the product-ops skill every 24 hours to generate a morning check-in.

### Manual Checklist
If automation isn't desired, provide the user with this checklist:
- [ ] 9:00 — Morning check-in (KPIs, alerts, calendar)
- [ ] 9:30 — Team standup (or post async update)
- [ ] 10:00-12:00 — Deep work (data analysis, user feedback, experiments)
- [ ] 14:00-16:00 — Cross-team sync (meetings, reviews, approvals)
- [ ] 16:00-17:30 — Content & communication (release notes, docs, stakeholder updates)
- [ ] 17:30 — End-of-day summary

---

## Integration Notes

- **Lark/飞书 users**: For best results, ensure `lark-calendar`, `lark-task`, `lark-sheets`, and `lark-im` skills are available
- **Slack users**: Describe your Slack workspace setup; Claude can draft messages for copy-paste
- **Notion users**: Describe your Notion database structure for KPI tracking
