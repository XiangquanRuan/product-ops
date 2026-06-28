# Growth Experiments / 增长实验

A/B testing, growth strategies, and experimentation workflows for product operations.

## Language

Check for `[Language: 中文]` or `[Language: English]` in context. Default to 中文 if user writes in Chinese.

---

## 1. A/B Test Design / A/B测试设计

### When to Run an A/B Test

Good candidates for A/B testing:
- ✅ UI/UX changes (button color, layout, copy)
- ✅ Algorithm changes (ranking, recommendation)
- ✅ Pricing experiments
- ✅ Onboarding flow variations
- ✅ Push notification timing/content

NOT good for A/B testing:
- ❌ New features (use feature flags + phased rollout)
- ❌ Brand changes (measurable but long-term)
- ❌ Things with network effects (control spills into test)
- ❌ Very small user bases (can't reach significance)

### Test Design Template

Work through these questions with the user:

```
🧪 A/B 测试设计 | Experiment Design

1. 实验背景 Background:
   • 为什么要做这个实验？Why this experiment?
   • 目前的数据表现 Current baseline: {metric} = {value}

2. 假设 Hypothesis:
   • 如果 [change]，就会 [expected outcome]，因为 [reasoning]
   • If we [change], then [outcome] will happen, because [reason]

3. 实验方案 Variants:
   • Control (A): {current experience}
   • Variant (B): {proposed change}
   • (Optional) Variant (C): {alternative}
   • 流量分配 Traffic split: A {50}% / B {50}%

4. 核心指标 Metrics:
   • 主要指标 Primary Metric: {metric} — 预期提升 Expected lift: +{X}%
   • 辅助指标 Secondary Metrics: {metrics}
   • 护栏指标 Guardrail Metrics: {metrics that must NOT degrade}
   • 监控指标 Monitoring: {metrics to watch but not decide on}

5. 样本量与时长 Sample Size & Duration:
   • 预计所需样本 Estimated sample size: {n} per variant
   • 预计实验时长 Estimated duration: {days} days
   • 最小检测效应 Minimum Detectable Effect (MDE): {X}%
   • 统计显著性 Statistical significance: 95% (standard)

6. 风险与缓解 Risks & Mitigations:
   • {risk} → {mitigation}
   • {risk} → {mitigation}

7. 决策标准 Decision Criteria:
   • ✅ 发布 Ship if: primary metric {significantly improves} AND guardrails {don't degrade}
   • ❌ 放弃 Kill if: primary metric {significantly degrades} OR guardrails {degrade}
   • 🔄 迭代 Iterate if: {inconclusive / directional but not significant}
```

### For Statistical Rigor

If the user needs deep statistical design (sample size calculation, power analysis, multiple comparison correction) → route to `/pmprompt:ab-test-designer` and `/pmprompt:trustworthy-experiments`

---

## 2. Experiment Results Analysis / 实验结果分析

### Analysis Framework

When the user has experiment results, guide them through:

1. **Sanity checks first**:
   - Were control and test groups balanced? (check pre-experiment metrics)
   - Any SRM (Sample Ratio Mismatch)?
   - Any data pipeline issues?

2. **Primary metric analysis**:
   - Point estimate: {lift}%
   - Confidence interval: [{lower}%, {upper}%]
   - p-value: {value}
   - Is it practically significant? (not just statistically)

3. **Segmentation**:
   - Does the effect vary by platform/region/user type?
   - Any Simpson's paradox risks?

4. **Guardrails check**:
   - Any metrics that degraded?

5. **Decision**:
   - Ship / Kill / Iterate

### Output Format

```
📊 实验结果 | Experiment Results — {Experiment Name}

实验概况 Summary:
• 实验时长 Duration: {start} → {end} ({n} days)
• 总样本量 Total Users: {n} | Control: {nc} | Variant: {nv}
• 状态 Status: {completed / running / stopped early}

主要指标 Primary Metric: {metric name}
• Control (A): {value} ± {error}
• Variant (B): {value} ± {error}
• 提升 Lift: +{X}% [{lower}%, {upper}% CI]
• p-value: {value} → {significant / not significant}
• 结论: ✅ 证实 / ❌ 未证实 / 🔄 不确定

护栏指标 Guardrail Metrics:
• {metric}: {change}% → {ok / degraded}
• {metric}: {change}% → {ok / degraded}

分维度结果 Segmented Results:
| 维度 Segment | Control | Variant | Lift |
|-------------|---------|---------|------|
| {segment 1} | {v} | {v} | {+/-}% |
| {segment 2} | {v} | {v} | {+/-}% |

🎯 决策 Decision:
• {Ship / Kill / Iterate}
• 理由 Rationale: {explanation}
• 下一步 Next Step: {action}

💡 学到的 Learning:
• {key takeaway for future experiments}
```

---

## 3. Growth Strategy Design / 增长策略设计

### Growth Framework

Use the AARRR framework (Acquisition → Activation → Retention → Revenue → Referral):

```
🎯 增长诊断 Growth Diagnostic — {Product}

获客 Acquisition:
• 主要渠道 Top Channels: {list}
• 渠道效率 Efficiency (CAC by channel): {data}
• 增长来源 Growth Sources: paid {X}% | organic {Y}% | viral {Z}%

激活 Activation:
• 激活定义 "Aha moment": {definition}
• 当前激活率 Activation Rate: {value}%
• 激活瓶颈 Bottleneck: {stage where most users drop}

留存 Retention:
• D1/D7/D30: {values}
• 留存曲线形状 Shape: {smiling / flattening / declining}
• 留存拐点 "Retention cliff" at day {n}

变现 Revenue:
• 付费转化 Pay Conversion: {value}%
• ARPU: {value} | LTV: {value}
• 定价策略 Pricing: {description}

传播 Referral:
• 病毒系数 Viral Coefficient: {value}
• 邀请发送率 Invite Send Rate: {value}%
• NPS: {value}
```

For deep growth loop design → `/pmprompt:growth-loops`

---

## 4. Feature Prioritization / 功能优先级排序

### RICE Framework

When the user needs to prioritize features or growth initiatives:

```
🔢 RICE 优先级排序 | Feature Prioritization

| 项目 Item | Reach 触达 | Impact 影响 | Confidence 信心 | Effort 投入 | RICE Score |
|-----------|-----------|------------|-----------------|------------|------------|
| {feature} | {n}/10 | {n}/10 | {n}% | {n}人周 | {score} |
| {feature} | {n}/10 | {n}/10 | {n}% | {n}人周 | {score} |
| {feature} | {n}/10 | {n}/10 | {n}% | {n}人周 | {score} |

RICE = (Reach × Impact × Confidence) / Effort

✅ 优先做 Priority:
1. {feature} (RICE: {score})
2. {feature} (RICE: {score})

⏸ 暂缓 Defer:
3. {feature} (RICE: {score})
```

For deep RICE facilitation → `/pmprompt:feature-prioritization-assistant`

---

## 5. PMF Assessment / 产品市场契合度评估

### Sean Ellis Test

Ask the user to survey their users with:
> "How disappointed would you be if you could no longer use [product]?"
> - Very disappointed
> - Somewhat disappointed
> - Not disappointed

**Threshold**: ≥40% "very disappointed" = PMF signal

For formal PMF survey design → `/pmprompt:pmf-survey`

---

## 6. Experimentation Cadence

### Weekly Experiment Review
See `weekly-operations.md` — growth metrics section

### Monthly Experiment Strategy
See `monthly-operations.md` — OKR & strategy review

### Template
A/B test design template in `assets/ab-test-design-template.md`

---

## External Skill Routing Summary

| Need | Route To |
|------|----------|
| Rigorous A/B test design with sample size calc | `/pmprompt:ab-test-designer` |
| Trustworthy experiment methodology | `/pmprompt:trustworthy-experiments` |
| Growth loop design (Reforge) | `/pmprompt:growth-loops` |
| Feature prioritization (RICE) | `/pmprompt:feature-prioritization-assistant` |
| PMF survey design | `/pmprompt:pmf-survey` |
| Product-led growth strategy | `/pmprompt:product-led-growth` |
| Deep business diagnosis for growth stalls | `/money-diagnose` |
