# Project Coordination / 项目协同

Cross-team communication, meeting management, sprint planning, stakeholder updates, and approval workflows for product operations.

## Language

Check for `[Language: 中文]` or `[Language: English]` in context. Default to 中文 if user writes in Chinese.

## Context Injection

If `context.json` is loaded, inject these fields into every output in this file:

| Placeholder | Context Path | Fallback |
|-------------|-------------|----------|
| `{Product Name}` | `company.product_name` | "产品" |
| `{team structure}` | `team.structure` | (omit) |
| `{team roles}` | `team.roles` | (omit) |
| `{sprint cadence}` | `team.sprint_cadence` | "2-week" |
| `{comms tool}` | `tools.communication` | "Slack" |
| `{task tool}` | `tools.task_management` | "Jira" |
| `{doc tool}` | `tools.documentation` | "Notion" |
| `{cicd tool}` | `tools.cicd` | (omit) |

**Rule**: Never fabricate context. If a field is null/absent, use the fallback. If the fallback is "(omit)", remove that line/section entirely.

---

## 1. Cross-Team Communication / 跨部门沟通

Product ops sits at the intersection of product, engineering, marketing, sales, and support. Effective communication is critical.

### Communication Templates

**Status Update to Leadership** (weekly/bi-weekly):

```
📊 {Project/Product} 进展同步 | Status Update — {Date}

⚡ TL;DR:
{1-2 sentence summary — what should leadership know?}

📈 关键数据 Key Metrics:
• {metric}: {current} (目标 Target: {target}, {status})
• {metric}: {current} (目标 Target: {target}, {status})

✅ 完成 Done:
• {item} — 影响 Impact: {what changed}

🔨 进行中 In Progress:
• {item} — 预计 ETA: {date} — 风险 Risk: {low/med/high}

🚧 阻塞 Blockers:
• {blocker} — 需要: @{person} 协助

📅 下一步 Next Steps:
• {next action}
```

**Escalation** (when something needs immediate attention):

```
🚨 需要升级 | Escalation: {Issue}

问题 What: {one-line description of the issue}
影响 Impact: {how many users / how much revenue affected}
时间线 Timeline: {when it started, when it was detected}
状态 Status: {what's being done right now}
需要 Need: {what you need from the recipient}
```

**Alignment Request** (getting buy-in from another team):

```
🤝 协同请求 | Collaboration Request: {Topic}

背景 Context: {1-2 sentences on why this matters}
方案 Proposal: {what we want to do}
需要你做什么 What we need from your team: {specific ask}
截止时间 Deadline: {date}
```

---

## 2. Meeting Management / 会议管理

### Meeting Agenda Template

```
📋 会议议程 | Meeting Agenda — {Meeting Name}
📅 {Date} {Time} ({Duration})
👥 参会人 Attendees: {names}

会前准备 Pre-read:
• {document or context to read beforehand}

议程 Agenda:

1. {Topic} ({allocated time} min)
   • 目标 Goal: {decision / discussion / info sharing}
   • 材料 Materials: {link}

2. {Topic} ({allocated time} min)
   • 目标 Goal: {decision / discussion / info sharing}
   • 材料 Materials: {link}

3. {Topic} ({allocated time} min)
   • 目标 Goal: {decision / discussion / info sharing}
   • 材料 Materials: {link}

📝 会议纪要 Meeting Notes:
[to be filled during/after meeting]

✅ 决议 Decisions:
• 

📋 待办 Action Items:
• {action} — @{owner} — {deadline}
• {action} — @{owner} — {deadline}
```

### Meeting Minutes Template

```
📝 会议纪要 | Meeting Minutes — {Meeting Name}
📅 {Date} | ⏱ {Duration} | 👥 {Attendees}

一、会议摘要 Summary:
{brief summary of what was discussed and decided}

二、讨论要点 Discussion:

1. {Topic}
   • 讨论 Discussion: {key points raised}
   • 决议 Decision: {what was decided}
   • 分歧 Disagreements: {if any, and how resolved}

2. {Topic}
   ...

三、决议 Decisions Made:
• {Decision 1} — 通过 Approved by: {who}
• {Decision 2} — 通过 Approved by: {who}

四、待办事项 Action Items:

| # | 事项 Action | 负责人 Owner | 截止日 Deadline | 状态 |
|---|-----------|-------------|---------------|------|
| 1 | {action} | @{name} | {date} | ⏳ |
| 2 | {action} | @{name} | {date} | ⏳ |

五、下次会议 Next Meeting:
• 时间 When: {date/time}
• 议题 Topics: {preliminary topics}
```

For Feishu/Lark meeting management → `/lark-minutes` for recording, transcription, and AI summaries.

---

## 3. Sprint / Iteration Planning / 迭代规划

### Sprint Planning Checklist

When the team is planning a sprint/iteration:

1. **Review last sprint** (10 min):
   - What shipped? What didn't? Why?
   - What was the velocity?
   - What went well? What to improve?

2. **Set sprint goal** (5 min):
   - One clear, measurable goal for this sprint
   - "By the end of this sprint, we will..."

3. **Prioritize and scope** (20 min):
   - What's the highest priority work?
   - What fits in this sprint?
   - Are there dependencies?
   - What's explicitly NOT in this sprint?

4. **Estimate and assign** (15 min):
   - Who's working on what?
   - Any capacity constraints (PTO, on-call)?
   - Buffer for bugs/unknowns (typically 20%)

5. **Define success** (5 min):
   - How will we know the sprint was successful?
   - What metrics will we track?

### Sprint Planning Output

```
🏃 Sprint {N} 规划 | Sprint Planning
📅 {Start Date} → {End Date} ({n} weeks)

🎯 Sprint 目标 Sprint Goal:
{one clear, measurable goal}

📋 计划事项 Planned Items:

| 优先级 Priority | 事项 Item | 类型 Type | 估算 Est. | 负责人 Owner |
|---------------|----------|---------|---------|------------|
| P0 | {item} | Feature | {n}d | @{name} |
| P0 | {item} | Bug | {n}d | @{name} |
| P1 | {item} | Improvement | {n}d | @{name} |
| P1 | {item} | Tech Debt | {n}d | @{name} |

📊 容量 Capacity:
• 总容量 Total: {n} 人天
• 已分配 Allocated: {n} 人天 ({n}%)
• 缓冲 Buffer: {n} 人天 ({n}%)

🚫 本迭代不做 Not in This Sprint:
• {item} — 原因: {reason}

📈 成功标准 Success Criteria:
• {metric or outcome}
```

---

## 4. Stakeholder Update / 向上汇报

### Choosing the Right Format

| Audience | Format | Frequency | Focus |
|----------|--------|-----------|-------|
| Direct manager | 1:1 async update | Weekly | Progress, blockers, needs |
| Leadership team | Structured update | Bi-weekly/Monthly | Metrics, milestones, risks |
| Cross-functional partners | Slack/Lark post | Weekly | What affects them |
| Company-wide | Newsletter / All-hands | Monthly | Wins, launches, learnings |

For formal stakeholder updates → `/pmprompt:stakeholder-update-generator`

### Quick Leadership Update Template

```
📊 月度汇报 | Monthly Leadership Update — {Month}

一句话总结 One-Liner:
{most important thing leadership needs to know}

数据亮点 Metrics Highlights:
• {metric}: {value} (🟢 on track / 🟡 at risk / 🔴 off track)
• {metric}: {value} (🟢 on track / 🟡 at risk / 🔴 off track)
• {metric}: {value} (🟢 on track / 🟡 at risk / 🔴 off track)

本月最大的进展 Biggest Wins:
1. {win} — 为什么重要 Why it matters: {reason}
2. {win} — 为什么重要 Why it matters: {reason}

最大的风险 Biggest Risks:
1. {risk} — 缓解计划 Mitigation: {plan}
2. {risk} — 缓解计划 Mitigation: {plan}

需要的支持 Asks for Leadership:
• {specific ask} — 为什么 Why: {reason}

下月重点 Next Month Focus:
• {priority 1}
• {priority 2}
```

---

## 5. Process Documentation / SOP 流程文档

When documenting a repeatable process:

```
📋 {Process Name} SOP

目的 Purpose:
{why this process exists}

适用范围 Scope:
{when to use / when not to use}

角色与职责 Roles:
• {Role}: {responsibility}
• {Role}: {responsibility}

前置条件 Prerequisites:
• {check item}
• {check item}

流程步骤 Steps:

1. {Step Name} ({estimated time})
   • {detailed instruction}
   • 检查点 Checkpoint: {what to verify before moving on}

2. {Step Name} ({estimated time})
   • {detailed instruction}
   • 检查点 Checkpoint: {what to verify before moving on}

3. {Step Name} ({estimated time})
   ...

异常处理 Exceptions:
• 如果 If {condition}: {what to do}
• 如果 If {condition}: {what to do}

相关资源 Related Resources:
• {link to doc/template}
• {link to doc/template}

最后更新 Last Updated: {date}
负责人 Owner: {name}
```

---

## 6. External Skill Routing

| Need | Route To |
|------|----------|
| Feishu meeting minutes + recording | `/lark-minutes` |
| Feishu task creation & tracking | `/lark-task` |
| Feishu approval workflows | `/lark-approval` |
| Feishu calendar scheduling | `/lark-calendar` |
| Feishu document collaboration | `/lark-doc` |
| Feishu wiki for SOPs | `/lark-wiki` |
| Feishu IM for team communication | `/lark-im` |
| Formal stakeholder update | `/pmprompt:stakeholder-update-generator` |
| PRD writing | `/pmprompt:prd-writer` |
| Feature prioritization | `/pmprompt:feature-prioritization-assistant` |
| OKR setting | `/pmprompt:okrs` |
| Shape-up style planning | `/pmprompt:shape-up` |
| SOP documentation | `/sop-creator` |
