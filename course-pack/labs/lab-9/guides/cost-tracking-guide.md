# Cost Tracking Guide

**Goal:** Track every API call's cost, latency, and success. You can't optimize what you don't measure.

---

## Why Track Costs?

**Without tracking:**
```
"How much does my capstone cost?" 
→ "Uh... maybe $50/month?"
→ Actual: $500/month 😱
```

**With tracking:**
```
"How much does my capstone cost?"
→ "$127.34/month"
→ "RAG queries cost $89 (70%), summaries $31 (24%), other $7 (6%)"
→ "Let's optimize RAG first"
```

---

## What to Track

### Essential Metrics (Track These Always)

| Metric | Why | Example |
|--------|-----|---------|
| Cost per query | Identify expensive operations | $0.0067 |
| Latency | User experience | 2.3s |
| Success/failure | Reliability | 99.2% success |
| Model used | Optimization opportunities | GPT-4o |
| Input tokens | Cost breakdown | 1500 |
| Output tokens | Cost breakdown | 300 |

### Optional Metrics (Nice to Have)

| Metric | Why | Example |
|--------|-----|---------|
| Cache hit rate | Caching effectiveness | 65% |
| User ID | Per-user costs | user_123 |
| Query type | Route optimization | "faq" |
| Error type | Debugging | "timeout" |
| Time of day | Traffic patterns | "14:30" |

---

## Implementation

### Level 1: Basic Logging (Start Here)

**Simple print statements:**

```python
import time

def tracked_llm_call(prompt):
    start = time.time()
    
    try:
        result = call_llm(prompt)
        latency = time.time() - start
        
        # Calculate cost
        cost = calculate_cost(result.usage)
        
        # Log it
        print(f"✅ Success | Cost: ${cost:.4f} | Latency: {latency:.2f}s")
        
        return result
        
    except Exception as e:
        latency = time.time() - start
        print(f"❌ Error | {e} | Latency: {latency:.2f}s")
        raise

# Calculate cost from usage
def calculate_cost(usage):
    input_cost = (usage.input_tokens / 1_000_000) * INPUT_PRICE
    output_cost = (usage.output_tokens / 1_000_000) * OUTPUT_PRICE
    return input_cost + output_cost
```

**Pros:** Simple, immediate feedback
**Cons:** No history, hard to analyze

### Level 2: File Logging (Production Ready)

**Log to JSONL file:**

```python
import json
import time
from datetime import datetime

LOG_FILE = "llm_calls.jsonl"

def tracked_llm_call(prompt, user_id=None, query_type=None):
    start = time.time()
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "user_id": user_id,
        "query_type": query_type,
        "prompt_length": len(prompt)
    }
    
    try:
        result = call_llm(prompt)
        latency = time.time() - start
        cost = calculate_cost(result.usage)
        
        log_entry.update({
            "status": "success",
            "model": result.model,
            "input_tokens": result.usage.input_tokens,
            "output_tokens": result.usage.output_tokens,
            "cost": cost,
            "latency": latency,
            "cached": getattr(result.usage, 'cache_hit', False)
        })
        
        # Write to log file
        with open(LOG_FILE, "a") as f:
            f.write(json.dumps(log_entry) + "\n")
        
        return result
        
    except Exception as e:
        latency = time.time() - start
        log_entry.update({
            "status": "error",
            "error": str(e),
            "latency": latency
        })
        
        with open(LOG_FILE, "a") as f:
            f.write(json.dumps(log_entry) + "\n")
        
        raise
```

**Pros:** Persistent, analyzable, git-friendly
**Cons:** Manual analysis, no real-time dashboard

### Level 3: Structured Logging (Best Practice)

**Use Python logging module:**

```python
import logging
import json
from datetime import datetime

# Configure logger
logging.basicConfig(
    filename='llm_costs.log',
    level=logging.INFO,
    format='%(message)s'
)

def log_llm_call(prompt, result=None, error=None, latency=0):
    log_data = {
        "timestamp": datetime.now().isoformat(),
        "prompt_length": len(prompt),
        "latency": latency,
        "status": "success" if result else "error"
    }
    
    if result:
        log_data.update({
            "model": result.model,
            "input_tokens": result.usage.input_tokens,
            "output_tokens": result.usage.output_tokens,
            "cost": calculate_cost(result.usage)
        })
    elif error:
        log_data["error"] = str(error)
    
    logging.info(json.dumps(log_data))

# Usage
def tracked_call(prompt):
    start = time.time()
    try:
        result = call_llm(prompt)
        log_llm_call(prompt, result=result, latency=time.time()-start)
        return result
    except Exception as e:
        log_llm_call(prompt, error=e, latency=time.time()-start)
        raise
```

---

## Analyzing Your Logs

### Reading JSONL Logs

```python
import json
import pandas as pd

def load_logs(filename="llm_calls.jsonl"):
    logs = []
    with open(filename, "r") as f:
        for line in f:
            logs.append(json.loads(line))
    return pd.DataFrame(logs)

# Load and analyze
df = load_logs()

# Basic stats
print(f"Total queries: {len(df)}")
print(f"Total cost: ${df['cost'].sum():.2f}")
print(f"Avg cost/query: ${df['cost'].mean():.4f}")
print(f"Avg latency: {df['latency'].mean():.2f}s")
print(f"Success rate: {(df['status']=='success').mean()*100:.1f}%")
```

### Cost Breakdown

```python
# By model
print("\nCost by Model:")
print(df.groupby('model')['cost'].agg(['sum', 'mean', 'count']))

# By query type
print("\nCost by Query Type:")
print(df.groupby('query_type')['cost'].agg(['sum', 'mean', 'count']))

# By hour
df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
print("\nCost by Hour:")
print(df.groupby('hour')['cost'].sum())
```

### Finding Expensive Queries

```python
# Top 10 most expensive queries
expensive = df.nlargest(10, 'cost')[['timestamp', 'cost', 'prompt_length', 'query_type']]
print("\nMost Expensive Queries:")
print(expensive)

# Queries over $0.01
expensive_threshold = df[df['cost'] > 0.01]
print(f"\nQueries costing >$0.01: {len(expensive_threshold)}")
```

### Latency Analysis

```python
# Percentiles
print("\nLatency Percentiles:")
print(f"p50: {df['latency'].quantile(0.50):.2f}s")
print(f"p95: {df['latency'].quantile(0.95):.2f}s")
print(f"p99: {df['latency'].quantile(0.99):.2f}s")

# Slow queries
slow = df[df['latency'] > 5.0]
print(f"\nQueries >5s: {len(slow)} ({len(slow)/len(df)*100:.1f}%)")
```

---

## Simple Dashboard

### Option 1: Python Script

```python
import matplotlib.pyplot as plt
import pandas as pd

df = load_logs()

# Create 2x2 dashboard
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# 1. Daily cost trend
daily_cost = df.groupby(pd.to_datetime(df['timestamp']).dt.date)['cost'].sum()
axes[0, 0].plot(daily_cost.index, daily_cost.values)
axes[0, 0].set_title('Daily Cost')
axes[0, 0].set_ylabel('Cost ($)')

# 2. Cost by model
model_cost = df.groupby('model')['cost'].sum()
axes[0, 1].bar(model_cost.index, model_cost.values)
axes[0, 1].set_title('Cost by Model')
axes[0, 1].set_ylabel('Total Cost ($)')

# 3. Latency distribution
axes[1, 0].hist(df['latency'], bins=50)
axes[1, 0].set_title('Latency Distribution')
axes[1, 0].set_xlabel('Latency (s)')

# 4. Success rate
success_rate = (df['status'] == 'success').value_counts()
axes[1, 1].pie(success_rate.values, labels=success_rate.index, autopct='%1.1f%%')
axes[1, 1].set_title('Success Rate')

plt.tight_layout()
plt.savefig('dashboard.png')
print("Dashboard saved to dashboard.png")
```

### Option 2: Streamlit Dashboard

```python
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("LLM Cost Dashboard")

# Load data
df = load_logs()

# Metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Cost", f"${df['cost'].sum():.2f}")
col2.metric("Queries", len(df))
col3.metric("Avg Latency", f"{df['latency'].mean():.2f}s")
col4.metric("Success Rate", f"{(df['status']=='success').mean()*100:.1f}%")

# Daily trend
st.subheader("Daily Cost Trend")
daily = df.groupby(pd.to_datetime(df['timestamp']).dt.date)['cost'].sum().reset_index()
fig = px.line(daily, x='timestamp', y='cost')
st.plotly_chart(fig)

# Model breakdown
st.subheader("Cost by Model")
model_cost = df.groupby('model')['cost'].sum().reset_index()
fig = px.bar(model_cost, x='model', y='cost')
st.plotly_chart(fig)

# Run with: streamlit run dashboard.py
```

---

## Real-Time Monitoring

### Set Alerts

```python
import smtplib

DAILY_BUDGET = 10.00  # $10/day budget
ALERT_EMAIL = "your@email.com"

def check_budget():
    df = load_logs()
    today = datetime.now().date()
    today_cost = df[pd.to_datetime(df['timestamp']).dt.date == today]['cost'].sum()
    
    if today_cost > DAILY_BUDGET:
        send_alert(
            f"⚠️ Budget Alert: Today's cost is ${today_cost:.2f} (budget: ${DAILY_BUDGET})"
        )

def send_alert(message):
    # Send email or Slack notification
    print(f"ALERT: {message}")
```

### Cost Thresholds

```python
# Alert on expensive queries
def log_with_alert(prompt, result, latency):
    cost = calculate_cost(result.usage)
    
    # Log as usual
    log_llm_call(prompt, result, latency)
    
    # Alert if expensive
    if cost > 0.05:  # $0.05 threshold
        print(f"⚠️ EXPENSIVE QUERY: ${cost:.4f}")
        # Could send Slack notification here
```

---

## Decorator Pattern (Clean Code)

```python
from functools import wraps
import time

def track_llm_cost(query_type=None):
    """Decorator to automatically track LLM costs"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            try:
                result = func(*args, **kwargs)
                latency = time.time() - start
                
                # Log success
                log_llm_call(
                    prompt=kwargs.get('prompt', ''),
                    result=result,
                    latency=latency,
                    query_type=query_type
                )
                
                return result
            except Exception as e:
                latency = time.time() - start
                log_llm_call(
                    prompt=kwargs.get('prompt', ''),
                    error=e,
                    latency=latency,
                    query_type=query_type
                )
                raise
        return wrapper
    return decorator

# Usage
@track_llm_cost(query_type="rag_query")
def rag_query(prompt, context):
    return call_llm(f"{context}\n\nQuery: {prompt}")

@track_llm_cost(query_type="summary")
def summarize(text):
    return call_llm(f"Summarize: {text}")
```

---

## Capstone Integration Examples

### RAG Study Helper

```python
def study_helper_query(question, user_id):
    # Retrieve context
    context = get_rag_context(question)
    
    # Build prompt
    prompt = f"Context: {context}\n\nQuestion: {question}"
    
    # Track the call
    start = time.time()
    result = call_llm(prompt)
    latency = time.time() - start
    
    # Log with metadata
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "user_id": user_id,
        "query_type": "study_question",
        "cost": calculate_cost(result.usage),
        "latency": latency,
        "rag_chunks_used": len(context.split('\n\n'))
    }
    
    with open("study_helper_logs.jsonl", "a") as f:
        f.write(json.dumps(log_entry) + "\n")
    
    return result.content
```

### E-commerce Assistant

```python
def product_assistant(user_query, user_id):
    # Classify query type
    query_type = classify_query(user_query)  # "faq", "product_search", etc.
    
    # Route to appropriate model
    if query_type == "faq":
        model = "gpt-4o-mini"
    else:
        model = "gpt-4o"
    
    # Make call
    start = time.time()
    result = call_llm(user_query, model=model)
    latency = time.time() - start
    
    # Log with business metrics
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "user_id": user_id,
        "query_type": query_type,
        "model": model,
        "cost": calculate_cost(result.usage),
        "latency": latency
    }
    
    # Track by query type
    with open(f"logs/{query_type}.jsonl", "a") as f:
        f.write(json.dumps(log_entry) + "\n")
    
    return result.content
```

---

## Common Mistakes

### Mistake 1: Not Tracking Anything
**Problem:** Can't optimize without data
**Fix:** Start with basic print logging today

### Mistake 2: Logging Too Much
**Problem:** 50 fields per log entry, hard to analyze
**Fix:** Start with essentials: cost, latency, success/fail

### Mistake 3: Not Analyzing Logs
**Problem:** Logs collected but never looked at
**Fix:** Weekly review: What's expensive? What's slow?

### Mistake 4: No Alerts
**Problem:** Cost spirals unnoticed
**Fix:** Set daily budget alert

---

## Week 11 Integration

**This Week (Lab 9):**
- Track cost and latency
- Identify expensive operations
- Optimize for cost/speed

**Next Week (Lab 10):**
- Add quality metrics
- Track accuracy, user satisfaction
- Balance cost vs quality

**Together:**
```python
log_entry = {
    # Week 10 metrics
    "cost": cost,
    "latency": latency,
    "model": model,
    
    # Week 11 metrics (coming next week)
    "quality_score": quality_score,
    "user_rating": user_rating,
    "correct": correct
}
```

---

## Action Items

### Today (In Lab)
1. Add basic logging to your capstone
2. Run 20 queries, check logs
3. Calculate total cost and avg latency

### This Week (Homework)
1. Log 50+ queries
2. Analyze: What's most expensive?
3. Create simple dashboard (Python or Streamlit)

### Ongoing
1. Check logs weekly
2. Set budget alerts
3. Review before optimizations

---

## Resources

**Tools:**
- Logging: Python `logging` module
- Analysis: `pandas`
- Visualization: `matplotlib`, `plotly`, `streamlit`
- Alerts: email, Slack webhooks

**Code:**
- See `/code-examples/` for logging templates
- Week 10 Slide 18 for dashboard examples

---

**Remember:** "If you can't measure it, you can't improve it." Start logging today!
