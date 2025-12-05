# Cost Calculation Template

Use this template to calculate your capstone's costs accurately. Copy to Excel/Google Sheets for automatic calculations.

---

## Pricing Reference (2025)

### OpenAI Pricing (per 1M tokens)
| Model | Input | Output |
|-------|--------|--------|
| GPT-4o | $2.50 | $10.00 |
| GPT-4o-mini | $0.15 | $0.60 |
| GPT-3.5-turbo | $0.50 | $1.50 |

### Anthropic Pricing (per 1M tokens)
| Model | Input | Output |
|-------|--------|--------|
| Claude 3.7 Sonnet | $3.00 | $15.00 |
| Claude 3.5 Haiku | $0.80 | $4.00 |

### Google Pricing (per 1M tokens)
| Model | Input | Output |
|-------|--------|--------|
| Gemini 1.5 Pro | $1.25 | $5.00 |
| Gemini 1.5 Flash | $0.075 | $0.30 |

**Note:** Prices change. Check provider websites for current rates.

---

## Calculator

### Single Query Cost

**Fill in your values:**

| Parameter | Your Value |
|-----------|-----------|
| Input tokens | _____ |
| Output tokens | _____ |
| Model used | _____ |
| Input price (per 1M) | $_____ |
| Output price (per 1M) | $_____ |

**Formulas:**

```
Input cost = (Input tokens / 1,000,000) × Input price
Output cost = (Output tokens / 1,000,000) × Output price
Total cost per query = Input cost + Output cost
```

**Example Calculation:**
```
Input: 1500 tokens × $2.50/1M = $0.00375
Output: 300 tokens × $10.00/1M = $0.00300
Total: $0.00675 per query
```

---

## Daily/Monthly Projection

### Usage Estimate

| Metric | Your Value |
|--------|-----------|
| Cost per query | $_____ |
| Queries per day | _____ |
| Days per month | 30 |

**Formulas:**

```
Daily cost = Cost per query × Queries per day
Monthly cost = Daily cost × 30
Annual cost = Monthly cost × 12
```

**Example:**
```
$0.00675 per query × 1000 queries/day = $6.75/day
$6.75/day × 30 = $202.50/month
```

---

## Optimization Impact Calculator

### Baseline (Before Optimization)

| Metric | Value |
|--------|-------|
| Cost per query | $_____ |
| Queries per day | _____ |
| Daily cost | $_____ |
| Monthly cost | $_____ |

### Optimized (After Optimization)

| Metric | Value |
|--------|-------|
| Cost per query | $_____ |
| Queries per day | _____ (same) |
| Daily cost | $_____ |
| Monthly cost | $_____ |

### Savings Calculation

**Formulas:**

```
Cost reduction $ = Baseline monthly - Optimized monthly
Cost reduction % = (Cost reduction $ / Baseline monthly) × 100

Annual savings = Cost reduction $ × 12
```

**Example:**
```
Baseline: $202.50/month
Optimized: $60.75/month
Reduction: $141.75/month (70% reduction)
Annual savings: $1,701
```

---

## Model Cascading Cost Calculator

### Scenario: Route queries intelligently

| Scenario | % of Queries | Model | Cost/Query | Subtotal |
|----------|--------------|-------|-----------|----------|
| Simple (Haiku handles) | _____% | Haiku | $_____  | $_____ |
| Medium (Mini handles) | _____% | Mini | $_____ | $_____ |
| Complex (GPT-4o needed) | _____% | GPT-4o | $_____ | $_____ |
| **Total** | **100%** | - | - | $_____ |

**Formula:**
```
Average cost = (Simple% × Simple cost) + (Medium% × Medium cost) + (Complex% × Complex cost)
```

**Example:**
```
70% × $0.001 (Haiku) = $0.0007
20% × $0.003 (Mini) = $0.0006
10% × $0.007 (GPT-4o) = $0.0007
Average = $0.002 per query (vs $0.007 all GPT-4o = 71% savings)
```

---

## Caching Cost Calculator

### With Result Caching

| Metric | Value |
|--------|-------|
| Total queries per day | _____ |
| Cache hit rate | _____% |
| Cache miss rate | _____% |
| Cost per cache hit | $0.00 (instant return) |
| Cost per cache miss | $_____ (full API call) |

**Formula:**
```
Daily cost with cache = (Cache miss % × Total queries × Cost per query)
```

**Example:**
```
1000 queries/day
70% cache hit rate (700 queries = $0)
30% cache miss rate (300 queries × $0.00675) = $2.025/day
Monthly: $60.75 (vs $202.50 without cache = 70% savings)
```

---

## Batch API Calculator (OpenAI)

### Standard vs Batch

| Type | Queries | Cost/Query | Total Cost |
|------|---------|-----------|-----------|
| Standard API | _____ | $_____ | $_____ |
| Batch API (50% off) | _____ | $_____ | $_____ |

**Formula:**
```
Batch cost = Standard cost × 0.5
```

**Example:**
```
Process 10,000 reviews
Standard: 10,000 × $0.00675 = $67.50
Batch: 10,000 × $0.003375 = $33.75 (50% savings)
```

---

## Advanced: Multi-Optimization Calculator

If you implement multiple optimizations, they compound:

| Optimization | Reduction % | Cumulative Cost |
|--------------|-------------|-----------------|
| Baseline | 0% | $200.00 |
| Add cascading | 30% | $140.00 |
| Add caching | 50% (on $140) | $70.00 |
| Add batching | 50% (on $70) | $35.00 |

**Total reduction:** 82.5% (from $200 to $35)

**Formula for compound savings:**
```
Final cost = Baseline × (1 - Opt1%) × (1 - Opt2%) × (1 - Opt3%)
```

---

## Real Production Example

### Case Study: E-commerce Support Bot

**Before optimization:**
- Model: GPT-4o for everything
- 10,000 queries/day
- Avg 1500 input + 300 output tokens
- Cost: $0.00675/query
- Monthly: $2,025

**After optimization:**
- Model cascading: 80% Haiku, 15% Mini, 5% GPT-4o
- Result caching: 65% hit rate
- Batching: 50% off for report generation

**New cost:**
- Cascading saves: 60% ($2,025 → $810)
- Caching saves: 65% on remaining ($810 → $283)
- Batching saves: 50% on reports ($283 → $192)

**Final: $192/month (90.5% reduction)**

---

## Your Capstone Calculation

Use this space for your specific calculations:

### Baseline
- Model: _____________________
- Input tokens: _____
- Output tokens: _____
- Cost per query: $_____
- Queries per day: _____
- **Monthly cost: $_____**

### Optimization Strategy
Technique: _____________________

### Expected Result
- New cost per query: $_____
- **New monthly cost: $_____**
- **Savings: $_____/month (_____% reduction)**

---

## Pro Tips

1. **Token estimation:** If you don't have exact counts, use `len(text) / 4` for rough estimate
2. **Cache hit rates:** Start conservative (30-40%), measure actual rates
3. **Model distribution:** Log actual routing decisions to get accurate percentages
4. **Include all costs:** Don't forget embeddings, tool calls, image generation
5. **Budget buffer:** Add 20% buffer for unexpected spikes

---

## Export to Spreadsheet

Copy this structure to Google Sheets or Excel:

**Column A:** Metric name
**Column B:** Value
**Column C:** Formula (if applicable)
**Column D:** Notes

Then use spreadsheet formulas like:
```
=B2*B3  (multiply queries × cost)
=(B10-B11)/B10  (calculate reduction %)
```

---

**Remember:** These are estimates. Real costs may vary based on actual token usage. Always measure production metrics!
