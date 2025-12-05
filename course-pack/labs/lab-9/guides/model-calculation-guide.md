# Model Selection Guide

**Goal:** Choose the right model for each task to balance cost, speed, and quality.

---

## The Model Landscape (2025)

### Frontier Models (Complex Reasoning)
**Use for:** Legal analysis, creative writing, complex coding, medical advice

| Model | Input Cost | Output Cost | Speed | Best For |
|-------|-----------|-------------|-------|----------|
| GPT-4o | $2.50/1M | $10.00/1M | Slow | Complex reasoning |
| Claude 3.7 Sonnet | $3.00/1M | $15.00/1M | Medium | Analysis, writing |
| Gemini Pro | $1.25/1M | $5.00/1M | Medium | Balanced tasks |

### Fast/Efficient Models (High Volume)
**Use for:** Classification, simple Q&A, routing, extraction

| Model | Input Cost | Output Cost | Speed | Best For |
|-------|-----------|-------------|-------|----------|
| GPT-4o-mini | $0.15/1M | $0.60/1M | Fast | Most tasks |
| Claude Haiku | $0.80/1M | $4.00/1M | Fastest | Classification |
| Gemini Flash | $0.075/1M | $0.30/1M | Fast | High volume |

### Edge/Specialized Models
**Use for:** Local-first, privacy, routing

| Model | Cost | Speed | Best For |
|-------|------|-------|----------|
| Llama 3.2 1B/3B | Free (self-host) | Instant | Edge devices |
| Phi-4 | Free (self-host) | Fast | Privacy-first |

---

## The 4-Question Decision Method

### Question 1: What's the task complexity?

**Simple tasks** → Fast model
- Intent classification
- Sentiment analysis
- Simple summaries
- Yes/no questions
- Keyword extraction

**Complex tasks** → Frontier model
- Legal contract review
- Medical diagnosis
- Multi-step reasoning
- Creative writing
- Code generation (large)

**Example Decision:**
```
"Is this email spam?" → Haiku (simple classification)
"Write legal analysis of this contract" → GPT-4o (complex reasoning)
```

### Question 2: What's the acceptable latency?

**Real-time (<2s required)** → Fast model
- Chat responses
- Auto-complete
- Real-time classification

**Analysis (5-10s OK)** → Can use slower models
- Document analysis
- Research
- Report generation

**Background (30s+ OK)** → Optimize for cost, not speed
- Batch processing
- Overnight jobs
- Data labeling

**Example Decision:**
```
Live chat: Use Haiku (0.5-1.5s response)
Weekly report: Use GPT-4o (quality > speed)
```

### Question 3: What's the cost constraint?

**High volume** → Budget model
- 10,000+ requests/day
- Cost matters more than perfection
- Acceptable to miss edge cases

**High value** → Frontier model
- Low volume, high stakes
- Mistakes are expensive
- Quality is critical

**Example Decision:**
```
Customer support (1000/day): Use cascading
Medical advice (10/day): Use GPT-4o always
```

### Question 4: What's the error cost?

**Low error cost** → Cheap model OK
- Product suggestions
- Content recommendations
- Casual conversation

**High error cost** → Frontier model required
- Medical advice
- Legal guidance
- Financial decisions
- Safety-critical systems

**Example Decision:**
```
"Suggest similar products": Haiku is fine
"Diagnose medical symptoms": GPT-4o required
```

---

## Decision Tree for Your Capstone

```
START: What does your capstone do?

├── Classification/Routing
│   ├── Real-time? → Haiku
│   └── Batch? → Gemini Flash
│
├── Q&A / RAG
│   ├── Simple questions → Mini
│   ├── Complex questions → GPT-4o
│   └── Mixed complexity → CASCADING
│
├── Content Generation
│   ├── Short text → Mini
│   ├── Creative/long → GPT-4o
│   └── Factual → Gemini Pro
│
├── Code Assistance
│   ├── Simple completions → Mini
│   ├── Full functions → GPT-4o
│   └── Explain/debug → Gemini Pro
│
└── Agent with Tools
    ├── Tool selection → Haiku
    ├── Reasoning → Mini
    └── Complex decisions → GPT-4o
```

---

## Pattern: Model Cascading

**Concept:** Try cheap model first, escalate if confidence is low.

### When to Use Cascading
✅ **Good for:**
- Mixed query complexity (some easy, some hard)
- Cost-sensitive applications
- Can tolerate slight quality variance
- Have confidence scores or fallback logic

❌ **Bad for:**
- All queries need frontier model
- Latency is critical (cascading adds calls)
- Can't measure confidence
- Error cost is very high

### Cascading Strategies

**Strategy 1: Confidence-Based**
```python
result = call_haiku(query)
if result.confidence < 0.8:
    result = call_mini(query)
if result.confidence < 0.9:
    result = call_gpt4o(query)
return result
```

**Pros:** Smart routing, optimal cost
**Cons:** Adds latency on escalation

**Strategy 2: Complexity-Based**
```python
complexity = classify_query(query)  # Cheap classifier
if complexity == "simple":
    return call_haiku(query)
elif complexity == "medium":
    return call_mini(query)
else:
    return call_gpt4o(query)
```

**Pros:** One call per query, predictable latency
**Cons:** Classifier must be accurate

**Strategy 3: Keyword-Based**
```python
if has_keywords(query, ["analyze", "explain", "complex"]):
    return call_gpt4o(query)
else:
    return call_haiku(query)
```

**Pros:** Simple, no ML needed
**Cons:** Easy to game, less accurate

### Real Example: Customer Support

**Query type distribution:**
- 70% simple: "What's my order status?"
- 20% medium: "How do I return this?"
- 10% complex: "Your product broke, I want compensation"

**Cascading setup:**
1. Try Haiku for all queries ($0.001/query)
2. If confidence <0.8 OR keywords detected → Mini ($0.003/query)
3. If still low confidence → GPT-4o ($0.007/query)

**Result:**
- 70% handled by Haiku: $0.0007
- 20% by Mini: $0.0006
- 10% by GPT-4o: $0.0007
- **Average: $0.002/query (vs $0.007 all GPT-4o = 71% savings)**

---

## Capstone-Specific Recommendations

### RAG-Powered Study Helper
**Queries:** "Explain photosynthesis", "What is Newton's law?"

**Recommendation:**
- **Use:** GPT-4o-mini for most queries
- **Reason:** Educational content needs accuracy, but not frontier model
- **Cascading:** Haiku for factual recall → Mini for explanations

**Code example:**
```python
if is_factual_query(query):
    response = call_haiku(query, context=rag_chunks)
else:
    response = call_mini(query, context=rag_chunks)
```

### Document Q&A Chatbot
**Queries:** "Summarize page 5", "What does section 2.3 say?"

**Recommendation:**
- **Use:** Claude Haiku (best at document understanding)
- **Reason:** Fast, accurate for retrieval-based answers
- **Cost:** $0.001/query vs $0.007 for GPT-4o

### E-commerce Product Assistant
**Queries:** "Show me red shoes", "What's the return policy?"

**Recommendation:**
- **Use:** Model cascading (Haiku → Mini)
- **Reason:** Most queries are simple, occasional complex questions
- **Savings:** 80%+ vs using GPT-4o for everything

### Code Review Agent
**Queries:** "Find bugs in this code", "Suggest improvements"

**Recommendation:**
- **Use:** GPT-4o or Claude 3.7
- **Reason:** Code quality is critical, bugs are expensive
- **Don't cascade:** Code errors are high-cost mistakes

---

## Implementation Guide

### Step 1: Classify Your Queries

Analyze 100 sample queries:
- How many are simple? (1-2 sentence answers)
- How many need reasoning? (multi-step logic)
- How many need creativity? (generation tasks)

**Tool:** Manually label 100 queries or use cheap classifier

### Step 2: Choose Models

| Query Type | % of Queries | Model Choice | Why |
|-----------|--------------|--------------|-----|
| Simple | _____% | __________ | __________ |
| Medium | _____% | __________ | __________ |
| Complex | _____% | __________ | __________ |

### Step 3: Implement Routing

**Option A: Use code from `/code-examples/model_cascading.py`**

**Option B: Simple if/else**
```python
def route_query(query, user_input):
    if len(user_input) < 50:  # Short query
        return call_haiku(query)
    elif has_complex_keywords(query):
        return call_gpt4o(query)
    else:
        return call_mini(query)
```

### Step 4: Measure & Iterate

Track for each query:
- Which model was used
- Cost
- User satisfaction
- Escalation rate (if cascading)

**Tune thresholds based on data.**

---

## Common Mistakes

### Mistake 1: Using Frontier Model for Everything
**Problem:** Paying $0.007/query when $0.001 would work
**Fix:** Profile your queries, most are simpler than you think

### Mistake 2: Cascading Everything
**Problem:** Adding latency unnecessarily
**Fix:** Only cascade if queries have mixed complexity

### Mistake 3: Ignoring Quality Drops
**Problem:** Saving money but users unhappy
**Fix:** Measure quality, not just cost (Week 11!)

### Mistake 4: Over-Optimizing Too Early
**Problem:** Spending 10 hours to save $5/month
**Fix:** Optimize high-cost parts first (Week 10 Slide 19)

---

## Testing Your Model Choice

### Quick Test: Run same 20 queries on different models

| Query | Haiku Result | Mini Result | GPT-4o Result |
|-------|-------------|------------|---------------|
| "What is AI?" | Good | Good | Good |
| "Explain quantum..." | Poor | Good | Excellent |
| ... | ... | ... | ... |

**Conclusion:** Use Mini for most, GPT-4o for complex topics

---

## Next Steps

1. **Profile your queries** (Week 10 Slide 20)
2. **Choose model(s)** using 4-question method
3. **Implement routing** (copy code examples)
4. **Measure impact** (baseline vs optimized)
5. **Iterate** based on data

**Remember:** Start simple (one model), optimize later (cascading). Don't over-engineer early.
