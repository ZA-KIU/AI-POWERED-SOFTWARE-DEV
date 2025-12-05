# Caching Implementation Guide

**Goal:** Stop recomputing what you already know. Cache = Free speed + massive cost savings.

---

## Why Caching Matters

**Without caching:**
```
Query 1: "What's the weather?" → API call → $0.005 → 2.3s
Query 2: "What's the weather?" → API call → $0.005 → 2.1s
Query 3: "What's the weather?" → API call → $0.005 → 2.4s
```
**Cost:** $0.015, Time: 6.8s

**With caching:**
```
Query 1: "What's the weather?" → API call → $0.005 → 2.3s → SAVE TO CACHE
Query 2: "What's the weather?" → FROM CACHE → $0.000 → 0.001s
Query 3: "What's the weather?" → FROM CACHE → $0.000 → 0.001s
```
**Cost:** $0.005 (67% savings), Time: 2.3s (99% faster on hits)

---

## Three Types of Caching

### 1. Prompt Caching (Provider-Level)
**What:** Provider automatically caches long prefixes (>1024 tokens)
**Best for:** RAG context, long system prompts, few-shot examples
**Savings:** 90% off input tokens (automatic with Anthropic)

### 2. Result Caching (Application-Level)
**What:** You cache full API responses by query
**Best for:** Repeated exact questions (FAQ, common queries)
**Savings:** 100% on cache hits (no API call)

### 3. Semantic Caching (Embedding-Based)
**What:** Cache similar (not identical) queries using embeddings
**Best for:** Variations of same question ("weather in NYC" ≈ "NYC weather")
**Savings:** 100% on semantic hits (no API call)

---

## 1. Prompt Caching (Anthropic)

### How It Works
Anthropic automatically caches prompt prefixes >1024 tokens for 5 minutes.

**Example:**
```python
# First call: Full price for 8000 tokens
response = anthropic.messages.create(
    model="claude-sonnet-4.5",
    max_tokens=1024,
    system=[
        {
            "type": "text",
            "text": long_system_prompt,  # 3000 tokens
            "cache_control": {"type": "ephemeral"}
        },
        {
            "type": "text", 
            "text": rag_context,  # 5000 tokens
            "cache_control": {"type": "ephemeral"}
        }
    ],
    messages=[{"role": "user", "content": user_query}]
)

# Next calls (within 5 min): 90% off on cached 8000 tokens
```

**When to Use:**
- RAG applications (context is reused)
- Long system prompts (instructions, examples)
- Few-shot learning (examples stay same)
- High-volume applications (many queries/min)

**Savings Example:**
- Without caching: 8000 input tokens × $3.00/1M = $0.024
- With caching (cached): 8000 tokens × $0.30/1M = $0.0024
- **Savings: 90% on input costs**

**Code in Your Capstone:**
```python
# Mark long, reusable content for caching
system_message = {
    "type": "text",
    "text": f"You are a study helper. Here is context:\n\n{rag_docs}",
    "cache_control": {"type": "ephemeral"}  # Cache this!
}
```

---

## 2. Result Caching (Redis)

### How It Works
Save full API responses in Redis (or dict). Return from cache if seen before.

### Simple Implementation (In-Memory Dict)

**For prototyping:**
```python
cache = {}

def cached_llm_call(prompt):
    # Create cache key
    cache_key = hashlib.md5(prompt.encode()).hexdigest()
    
    # Check cache
    if cache_key in cache:
        print("Cache HIT! 🎯")
        return cache[cache_key]
    
    # Cache miss - call API
    print("Cache MISS - calling API...")
    result = call_llm(prompt)
    
    # Save to cache
    cache[cache_key] = result
    return result
```

**Pros:** Simple, no dependencies
**Cons:** Lost on restart, no TTL, memory limited

### Production Implementation (Redis)

**Install Redis:**
```bash
# Mac
brew install redis
brew services start redis

# Linux
sudo apt install redis
sudo systemctl start redis

# Cloud: Use Upstash free tier
```

**Code:**
```python
import redis
import json
import hashlib

redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)
TTL = 3600  # 1 hour

def cached_llm_call(prompt, options=None):
    # Create cache key
    cache_key = f"llm:{hashlib.md5(prompt.encode()).hexdigest()}"
    
    # Try cache
    cached = redis_client.get(cache_key)
    if cached:
        print(f"Cache HIT! ✅")
        return json.loads(cached)
    
    # Cache miss
    print(f"Cache MISS - calling API...")
    result = call_llm(prompt, options)
    
    # Cache with TTL
    redis_client.setex(
        cache_key,
        TTL,
        json.stringify(result)
    )
    
    return result
```

**Pros:** Persistent, TTL support, scalable
**Cons:** Requires Redis server

### When to Use Result Caching

✅ **Good for:**
- FAQ systems (same questions repeated)
- Product descriptions (static content)
- Common translations
- Standard summaries
- High-repeat queries (measure >30% hit rate)

❌ **Bad for:**
- Unique user-specific queries
- Time-sensitive data
- Personalized responses
- Creative generation (want variety)

### Measuring Cache Hit Rate

```python
cache_hits = 0
cache_misses = 0

def cached_call(prompt):
    global cache_hits, cache_misses
    
    if cache_key in cache:
        cache_hits += 1
        return cache[cache_key]
    else:
        cache_misses += 1
        result = call_llm(prompt)
        cache[cache_key] = result
        return result

# Calculate hit rate
hit_rate = cache_hits / (cache_hits + cache_misses) * 100
print(f"Cache hit rate: {hit_rate:.1f}%")
```

**Target hit rates:**
- FAQ bot: 60-80%
- General chatbot: 20-40%
- Unique queries: <10% (caching not worth it)

---

## 3. Semantic Caching

### How It Works
Match similar (not exact) queries using embeddings.

**Example:**
```
"What's the weather in NYC?" 
≈ "NYC weather?"
≈ "Tell me weather for New York"
→ All return same cached result
```

### Implementation

```python
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')  # Fast, small model
semantic_cache = {}  # {embedding: result}
SIMILARITY_THRESHOLD = 0.95  # Tune this!

def semantic_cached_call(query):
    # Get query embedding
    query_embedding = model.encode(query)
    
    # Search for similar cached queries
    for cached_emb, cached_result in semantic_cache.items():
        similarity = np.dot(query_embedding, cached_emb) / (
            np.linalg.norm(query_embedding) * np.linalg.norm(cached_emb)
        )
        
        if similarity > SIMILARITY_THRESHOLD:
            print(f"Semantic cache HIT! Similarity: {similarity:.3f} 🎯")
            return cached_result
    
    # No match - call API
    print("Semantic cache MISS")
    result = call_llm(query)
    
    # Cache with embedding
    semantic_cache[query_embedding.tobytes()] = result
    return result
```

### Tuning Similarity Threshold

**Too high (0.99):** Misses variations, low hit rate
**Too low (0.85):** False matches, wrong answers
**Sweet spot:** 0.93-0.97 (test with your data)

**Test:**
```python
queries = [
    "What's the weather?",
    "Weather?",
    "Tell me the weather",
    "What's the time?"  # Should NOT match
]

for q in queries:
    result = semantic_cached_call(q)
```

### When to Use Semantic Caching

✅ **Good for:**
- Customer support (paraphrased questions)
- FAQ with variations
- Search queries
- When users ask same thing differently

❌ **Bad for:**
- High precision needed (legal, medical)
- Personalized queries
- Small variations matter
- Low query volume (<100/day)

---

## Choosing Your Caching Strategy

### Decision Tree

```
START: Should I cache?

├── Do I have long RAG context (>1024 tokens)?
│   └── YES → Use prompt caching (Anthropic automatic)
│
├── Do users ask exact same questions?
│   └── YES → Use result caching (Redis)
│
├── Do users ask similar (paraphrased) questions?
│   └── YES → Use semantic caching
│
└── All queries unique?
    └── Caching won't help much
```

### Capstone-Specific Recommendations

**RAG Study Helper:**
- **Prompt caching:** YES (RAG context reused)
- **Result caching:** MAYBE (if FAQs common)
- **Semantic caching:** YES (students paraphrase)

**Document Q&A:**
- **Prompt caching:** YES (document chunks reused)
- **Result caching:** YES (same sections queried)
- **Semantic caching:** NO (precision matters)

**E-commerce Assistant:**
- **Prompt caching:** NO (short prompts)
- **Result caching:** YES (product FAQs)
- **Semantic caching:** YES ("return policy" = "how to return")

**Code Assistant:**
- **Prompt caching:** MAYBE (if using examples)
- **Result caching:** NO (code is unique)
- **Semantic caching:** NO (precision critical)

---

## Implementation Steps

### Step 1: Measure Query Patterns

Run 100 queries through your capstone. Analyze:
```python
from collections import Counter

queries = [...]  # Your 100 test queries
query_counts = Counter(queries)

# How many duplicates?
duplicates = sum(1 for count in query_counts.values() if count > 1)
print(f"Duplicate queries: {duplicates}%")

# Most common queries
print("Top 10 queries:")
for query, count in query_counts.most_common(10):
    print(f"  {count}x: {query}")
```

**If duplicates >20%:** Result caching will help
**If duplicates <10%:** Caching might not be worth it

### Step 2: Choose Strategy

| Pattern | Best Strategy |
|---------|--------------|
| Exact duplicates >30% | Result caching |
| Paraphrased queries | Semantic caching |
| Long RAG context | Prompt caching |
| Mix of above | Combine strategies |

### Step 3: Implement Caching

**Start simple:**
1. Copy `/code-examples/redis_cache.py`
2. Adapt to your capstone
3. Test with 20 queries

**Measure:**
```python
baseline_cost = measure_cost_without_cache()
cached_cost = measure_cost_with_cache()
savings = (baseline_cost - cached_cost) / baseline_cost * 100
print(f"Caching saved {savings:.1f}%")
```

### Step 4: Tune TTL

**TTL (Time To Live):** How long to keep cached results

- **Static content:** 24 hours (86400s)
- **Semi-static:** 1 hour (3600s)
- **Dynamic:** 5 minutes (300s)
- **Prompt caching:** 5 minutes (automatic)

**Test different TTLs:**
```python
TTLs = [300, 3600, 86400]
for ttl in TTLs:
    hit_rate = test_caching_with_ttl(ttl)
    print(f"TTL {ttl}s → {hit_rate}% hit rate")
```

---

## Common Issues

### Issue 1: Cache Never Hits
**Cause:** Cache keys include dynamic data (timestamps, UUIDs)
**Fix:** Hash only query content, not metadata
```python
# BAD: Includes timestamp
cache_key = f"{query}_{datetime.now()}"

# GOOD: Only query
cache_key = hashlib.md5(query.encode()).hexdigest()
```

### Issue 2: Cache Serves Stale Data
**Cause:** TTL too long
**Fix:** Lower TTL or invalidate on updates
```python
# Invalidate cache when data changes
def update_product(product_id, new_data):
    save_to_database(product_id, new_data)
    cache_key = f"product:{product_id}"
    redis_client.delete(cache_key)  # Clear cache
```

### Issue 3: Semantic Cache False Matches
**Cause:** Similarity threshold too low
**Fix:** Raise threshold from 0.90 → 0.95
```python
# Test with edge cases
test_queries = [
    ("weather NYC", "weather NYC today"),  # Should match
    ("weather NYC", "time in NYC"),  # Should NOT match
]
```

### Issue 4: Memory Usage Too High
**Cause:** Caching everything, no eviction
**Fix:** Set max cache size, use LRU eviction
```python
from functools import lru_cache

@lru_cache(maxsize=1000)  # Keep only 1000 most recent
def cached_call(query):
    return call_llm(query)
```

---

## Measuring Cache Effectiveness

### Metrics to Track

```python
cache_stats = {
    "hits": 0,
    "misses": 0,
    "total_queries": 0,
    "cost_saved": 0,
    "time_saved": 0
}

def log_cache_result(is_hit, cost_saved, time_saved):
    cache_stats["total_queries"] += 1
    if is_hit:
        cache_stats["hits"] += 1
        cache_stats["cost_saved"] += cost_saved
        cache_stats["time_saved"] += time_saved
    else:
        cache_stats["misses"] += 1

# Calculate metrics
hit_rate = cache_stats["hits"] / cache_stats["total_queries"] * 100
avg_savings = cache_stats["cost_saved"] / cache_stats["total_queries"]

print(f"""
Cache Performance:
- Hit rate: {hit_rate:.1f}%
- Avg savings/query: ${avg_savings:.4f}
- Total cost saved: ${cache_stats['cost_saved']:.2f}
- Total time saved: {cache_stats['time_saved']:.1f}s
""")
```

---

## Real Example: E-commerce FAQ Bot

**Setup:**
- 1000 queries/day
- 40% are FAQ ("return policy", "shipping time")
- $0.005 per query without caching

**Implementation:**
```python
# Result caching for FAQ
faq_cache = {}  # {question: answer}

def handle_query(user_query):
    # Try FAQ cache
    if user_query in faq_cache:
        return faq_cache[user_query]  # Free!
    
    # Call LLM
    answer = call_llm(user_query)  # $0.005
    
    # Cache if FAQ
    if is_faq(user_query):
        faq_cache[user_query] = answer
    
    return answer
```

**Results:**
- 400 queries/day hit cache (40% hit rate)
- Savings: 400 × $0.005 = $2/day = $60/month
- Time saved: 400 × 2s = 800s/day

---

## Next Steps

1. **Analyze your queries** (duplicates? variations?)
2. **Choose caching strategy** (prompt vs result vs semantic)
3. **Implement** (start with dict, upgrade to Redis)
4. **Measure hit rate** (target >30% for result caching)
5. **Tune TTL** (balance freshness vs cost)

**Remember:** Caching is the easiest optimization. Start here!
