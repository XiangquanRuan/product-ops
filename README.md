# Product Operations Skill (产品运营技能)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-0.1.0-green)](.claude-plugin/plugin.json)

A unified Claude Code plugin for **Product Operations (产品运营)** professionals. Covers daily operations, data reporting, user feedback, content ops, growth experiments, competitive intelligence, launch playbooks, and cross-team coordination.

**Bilingual**: Full support for 中文 and English.

---

## What This Plugin Does

This plugin provides a **smart router skill** (`product-ops`) that understands what you need and routes you to the right workflow — whether it's an original product-ops playbook or an existing specialized skill.

### Daily Operations
> "今天站会" / "daily standup" → Morning check-in, standup report, EOD summary

### Weekly Operations
> "生成周报" / "weekly report" → Full weekly report with metrics, user insights, competitive scan

### Monthly Operations  
> "本月月报" / "monthly review" → Monthly business review, OKR tracking, next month planning

### Data Analysis & Reporting
> "帮我看看这个数据" / "analyze this data" → KPI dashboards, funnel analysis, cohort analysis

### User Feedback Management
> "用户反馈怎么处理" / "process user feedback" → Collection, categorization, prioritization, routing

### Content Operations
> "写上线公告" / "write release notes" → Release notes, push notifications, help center, content calendar

### Growth Experiments
> "设计一个A/B测试" / "design an A/B test" → Experiment design, results analysis, growth strategy

### Competitive Intelligence
> "竞品分析" / "competitive analysis" → Feature matrix, market signals, battle cards

### Project Coordination
> "帮我排需求优先级" / "prioritize features" → Sprint planning, meeting management, stakeholder updates

### Launch Playbook
> "产品要上线了" / "product launch" → Pre-launch checklist, launch day ops, post-launch monitoring

---

## Installation

### Prerequisites

- [Claude Code](https://claude.ai/code) installed

### Install via GitHub

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/product-ops.git

# Install as a Claude Code plugin
claude plugins install ./product-ops
```

Or install directly from GitHub:

```bash
claude plugins install https://github.com/YOUR_USERNAME/product-ops.git
```

### Manual Installation

Copy the `skills/product-ops/` directory to your Claude Code skills folder:

```bash
cp -r skills/product-ops ~/.claude/skills/
```

---

## Usage

Once installed, the `product-ops` skill is auto-discovered. Simply say:

```
/product-ops 帮我生成本周周报
```

Or just describe what you need — Claude will auto-trigger the skill:

```
我需要写一份本周的产品运营周报，包含数据分析和用户反馈
```

### Recommended Companion Skills

For full functionality, install these companion skills:

| Plugin / Skill | Purpose |
|---------------|---------|
| `@orrisai/show-me-the-money` | Business automation suite (money-*) |
| `pmprompt-skills` | Product management frameworks |
| `lark-*` skills | Feishu/Lark integration (for 飞书 users) |
| `pandas-data-analysis` | Python data analysis |
| `chart-visualization` | Data visualization |

---

## Plugin Structure

```
product-ops/
├── .claude-plugin/
│   └── plugin.json              # Plugin manifest
├── skills/
│   └── product-ops/
│       ├── SKILL.md             # Main router (entry point)
│       ├── references/          # 12 domain workflow files
│       │   ├── onboarding.md          # One-time context setup wizard (NEW)
│       │   ├── daily-operations.md
│       │   ├── weekly-operations.md
│       │   ├── monthly-operations.md
│       │   ├── data-reporting.md
│       │   ├── user-feedback.md
│       │   ├── content-operations.md
│       │   ├── growth-experiments.md
│       │   ├── competitive-intel.md
│       │   ├── project-coordination.md
│       │   ├── launch-playbook.md
│       │   └── skill-routing.md
│       └── assets/              # 7 fill-in templates
│           ├── context-schema.md       # Context JSON schema reference (NEW)
│           ├── daily-standup-template.md
│           ├── weekly-report-template.md
│           ├── monthly-report-template.md
│           ├── launch-checklist.md
│           ├── ab-test-design-template.md
│           └── stakeholder-update-template.md
├── README.md
└── LICENSE
```

---

## Privacy & Security / 隐私与安全

Your company data stays with you — always:

| Concern | Answer |
|---------|--------|
| **Where is my data stored?** | Local file: `~/.product-ops/projects/{slug}/context.json` |
| **Is it uploaded anywhere?** | No. Never automatically transmitted. |
| **Is it in the GitHub repo?** | No. Excluded via `.gitignore`. |
| **What about the API?** | Data loaded into conversations goes through the Claude API, same as anything you type. Follows [Anthropic's data usage policy](https://www.anthropic.com/legal). |
| **Can I see what's stored?** | Say 「查看我的配置」/ "show my context" |
| **Can I delete it?** | Say 「删除配置」/ "delete context" — removes everything |
| **What should I NOT store?** | Passwords, API keys, exact revenue numbers, user PII. Provide these in conversation, not in config. |
| **Industry compliance?** | Built for general use. For HIPAA/SOC2/PCI, evaluate with your security team. |

**Design principles**:
- 🟢 **Tier 1** (recommended): Product name, industry, competitor names — low sensitivity
- 🟡 **Tier 2** (optional): Metric definitions, team structure, brand tone
- 🔴 **Tier 3** (per-session only): Specific revenue, DAU numbers, user data — never stored

---

## Contributing

Contributions welcome! Common ways to contribute:

1. **Add workflows** — New product ops scenarios not yet covered
2. **Improve templates** — Make them more comprehensive or industry-specific
3. **Translate** — Improve English or Chinese localization
4. **Add integrations** — Connect with more tools (Jira, Linear, Notion, etc.)

### Development

```bash
# Clone and enter
git clone https://github.com/YOUR_USERNAME/product-ops.git
cd product-ops

# Test the skill in Claude Code
claude
# Then: /product-ops 测试

# Validate plugin structure
claude plugins validate .
```

---

## Roadmap

- [ ] Notion/Jira/Linear integration workflows
- [ ] User segmentation & cohort analysis templates
- [ ] Revenue operations (RevOps) workflows
- [ ] Community management workflows
- [ ] Automated recurring schedule setup scripts
- [ ] Industry-specific variants (SaaS, E-commerce, Gaming, Fintech)

---

## License

MIT © Product Ops Community

---

## About

Built for product operations professionals who want to leverage AI to automate their daily workflows, generate better reports, and make data-driven decisions — in both Chinese and English environments.

**Made with Claude Code**
