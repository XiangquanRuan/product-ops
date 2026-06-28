# User Feedback Management / 用户反馈管理

Systematic user feedback collection, categorization, prioritization, and action routing for product operations.

## Language

Check for `[Language: 中文]` or `[Language: English]` in context. Default to 中文 if user writes in Chinese.

## Context Injection

If `context.json` is loaded, inject these fields into every output in this file:

| Placeholder | Context Path | Fallback |
|-------------|-------------|----------|
| `{Product Name}` | `company.product_name` | "产品" |
| `{target users}` | `product.target_users_icp` | (omit) |
| `{comms tool}` | `tools.communication` | "Slack" |
| `{task tool}` | `tools.task_management` | (omit) |
| `{doc tool}` | `tools.documentation` | (omit) |
| `{feedback sources}` | (infer from tools + channels) | (omit) |

**Rule**: Never fabricate context. If a field is null/absent, use the fallback. If the fallback is "(omit)", remove that line/section entirely.

---

## 1. Feedback Collection Framework / 反馈收集框架

### Common Sources

| Source | What You Get | How to Access |
|--------|-------------|---------------|
| App Store reviews | Star rating + text | App Store Connect, Google Play Console |
| Support tickets | Detailed problem reports | Zendesk, Intercom, 飞书服务台 |
| NPS surveys | Score + open feedback | Typeform, 问卷星, 飞书问卷 |
| User interviews | Deep qualitative insights | Recording, transcripts |
| Social media mentions | Unfiltered opinions | X/Twitter, Reddit, 小红书, 微博 |
| Product analytics | Behavioral signals | Amplitude, Mixpanel, 神策 |
| In-app feedback | Contextual feedback | In-app widgets, 反馈入口 |
| Beta testing | Pre-release feedback | TestFlight, 内测群 |

### Ask the User

When a user says "帮我看看用户反馈":
1. Ask which sources they have
2. Ask them to paste/share the feedback (or point to it)
3. Ask how many feedback items there are (rough count)

---

## 2. Feedback Categorization / 反馈分类

### Categorization Framework

Process each piece of feedback into:

```
每条反馈处理模板:

📝 原文 Original: "{user's exact words}"

🏷 分类 Category:
• Bug / 缺陷
• Feature Request / 功能需求
• UX Issue / 体验问题
• Content/Docs / 内容问题
• Performance / 性能问题
• Pricing/Billing / 付费问题
• Other / 其他

🔥 严重程度 Severity:
• P0 — 核心功能不可用 / Core flow broken
• P1 — 严重影响使用 / Major impact
• P2 — 中等影响，有Workaround / Moderate impact
• P3 — 低影响，锦上添花 / Minor / Nice-to-have

👥 影响面 Reach:
• 个别用户 Individual ({count} reports)
• 小范围 Small group ({count} reports)
• 广泛 Widespread ({count} reports)
• 未知 Unknown

🎯 关联功能 Affected Feature: {feature name}

💡 建议动作 Suggested Action:
• 立刻修复 Fix now
• 下个版本 Next release
• 排入Backlog Roadmap
• 回复用户 Reply to user
• 继续观察 Monitor
```

---

## 3. Feedback Synthesis / 反馈汇总

Produce a structured synthesis when processing multiple feedback items:

### Output Format

```
🗣 用户反馈汇总 | User Feedback Digest
📅 {Date Range or Batch}

━━━━━━━━━━━━━━━━━━━━━━━

📊 概览 Overview:
• 总反馈数 Total: {n}
• Bug: {n} | 功能需求 Feature Req: {n} | 体验 UX: {n} | 内容 Content: {n} | 其他 Other: {n}
• P0: {n} | P1: {n} | P2: {n} | P3: {n}

━━━━━━━━━━━━━━━━━━━━━━━

🔴 需要立刻处理 Urgent (P0/P1):

1. {issue title}
   • 来源 Source: {source}
   • 影响 Impact: {description of impact}
   • 用户声音 User Voice: "{quote}"
   • 建议 Action: {what to do}
   • 提案人 Reported by: {n} users

2. {issue title}
   ...

━━━━━━━━━━━━━━━━━━━━━━━

🟡 需要关注 Important (P2):

1. {issue title} — {n} users reported
2. {issue title} — {n} users reported

━━━━━━━━━━━━━━━━━━━━━━━

🟢 可后续处理 Backlog (P3):

{n} items — 摘要 Summary: {one-line summary}

━━━━━━━━━━━━━━━━━━━━━━━

📈 趋势 Trends:
• {trend 1}: {description}
• {trend 2}: {description}

💡 洞察 Insights:
• {insight 1}
• {insight 2}
```

---

## 4. From Feedback to Product Action

### Workflow

```
Collect → Categorize → Prioritize → Route → Track
```

1. **Collect**: Gather feedback from all sources
2. **Categorize**: Apply categories + severity + affect
3. **Prioritize**: Which feedback items matter most?
4. **Route**: Send to the right team/person
   - Bug → Engineering (via `/lark-task` or issue tracker)
   - Feature Request → PM backlog (route to `/pmprompt:feature-prioritization-assistant`)
   - UX → Design team
   - Content/Docs → Content team
5. **Track**: Follow up and close the loop with users

### Prioritization Matrix

Use Impact × Frequency to prioritize:

```
                高频 High Frequency
                      │
      快速修复         │        核心优化
   Quick Fix          │       Core Improvement
                      │
   ──────────────────┼──────────────────
                      │
      低优先级         │        调研评估
   Low Priority       │       Investigate
                      │
                低频 Low Frequency
              
小影响 Small Impact           大影响 Big Impact
```

---

## 5. Closing the Loop with Users / 用户回复

After resolving feedback, help draft user replies:

### Reply Templates

**Bug fixed**:
```
"Hi {name}, thanks for reporting the {issue}. This has been fixed in version {version}. 
Let us know if you see it again! 
感谢反馈，该问题已在 {version} 版本修复。如有问题请随时告知。"
```

**Feature request received**:
```
"Hi {name}, thanks for the suggestion! We've added {feature} to our roadmap. 
We'll keep you posted on progress. 
感谢你的建议！{feature} 已加入我们的产品路线图，有进展会同步给你。"
```

**Need more info**:
```
"Hi {name}, thanks for the feedback. Could you share more about {specific question}? 
It would help us understand better. 
感谢反馈。方便分享更多关于 {specific question} 的信息吗？这能帮助我们更好地理解你的需求。"
```

---

## 6. External Skill Routing

For specific needs:
- **Deep feedback theme extraction** → `/pmprompt:user-feedback-synthesizer`
- **Understanding underlying user motivations** → `/pmprompt:jobs-to-be-done`
- **Feature prioritization** → `/pmprompt:feature-prioritization-assistant`
- **Bug quality review** → `/money-quality`
- **Creating tasks for feedback follow-up** → `/lark-task`
- **Writing survey questions** → `/lark-minutes` (or draft directly)

---

## Integration Notes

- **Lark/飞书 users**: Use `/lark-sheets` to track feedback in a spreadsheet; `/lark-task` to create action items; `/lark-im` to notify teams
- **For large datasets** (>100 feedback items): Suggest using `/pandas-data-analysis` for batch processing
- **For user interviews**: Route to `/lark-minutes` for transcription and summary
