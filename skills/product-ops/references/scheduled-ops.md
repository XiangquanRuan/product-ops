# Scheduled Operations / 定时运营

Set up recurring product ops tasks that run automatically — daily standups, weekly reports, monthly reviews.

## Language

Check for `[Language: 中文]` or `[Language: English]` in context.

---

## Available Scheduling Methods

| Method | Best For | Setup Difficulty |
|--------|----------|:---:|
| `/loop` command | Simple recurring prompts | ⭐ Easy |
| System cron / Task Scheduler | External trigger + script | ⭐⭐ Medium |
| `money-ops` skill | Full 24/7 autonomous orchestration | ⭐⭐⭐ Advanced |

---

## Method 1: `/loop` Command (Recommended)

Claude Code's built-in loop command. Runs a prompt on a fixed interval.

### Daily Tasks

```
/loop 24h /product-ops 生成今日站报
```

This fires every 24 hours. The skill loads context, fetches data, generates a standup, and offers to send it to IM.

**Best time**: Schedule at 09:00 — catches the morning routine.

**Other daily options**:
```
/loop 24h /product-ops 日终总结    # End-of-day wrap-up at 17:30
/loop 6h /product-ops 数据健康检查  # Check metrics every 6 hours
```

### Weekly Tasks

```
/loop 168h /product-ops 生成本周周报
```

168 hours = 7 days. Fires once a week.

**Best time**: Friday 16:00 or Monday 09:00.

### Monthly Tasks

```
# Monthly is trickier — use cron instead (see Method 2)
```

`/loop` doesn't support "first Monday of month" patterns. Use Method 2 for monthly.

### `/loop` Limitations

- Runs only when Claude Code is open and idle
- Doesn't survive terminal close (session-only)
- No conditional logic (runs regardless of whether it's a workday)

---

## Method 2: System Scheduler

For reliable, always-on scheduling independent of Claude Code.

### Windows (Task Scheduler)

Create a scheduled task that invokes Claude Code:

```powershell
# Create a daily 9:00 AM standup trigger
$action = New-ScheduledTaskAction -Execute "claude" -Argument "code /product-ops 生成今日站报"
$trigger = New-ScheduledTaskTrigger -Daily -At 9:00AM
Register-ScheduledTask -TaskName "ProductOps-DailyStandup" -Action $action -Trigger $trigger
```

### macOS / Linux (cron)

```bash
# Add to crontab: crontab -e

# Daily standup at 9:00 AM
0 9 * * 1-5 cd ~/myproject && claude code "/product-ops 生成今日站报"

# Weekly report Friday 4:00 PM
0 16 * * 5 cd ~/myproject && claude code "/product-ops 生成本周周报"

# Monthly review on the 1st at 10:00 AM
0 10 1 * * cd ~/myproject && claude code "/product-ops 生成本月月报"
```

### System Scheduler Limitations

- Claude Code may prompt for permissions (use auto mode or pre-approve)
- No session context from previous runs
- Need to ensure `context.json` exists before first run

---

## Method 3: `money-ops` Skill (Advanced)

For users who want full 24/7 autonomous operations with health scoring, canary monitoring, and safety guardrails. Install `@orrisai/show-me-the-money` and use:

```
/money-ops
```

This integrates with `product-ops` automatically — the two skills share context and can route to each other.

---

## Recommended Schedule

A complete product ops automation schedule:

```
📅 运营自动化日历 | Ops Automation Calendar

═ 每日 Daily ═
09:00  晨间站报     /loop 24h /product-ops 今日站报
17:30  日终总结     /loop 24h /product-ops 日终总结

═ 每周 Weekly ═
周五 16:00  周报    /loop 168h /product-ops 本周周报
周一 09:00  竞品扫描  /loop 168h /product-ops 竞品本周动态

═ 每月 Monthly ═
1号 10:00   月报    (system cron) /product-ops 本月月报
1号 14:00   OKR回顾  (system cron) /product-ops OKR进展回顾

═ 按需 On-Demand ═
上线时      发布检查  /product-ops 上线检查清单
收到反馈    用户反馈  /product-ops 处理用户反馈
启动实验    A/B测试  /product-ops 设计A/B测试
```

---

## Setup Wizard

When user says "设置定时任务" / "schedule ops" / "自动化运营":

1. Ask which tasks they want automated:
   > 你想自动化哪些？
   > 1. 📅 每日站报 (每天 9:00)
   > 2. 📊 每周周报 (每周五 16:00)
   > 3. 📈 每月月报 (每月1号 10:00)
   > 4. 🔍 竞品周扫描 (每周一 9:00)
   > 5. 全部

2. Recommend the right scheduling method:
   - If they always have Claude Code open → `/loop`
   - If they want guaranteed execution → system cron
   - If they want full autonomy → `/money-ops`

3. Generate the exact commands they need
4. Explain how to stop: `/loop stop` or `crontab -e` to remove

---

## Integration with Output Actions

When a scheduled task fires, the output should be auto-delivered:

| Scheduled Task | Auto-Delivery |
|---------------|--------------|
| Daily standup | → IM (group chat) |
| Weekly report | → Doc + IM summary |
| Monthly review | → Doc + .docx save |
| Data health check | → IM only if anomaly detected |
| Competitive scan | → Doc |

User can configure this in context.json:
```json
{
  "schedules": {
    "daily_standup": {
      "enabled": true,
      "time": "09:00",
      "method": "loop",
      "auto_deliver": "im"
    },
    "weekly_report": {
      "enabled": true,
      "time": "fri_16:00",
      "method": "loop",
      "auto_deliver": "doc_and_im"
    }
  }
}
```
