# Lab 8: Production Optimization Workshop

**Week 10 | Building AI-Powered Applications**

Welcome back from midterm! This lab shifts focus to making your capstone production-ready. You'll apply cost optimization, caching strategies, and performance improvements that can reduce operational costs by 80%+ while maintaining or improving quality.

**Lab Duration:** 2 hours in-class + homework integration into capstone  
**Prerequisites:** Working capstone with API integration (from Labs 6-7)

## Learning Objectives

By the end of this lab, you will:

- Audit your capstone's current cost and latency patterns
- Implement prompt caching to reduce repeat costs by 60-90%
- Apply smart model selection to achieve 5-10x cost reductions
- Add batching for batch-processable tasks
- Implement cost tracking and alerting systems
- Document optimization decisions with before/after metrics

## What's Due This Week

### In-Lab Deliverable: Optimization Audit Report

Document in your capstone repository at `docs/optimization-audit.md`:

1. **Current State Analysis** - Baseline costs, latency, usage patterns
2. **Optimization Opportunities** - Identified improvements with projected impact
3. **Implementation Plan** - What you'll optimize, timeline, success metrics
4. **Cost Calculator** - Tool or spreadsheet showing cost projections

**Due:** End of lab session (submit link to your audit document)

### Homework: Implement Top 3 Optimizations

By end of Week 10, implement your top 3 optimization opportunities:

1. Update code with caching, model selection, or batching
2. Add cost tracking instrumentation
3. Document results in `docs/optimization-results.md`
4. Update your project README with new performance metrics

**Due:** End of Week 10 (see course calendar)  
**Points:** Part of Capstone ongoing development

## Why This Matters

Real-world context: A naive agent implementation costs $2,000/month for 10,000 requests. After optimization:
- Smart caching: $600/month (70% reduction)
- Model selection: $200/month (90% reduction from baseline)
- Batching: $120/month (94% reduction)

This lab teaches you patterns that separate hobbyist projects from production systems.

## Pre-Lab Preparation (Do Before Class)

**Required (30 minutes):**

1. **Review your capstone's current API usage**
   - Identify all LLM API calls in your code
   - Note which calls repeat similar requests
   - Check if you're tracking costs currently

2. **Gather baseline metrics** (if available)
   - Total API calls in last week
   - Average response latency
   - Estimated monthly cost (or calculate from API logs)

3. **Install required packages**
   ```bash
   pip install cachetools redis python-dotenv --break-system-packages
   ```

**Recommended (15 minutes):**

- Read [Week 10 Lecture Slides](../../lectures/week-10/) Slides 10-18 on caching and model selection
- Review your architecture diagram from Week 4 Design Review

## In-Class Activities (2 hours)

### Part 1: Cost Audit & Baseline (30 min)

**Objective:** Understand what your capstone currently costs to run.

**Tasks:**
1. Map all LLM API calls in your code (15 min)
2. Calculate baseline costs using [Cost Calculator Tool](./tools/cost-calculator.md) (10 min)
3. Identify hotspots - which calls cost the most (5 min)

**Deliverable:** Completed `Current State Analysis` section in audit document

**Instructor checkpoint:** Before moving to Part 2

---

### Part 2: Caching Opportunities (40 min)

**Objective:** Implement prompt caching for repeat queries.

**Tasks:**
1. Identify cacheable patterns in your app (10 min)
   - Repeated system prompts
   - Common user queries
   - Static context (docs, guidelines)

2. Implement in-memory caching (20 min)
   - Use [Caching Implementation Guide](./guides/caching-implementation.md)
   - Code walkthrough with instructor
   - Test with sample queries

3. Measure impact (10 min)
   - Calculate cache hit rate
   - Project monthly savings

**Deliverable:** Working cache implementation + impact analysis

---

### Part 3: Model Selection Strategy (30 min)

**Objective:** Use cheaper models where quality allows.

**Tasks:**
1. Categorize your use cases by complexity (10 min)
   - Simple: classification, extraction, formatting
   - Medium: summarization, Q&A, basic reasoning
   - Complex: multi-step reasoning, code generation, creative tasks

2. Map models to use cases (10 min)
   - Use [Model Selection Matrix](./guides/model-selection.md)
   - Identify opportunities to downgrade models
   - Plan A/B tests for uncertain cases

3. Calculate projected savings (10 min)
   - Use cost calculator with new model mix
   - Document decision rationale

**Deliverable:** Completed model selection strategy in audit

---

### Part 4: Implementation Planning (20 min)

**Objective:** Create concrete action plan for homework.

**Tasks:**
1. Prioritize optimization opportunities (10 min)
   - Impact vs. effort matrix
   - Select top 3 for homework implementation
   - Assign to team members

2. Define success metrics (10 min)
   - Baseline vs. target costs
   - Acceptable latency ranges
   - Quality evaluation criteria

**Deliverable:** Implementation plan section completed

**Final instructor checkpoint:** Review plan before leaving lab

## Homework Assignment

### Core Deliverables (Required)

**1. Implement Top 3 Optimizations**

Execute your implementation plan from lab. Common optimizations:

- **Caching Implementation**
  - Add prompt caching for repeated requests
  - Implement response caching with TTL
  - Document cache invalidation strategy

- **Model Selection**
  - Replace expensive models for simple tasks
  - Add fallback logic (cheap model first, expensive if needed)
  - A/B test to validate quality is maintained

- **Batching** (if applicable)
  - Batch similar requests together
  - Implement async processing for non-urgent tasks
  - Add job queue for batch operations

**Where to put it:** Update your existing capstone code

**2. Cost Tracking Instrumentation**

Add logging to track optimization impact:

```python
# Example structure
{
  "timestamp": "2025-01-15T10:30:00Z",
  "endpoint": "/api/analyze",
  "model": "gpt-3.5-turbo",
  "tokens_input": 150,
  "tokens_output": 75,
  "cost_usd": 0.0004,
  "latency_ms": 850,
  "cache_hit": false
}
```

**Where to put it:** `src/utils/cost_tracking.py` or similar

**3. Results Documentation**

Create `docs/optimization-results.md` with:

- Before/after metrics (cost, latency, quality)
- Implementation details and challenges
- Screenshots or data visualizations
- Lessons learned and future optimizations

**4. Update Project README**

Add "Performance" section showcasing:
- Current costs per 1K requests
- Average response times
- Optimization strategies employed
- Links to detailed optimization docs

## Detailed Requirements

### Optimization Audit (`docs/optimization-audit.md`)

Must include:

**Current State Analysis**
- API call inventory (which endpoints, which models)
- Baseline cost calculation (monthly projection)
- Latency measurements (p50, p95, p99 if available)
- Current cache status (none, basic, sophisticated)

**Optimization Opportunities**
- Minimum 5 identified opportunities
- Each with: description, projected savings, effort estimate, implementation notes
- Prioritization with justification

**Implementation Plan**
- Top 3 selected optimizations
- Team member assignments
- Timeline (specific dates)
- Success criteria (measurable metrics)
- Risk mitigation strategies

**Cost Calculator**
- Tool or spreadsheet that calculates costs
- Shows current state and projected optimized state
- Includes: model prices, token counts, request volumes
- Link to calculator file or screenshot of results

### Optimization Results (`docs/optimization-results.md`)

Must include:

**Metrics Comparison**
- Table showing before/after for each optimization
- Cost reduction percentages
- Latency impact (improvement or degradation)
- Quality assessment (if applicable)

**Implementation Details**
- Code changes made (with file references)
- Dependencies added
- Configuration changes
- Deployment considerations

**Challenges & Solutions**
- Problems encountered during implementation
- How they were resolved
- Workarounds or compromises made

**Future Work**
- Additional optimizations identified but not implemented
- Monitoring and alerting plans
- Scale testing plans

## Grading Criteria

This lab is part of your ongoing capstone development. Quality is assessed on:

**Optimization Audit (In-Lab) - Completeness Check**
- ✓ Current state thoroughly analyzed
- ✓ At least 5 opportunities identified with impact estimates
- ✓ Top 3 selected with clear justification
- ✓ Cost calculator functional and realistic

**Implementation (Homework) - Quality Assessment**
- **Impact (40%)**: Measurable cost or latency improvements
- **Quality (30%)**: Implementation follows best practices, code quality maintained
- **Documentation (20%)**: Clear explanation of changes and results
- **Instrumentation (10%)**: Cost tracking properly implemented

**Exceptional Work Indicators:**
- 70%+ cost reduction with maintained quality
- Novel optimization approach for your specific use case
- Production-grade monitoring dashboard
- Detailed A/B test results validating model downgrades

## Common Pitfalls to Avoid

### "We'll optimize later"
This IS later. Optimization is easiest to implement mid-project, not at the end when everything is hardcoded.

### "Caching is too complex"
Start simple - even in-memory caching with Python `dict` saves money. You can upgrade to Redis later.

### "Our costs are already low"
It's not just about current costs - it's about learning production patterns before you scale. $10/month becomes $1,000/month at 100x traffic.

### "We can't measure the impact"
If you don't have baseline metrics, start collecting them TODAY. Even rough estimates are better than nothing.

### "Quality might suffer"
That's why you test! Use your evaluation suite from Week 11. Set quality thresholds. Rollback if metrics degrade.

## FAQ

### Q: Our capstone doesn't have high API usage yet. Should we still optimize?

A: Yes! This lab teaches patterns you'll need in production. Implement them now while the codebase is manageable. Plus, it demonstrates professional engineering in your final demo.

### Q: Can we use third-party caching libraries like LangChain's cache?

A: Absolutely, but understand what they're doing under the hood. For your audit, document which library you're using and why.

### Q: What if optimization makes our code more complex?

A: Good observation. Balance is key. Document the complexity trade-off. Sometimes a 20% cost savings isn't worth 50% more code complexity. Make the trade-off explicit and justify your decision.

### Q: We're using an agent framework (LangChain, CrewAI). Can we still optimize?

A: Yes, but it's harder. Focus on: (1) Caching at the framework level if supported, (2) Model selection within framework config, (3) Monitoring framework costs. Document the limitations of optimization within your framework choice.

### Q: How do we handle cache invalidation?

A: Simple approach: Time-based TTL (time-to-live). Set cache entries to expire after N hours/days. Advanced: Event-based invalidation when underlying data changes. For this lab, TTL is sufficient.

### Q: What's a realistic cost reduction target?

A: Depends on your starting point:
- No caching → Adding cache: 40-80% reduction
- All GPT-4 → Mixed models: 60-90% reduction  
- No batching → Adding batches: 20-40% reduction

If you achieve 50% total reduction, that's excellent work.

## Resources

**In This Lab Folder:**
- [Cost Calculator Tool](./tools/cost-calculator.md)
- [Caching Implementation Guide](./guides/caching-implementation.md)
- [Model Selection Matrix](./guides/model-selection.md)
- [Batching Patterns](./guides/batching-patterns.md)
- [Cost Tracking Template](./templates/cost-tracking-template.py)

**External Resources:**
- OpenAI Pricing: https://openai.com/pricing
- Anthropic Pricing: https://www.anthropic.com/pricing
- Google AI Pricing: https://ai.google.dev/pricing
- Week 10 Lecture Materials: ../../lectures/week-10/

**Related Course Materials:**
- Week 4 Design Review (architecture context)
- Week 11 Evaluation (quality metrics)
- Week 12 Production Engineering (deployment patterns)

## Checklist: Ready to Submit?

**In-Lab Audit Document:**
- [ ] `docs/optimization-audit.md` exists in your repo
- [ ] Current state section complete with baseline metrics
- [ ] At least 5 optimization opportunities identified
- [ ] Top 3 selected with implementation plan
- [ ] Cost calculator included or linked
- [ ] Team member assignments clear
- [ ] Success metrics defined

**Homework Implementation:**
- [ ] Top 3 optimizations implemented and tested
- [ ] Cost tracking code added
- [ ] `docs/optimization-results.md` complete
- [ ] Before/after metrics documented
- [ ] Quality validation performed (no regressions)
- [ ] README updated with performance section
- [ ] Code committed to GitHub with clear commit messages

**Quality Checks:**
- [ ] No API keys in code (use .env)
- [ ] Cache invalidation strategy documented
- [ ] Model selection rationale explained
- [ ] Actual cost savings measured (not just projected)
- [ ] Latency impact assessed
- [ ] Team reviewed together

## What's Next?

**Week 11: Evaluation & Safety Audit**
- You'll need your optimization metrics for the safety audit
- Evaluation frameworks will measure if optimizations hurt quality
- Golden datasets will validate model selection choices

**Week 12: Production Engineering**
- Optimizations prepare you for CI/CD deployment
- Monitoring systems will track ongoing cost performance
- Production secrets management builds on .env patterns

**Week 15: Final Demo**
- Optimization results are a key demo talking point
- "We reduced costs 80% while maintaining quality" is impressive
- Performance metrics belong in your case study

Remember: Production optimization isn't just about saving money - it's about professional engineering discipline. The patterns you learn here apply to any resource-constrained system.

Good luck!
