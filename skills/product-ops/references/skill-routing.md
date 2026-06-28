# Complete Skill Routing Table / 技能路由表

When `product-ops` encounters a user need that a specialized skill handles better, route to that skill. This reference is the complete routing map.

## Decision Flow

```
User request
    │
    ├─ Is it a core ops cadence (daily/weekly/monthly)?
    │   └─ YES → Use internal references/ (daily/weekly/monthly-operations.md)
    │
    ├─ Is it a domain workflow covered by references/?
    │   └─ YES → Load the appropriate reference file
    │
    ├─ Is there a specialized skill that does it better?
    │   └─ YES → Route to that skill (this table)
    │
    └─ None of the above?
        └─ Handle directly with product ops expertise
```

---

## Routing Table

### Money-* Suite (Business Automation)

| User Need | Skill to Invoke | Trigger Keywords |
|-----------|----------------|------------------|
| Deep business diagnosis | `/money-diagnose` | "出什么问题了", "诊断", "为什么下降", "root cause", "diagnose" |
| Content writing (long-form) | `/money-content` | "写文章", "博客", "长文", "blog post", "article" |
| Social media strategy & posts | `/money-social` | "社交媒体", "发推", "小红书", "X/Twitter", "social" |
| SEO optimization | `/money-seo` | "SEO", "搜索优化", "排名", "关键词", "keyword" |
| Financial tracking | `/money-finance` | "收入", "财务", "MRR", "revenue", "finance" |
| Code/product quality review | `/money-quality` | "代码审查", "质量检查", "QA", "测试", "quality" |
| Full business strategy | `/money-strategy` | "战略", "商业模式", "GTM", "strategy" |
| Business retrospective | `/money-retro` | "复盘", "回顾", "反思", "retrospective" |
| Ad campaign management | `/money-ads` | "广告", "投放", "Google Ads", "Meta Ads", "ads" |
| Outreach & sales | `/money-outreach` | "外联", "合作", "BD", "cold email", "outreach" |
| Full product build | `/money-product` | "开发产品", "MVP", "部署", "build product" |
| Autonomous operations setup | `/money-ops` | "自动化", "24/7", "定时任务", "automate" |
| Learnings management | `/money-learn` | "记录经验", "learnings", "教训", "knowledge" |
| Save/restore state | `/money-save` or `/money-restore` | "保存进度", "恢复", "save", "restore" |

### PMPrompt:* Suite (Product Management Frameworks)

| User Need | Skill to Invoke | Trigger Keywords |
|-----------|----------------|------------------|
| PRD writing | `/pmprompt:prd-writer` | "PRD", "需求文档", "产品需求", "spec" |
| OKR setting & tracking | `/pmprompt:okrs` | "OKR", "目标", "关键结果", "objectives" |
| User feedback deep-dive | `/pmprompt:user-feedback-synthesizer` | "反馈分析", "用户声音", "sentiment", "cluster" |
| A/B test design (rigorous) | `/pmprompt:ab-test-designer` | "A/B测试设计", "样本量", "统计显著", "sample size" |
| Feature prioritization (RICE) | `/pmprompt:feature-prioritization-assistant` | "优先级排序", "RICE", "先做哪个", "prioritize" |
| Growth loop design | `/pmprompt:growth-loops` | "增长飞轮", "增长循环", "growth loop", "Reforge" |
| Competitive positioning | `/pmprompt:positioning-canvas` | "市场定位", "差异化", "positioning", "differentiation" |
| Stakeholder update | `/pmprompt:stakeholder-update-generator` | "汇报", "给老板看", "stakeholder", "progress update" |
| PMF survey | `/pmprompt:pmf-survey` | "PMF", "产品市场契合", "would you be disappointed" |
| Jobs-to-be-done | `/pmprompt:jobs-to-be-done` | "用户需求", "JTBD", "jobs to be done", "hire/fire" |
| Hooked model | `/pmprompt:hooked-model` | "用户习惯", "上瘾", "hook", "trigger" |
| Working backwards | `/pmprompt:working-backwards` | "PR/FAQ", "Amazon", "逆向工作", "press release" |
| Product-led growth | `/pmprompt:product-led-growth` | "PLG", "产品驱动增长", "self-serve" |
| Monetization strategy | `/pmprompt:monetizing-innovation` | "定价", "商业化", "变现", "pricing" |
| Strategic narrative | `/pmprompt:strategic-narrative` | "品牌叙事", "企业故事", "narrative" |
| Seven powers | `/pmprompt:seven-powers` | "护城河", "竞争优势", "competitive advantage" |
| Design sprint | `/pmprompt:design-sprint` | "设计冲刺", "5天", "prototype", "design sprint" |
| Shape-up | `/pmprompt:shape-up` | "6周", "appetite", "shaping", "37signals" |
| Opportunity solution tree | `/pmprompt:opportunity-solution-trees` | "机会树", "OST", "Teresa Torres" |
| Thinking in bets | `/pmprompt:thinking-in-bets` | "决策", "概率思维", "uncertainty", "Annie Duke" |
| Radical candor | `/pmprompt:radical-candor` | "反馈", "坦诚", "radical candor" |
| Trustworthy experiments | `/pmprompt:trustworthy-experiments` | "实验可信度", "假阳性", "false positive" |
| Hierarchy of engagement | `/pmprompt:hierarchy-of-engagement` | "用户参与度", "engagement hierarchy" |

### Lark/Feishu Suite (飞书工具)

| User Need | Skill to Invoke | Trigger Keywords |
|-----------|----------------|------------------|
| Create/edit documents | `/lark-doc` | "写文档", "飞书文档", "doc" |
| Work with spreadsheets | `/lark-sheets` | "表格", "飞书表格", "sheet" |
| Manage tasks | `/lark-task` | "任务", "待办", "task" |
| Schedule/manage calendar | `/lark-calendar` | "日历", "日程", "calendar", "会议时间" |
| Meeting minutes | `/lark-minutes` | "会议纪要", "minutes", "录制" |
| Approvals | `/lark-approval` | "审批", "approval" |
| Wiki/knowledge base | `/lark-wiki` | "知识库", "wiki", "文档库" |
| Send messages | `/lark-im` | "发消息", "群聊", "通知", "IM" |
| OKR management | `/lark-okr` | "飞书OKR", "OKR系统" |
| Video calls | `/lark-vc` | "视频会议", "VC", "飞书会议" |
| Whiteboard | `/lark-whiteboard` | "白板", "画图", "whiteboard" |
| File management | `/lark-drive` | "文件", "云盘", "drive" |
| Base/database | `/lark-base` | "多维表格", "base", "bitable" |

### Data & Visualization

| User Need | Skill to Invoke | Trigger Keywords |
|-----------|----------------|------------------|
| Python data analysis | `/pandas-data-analysis` | "pandas", "分析数据", "CSV", "dataframe" |
| Charts & graphs | `/chart-visualization` or `/plotly` | "图表", "画图", "可视化", "chart" |
| Excel automation | `/excel-automation` | "Excel", "xlsx", "表格处理" |
| PDF processing | `/pdf` | "PDF", "提取", "合并" |
| PPTX decks | `/pptx-generator` | "PPT", "幻灯片", "presentation" |
| Documentation (DOCX) | `/document-skills:docx` | "Word", "docx", "文档输出" |

---

## Routing Rules

1. **If the request is unclear**, clarify with one question, then route
2. **If multiple skills could apply**, ask: "This could be done via [A] or [B]. Which focus do you prefer?"
3. **If the skill is not installed**, tell the user and offer to handle the task directly with your product ops knowledge instead
4. **Always pass language context** when routing: "User prefers Chinese/English output"
