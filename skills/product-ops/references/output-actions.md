# Output Actions / 输出动作

After generating content, offer to deliver it — not just as text, but as real documents, messages, and files.

## Language

Check for `[Language: 中文]` or `[Language: English]` in context.

---

## Standard Output Channels

After every workflow that produces output, ask the user ONE question about delivery:

```
📤 输出方式：
1. 📄 创建飞书文档 (在线协作)
2. 💬 发送到群聊 (团队同步)
3. 💾 保存为文件 (.md / .docx)
4. 📋 复制到剪贴板 (我自己粘贴)
5. ⏭ 跳过 (已经够了)
```

### Channel 1: 飞书文档 (Lark Doc)

For reports, meeting minutes, PRDs, launch plans, and any content that needs team collaboration.

**Implementation**:
1. Format the content as Markdown
2. Call `/lark-doc` to create a new document
3. Set appropriate title: `{type} — {product} — {date}` (e.g., `周报 — TeamCollab — 2026-W26`)
4. Return the document link to the user

**Title conventions by workflow**:

| Workflow | Title Pattern |
|----------|-------------|
| Daily standup | `站报 — {date}` |
| Weekly report | `周报 — {product} — {week}` |
| Monthly review | `月报 — {product} — {month}` |
| Launch checklist | `上线检查 — {feature} — {date}` |
| Meeting minutes | `会议纪要 — {topic} — {date}` |
| Stakeholder update | `进展汇报 — {audience} — {date}` |
| Competitive intel | `竞品分析 — {competitor} — {date}` |
| PRD / Spec | `产品需求 — {feature} — {version}` |

### Channel 2: 群聊消息 (IM)

For standup updates, quick announcements, and short reports that teams need to see immediately.

**Implementation**:
1. Condense the output to a 3-5 bullet summary (standup-length)
2. Call `/lark-im` to send to the appropriate chat/group
3. Offer to include @mentions from context (`team.key_contacts`)

**Message length guidelines**:

| Content Type | Max Length | Format |
|-------------|-----------|--------|
| Standup | 5 bullets | Plain text |
| Weekly summary | 8 bullets | Plain text + link |
| Launch alert | 3 bullets | Bold key info |
| Urgent escalation | 2 bullets | @mention + action |
| Regular announcement | 1 paragraph | Friendly tone |

### Channel 3: 保存文件 (File Save)

For archival, offline access, or sharing with people outside Feishu.

**Formats**:

| Format | Use For | How |
|--------|---------|-----|
| `.md` | Developer-facing docs, GitHub | Direct write |
| `.docx` | Leadership reports, formal docs | `/document-skills:docx` |
| `.xlsx` | Data tables, metrics reports | `/document-skills:xlsx` or `/lark-sheets` |
| `.pptx` | Presentations, board decks | `/pptx-generator` |
| `.pdf` | Final deliverables | `/pdf` |

**File naming convention**: `{type}_{product}_{date}.{ext}` (e.g., `weekly-report_TeamCollab_2026-W26.docx`)

### Channel 4: 剪贴板 (Clipboard)

User just wants the text. Print it and move on.

---

## Integration with Context

If context.json is loaded:

- **`tools.communication` = `lark`** → Default to Channels 1 & 2 (飞书文档 + 群聊)
- **`tools.communication` = `slack`** → Format for Slack, draft as copy-paste
- **`tools.documentation` = `lark-wiki`** → Offer to save to wiki instead of doc
- **`brand.tone`** → Apply tone to all messages and document titles

---

## Auto-Delivery Rules

| Workflow | Default Channel | Rationale |
|----------|----------------|-----------|
| Daily standup | IM | Team needs to see it in chat |
| Weekly report | Doc + IM summary | Full doc for archive, summary for team |
| Monthly review | Doc + File (.docx) | Formal report for leadership |
| Launch checklist | Doc | Collaborative tracking |
| Stakeholder update | File (.docx) | Formal deliverable |
| Release notes | Doc + IM | Both team and users need it |
| Meeting minutes | Doc | Permanent record |

---

## Error Handling

- If `/lark-doc` fails → offer File save as fallback
- If `/lark-im` fails → format as copy-paste for manual posting
- If no external skill available → always fall back to Clipboard (Channel 4)
- **Never block delivery** — if one channel fails, offer alternatives
