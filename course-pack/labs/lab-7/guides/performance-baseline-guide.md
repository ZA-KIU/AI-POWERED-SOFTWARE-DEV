# Performance Baseline Guide

This guide shows you how to establish and document performance baselines for your AI application.

## Why Performance Baselines Matter

Baselines let you:
- Detect performance regressions
- Make data-driven optimization decisions
- Project costs at scale
- Set SLAs and alerts

Without baselines, you can't answer: "Is this slow? Is this expensive? Did my change help?"

## What to Measure

### 1. Latency
**End-to-end response time from user input to final output**

Measure these percentiles:
- **p50 (median)** - Typical user experience
- **p95** - Most users experience
- **p99** - Worst case (still common enough to matter)

Why percentiles? Average hides outliers. p95 shows what 95% of users actually experience.

### 2. Token Usage
**How many tokens each request consumes**

Track separately:
- Input tokens (prompt + context)
- Output tokens (generated response)
- Total tokens (sum)

Why? Cost scales with tokens. Optimization starts here.

### 3. Cost
**Dollars per request**

Calculate:
```
Cost = (input_tokens × input_rate) + (output_tokens × output_rate)
```

Example (GPT-4 Turbo):
```
Input: 127 tokens × $0.01/1000 = $0.00127
Output: 85 tokens × $0.03/1000 = $0.00255
Total: $0.00382 per request
```

### 4. Throughput (Week 8+)
**Requests per second your system can handle**

Test with concurrent requests to find breaking point.

## How to Measure

### Method 1: Manual Timing (Simple)

```python
import time

start = time.time()
response = call_llm(prompt)
latency_ms = (time.time() - start) * 1000
```

### Method 2: Structured Logging (Better)

```python
import logging
import time

def call_llm_with_logging(prompt, request_id):
    start = time.time()
    try:
        response = client.chat.completions.create(...)
        latency_ms = (time.time() - start) * 1000
        
        logging.info({
            "event": "llm_response",
            "request_id": request_id,
            "latency_ms": latency_ms,
            "input_tokens": response.usage.prompt_tokens,
            "output_tokens": response.usage.completion_tokens,
            "total_tokens": response.usage.total_tokens,
            "cost_usd": calculate_cost(response.usage)
        })
        return response
    except Exception as e:
        logging.error({
            "event": "llm_error",
            "request_id": request_id,
            "error": str(e)
        })
        raise
```

## Sample Size

**Minimum: 20 requests** for reliable statistics  
**Better: 50+ requests** to capture variability  
**Best: 100+ requests** with diverse inputs

Why? Single measurements lie. Distributions tell truth.

## Analysis

### Calculate Percentiles

```python
import numpy as np

latencies = [2100, 2300, 1800, 2500, 2200, ...]  # milliseconds

p50 = np.percentile(latencies, 50)
p95 = np.percentile(latencies, 95)
p99 = np.percentile(latencies, 99)
avg = np.mean(latencies)

print(f"p50: {p50}ms, p95: {p95}ms, p99: {p99}ms, avg: {avg}ms")
```

### Identify Bottlenecks

Break down latency by component:
```
Total latency: 3.2s
- Database query: 0.5s (15%)
- Document retrieval: 0.8s (25%)
- LLM API call: 1.7s (53%)
- Response processing: 0.2s (7%)
```

Optimize the 53% component first (LLM call).

### Cost Extrapolation

```
Cost per request: $0.004
Daily volume estimate: 1,000 requests
Monthly cost: $0.004 × 1,000 × 30 = $120/month
```

Test at 10x scale:
```
10,000 requests/day = $1,200/month
```

Is this sustainable? If no, optimize.

## Optimization Strategies

### For Latency

1. **Cache responses** - Identical queries return instantly
2. **Use faster model** - GPT-3.5 vs GPT-4 (3-5x faster)
3. **Parallel execution** - Don't wait for sequential operations
4. **Optimize prompts** - Shorter context = faster response
5. **Stream responses** - User sees progress immediately

### For Cost

1. **Use cheaper model** - Try GPT-3.5 first, upgrade only if needed
2. **Reduce context** - Trim irrelevant information
3. **Cache aggressively** - Same query = $0 cost
4. **Implement quotas** - Limit per-user usage
5. **Batch requests** - Some APIs offer batching discounts

## Documentation Template

```markdown
## Performance Baseline

### Test Methodology
- Date: [2025-01-15]
- Sample size: [25 requests]
- Test environment: [Laptop, WiFi]
- Test inputs: [Mix of short/long queries]

### Latency Results
| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| p50    | 2.1s  | <3s    | ✅ PASS |
| p95    | 4.7s  | <5s    | ✅ PASS |
| p99    | 8.3s  | <10s   | ✅ PASS |

### Token Usage
- Average input: 127 tokens
- Average output: 85 tokens
- Total average: 212 tokens

### Cost Analysis
- Per request: $0.0038
- Per 100 users/day: $11.40/month
- Per 1,000 users/day: $114/month

### Bottleneck Analysis
Slowest component: LLM API call (65% of latency)
Optimization: Consider GPT-3.5 for simple queries
```

## Week 8 Implications

Agent orchestration will 5-20x your metrics:

Current:
- 1 LLM call per request
- 2.1s latency
- $0.004 cost

With agents (10 steps):
- 10 LLM calls per request
- 21s latency (if sequential)
- $0.04 cost

**Action:** Implement parallel execution, caching, and streaming.

## Common Mistakes

❌ Measuring only average (hides outliers)  
✅ Measure p50, p95, p99

❌ Testing with one query type  
✅ Test diverse inputs (short, long, edge cases)

❌ Ignoring variability  
✅ Run 20+ samples

❌ Not documenting methodology  
✅ Document environment, sample size, test data

## Checklist

- [ ] Collected 20+ request measurements
- [ ] Calculated p50, p95, p99 latency
- [ ] Tracked token usage (input/output)
- [ ] Calculated cost per request
- [ ] Identified bottlenecks
- [ ] Extrapolated to scale (100x, 1000x)
- [ ] Documented methodology
- [ ] Assessed Week 8 readiness

Good baselines = informed decisions.
