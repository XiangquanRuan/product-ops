# Context Schema / 上下文数据模式

This document defines the structure of `~/.product-ops/projects/{slug}/context.json`.

**Privacy**: This file is always local — never uploaded or committed to git. See `references/onboarding.md` § Privacy & Security for full details.

---

## Schema

```json
{
  "_meta": {
    "version": "1.0",
    "created_at": "ISO8601",
    "updated_at": "ISO8601",
    "slug": "project-slug",
    "language": "zh-CN | en-US"
  },

  "company": {
    "name": "string | null",
    "product_name": "string | null",
    "url": "string | null",
    "industry": "saas | ecommerce | gaming | fintech | content-media | edtech | healthtech | enterprise | developer-tools | consumer-app | retail-local | service | hardware-iot | other",
    "industry_detail": "string | null",
    "stage": "seed | early | growth | mature",
    "size": "1-10 | 11-50 | 51-200 | 201-1000 | 1000+",
    "headquarters": "string | null",
    "founded": "YYYY | null"
  },

  "product": {
    "north_star_metric": "string | null",
    "core_value_prop": "string | null",
    "target_users_icp": "string | null",
    "platforms": ["web", "ios", "android", "desktop", "wechat-mini", "other"],
    "business_model": "subscription | transaction | advertising | freemium | usage-based | hybrid | other",
    "key_features": ["string (3-5 most important)"],
    "pricing_tiers": [
      {"name": "string", "price": "string", "description": "string"}
    ]
  },

  "metrics": {
    "definitions": {
      "dau": {"name": "string", "description": "string | null"},
      "new_users": {"name": "string", "description": "string | null"},
      "retention_d7": {"name": "string", "description": "string | null"},
      "retention_d30": {"name": "string", "description": "string | null"},
      "revenue": {"name": "string", "description": "string | null"},
      "conversion": {"name": "string", "description": "string | null"}
    },
    "data_sources": {
      "analytics_tool": "amplitude | mixpanel | shenCe | growingIo | googleAnalytics | firebase | custom | other | null",
      "dashboard_url": "string | null",
      "sheets_url": "string | null"
    },
    "targets": {
      "dau_target": "string | null",
      "revenue_target": "string | null",
      "retention_target_d7": "string | null",
      "conversion_target": "string | null"
    }
  },

  "competitors": {
    "direct": [
      {
        "name": "string",
        "url": "string | null",
        "strength": "string | null",
        "weakness": "string | null",
        "note": "string | null"
      }
    ],
    "indirect": [
      {
        "name": "string",
        "url": "string | null",
        "note": "string | null"
      }
    ],
    "our_differentiation": "string | null"
  },

  "team": {
    "structure": "string | null",
    "roles": ["string (e.g., PM, Engineer, Designer, Marketing, Support)"],
    "standup_time": "string | null",
    "sprint_cadence": "1-week | 2-week | other | null",
    "key_contacts": {
      "pm": "string | null",
      "engineering_lead": "string | null",
      "design_lead": "string | null",
      "marketing_lead": "string | null"
    }
  },

  "tools": {
    "communication": "lark | slack | dingtalk | teams | other | null",
    "task_management": "lark-task | jira | linear | notion | trello | other | null",
    "documentation": "lark-wiki | notion | confluence | gitbook | other | null",
    "analytics": "amplitude | mixpanel | shenCe | growingIo | googleAnalytics | other | null",
    "cicd": "github-actions | gitlab-ci | jenkins | other | null",
    "monitoring": "datadog | grafana | sentry | prometheus | other | null"
  },

  "brand": {
    "tone": "professional | casual | technical | playful | premium | warm | other",
    "voice_zh": "string | null",
    "voice_en": "string | null",
    "primary_channels": ["string (blog, wechat, xiaohongshu, twitter, linkedin, newsletter, etc.)"],
    "hashtags": ["string"]
  },

  "releases": {
    "typical_cadence": "daily | weekly | biweekly | monthly | continuous | other",
    "feature_flag_tool": "launchdarkly | split | custom | other | null",
    "rollout_strategy": "string | null",
    "rollback_procedure": "string | null"
  },

  "experiments": {
    "active_count": "number | null",
    "primary_tool": "string | null",
    "typical_sample_size": "string | null",
    "typical_duration_days": "number | null",
    "significance_level": "0.95 | 0.99 | null",
    "historical_learnings": ["string"]
  }
}
```

---

## Privacy Tier Classification

### 🟢 Tier 1: Low Sensitivity (recommended to fill)
Basic info that's usually public or already known in conversation.

- `_meta.*`
- `company.name`, `company.product_name`, `company.url`, `company.industry`
- `product.core_value_prop`, `product.platforms`, `product.business_model`
- `competitors.direct[].name`, `competitors.indirect[].name`
- `tools.*` (which tools you use, not credentials)
- `brand.tone`, `brand.primary_channels`
- `releases.typical_cadence`

### 🟡 Tier 2: Medium Sensitivity (fill if comfortable)
Descriptive but not numeric; useful for context-aware output.

- `company.stage`, `company.size`
- `product.north_star_metric`, `product.target_users_icp`, `product.key_features`
- `metrics.definitions.*` (metric names, not values)
- `metrics.data_sources.*` (tool names, not URLs)
- `competitors.our_differentiation`
- `team.structure`, `team.roles`, `team.sprint_cadence`
- `brand.voice_zh`, `brand.voice_en`

### 🔴 Tier 3: High Sensitivity (avoid storing — provide per-session)
Numeric metrics, dollar amounts, specific targets. Provide these in conversation, not in config.

- `metrics.targets.*` — provide when generating reports
- Actual DAU/revenue/retention numbers — provide per-session
- `product.pricing_tiers` — provide per-session if needed
- `team.key_contacts` — provide in conversation, not stored

---

## Examples

### Minimal (Tier 1 only)
```json
{
  "_meta": {"version": "1.0", "slug": "myapp", "language": "zh-CN"},
  "company": {"name": null, "product_name": "某协作工具", "industry": "saas"},
  "competitors": {
    "direct": [{"name": "Notion"}],
    "indirect": [{"name": "飞书文档"}]
  },
  "tools": {"communication": "lark", "task_management": "lark-task"}
}
```

### Medium (Tier 1 + Tier 2)
```json
{
  "_meta": {"version": "1.0", "slug": "myapp", "language": "zh-CN"},
  "company": {
    "name": "某科技有限公司",
    "product_name": "TeamCollab",
    "url": "https://teamcollab.io",
    "industry": "saas",
    "stage": "growth",
    "size": "51-200"
  },
  "product": {
    "north_star_metric": "周活跃团队数 Weekly Active Teams",
    "core_value_prop": "让远程团队10秒内开始高效协作",
    "target_users_icp": "10-100人的远程优先科技团队",
    "platforms": ["web", "ios", "android"],
    "business_model": "subscription",
    "key_features": ["实时文档协作", "视频会议", "项目管理"]
  },
  "metrics": {
    "definitions": {
      "dau": {"name": "日活跃团队数"},
      "revenue": {"name": "MRR"}
    },
    "data_sources": {
      "analytics_tool": "amplitude",
      "dashboard_url": "内部看板"
    }
  },
  "competitors": {
    "direct": [
      {"name": "Notion", "strength": "品牌认知度高", "weakness": "协作实时性弱"}
    ],
    "indirect": [
      {"name": "飞书", "note": "国内市场主要替代品"}
    ],
    "our_differentiation": "实时协作体验优于Notion，性价比高于飞书"
  },
  "team": {
    "structure": "产品+研发+设计+运营 共4个小组",
    "sprint_cadence": "2-week"
  },
  "brand": {
    "tone": "professional",
    "primary_channels": ["公众号", "小红书", "知乎"]
  }
}
```

---

## File Location

| Environment | Path |
|-------------|------|
| macOS/Linux | `~/.product-ops/projects/{slug}/context.json` |
| Windows | `C:\Users\{user}\.product-ops\projects\{slug}\context.json` |

`{slug}` is derived from the current working directory name or user-provided project name, sanitized to `[a-z0-9-]`.

---

## Lifecycle

1. **Create**: Onboarding wizard (`onboarding.md`) generates this file
2. **Load**: SKILL.md § Step 0.3 reads this file before routing
3. **Update**: User says "更新公司信息" / "update context" → reload onboarding
4. **Delete**: User deletes the file or entire project directory
5. **Export**: User can ask to see their current context at any time
