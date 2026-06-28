# A/B Test Design Template / A/B测试设计模板

> Fill in before starting any experiment. Share with team for alignment.

---

🧪 **实验名称 Experiment**: {Name}
📅 **时间 Timeframe**: {Start} → {End} (预计 {n} days)
👤 **负责人 Owner**: {Name}

---

## 1. 实验背景 Background

**为什么要做这个实验? Why this experiment?**
{context}

**当前基线 Current Baseline**:
• {metric}: {value}

---

## 2. 假设 Hypothesis

> 如果 [change]，就会 [expected outcome]，因为 [reasoning]

> If we [change], then [outcome] will happen, because [reason]

---

## 3. 实验方案 Variants

**Control (A)**: 
{current experience}

**Variant (B)**: 
{proposed change}

**Variant (C)** (optional): 
{alternative approach}

**流量分配 Traffic Split**:
• Control (A): {50}%
• Variant (B): {50}%
• Variant (C): {0}% (if applicable)

---

## 4. 指标 Metrics

**主要指标 Primary Metric**:
• {metric name} — 定义 Definition: {how calculated}
• 预期提升 Expected Lift: +{X}%
• 最小检测效应 MDE: {X}%

**辅助指标 Secondary Metrics**:
• {metric} — 预期 Expected: {direction}
• {metric} — 预期 Expected: {direction}

**护栏指标 Guardrail Metrics** (must NOT degrade):
• {metric} — 当前 Current: {value} — 阈值 Threshold: {value}
• {metric} — 当前 Current: {value} — 阈值 Threshold: {value}

---

## 5. 样本量与时长 Sample Size & Duration

• 所需样本 Sample Size: {n} per variant
• 每日可用流量 Daily Eligible Traffic: {n}
• 预计时长 Estimated Duration: {n} days
• 统计显著性目标 Significance: 95%
• 统计功效目标 Power: 80%

---

## 6. 风险与缓解 Risks & Mitigations

| 风险 Risk | 可能性 Prob | 影响 Impact | 缓解 Mitigation |
|----------|-----------|------------|----------------|
| | 高/中/低 | 高/中/低 | |
| | 高/中/低 | 高/中/低 | |

---

## 7. 决策标准 Decision Criteria

✅ **发布 Ship if**: 
• Primary metric significantly improves (p < 0.05) AND
• No guardrail metric significantly degrades AND
• Practical significance met (lift > MDE)

❌ **放弃 Kill if**: 
• Primary metric significantly degrades OR
• Any guardrail significantly degrades OR
• After max duration, no clear signal

🔄 **迭代 Iterate if**: 
• Positive direction but not significant → extend or refine variant
• Mixed results → analyze segments, consider new variant

---

## 8. 分组与实施 Segmentation & Implementation

**目标用户 Target Users**:
• {user segment criteria}
• 排除 Exclude: {who to exclude}

**技术实施 Tech Implementation**:
• Feature flag key: {flag_name}
• Tracking events: {event names}
• Dashboard: {link}

---

## 9. 结果 Results (fill after experiment)

**实际时长 Actual Duration**: {days} days
**实际样本 Actual Sample**: {n} per variant

**Primary Metric Results**:
| Variant | Value | Lift | p-value | CI |
|---------|-------|------|---------|-----|
| Control (A) | | — | — | — |
| Variant (B) | | +{X}% | | [{l}, {u}] |

**Guardrail Results**:
| Metric | Control | Variant | Change | Status |
|--------|---------|---------|--------|--------|
| | | | | ✅/⚠️ |

**决策 Decision**: [Ship / Kill / Iterate]
**理由 Rationale**: 

**学习 Learnings**: 
