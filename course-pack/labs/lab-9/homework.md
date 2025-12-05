# Lab 9 Homework: Production Optimization + Integration

**Due:** December 11th, 2025 23:59
**Submission:** optimization-report.md + updated capstone code in Git

## Part A: Complete Your Optimization (If Not Finished in Lab)

### Tasks
1. **Finish implementation** of your chosen optimization
2. **Run full evaluation** with 50+ test queries (not just 20)
3. **Document edge cases** you discovered
4. **Calculate final metrics:**
   - Cost reduction: `(baseline_cost - optimized_cost) / baseline_cost * 100`
   - Latency change: `optimized_p95 - baseline_p95`
   - Quality impact: Any accuracy/satisfaction changes?

### Deliverable
`optimization-report.md` with:
- Baseline metrics table
- Optimized metrics table
- Cost reduction %
- What worked / what didn't
- Code snippets of key changes

---

## Part B: Integrate Labs 8 + 9

### For Students WITH Agents (Lab 8)

Your agent is likely the most expensive part of your capstone. Apply optimization specifically to agent calls.

**Tasks:**
1. **Identify expensive agent operations:**
   - Which tools cost most to call?
   - Which reasoning steps use frontier models?
   - How many LLM calls per agent task?

2. **Apply optimizations:**
   - **Model cascading**: Use Haiku for tool selection, Mini/GPT-4o for complex reasoning
   - **Result caching**: Cache tool results (e.g., repeated searches)
   - **Batching**: If agent processes multiple items, batch them

3. **Measure agent-specific impact:**
   - Cost per agent task (before vs. after)
   - Agent success rate (did optimization hurt performance?)
   - Average tools called per task

**Deliverable:** Section in optimization-report.md titled "Agent Optimization" with agent-specific metrics

### For Students WITHOUT Agents

Apply optimization to your capstone's core LLM operations.

**Tasks:**
1. **Profile your capstone:**
   - What are the 3 most expensive API calls?
   - Which queries get repeated most?
   - Where is latency highest?

2. **Apply targeted optimization:**
   - If RAG: Implement semantic caching for similar questions
   - If classification: Use model cascading (Haiku → Mini)
   - If batch processing: Implement batching

3. **Document decision rationale:**
   - Why did you choose this optimization?
   - What alternatives did you consider?
   - What would you optimize next?

**Deliverable:** Section in optimization-report.md titled "Optimization Strategy" with decision rationale

---

## Part C: Optimization Plan for Week 11+

Based on what you learned, plan your next optimizations.

**Tasks:**
1. **Prioritize remaining optimizations** using Week 10 Slide 19 framework:
   - High priority: Costs unsustainable OR users complaining about speed
   - Medium priority: Costs manageable but could be better
   - Low priority: Working well, costs negligible

2. **Estimate potential savings:**
   - If you add caching, how much more could you save?
   - If you cascade models, what's the upside?
   - If you batch, what's realistic improvement?

3. **Set success criteria:**
   - Target monthly cost: $X
   - Target p95 latency: <Ys
   - Minimum quality threshold: Z%

**Deliverable:** Section in optimization-report.md titled "Next Steps" with prioritized plan

---

## Submission Requirements

### 1. optimization-report.md
Must include:
- [ ] Baseline metrics (cost, latency, quality)
- [ ] Optimized metrics (cost, latency, quality)
- [ ] Cost reduction % and latency change
- [ ] Code snippets of key optimizations
- [ ] Agent optimization (if Lab 8 agents) OR Optimization strategy (if no agents)
- [ ] Next steps plan
- [ ] Reflection: What surprised you? What was harder than expected?

### 2. Updated Capstone Code
- [ ] Committed to Git with tag `lab-9-optimization`
- [ ] README updated with optimization notes
- [ ] Logging added for cost/latency tracking

### 3. Evidence
- [ ] Screenshots or logs showing before/after metrics
- [ ] At least 50 test queries in your evaluation

---

## Grading Rubric (Self-Assessment)

**Baseline Measurement (2 points)**
- [ ] Documented cost per query
- [ ] Documented p95 latency
- [ ] Calculated monthly spend projection

**Implementation (3 points)**
- [ ] Working optimization code
- [ ] Properly integrated with capstone
- [ ] Handles edge cases

**Measurement & Analysis (3 points)**
- [ ] Ran 50+ test queries
- [ ] Calculated cost reduction accurately
- [ ] Documented quality impact (if any)

**Integration (Lab 8+9) (2 points)**
- [ ] Applied optimization to expensive parts
- [ ] Documented agent-specific impact (if applicable)
- [ ] Showed understanding of trade-offs

---

## Tips for Success

**Start Early**
- Measuring takes longer than you think
- API calls cost real money (plan your test budget)
- Edge cases will surprise you

**Be Honest**
- If optimization didn't work, say so and explain why
- Negative results are valuable learning
- "I tried X but it made Y worse" is good analysis

**Think Long-Term**
- This week's optimization is one of many
- Small gains compound (30% + 20% + 15% = big savings)
- Your Week 11 Safety Audit will need these metrics

**Use Office Hours**
- Bring your metrics if confused
- Get help debugging caching issues
- Discuss optimization strategy

---

## Common Questions

**Q: Can I implement multiple optimizations?**
A: Yes! But focus on ONE first, measure it, then add more. Don't optimize everything at once.

**Q: My cost reduction is only 15%, is that bad?**
A: No! 15% is great. Document it honestly. Multiple optimizations compound.

**Q: What if optimization hurt my quality?**
A: Document it! Then either tune thresholds or revert. This is realistic production work.

**Q: Do I need to use Redis?**
A: No. In-memory dict is fine for homework. Redis is better for real production.

**Q: How does this connect to Week 11?**
A: Week 11 focuses on quality measurement (golden sets, evaluation). This week focused on cost/speed. Both are needed for production.

---

**Remember:** Optimization without measurement is guessing. You're building real production skills.
