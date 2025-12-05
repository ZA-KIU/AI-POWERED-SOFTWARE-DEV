# Optimization Plan: [Your Capstone Name]

**Date:** [Fill in]
**Your Name:** [Fill in]

---

## 1. Which model(s) should I use?

### Current Model Usage
- [ ] **Model(s) currently using:** _____________________
- [ ] **Why I chose this model originally:** _____________________

### Task Complexity Analysis
My capstone's queries are:
- [ ] Simple classification (→ Fast model like Haiku)
- [ ] Moderate complexity (→ Mid-tier like GPT-4o-mini)
- [ ] Complex reasoning (→ Frontier like GPT-4o)
- [ ] **Mixed complexity** (→ Consider cascading)

### Error Cost
If my system makes a mistake:
- [ ] Low cost (suggestions, non-critical) → Can use cheaper model
- [ ] Medium cost (user annoyance) → Balance cost vs accuracy
- [ ] High cost (medical, legal, financial) → Use frontier model

**Decision:** I should use _____________________ model(s) because _____________________

---

## 2. Where should I cache?

### Query Patterns
- [ ] **Do users ask similar questions?** Yes / No
- [ ] **Do I have repeated queries in logs?** Yes / No
- [ ] **Is my context/prompt reused often?** Yes / No

### Cache Hit Rate Estimate
Based on my data:
- [ ] Expected cache hit rate: _____%
- [ ] How I estimated this: _____________________

### Cache Strategy
- [ ] **Prompt caching** (Anthropic auto-caches long prompts >1024 tokens)
- [ ] **Result caching** (Cache full API responses)
- [ ] **Semantic caching** (Cache similar queries via embeddings)
- [ ] **No caching needed** (All queries unique)

**Decision:** I should cache _____________________ because _____________________

---

## 3. What's my cost budget?

### Current Costs
- [ ] **Cost per query:** $___________________
- [ ] **Expected queries per day:** _____________________
- [ ] **Monthly projection:** $___________________
- [ ] **Is this sustainable?** Yes / No

### Cost Breakdown
Analyze where money goes:
- [ ] Input tokens: ____% of cost
- [ ] Output tokens: ____% of cost
- [ ] Model choice: ____% of cost
- [ ] Other (embeddings, tools): ____% of cost

**Most expensive part:** _____________________

**Decision:** My target monthly cost is $___________________

---

## 4. What's acceptable latency?

### Current Latency
- [ ] **Average response time:** _____ seconds
- [ ] **p95 latency:** _____ seconds
- [ ] **User feedback on speed:** _____________________

### Use Case Requirements
- [ ] **Real-time chat** (<2s required)
- [ ] **Analysis/research** (5-10s OK)
- [ ] **Background processing** (30s+ OK)

### Latency Targets
- [ ] **Target average:** _____ seconds
- [ ] **Target p95:** _____ seconds
- [ ] **Maximum acceptable:** _____ seconds

**Decision:** I can accept up to _____ seconds latency to save costs: Yes / No

---

## 5. What will I measure?

### Baseline Metrics (BEFORE optimization)
Document current state:

| Metric | Value |
|--------|-------|
| Cost per query | $_____ |
| Average latency | _____ s |
| p95 latency | _____ s |
| Error rate | _____% |
| Cache hit rate | N/A (or _____%) |
| Model distribution | _____% Haiku, _____% Mini, _____% GPT-4o |

### Success Criteria (AFTER optimization)
What would make this optimization successful?

- [ ] **Cost reduction target:** >_____%
- [ ] **Latency change acceptable:** <_____ seconds increase
- [ ] **Quality maintained:** <_____%  accuracy drop
- [ ] **Cache hit rate:** >_____% (if caching)

**How I'll measure quality:**
- [ ] Manual review of responses
- [ ] User feedback
- [ ] Comparison to baseline outputs
- [ ] Golden set evaluation (Week 11)

---

## 6. When will I optimize?

### Priority Analysis (Week 10 Slide 19 Framework)

**🔥 High Priority** (Optimize IMMEDIATELY):
- [ ] Costs burning budget
- [ ] Users complaining about speed
- [ ] Hitting rate limits
- [ ] Quality issues

**⚠️ Medium Priority** (Optimize SOON):
- [ ] Costs manageable but high
- [ ] Latency acceptable but slow
- [ ] Obvious inefficiencies
- [ ] Preparing for scale

**✅ Low Priority** (Can WAIT):
- [ ] Costs negligible (<$10/day)
- [ ] Users happy with speed
- [ ] Working well
- [ ] Limited traffic

**My optimization priority:** High / Medium / Low

**Justification:** _____________________

---

## My Optimization Choice

Based on the analysis above:

### Chosen Optimization
- [ ] **Model Cascading** (Haiku → Mini → GPT-4o)
- [ ] **Result Caching** (Redis or in-memory)
- [ ] **Semantic Caching** (Embeddings + similarity)
- [ ] **Batching** (Process multiple items together)
- [ ] **Other:** _____________________

### Why This Choice?
_____________________
_____________________
_____________________

### Expected Impact
- **Cost reduction:** _____%
- **Latency change:** +/- _____ seconds
- **Quality impact:** No change / Minor drop / Improvement

### Implementation Plan
**Step 1:** _____________________
**Step 2:** _____________________
**Step 3:** _____________________

### Risks & Mitigation
**Risk 1:** _____________________
**Mitigation:** _____________________

**Risk 2:** _____________________
**Mitigation:** _____________________

---

## Next Steps After This Optimization

If this optimization works, what should I optimize next?

**Second optimization:** _____________________
**Third optimization:** _____________________

**Path to target cost:** $_____ current → $_____ after optimization 1 → $_____ after optimization 2 → $_____ target

---

## Approval Checkpoint

**Instructor signature/approval:** _____________________

**Date:** _____________________

**Feedback/suggestions:** _____________________
