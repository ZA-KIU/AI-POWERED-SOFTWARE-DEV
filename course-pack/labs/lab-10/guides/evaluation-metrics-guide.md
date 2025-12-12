# Evaluation Metrics Guide

**Purpose:** Learn which metrics to track, how to calculate them, and what thresholds to set for your AI system.

---

## Overview

**Evaluation metrics** quantify your system's quality, performance, and cost. They turn subjective questions ("Is my system good?") into objective measurements ("My system has 84% accuracy, 2.3s latency, costs $0.18/query").

### Why Metrics Matter

**Without metrics:**
- "It seems to work most of the time" ← Vague
- Can't measure improvements
- Don't know when quality degrades
- Hard to justify changes

**With metrics:**
- "84% accuracy, improved from 79%" ← Specific
- Track improvements over time
- Catch degradation early
- Data-driven decisions

---

## Categories of Metrics

### 1. Quality Metrics
How correct/useful are outputs?

### 2. Performance Metrics
How fast is the system?

### 3. Cost Metrics
How expensive to run?

### 4. Reliability Metrics
How often does it fail?

### 5. User Experience Metrics
How do users perceive it?

---

## Quality Metrics

### Accuracy (For All Systems)

**Definition:** Percentage of queries that produce correct/acceptable outputs

**Calculation:**
```python
accuracy = correct_responses / total_queries
```

**Example:**
- 30 queries in golden set
- 25 produce correct outputs
- Accuracy = 25/30 = 83.3%

**When to use:**
- Any system with right/wrong answers
- Most common quality metric

**Threshold guidance:**
- Minimum: 75% (below this, system is not reliable)
- Good: 80-85%
- Excellent: 90%+
- Perfect: Impossible for complex AI systems

**How to measure:**
```python
def calculate_accuracy(results):
    """
    results: list of dicts with 'passed' boolean
    """
    passed = sum(1 for r in results if r.get('passed', False))
    total = len(results)
    return passed / total if total > 0 else 0
```

---

### BLEU Score (For Text Generation)

**Definition:** Measures n-gram overlap between generated and reference text (0-1 scale)

**When to use:**
- Machine translation
- Text summarization
- Content generation with reference text

**Calculation:**
```python
from nltk.translate.bleu_score import sentence_bleu

reference = [["The", "cat", "sat", "on", "the", "mat"]]
candidate = ["The", "cat", "is", "on", "the", "mat"]

score = sentence_bleu(reference, candidate)  # 0.0 to 1.0
```

**Interpretation:**
- 0.0-0.2: Poor overlap
- 0.2-0.4: Some overlap
- 0.4-0.6: Good overlap
- 0.6-0.8: Very good overlap
- 0.8-1.0: Excellent overlap (near identical)

**Threshold guidance:**
- Minimum: 0.3
- Good: 0.5+
- Excellent: 0.7+

**Limitations:**
- Focuses on word overlap, not meaning
- Can be gamed by copying
- Doesn't capture creativity

---

### ROUGE Score (For Summarization)

**Definition:** Recall-oriented metric measuring overlap (ROUGE-1, ROUGE-2, ROUGE-L)

**When to use:**
- Summarization tasks
- Content compression
- Key point extraction

**Types:**
- **ROUGE-1:** Unigram (word) overlap
- **ROUGE-2:** Bigram (2-word phrase) overlap
- **ROUGE-L:** Longest common subsequence

**Calculation:**
```python
from rouge import Rouge

reference = "The cat sat on the mat"
candidate = "The cat is on the mat"

rouge = Rouge()
scores = rouge.get_scores(candidate, reference)
# Returns: {'rouge-1': {'f': 0.75, 'p': 0.75, 'r': 0.75}, ...}
```

**Interpretation:**
- F-score combines precision and recall
- 0.5+ is typically good for summaries

**Threshold guidance:**
- Minimum: ROUGE-1 > 0.3
- Good: ROUGE-1 > 0.5
- Excellent: ROUGE-1 > 0.7

---

### Semantic Similarity (For Open-Ended Text)

**Definition:** How similar in meaning (not just words) are two texts?

**When to use:**
- Open-ended generation
- When BLEU/ROUGE too strict
- Paraphrasing tasks

**Calculation:**
```python
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

reference = "The cat sat on the mat"
candidate = "A feline rested on the rug"

emb1 = model.encode(reference, convert_to_tensor=True)
emb2 = model.encode(candidate, convert_to_tensor=True)

similarity = util.cos_sim(emb1, emb2)  # 0 to 1
```

**Interpretation:**
- 0.0-0.3: Not similar
- 0.3-0.5: Somewhat similar
- 0.5-0.7: Similar
- 0.7-0.9: Very similar
- 0.9-1.0: Nearly identical

**Threshold guidance:**
- Minimum: 0.5
- Good: 0.7+
- Excellent: 0.8+

---

### Precision, Recall, F1 (For Classification/Extraction)

**Definitions:**
- **Precision:** Of items identified, how many correct?
- **Recall:** Of correct items, how many found?
- **F1:** Harmonic mean of precision and recall

**When to use:**
- Named entity extraction
- Classification tasks
- Information retrieval

**Calculation:**
```python
def calculate_precision_recall_f1(true_positives, false_positives, false_negatives):
    precision = true_positives / (true_positives + false_positives) if (true_positives + false_positives) > 0 else 0
    recall = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) > 0 else 0
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
    
    return precision, recall, f1
```

**Example:**
- System extracts 100 entities
- 80 are correct (true positives)
- 20 are wrong (false positives)
- 10 were missed (false negatives)

```
Precision = 80/100 = 80%
Recall = 80/90 = 88.9%
F1 = 2 * (0.80 * 0.889) / (0.80 + 0.889) = 84.2%
```

**Threshold guidance:**
- Minimum: F1 > 0.7
- Good: F1 > 0.8
- Excellent: F1 > 0.9

---

### Hallucination Rate (For Factual Systems)

**Definition:** Percentage of responses containing false information

**When to use:**
- Q&A systems
- Information retrieval
- Factual generation

**Calculation:**
```python
def detect_hallucinations(response, source_docs):
    """
    Manually or automatically verify claims against sources
    """
    claims = extract_claims(response)
    hallucinations = 0
    
    for claim in claims:
        if not verify_in_sources(claim, source_docs):
            hallucinations += 1
    
    return hallucinations / len(claims) if claims else 0
```

**Methods:**
1. **Manual:** Human reviewers check facts (gold standard)
2. **Automated:** Cross-reference against source documents
3. **LLM-as-judge:** Use another LLM to verify claims

**Interpretation:**
- 0%: No hallucinations (ideal but rare)
- 1-5%: Acceptable for most use cases
- 5-10%: Problematic, needs mitigation
- 10%+: Serious issue

**Threshold guidance:**
- Maximum: 5% for critical applications
- Acceptable: 10% for non-critical

---

### Citation Quality (For RAG Systems)

**Definition:** Are sources cited correctly and relevantly?

**When to use:**
- RAG (Retrieval Augmented Generation)
- Document Q&A
- Research assistants

**Aspects to measure:**
1. **Citation completeness:** Are sources provided?
2. **Citation accuracy:** Do cited sources contain the info?
3. **Citation relevance:** Are the right sources cited?

**Calculation:**
```python
def evaluate_citation_quality(response, citations, source_docs):
    if not citations:
        return 0.0  # No citations provided
    
    scores = []
    for citation in citations:
        # Check if citation is accurate
        source = find_source(citation, source_docs)
        if source and verify_claim_in_source(response, source):
            scores.append(1.0)
        else:
            scores.append(0.0)
    
    return sum(scores) / len(scores)
```

**Threshold guidance:**
- Minimum: 70% of claims cited
- Good: 90% of claims cited correctly
- Excellent: 95%+ of claims cited correctly

---

## Performance Metrics

### Latency (Critical for UX)

**Definition:** Time from query to response

**Calculation:**
```python
import time

start = time.time()
response = your_system.query(query)
latency = time.time() - start  # seconds
```

**Measurements:**
- **Mean latency:** Average across all queries
- **P50 latency:** Median (50th percentile)
- **P95 latency:** 95th percentile (worst-case for most users)
- **P99 latency:** 99th percentile (worst-case outliers)

**Example:**
```
Mean: 2.3s
P50: 2.1s (half of queries faster than this)
P95: 4.5s (95% of queries faster than this)
P99: 8.2s (outliers, rare)
```

**Threshold guidance by use case:**

| Use Case | Max Acceptable | Good | Excellent |
|----------|----------------|------|-----------|
| Chat/conversation | 3s | 2s | 1s |
| Search | 1s | 500ms | 200ms |
| Background task | 30s | 10s | 5s |
| Code generation | 10s | 5s | 3s |

**User perception:**
- < 1s: Instant
- 1-2s: Fast
- 2-3s: Acceptable
- 3-5s: Noticeable delay
- 5-10s: Slow, needs progress indicator
- 10s+: Very slow, users may leave

---

### Throughput

**Definition:** Queries processed per second/minute/hour

**Calculation:**
```python
queries_processed = 1000
time_taken = 300  # seconds

throughput = queries_processed / time_taken  # 3.33 queries/second
```

**When to use:**
- High-traffic systems
- Batch processing
- Load testing

**Threshold guidance:**
- Depends entirely on expected traffic
- Calculate: peak_users × queries_per_user / time_window

---

## Cost Metrics

### Cost Per Query

**Definition:** API costs for a single query

**Calculation:**
```python
def estimate_cost(query, response, model="gpt-4"):
    # Rough token estimation: ~4 chars per token
    input_tokens = len(query) / 4
    output_tokens = len(response) / 4
    
    # Pricing (as of Dec 2024)
    if model == "gpt-4":
        cost = (input_tokens / 1000 * 0.03) + (output_tokens / 1000 * 0.06)
    elif model == "gpt-3.5-turbo":
        cost = (input_tokens / 1000 * 0.0015) + (output_tokens / 1000 * 0.002)
    elif model == "claude-sonnet":
        cost = (input_tokens / 1000 * 0.003) + (output_tokens / 1000 * 0.015)
    
    return cost
```

**Track:**
- Mean cost per query
- Min/max cost
- Cost by query type
- Daily/monthly totals

**Threshold guidance:**
- Budget-dependent
- For student projects: < $0.25/query
- For MVPs: < $0.10/query
- For production: Depends on business model

**Cost optimization strategies:**
1. Shorter prompts
2. Cheaper models for simple queries
3. Caching frequently asked queries
4. Prompt compression techniques

---

### Cost Efficiency

**Definition:** Cost relative to quality

**Calculation:**
```python
cost_efficiency = accuracy / cost_per_query

# Example:
# System A: 90% accuracy, $0.20/query → 450 points per dollar
# System B: 85% accuracy, $0.10/query → 850 points per dollar
# System B is more cost-efficient
```

**When to use:**
- Comparing different models
- Optimizing for budget
- Making cost/quality tradeoffs

---

## Reliability Metrics

### Error Rate

**Definition:** Percentage of queries that fail

**Calculation:**
```python
error_rate = failed_queries / total_queries
```

**Types of errors:**
- API timeouts
- Rate limiting (429 errors)
- Invalid responses
- System crashes

**Threshold guidance:**
- Maximum: 5%
- Good: < 2%
- Excellent: < 1%

---

### Uptime

**Definition:** Percentage of time system is available

**Calculation:**
```python
uptime = (total_time - downtime) / total_time
```

**Standard expectations:**
- 99% uptime: ~7 hours downtime/month
- 99.9% uptime: ~43 minutes downtime/month
- 99.99% uptime: ~4 minutes downtime/month

**For student projects:**
- Target: 95%+ (acceptable for demo)

---

## User Experience Metrics

### User Satisfaction (If Applicable)

**Definition:** How satisfied are users?

**Measurement methods:**
1. **Thumbs up/down:** Simple feedback
2. **1-5 star rating:** More nuanced
3. **Net Promoter Score (NPS):** Would recommend?

**Calculation:**
```python
satisfaction_rate = thumbs_up / (thumbs_up + thumbs_down)
```

**Threshold guidance:**
- Minimum: 70% positive
- Good: 80% positive
- Excellent: 90% positive

---

## Choosing the Right Metrics

### By Project Type

**Document Q&A:**
- ✅ Accuracy
- ✅ Citation quality
- ✅ Hallucination rate
- ✅ Latency
- ✅ Cost per query

**Code Generator:**
- ✅ Correctness (does it run?)
- ✅ Efficiency (time/space complexity)
- ✅ Readability
- ✅ Latency
- ✅ Cost per query

**Content Generator:**
- ✅ BLEU/ROUGE (if reference exists)
- ✅ Semantic similarity
- ✅ User satisfaction
- ✅ Latency
- ✅ Cost per query

**Chatbot:**
- ✅ Accuracy
- ✅ Conversation quality
- ✅ Response appropriateness
- ✅ Latency (must be fast!)
- ✅ Cost per conversation

---

## Setting Thresholds

### Process

1. **Establish baseline** - Run golden set, record current metrics
2. **Research benchmarks** - What do similar systems achieve?
3. **Consider user needs** - What's acceptable for your use case?
4. **Set realistic targets** - Achievable but challenging
5. **Define minimums** - Below this = system is broken

### Example Threshold Setting

**Project:** Document Q&A System

**Baseline (Week 11):**
- Accuracy: 79%
- Latency: 3.2s
- Cost: $0.22/query
- Hallucination rate: 8%

**Thresholds:**
- Accuracy: > 75% (minimum), target 85% (by Week 15)
- Latency: < 3.5s (minimum), target < 2.5s
- Cost: < $0.25 (budget limit)
- Hallucination rate: < 10% (minimum), target < 5%

**Why these thresholds:**
- Accuracy: Baseline is 79%, so 75% is achievable minimum
- Latency: 3.5s gives some buffer, but push toward 2.5s for better UX
- Cost: Budget constraint from sponsor
- Hallucination: 10% is too high but realistic for now, aim to improve

---

## Calculating Metrics from Golden Set

### Complete Example

```python
import json
import time
from typing import List, Dict, Any

def run_evaluation(golden_set_path: str) -> Dict[str, Any]:
    """
    Run golden set and calculate all metrics
    """
    # Load golden set
    with open(golden_set_path) as f:
        data = json.load(f)
    golden_set = data['golden_set']
    
    results = []
    for test in golden_set:
        try:
            # Time the query
            start = time.time()
            response = your_system.query(test['query'])
            latency = time.time() - start
            
            # Evaluate quality
            if 'expected' in test:
                quality = 1.0 if response.lower() == test['expected'].lower() else 0.0
            elif 'expected_keywords' in test:
                keywords_found = sum(1 for kw in test['expected_keywords'] 
                                   if kw.lower() in response.lower())
                quality = keywords_found / len(test['expected_keywords'])
            else:
                quality = 0.5  # Manual review needed
            
            # Estimate cost
            cost = estimate_cost(test['query'], response)
            
            results.append({
                'test_id': test['id'],
                'quality': quality,
                'passed': quality >= test.get('min_quality_score', 0.8),
                'latency_ms': latency * 1000,
                'cost_usd': cost,
                'difficulty': test['difficulty']
            })
            
        except Exception as e:
            results.append({
                'test_id': test['id'],
                'error': str(e),
                'passed': False
            })
    
    # Calculate aggregate metrics
    successful = [r for r in results if 'error' not in r]
    
    metrics = {
        # Quality
        'accuracy': sum(r['passed'] for r in results) / len(results),
        'avg_quality': sum(r['quality'] for r in successful) / len(successful),
        
        # Performance
        'avg_latency_ms': sum(r['latency_ms'] for r in successful) / len(successful),
        'p50_latency_ms': sorted([r['latency_ms'] for r in successful])[len(successful)//2],
        'p95_latency_ms': sorted([r['latency_ms'] for r in successful])[int(len(successful)*0.95)],
        
        # Cost
        'total_cost_usd': sum(r['cost_usd'] for r in successful),
        'avg_cost_per_query': sum(r['cost_usd'] for r in successful) / len(successful),
        
        # Reliability
        'error_rate': sum(1 for r in results if 'error' in r) / len(results),
        
        # By difficulty
        'accuracy_easy': sum(1 for r in results if r['difficulty']=='easy' and r['passed']) / 
                        sum(1 for r in results if r['difficulty']=='easy'),
        'accuracy_medium': sum(1 for r in results if r['difficulty']=='medium' and r['passed']) / 
                          sum(1 for r in results if r['difficulty']=='medium'),
        'accuracy_hard': sum(1 for r in results if r['difficulty']=='hard' and r['passed']) / 
                        sum(1 for r in results if r['difficulty']=='hard'),
    }
    
    return metrics, results
```

---

## Metrics Dashboard (Optional)

Create a simple dashboard to visualize metrics:

```python
import json
from datetime import datetime

def create_metrics_dashboard(metrics_history: List[Dict]):
    """
    Simple text-based metrics dashboard
    """
    print("=" * 60)
    print("METRICS DASHBOARD")
    print("=" * 60)
    
    latest = metrics_history[-1]
    
    print(f"\n📊 Overall Performance (as of {latest['timestamp']})")
    print(f"  Accuracy: {latest['accuracy']:.1%}")
    print(f"  Avg Latency: {latest['avg_latency_ms']:.0f}ms")
    print(f"  Avg Cost: ${latest['avg_cost_per_query']:.4f}")
    print(f"  Error Rate: {latest['error_rate']:.1%}")
    
    if len(metrics_history) > 1:
        prev = metrics_history[-2]
        print(f"\n📈 Changes from Last Run")
        print(f"  Accuracy: {(latest['accuracy']-prev['accuracy']):.1%}")
        print(f"  Latency: {(latest['avg_latency_ms']-prev['avg_latency_ms']):.0f}ms")
        print(f"  Cost: ${(latest['avg_cost_per_query']-prev['avg_cost_per_query']):.4f}")
    
    print(f"\n🎯 By Difficulty")
    print(f"  Easy: {latest['accuracy_easy']:.1%}")
    print(f"  Medium: {latest['accuracy_medium']:.1%}")
    print(f"  Hard: {latest['accuracy_hard']:.1%}")
    
    print("\n" + "=" * 60)
```

---

## Common Mistakes

### Mistake 1: Tracking too many metrics
**Problem:** Analysis paralysis, hard to act on  
**Fix:** Pick 3-5 key metrics, track the rest occasionally

### Mistake 2: Setting impossible thresholds
**Problem:** Always failing, demoralizing  
**Fix:** Set achievable minimums, aspirational targets

### Mistake 3: Ignoring variance
**Problem:** Focusing only on averages  
**Fix:** Look at P50, P95, min, max

### Mistake 4: Not segmenting by difficulty
**Problem:** Miss that easy queries work but hard ones fail  
**Fix:** Calculate metrics per difficulty level

### Mistake 5: Comparing incomparable systems
**Problem:** "System A is faster than B" but they do different things  
**Fix:** Only compare systems on same tasks

---

## Summary

**Essential Metrics for All Projects:**
1. **Accuracy** - How often is it correct?
2. **Latency** - How fast?
3. **Cost** - How expensive?
4. **Error rate** - How reliable?

**Choose 1-2 specialized metrics based on your project:**
- RAG systems: Citation quality, hallucination rate
- Code generation: Correctness, efficiency
- Content generation: BLEU/ROUGE, semantic similarity

**Process:**
1. Run golden set
2. Calculate metrics
3. Set thresholds
4. Track over time
5. Improve iteratively

**Remember:** Metrics are tools for improvement, not goals in themselves. Focus on metrics that matter for your users and use case.

**Good luck measuring your system! 📊**
