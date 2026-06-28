# Onboarding / 项目配置向导

One-time setup to configure the skill for your company, product, and industry. This creates a local `context.json` file that all workflows automatically load.

## Language

Check for `[Language: 中文]` or `[Language: English]` in context. Default to 中文 if user writes in Chinese.

---

## Privacy Notice (shown to user first)

Before collecting any information, show this:

```
🔒 隐私说明 | Privacy Notice

在开始配置之前，请了解以下重要信息：

1. 所有信息保存在本地文件: ~/.product-ops/projects/{slug}/context.json
2. 不会自动上传到任何服务器
3. 不会随 GitHub 共享（已配置 .gitignore 排除）
4. 配置分为三层，你可以自由选择填写程度：
   🟢 基础层 — 推荐填写（行业、产品名、竞品名等公开信息）
   🟡 进阶层 — 可选填写（指标定义、团队结构等描述信息）
   🔴 敏感层 — 不存储（具体营收数字、用户数据等，每次对话中临时提供）
5. 你可以随时说「查看我的配置」「删除配置」「修改配置」

准备好了吗？我们开始吧。
```

---

## Step 1: Project Slug

Determine the project slug for file storage:

1. Check current working directory: `basename($(pwd))`, sanitize to `[a-z0-9-]`
2. Ask user to confirm or provide an alternative name
3. Slug is used for file path: `~/.product-ops/projects/{slug}/context.json`

> 📁 项目标识: `{slug}` (从当前目录自动检测)
> 确认使用这个名称？输入新的名称来修改，或直接回车确认。

---

## Step 2: Tier 1 Configuration (🟢 Basic)

Collect the low-sensitivity basics. Keep it conversational — one message, not a survey.

> 先来一些基础信息（全部可选，跳过也可以）：
>
> 1. 🏢 **公司和产品名称** — 例：某科技公司 / TeamCollab
> 2. 🌐 **产品网址** — 例：https://teamcollab.io
> 3. 🏭 **行业** — SaaS / 电商 / 游戏 / 金融 / 内容媒体 / 教育 / 医疗 / 企业服务 / 开发者工具 / 消费应用 / 本地零售 / 服务 / 硬件IoT / 其他
> 4. 📱 **产品平台** — Web / iOS / Android / 桌面 / 微信小程序 / 其他
> 5. 💰 **商业模式** — 订阅 / 交易抽成 / 广告 / 免费增值 / 按量计费 / 混合 / 其他
> 6. 🎯 **一句话价值主张** — 你的产品帮用户解决什么问题？

Parse the user's response. Fill what they give, leave blanks for what they skip. No pressure.

---

## Step 3: Tier 2 Configuration (🟡 Advanced)

Ask only the questions that matter based on what they'll use. Frame as "这些信息能让周报和分析更精准":

> 以下信息让输出更贴近你的实际情况（同样全部可选）：
>
> 1. 📊 **怎么称呼你的核心指标？**
>    - 日活叫什么？（DAU / 日活跃用户 / 日活跃团队 / ...）
>    - 收入叫什么？（MRR / GMV / 流水 / ...）
> 2. 📈 **数据在哪看？**
>    - 分析工具: Amplitude / 神策 / Google Analytics / 飞书表格 / CSV / 手动
>    - 如果用飞书表格: **直接粘贴表格链接**，以后说「周报」自动拉数据
>    - 如果用其他工具: 暂时需要手动粘贴或导出 CSV（社区正在开发更多连接器）
>    - 看板链接（如果有的话）
> 3. 👥 **目标用户是谁？** — 一两句话描述核心用户画像
> 4. 🏃 **团队基本结构** — 有哪些角色？迭代周期多长？
> 5. 🎨 **品牌调性** — 专业正式 / 轻松活泼 / 技术极客 / 温暖亲切 / ...
> 6. 📢 **主要发布渠道** — 公众号 / 小红书 / Twitter / LinkedIn / 邮件 / ...

Again, parse natural responses. Nothing is required.

---

## Step 4: Competitor Setup

Competitor context is especially valuable. Make it easy:

> 说几个你的竞品，我就帮你追踪：
>
> **直接竞品**（用户会拿你们对比的）：
> 1. {name} — 它比你们强在哪？比你们弱在哪？（可选）
> 2. {name} — ...
>
> **间接竞品**（替代方案，但不是同类产品）：
> 1. {name}
> 2. {name}
>
> **你的差异化优势**（你和他们最大的不同是什么？）（可选）

Accept "Notion / 飞书 / Confluence" shorthand format — expand into entries.

---

## Step 5: Tool Chain

This determines which companion skills are relevant:

> 你们团队用什么工具？（选填）：
>
> • 沟通: 飞书 / Slack / 钉钉 / Teams / 其他
> • 任务管理: 飞书任务 / Jira / Linear / Notion / Trello / 其他
> • 文档: 飞书知识库 / Notion / Confluence / 其他
> • 上线发布节奏: 每日 / 每周 / 双周 / 每月 / 持续部署
> • 监控工具: Datadog / Grafana / Sentry / 其他

## Step 5.5: Data Source Setup (if applicable)

If the user selected 飞书表格 as their data source in Step 3:

> 我可以通过飞书表格自动读取你的运营数据。
>
> 📋 **推荐表格结构**（可直接复制创建）：
> ```
> | 日期 | DAU | 新增用户 | D7留存 | 收入 | 转化率 | 崩溃率 |
> ```
>
> 📎 粘贴你的表格链接，以后说「周报」我会自动拉数据。没准备好的话说「跳过」，后续手动输入也行。

If the user selected another tool (Amplitude etc.):

> {tool} 目前还不支持自动拉取数据。两种方式：
> 1. 每周导出 CSV 给我，我自动解析
> 2. 直接粘贴数字，同样很快
>
> 💡 更多连接器正在由社区开发中。你也可以贡献一个：`connectors/CONTRIBUTING.md`

---

## Step 6: Generate Context

After collecting responses, generate the `context.json` file:

### File Creation

```python
# Pseudocode for how the skill generates the file

import json, os
from datetime import datetime

slug = "teamcollab"  # from Step 1
context_dir = os.path.expanduser(f"~/.product-ops/projects/{slug}")
os.makedirs(context_dir, exist_ok=True)

context = {
    "_meta": {
        "version": "1.0",
        "created_at": datetime.now().isoformat(),
        "slug": slug,
        "language": "zh-CN"  # from language selection
    },
    "company": { ... },   # from Step 2
    "product": { ... },   # from Step 2-3
    "metrics": { ... },   # from Step 3
    "competitors": { ... },# from Step 4
    "team": { ... },      # from Step 3
    "tools": { ... },     # from Step 5
    "brand": { ... },     # from Step 3
    "releases": { ... },  # from Step 5
    "experiments": {}     # empty, populated incrementally
}

with open(os.path.join(context_dir, "context.json"), "w", encoding="utf-8") as f:
    json.dump(context, f, ensure_ascii=False, indent=2)
```

### Confirmation Message

After saving, show the user what was saved and what to do next:

```
✅ 配置完成！已保存到 ~/.product-ops/projects/{slug}/context.json

📋 已保存的信息:
🟢 Tier 1: {summary of what was filled}
🟡 Tier 2: {summary of what was filled}
🔌 数据连接: {lark-sheets auto-fetch / manual / csv}

🔜 下一步:
• 试试说「本周周报」— 如果你配了飞书表格，数据会自动拉取
• 没有配数据源？下次说「周报」时手动粘贴数字也能用
• 随时说「修改配置」来更新
• 说「查看我的配置」来看当前保存了哪些信息
• 说「删除配置」来清除所有已保存信息
```

---

## Onboarding Update Path

User says any of these to modify context:

| User says | Action |
|-----------|--------|
| "更新公司信息" / "update company" | Re-do Step 2 only |
| "修改配置" / "update context" | Show current context, ask which section to update |
| "添加竞品" / "add competitor" | Add to competitors list |
| "查看我的配置" / "show my context" | Display current context.json contents |
| "删除配置" / "delete context" | Confirm then delete `~/.product-ops/projects/{slug}/` |
| "重新配置" / "reset context" | Wipe and re-run full onboarding |

---

## References

- Context schema: `assets/context-schema.md`
- All context-aware workflows are in `references/` (see each file's § Context Loading section)
