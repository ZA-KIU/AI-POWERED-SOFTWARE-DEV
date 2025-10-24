# Token Usage & Cost Model (Version 2)

**Project Name:** [Your Project Name]  
**Team Members:** [Names]  
**Date:** Week 4, [Date]  
**Version:** 2.0 (Updated with Week 3-4 actual data)

---

## 📊 Executive Summary

**Current Cost Per Query:** $[X.XX]  
**Projected Monthly Cost (Production):** $[XXX]  
**Optimization Potential:** [X]% cost reduction identified  
**Budget Status:** [On track / Needs attention / Critical]

**Key Insight:**
> [1-2 sentence summary of biggest cost finding or optimization opportunity]

---

## 1. Current Baseline (Week 4)

### Token Usage Breakdown

Based on actual usage from Week 3-4 testing:

**Per Query Analysis:**

| Component | Tokens | Cost | % of Total |
|-----------|--------|------|------------|
| **System Prompt** | [XXX] tokens | $[X.XXX] | [XX]% |
| **User Query** | [XXX] tokens | $[X.XXX] | [XX]% |
| **Retrieved Context** (if RAG) | [XXX] tokens | $[X.XXX] | [XX]% |
| **Input Subtotal** | [XXX] tokens | $[X.XXX] | [XX]% |
| **Output (Response)** | [XXX] tokens | $[X.XXX] | [XX]% |
| **TOTAL PER QUERY** | **[XXX] tokens** | **$[X.XXX]** | **100%** |

**Example (Receipt Scanner):**

| Component | Tokens | Cost (GPT-4o) | % of Total |
|-----------|--------|---------------|------------|
| **System Prompt** | 500 tokens | $0.00250 | 19% |
| **User Query** | 200 tokens | $0.00100 | 8% |
| **Retrieved Context** | 0 tokens (no RAG) | $0.00000 | 0% |
| **Input Subtotal** | 700 tokens | $0.00350 | 27% |
| **Output (JSON response)** | 600 tokens | $0.00900 | 73% |
| **TOTAL PER QUERY** | **1,300 tokens** | **$0.01250** | **100%** |

**Key Findings:**
- Output tokens are 73% of total cost
- System prompt is 38% of input cost (optimization opportunity!)
- Average query: ~1,300 tokens @ $0.0125

---

### Current Usage Patterns

**Week 3-4 Testing Data:**

| Metric | Value |
|--------|-------|
| Total queries (Week 3-4) | [XX] queries |
| Average queries/day | [X] queries |
| Total tokens used | [X,XXX] tokens |
| Total cost incurred | $[XX.XX] |
| Model used | [GPT-4o / GPT-4o-mini / mix] |

**Cost Breakdown by Day:**

| Date | Queries | Tokens | Cost |
|------|---------|--------|------|
| Oct 15 | 12 | 15,600 | $1.95 |
| Oct 16 | 18 | 23,400 | $2.93 |
| Oct 17 | 8 | 10,400 | $1.30 |
| Oct 18 | 15 | 19,500 | $2.44 |
| **Total** | **53** | **68,900** | **$8.62** |

---

## 2. Cost Model (Current vs. Projected)

### Development Phase (Weeks 3-9)

**Current Usage:**
- Queries per day: ~10-20 (testing)
- Days remaining: 42 days (6 weeks)
- Estimated queries: 630-1,260 queries
- **Projected cost: $7.88 - $15.75**

### Production Phase (Weeks 10-15)

**Expected Usage:**
- Queries per day: 50-100 (user testing + demo prep)
- Days: 42 days (6 weeks)
- Estimated queries: 2,100-4,200 queries
- **Projected cost: $26.25 - $52.50**

### Total Semester Projection

| Phase | Queries | Cost (Current Model) | Cost (Optimized) | Savings |
|-------|---------|----------------------|------------------|---------|
| Development (W3-9) | 630-1,260 | $7.88-$15.75 | $3.15-$6.30 | 60% |
| Production (W10-15) | 2,100-4,200 | $26.25-$52.50 | $10.50-$21.00 | 60% |
| **TOTAL** | **2,730-5,460** | **$34-$68** | **$14-$27** | **60%** |

**Budget Allocation:**
- AI API costs: $27 (optimized)
- User testing incentives: $50 (5 participants × $10)
- Infrastructure (Vercel, Railway): $10
- Image storage (Cloudinary): $5
- Buffer/contingency: $8
- **Total Budget: $100** (well within $200 course budget)

---

## 3. Optimization Strategies

### Strategy 1: Compress System Prompt ⭐ High Impact

**Current System Prompt (500 tokens):**
```
You are an expert receipt analyzer. Your job is to extract information 
from receipt images. Be thorough and accurate. Always include merchant 
name, date, total amount, and itemized list. Format your response as JSON. 
Be polite and professional. If you're unsure about any information, 
indicate that in your confidence score. Remember that accuracy is critical 
for tax purposes. Users rely on your extractions. Double-check all numbers. 
[... continues for 500 tokens]
```

**Optimized System Prompt (200 tokens - 60% reduction):**
```
Extract receipt data: merchant, date, amount, items. Return JSON. 
Accuracy critical (tax purposes). Include confidence score (0-1) if uncertain.
```

**Why This Works:**
- Removes fluff ("be polite and professional")
- Removes redundancy (multiple mentions of accuracy)
- Keeps critical instructions (JSON format, confidence score)
- LLMs don't need verbose instructions

**Token Savings:** 300 tokens input per query  
**Cost Savings:** $0.0015/query → **$8.19/semester (24% reduction)**

---

### Strategy 2: Use Structured Output (JSON Schema) ⭐ High Impact

**Current Output (600 tokens):**
```json
{
  "merchant": "Whole Foods Market",
  "explanation": "The merchant name is clearly visible at the top...",
  "date": "2024-10-15",
  "date_confidence": "High - clearly printed",
  "amount": 87.43,
  "amount_note": "This is the total after tax",
  "items": [
    {"name": "Organic Bananas", "price": 3.99, "note": "Produce section"},
    ...
  ],
  "summary": "This receipt appears to be from a grocery store purchase..."
}
```

**Optimized Output with JSON Schema (300 tokens - 50% reduction):**
```json
{
  "merchant": "Whole Foods Market",
  "date": "2024-10-15",
  "amount": 87.43,
  "items": [
    {"name": "Organic Bananas", "price": 3.99},
    {"name": "Milk", "price": 4.99}
  ],
  "confidence": 0.95
}
```

**Implementation:**
```python
from pydantic import BaseModel
from typing import List

class ReceiptItem(BaseModel):
    name: str
    price: float

class ReceiptData(BaseModel):
    merchant: str
    date: str
    amount: float
    items: List[ReceiptItem]
    confidence: float

response = client.chat.completions.create(
    model="gpt-4o-2024-08-06",
    messages=messages,
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "receipt_extraction",
            "schema": ReceiptData.model_json_schema()
        }
    }
)
```

**Token Savings:** 300 tokens output per query  
**Cost Savings:** $0.0045/query → **$12.29/semester (37% reduction)**

---

### Strategy 3: Remove Redundant User Query

**Current:**
```
User: "Please analyze this receipt image and extract all relevant information."
+ [image]
```

**Optimized:**
```
User: [image only, no text]
```

**Rationale:** System prompt already explains the task. User query is redundant.

**Token Savings:** 200 tokens input per query  
**Cost Savings:** $0.0010/query → **$2.73/semester (8% reduction)**

---

### Strategy 4: Implement Caching ⭐ High Impact

**Strategy:** Cache results for identical or similar queries

**Expected Cache Hit Rate:** 40% (users often upload same receipt accidentally, or very similar receipts)

**Implementation:**
```python
import redis
import hashlib

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def get_image_hash(image_bytes):
    return hashlib.md5(image_bytes).hexdigest()

def process_receipt(image):
    image_hash = get_image_hash(image)
    
    # Check cache
    cached = redis_client.get(f"receipt:{image_hash}")
    if cached:
        return json.loads(cached)  # Cache hit!
    
    # Cache miss - call API
    result = call_openai_api(image)
    
    # Cache for 7 days
    redis_client.setex(
        f"receipt:{image_hash}",
        604800,
        json.dumps(result)
    )
    
    return result
```

**Cost Savings (40% cache hit rate):**
- Prevents ~1,092 API calls (40% of 2,730)
- Saves ~$13.65 (40% of optimized cost)
- **Total savings: 50% additional reduction**

**Infrastructure Cost:** $5/month for Redis (Upstash free tier)

---

### Strategy 5: Hybrid Model Selection ⭐ High Impact

**Strategy:** Use GPT-4o-mini for clear images, GPT-4o only for poor quality

**Current Model:** GPT-4o for everything  
**Optimized:** 80% GPT-4o-mini, 20% GPT-4o

**Model Pricing:**
- GPT-4o: $0.005/1K input, $0.015/1K output
- GPT-4o-mini: $0.00015/1K input, $0.0006/1K output (96% cheaper!)

**Cost Calculation:**

**GPT-4o (current - 100% of queries):**
- Input: 200 tokens × $0.005/1K = $0.001/query
- Output: 300 tokens × $0.015/1K = $0.0045/query
- **Total: $0.0055/query**

**GPT-4o-mini:**
- Input: 200 tokens × $0.00015/1K = $0.00003/query
- Output: 300 tokens × $0.0006/1K = $0.00018/query
- **Total: $0.00021/query**

**Blended (80% mini, 20% full):**
- Mini: 0.80 × $0.00021 = $0.000168/query
- Full: 0.20 × $0.0055 = $0.0011/query
- **Total: $0.001268/query (77% savings!)**

**Implementation:**
```python
def assess_image_quality(image):
    # Simple heuristic: check contrast, sharpness
    # Return score 0-1
    return quality_score

def choose_model(image):
    quality = assess_image_quality(image)
    
    if quality > 0.7:
        return "gpt-4o-mini"  # Clear image
    else:
        return "gpt-4o"       # Poor quality, needs better model
```

**Token Savings:** N/A (model switch, not token reduction)  
**Cost Savings:** 77% reduction → **Save ~$17/semester**

---

## 4. Combined Optimization Impact

### Cumulative Savings

| Optimization | Token Reduction | Cost Savings | Implementation Effort |
|--------------|-----------------|--------------|----------------------|
| #1: Compress System Prompt | 300 input | $8.19 (24%) | 30 min |
| #2: Structured Output | 300 output | $12.29 (37%) | 2 hours |
| #3: Remove User Query | 200 input | $2.73 (8%) | 15 min |
| #4: Caching (40% hit rate) | All tokens (40% calls) | $13.65 (50% additional) | 4-6 hours |
| #5: Hybrid Model Selection | N/A | $17.00 (77%) | 3 hours |

**Original Projected Cost:** $34-$68/semester  
**After #1-3 (Quick wins):** $11-$22/semester (68% reduction)  
**After #4 (Caching):** $6.60-$13.20/semester (81% reduction)  
**After #5 (Hybrid model):** $2.65-$5.30/semester (92% reduction!)**

---

## 5. Implementation Roadmap

### Week 4 (Immediate - Do Now)

- [ ] **Optimize system prompt** (30 min)
  - Reduce from 500 to 200 tokens
  - Test that quality is maintained
  - Deploy to production

- [ ] **Remove redundant user query** (15 min)
  - Update API to accept image-only requests
  - Test end-to-end flow

**Expected Savings:** 32% cost reduction ($11 saved)

---

### Week 5 (High Priority)

- [ ] **Implement structured output** (2 hours)
  - Define Pydantic models
  - Update OpenAI API call with JSON schema
  - Test with 10 receipts
  - Validate format consistency

**Expected Savings:** Additional 37% reduction ($12 saved)

---

### Week 6 (High Priority)

- [ ] **Implement hybrid model selection** (3 hours)
  - Write image quality assessment function
  - Add model routing logic
  - Test quality on both models
  - Monitor cost difference

**Expected Savings:** 77% reduction on model costs ($17 saved)

---

### Week 7-8 (Medium Priority)

- [ ] **Add Redis caching** (4-6 hours)
  - Set up Redis (Upstash free tier)
  - Implement cache-aside pattern
  - Add cache invalidation logic (if user edits)
  - Monitor cache hit rate

**Expected Savings:** 50% additional reduction ($13 saved)

---

## 6. Cost Tracking Dashboard

### Metrics to Monitor

**Daily:**
- [ ] Cost per query (running average)
- [ ] Total daily spend
- [ ] Token usage trend
- [ ] Model distribution (% mini vs full)

**Weekly:**
- [ ] Weekly cost total
- [ ] Cache hit rate (if implemented)
- [ ] Budget burn rate
- [ ] Projected end-of-semester cost

**Monthly:**
- [ ] Month-to-date spend
- [ ] Cost optimization impact measurement
- [ ] Budget health check

### Dashboard Implementation

**Option 1: Simple Spreadsheet**
```
Date | Queries | Tokens | Cost | Model | Cache Hit | Notes
-----|---------|--------|------|-------|-----------|------
Oct 15 | 12 | 15,600 | $1.95 | GPT-4o | N/A | Baseline
Oct 16 | 18 | 23,400 | $2.93 | GPT-4o | N/A | Baseline
Oct 22 | 15 | 6,000 | $0.30 | 80% mini | 40% | Optimized!
```

**Option 2: Automated Dashboard**
- Log every API call to database
- Create Grafana/Metabase dashboard
- Set up cost alerts (>$5/day)

---

## 7. Budget Allocation (Full Semester)

### Cost Categories

| Category | Budgeted | Actual (W1-4) | Projected (W5-15) | Total |
|----------|----------|---------------|-------------------|-------|
| **AI API (Optimized)** | $30 | $8.62 | $18.38 | $27 |
| **User Testing Incentives** | $50 | $0 | $50 | $50 |
| **Infrastructure** | | | | |
| - Vercel (Frontend) | $0 | $0 | $0 | $0 |
| - Railway (Backend+DB) | $5 | $1 | $4 | $5 |
| - Cloudinary (Images) | $0 | $0 | $0 | $0 |
| - Redis (Cache) | $5 | $0 | $5 | $5 |
| **Buffer/Contingency** | $10 | $0 | $10 | $10 |
| **TOTAL** | **$100** | **$9.62** | **$87.38** | **$97** |

**Budget Health:** ✅ Healthy (under $200 course limit by $103)

---

## 8. Cost Alerts & Thresholds

### Alert Levels

**Warning (Yellow):**
- Daily spend >$3
- Weekly spend >$15
- Monthly projection >$60

**Action Required (Orange):**
- Daily spend >$5
- Weekly spend >$25
- 80% of semester budget consumed

**Critical (Red):**
- Daily spend >$10
- Weekly spend >$40
- 90% of semester budget consumed

### Response Plan

**If Yellow Alert:**
- Review recent queries for anomalies
- Check for optimization opportunities
- Notify team in Slack

**If Orange Alert:**
- Immediate optimization deployment
- Reduce testing volume if needed
- Team meeting to discuss

**If Red Alert:**
- Pause non-essential API calls
- Switch to GPT-4o-mini exclusively
- Escalate to instructor

---

## 9. Alternative Models Consideration

### Model Comparison

| Model | Input Cost | Output Cost | Quality | Notes |
|-------|------------|-------------|---------|-------|
| **GPT-4o** | $0.005/1K | $0.015/1K | Excellent | Current baseline |
| **GPT-4o-mini** | $0.00015/1K | $0.0006/1K | Very good | 96% cheaper, slight quality drop |
| **Claude 3.5 Sonnet** | $0.003/1K | $0.015/1K | Excellent | Alternative option |
| **Gemini Pro** | $0.00025/1K | $0.0005/1K | Good | Cheapest, but quality concerns |

**Decision:** Stick with OpenAI GPT-4o-mini/GPT-4o hybrid
- Best quality-to-cost ratio
- Already integrated
- Structured output support

---

## 10. Long-Term Cost Sustainability

### Post-Course Considerations

**If we launch this as real product:**

**Expected Scale:**
- 100 users
- 10 queries per user per month
- 1,000 queries/month

**Costs (Optimized Model):**
- 1,000 queries × $0.00127/query = $1.27/month
- Infrastructure: $10/month (upgraded tiers)
- **Total: ~$11/month**

**Revenue Model (If Monetizing):**
- Freemium: $0 (50 queries/month)
- Pro: $9.99/month (unlimited queries)
- Need: 2 paying users to break even

**Conclusion:** Economically viable post-course!

---

## ✅ Cost Optimization Checklist

**Week 4 (This Week):**
- [ ] Compress system prompt (30 min)
- [ ] Remove redundant user query (15 min)
- [ ] Set up cost tracking spreadsheet
- [ ] Measure baseline performance

**Week 5:**
- [ ] Implement structured output
- [ ] Measure token reduction
- [ ] Update cost projections

**Week 6:**
- [ ] Implement hybrid model selection
- [ ] A/B test quality difference
- [ ] Measure cost savings

**Week 7-8:**
- [ ] Set up Redis caching
- [ ] Monitor cache hit rate
- [ ] Validate final cost model

**Ongoing:**
- [ ] Monitor daily costs
- [ ] Review weekly spend
- [ ] Adjust if needed

---

**Document Version:** 2.0  
**Last Updated:** Week 4, [Date]  
**Next Review:** Week 6 (after optimization implementation)

---

## 📊 Appendix: Token Calculation Reference

### OpenAI Pricing (as of Oct 2024)

**GPT-4o:**
- Input: $0.005 per 1K tokens
- Output: $0.015 per 1K tokens

**GPT-4o-mini:**
- Input: $0.00015 per 1K tokens
- Output: $0.0006 per 1K tokens

### Token Estimation Guide

**Rough estimates:**
- 1 token ≈ 4 characters
- 1 token ≈ 0.75 words
- 100 words ≈ 133 tokens
- 1,000 characters ≈ 250 tokens

**Use `tiktoken` library for accurate counts:**
```python
import tiktoken

encoding = tiktoken.encoding_for_model("gpt-4o")
text = "Your prompt here..."
token_count = len(encoding.encode(text))
print(f"Token count: {token_count}")
```
