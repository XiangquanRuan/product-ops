# Product Launch Checklist / 产品上线检查清单

> Copy and check off items for each launch. Adapt to your launch level.

🚀 **Launch**: {Feature/Version Name}
📅 **Date**: {Launch Date}
🔴🟡🟢 **Level**: {Major / Feature / Minor}

---

## T-7 Days (一周前)

### Product Readiness
- [ ] 功能验收 Feature sign-off (PM)
- [ ] 设计验收 Design QA (Designer)
- [ ] 测试通过 QA sign-off (QA)
- [ ] 性能测试 Performance test
- [ ] 安全检查 Security review
- [ ] 无障碍检查 Accessibility check

### Operational Readiness
- [ ] 监控配置 Monitoring dashboards & alerts
- [ ] 数据分析埋点 Analytics events verified
- [ ] 帮助文档 Help docs ready
- [ ] 客服培训 Support team briefed
- [ ] 降级方案 Rollback plan documented
- [ ] 灰度方案 Gradual rollout plan

### Communications Readiness
- [ ] 发布公告 Release notes drafted
- [ ] 应用商店文案 App Store copy updated (if applicable)
- [ ] 社交媒体帖子 Social posts ready
- [ ] 用户通知 User notification drafted
- [ ] 内部通告 Internal announcement drafted

---

## T-3 Days (三天前)

- [ ] 预发布环境验证 Staging regression
- [ ] 灰度配置 Feature flags configured
- [ ] 客服话术 Support response templates ready
- [ ] 关键人员确认 Key people confirmed for launch day
- [ ] 媒体/PR 准备 Press materials ready (if major launch)

---

## T-1 Day (一天前)

- [ ] 上线准备会 Launch readiness meeting (go/no-go)
- [ ] 值班安排 On-call schedule confirmed
- [ ] 沟通渠道确认 Launch comms channel created
- [ ] 回滚流程确认 Rollback procedure rehearsed
- [ ] 最终构建验证 Final build verified

---

## Launch Day (上线当天)

### T-2h: Pre-Launch
- [ ] 值班人员到位 On-call team online
- [ ] 监控面板打开 Monitoring dashboards open
- [ ] 沟通渠道测试 Comms channel test

### T-0: Launch
- [ ] 灰度发布开始 Rollout started at ___%
- [ ] 实时监控确认 Real-time monitoring active
- [ ] 内部发布通告 Internal launch announcement sent

### Rollout Stages
- [ ] 1% → 观察 {n} min → 状态: ✅ ⏸ 🔙
- [ ] 5% → 观察 {n} min → 状态: ✅ ⏸ 🔙
- [ ] 25% → 观察 {n} min → 状态: ✅ ⏸ 🔙
- [ ] 100% → 全量发布完成 Full rollout complete

### T+1h: First Checkpoint
- [ ] 崩溃率正常 Crash rate normal: ___%
- [ ] 错误率正常 Error rate normal: ___%
- [ ] 核心流程正常 Core funnel normal
- [ ] 用户反馈无异常 No unusual user reports

### T+4h: Second Checkpoint
- [ ] 全量发布完成 Full rollout complete
- [ ] 关键指标稳定 Key metrics stable
- [ ] 客服工单量正常 Support tickets normal

### T+24h: 24h Post-Launch
- [ ] 24h 数据报告生成
- [ ] 发布全量通知 Full launch announcement sent
- [ ] 用户反馈汇总 User feedback summarized

---

## Post-Launch (上线后)

- [ ] T+72h: 稳定性检查 Stabilization check
- [ ] T+7d: 一周数据回顾 1-week data review
- [ ] T+7d: 上线复盘会 Launch retrospective meeting
- [ ] T+14d: 新功能留存检查 Feature retention check

---

## Notes / 备注

```
{Add launch-specific notes, risks, contact info here}
```

**On-Call Contacts**:
• Engineering: @{name} — {phone}
• PM: @{name} — {phone}
• Ops: @{name} — {phone}

**Escalation Path**:
1. {Level 1}: @{name}
2. {Level 2}: @{name}
3. {Level 3}: @{name}
