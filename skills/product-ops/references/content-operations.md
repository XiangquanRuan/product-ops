# Content Operations / 内容运营

Content creation, release notes, push notifications, help center management, and content calendar workflows for product operations.

## Language

Check for `[Language: 中文]` or `[Language: English]` in context. Default to 中文 if user writes in Chinese.

## Context Injection

If `context.json` is loaded, inject these fields into every output in this file:

| Placeholder | Context Path | Fallback |
|-------------|-------------|----------|
| `{Product Name}` | `company.product_name` | "产品" |
| `{brand tone}` | `brand.tone` | "professional" |
| `{brand voice (zh)}` | `brand.voice_zh` | (omit) |
| `{brand voice (en)}` | `brand.voice_en` | (omit) |
| `{primary channels}` | `brand.primary_channels` | "公众号/邮件" |
| `{hashtags}` | `brand.hashtags` | (omit) |
| `{doc tool}` | `tools.documentation` | (omit) |
| `{comms tool}` | `tools.communication` | (omit) |

**Rule**: Never fabricate context. If a field is null/absent, use the fallback. If the fallback is "(omit)", remove that line/section entirely.

---

## 1. Content Calendar / 内容日历

### Weekly Content Planning

Help the user plan and manage content across all channels:

| Day | Blog/公众号 | Social Media | Push/EDM | Release Notes |
|-----|------------|-------------|----------|---------------|
| Mon | — | Product tip | — | — |
| Tue | Feature deep-dive | User story | — | — |
| Wed | — | Industry insight | Feature update | If released |
| Thu | How-to guide | Behind the scenes | Weekly digest | — |
| Fri | — | Community spotlight | — | Changelog |

### Output Format: Weekly Content Calendar

```
📅 内容日历 | Content Calendar — {Week}

周一 Monday:
• 公众号/博客: {topic} — 状态: {draft/ready/published}
• 社交媒体: {post type + topic}
• 推送: {audience + message}

周二 Tuesday:
...

本周重点内容 Key Content:
🎯 {theme or campaign}
📊 目标 KPI: {views/engagement/conversion targets}

上周内容复盘 Last Week Review:
• 最佳内容 Top Performer: {title} — {views} views, {engagement}% engagement
• 需要优化 Needs Improvement: {title} — {note}
```

---

## 2. Release Notes / 产品更新公告

### Structure

Every release note should answer:
1. **What's new?** (新功能/改进)
2. **Why does it matter?** (用户价值)
3. **How to use it?** (快速指引)
4. **What's fixed?** (修复)

### Template: Standard Release Notes

```
🚀 {Product Name} v{version} 更新 | Release Notes
📅 {Date}

✨ 新功能 New Features

{Feature Name}
{一句话描述价值 One-line value proposition}
• {capability 1}
• {capability 2}
→ 如何使用 How to use: {brief instruction or link}

🔧 改进 Improvements
• {improvement 1}
• {improvement 2}

🐛 修复 Bug Fixes
• {issue} — 感谢 @{user} 的反馈
• {issue}

📲 更新方式 How to Update:
• Web: 已自动更新 Already live
• iOS/Android: App Store / Google Play 更新
```

### Release Notes Length Guide

| Channel | Length | Tone |
|---------|--------|------|
| In-app popup | 3-5 bullet points | Excitement + value |
| App Store update | 2-3 paragraphs | Feature-focused |
| Blog post | 500-800 words | Detailed + narrative |
| Push notification | 1-2 sentences | Action-oriented |
| Email newsletter | 3-5 sections | Value + links |
| Slack/Lark announcement | 1 paragraph + link | Team-focused |

---

## 3. Push Notifications / 推送通知

### Push Notification Strategy

```
📲 推送策略 | Push Notification Strategy

推送类型 Types:
• 功能更新 Feature Update: 新功能上线通知
• 内容推荐 Content: 个性化内容推送
• 行为触发 Behavioral: 用户行为触发(如: 24h未登录)
• 活动营销 Campaign: 促销/活动通知
• 系统通知 System: 安全/隐私/条款更新
• 社交互动 Social: 评论/点赞/关注

推送频次 Frequency Guidelines:
• 每日上限 Max/day: {2-3}
• 每周上限 Max/week: {5-7}
• 最佳时段 Best time: {based on user analytics}
• 静默时段 Quiet hours: {22:00-08:00}

A/B 测试要点 A/B Test Checklist:
• 标题 Title: {2+ variants}
• 文案 Body: {2+ variants}
• 发送时间 Send time: {test morning vs evening}
• 深度链接 Deep link: {direct to feature vs home}
```

### Push Copy Template

```
📱 推送文案 | Push Copy

标题 Title (max ~40 chars):
• "{compelling hook}"

正文 Body (max ~120 chars):
• "{value prop + call to action}"

深度链接 Deep Link:
• {scheme://path}

发送时间 Send Time:
• {datetime}

目标用户 Audience:
• {segment description}
• 预计触达 Estimated Reach: {n} users
```

---

## 4. Help Center & FAQ Management / 帮助中心管理

### Help Center Gap Analysis

Periodically audit what's missing from help docs:

1. **Review top support tickets** — what questions are users asking?
2. **Check search queries** — what are users searching for in help?
3. **Audit new features** — do all new features have docs?
4. **Check outdated content** — any screenshots or steps no longer accurate?

### FAQ Article Template

```
❓ {Question as user would ask it}

简短回答 Short Answer:
{1-2 sentence direct answer}

详细步骤 Step-by-Step:
1. {step 1}
2. {step 2}
3. {step 3}

📸 截图 Screenshots:
[insert or mark placeholder]

💡 提示 Tips:
• {helpful tip}

🔗 相关文章 Related:
• {link to related FAQ}
• {link to related FAQ}

遇到问题？Need Help?
联系客服 Contact support: {channel}
```

---

## 5. Social Media Content / 社交媒体内容

For social media strategy and post writing → route to `/money-social` for comprehensive platform strategies.

For quick social post drafting in this skill:

### Platform-Specific Formats

**X/Twitter Thread**:
```
1/ {hook — main insight}
2/ {supporting point or data}
3/ {example or story}
4/ {key takeaway}
5/ {call to action + link}
```

**小红书 Post**:
```
📌 {标题: 突出痛点或效果}
{正文: 个人经历 + 解决方案 + 效果展示}
#标签1 #标签2 #标签3
📸 {图1: 效果对比} {图2: 使用过程}
```

**LinkedIn Post**:
```
{Strong opening hook — 2 lines max}
{Story or insight — 3-4 paragraphs}
{Key takeaway — bold or bullet}
{Call to action — question or link}
#hashtag1 #hashtag2
```

---

## 6. Content Performance Review / 内容效果复盘

### Metrics to Track by Content Type

| Content Type | Primary Metric | Secondary Metrics |
|-------------|---------------|-------------------|
| Blog post | Page views | Time on page, shares, backlinks, conversions |
| Release notes | Read rate | Feature adoption after read |
| Push notification | CTR | Conversion, opt-out rate |
| Email newsletter | Open rate | CTR, unsubscribe rate |
| Social post | Engagement rate | Shares, comments, link clicks |
| Help article | Was-this-helpful % | Search ranking, ticket deflection |

### Content Review Template

```
📊 内容效果复盘 | Content Performance Review — {Period}

🏆 表现最佳 Top Performers:
1. {title} — {metric}: {value} — 亮点 Why it worked: {reason}
2. {title} — {metric}: {value} — 亮点 Why it worked: {reason}

📉 需要优化 Underperformers:
1. {title} — {metric}: {value} — 原因 Why: {reason} — 调整 Adjust: {change}

📈 趋势 Trends:
• 总体阅读量 Total views: {current} vs previous ({change}%)
• 平均互动率 Avg engagement: {current}% vs previous ({change}%)
• 转化率 Conversion rate: {current}% vs previous ({change}%)

💡 内容策略调整 Content Strategy Pivot:
• 继续做 Keep: {practices that work}
• 停止做 Stop: {practices that don't}
• 开始做 Start: {new things to try}
```

---

## 7. External Skill Routing

| Need | Route To |
|------|----------|
| Full article/blog writing | `/money-content` |
| Social media strategy | `/money-social` |
| SEO optimization for content | `/money-seo` |
| Creating docs in Feishu | `/lark-doc` |
| Updating wiki | `/lark-wiki` |
| Sending announcements via IM | `/lark-im` |
| Email campaign copy | `/money-outreach` |

---

## Templates

- Content calendar: Draft in conversation or use `/lark-sheets`
- Release notes: `assets/` (coming in next iteration)
