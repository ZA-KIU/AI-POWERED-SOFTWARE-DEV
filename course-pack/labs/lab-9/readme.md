# Lab 9: Production Optimization for Your Capstone

## Overview
Apply Week 10's production optimization techniques to YOUR capstone project. Focus on reducing costs 30%+ while maintaining quality.

## Learning Objectives
By the end of this lab, you will:
- Document baseline cost and latency metrics for your capstone
- Implement ONE production optimization (model selection OR caching OR batching)
- Measure optimization impact with real data
- Make data-driven decisions about cost vs. quality trade-offs

## Prerequisites
- Working capstone code that makes LLM API calls
- Ability to make 20+ test queries to your system
- API keys for your LLM provider
- Basic understanding of caching (Redis optional but recommended)

## Time Estimate
- **In-lab**: 2 hours (structured workshop)
- **Homework**: 2-3 hours (complete optimization + integrate with Lab 8 if applicable)

## Lab Structure

### Part 1: Baseline Measurement (20 min)
Document your current state before optimizing anything.

**Tasks:**
1. Run 20+ queries through your capstone
2. Log cost per query, latency (p95), model used
3. Calculate monthly spend projection
4. Fill out `optimization-plan-template.md`

**Success:** You have baseline.json with real metrics

### Part 2: Choose Your Optimization (30 min)
Pick ONE technique to implement based on your capstone needs.

**Options:**
- **Model Cascading**: Start with cheap model, escalate if needed (best for: varied complexity queries)
- **Result Caching**: Cache repeated queries (best for: FAQ, common questions)
- **Batching**: Process multiple items together (best for: bulk processing, reports)

**Tasks:**
1. Review guides in `/guides/`
2. Choose optimization using Week 10 decision framework
3. Get instructor checkpoint before coding

**Success:** Clear implementation plan approved by instructor

### Part 3: Implementation (50 min)
Build your chosen optimization.

**Tasks:**
1. Copy starter code from `/code-examples/`
2. Adapt to your capstone
3. Test with sample queries
4. Debug and iterate

**Success:** Working code that runs your optimization

### Part 4: Measure Impact (20 min)
Prove your optimization works with data.

**Tasks:**
1. Run same 20+ queries from baseline
2. Calculate cost reduction %
3. Measure latency change
4. Document quality impact (if any)
5. Fill out optimization report

**Success:** Completed optimization-report.md with metrics

## Files in This Lab

### Templates
- `optimization-plan-template.md` - Your optimization strategy
- `cost-calculation-template.md` - Excel-style calculator for costs

### Guides
- `model-selection-guide.md` - When to use which model + cascading
- `caching-implementation-guide.md` - Three types of caching
- `cost-tracking-guide.md` - How to measure everything

### Code Examples
- `model_cascading.py` - Haiku → Mini → GPT-4o pattern
- `redis_cache.py` - Result caching with Redis

## Homework Assignment
See `homework-assignment.md` for:
- Completing your optimization
- Integrating Labs 8 + 9 (agents + optimization)
- Final optimization report submission

## Common Issues

**"I don't know which optimization to pick"**
- Use the decision tree in `model-selection-guide.md`
- Ask: What's expensive in my capstone?

**"I don't have Redis installed"**
- Use in-memory dict for caching (see examples)
- Redis is optional but recommended

**"My optimization made things worse"**
- Check if you're measuring correctly
- Quality might have dropped - add quality checks
- Some optimizations need tuning (thresholds, TTLs)

**"I can't get 30% cost reduction"**
- That's OK! Even 15% is valuable
- Document what you learned
- Multiple optimizations compound over time

## Resources
- Week 10 lecture slides (model selection, caching, batching)
- Redis documentation: https://redis.io/docs/
- OpenAI pricing: https://openai.com/pricing
- Anthropic pricing: https://anthropic.com/pricing

## Next Week Preview
Week 11: Evaluation & Observability
- Golden sets for testing
- Regression tests
- Production telemetry
- Quality metrics

---

**Remember:** Measure before optimizing. Optimize what matters. Measure to prove it works.
