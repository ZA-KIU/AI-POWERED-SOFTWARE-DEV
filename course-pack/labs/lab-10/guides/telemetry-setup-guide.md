# Telemetry & Logging Setup Guide

**Purpose:** Track quality metrics in production to catch issues early and improve your system.

---

## What is Telemetry?

**Telemetry** = Collecting metrics from your running system

**Why it matters:**
- Know when things break
- Understand usage patterns
- Measure improvements
- Debug production issues

---

## Step 1: Add Structured Logging (15 min)

### Basic Setup

```python
import logging
import json
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/application.log'),
        logging.StreamHandler()  # Also print to console
    ]
)

logger = logging.getLogger(__name__)
```

### Log Every Query

```python
def query_handler(query: str) -> str:
    """Main query handler with telemetry"""
    start_time = time.time()
    query_id = str(uuid.uuid4())
    
    # Log request
    logger.info(json.dumps({
        'event': 'query_start',
        'query_id': query_id,
        'query_preview': query[:100],  # First 100 chars
        'timestamp': datetime.now().isoformat()
    }))
    
    try:
        # Process query
        response = your_ai_system(query)
        latency = time.time() - start_time
        cost = estimate_cost(query, response)
        
        # Log success
        logger.info(json.dumps({
            'event': 'query_success',
            'query_id': query_id,
            'latency_ms': round(latency * 1000, 2),
            'cost_usd': round(cost, 4),
            'response_length': len(response),
            'model': 'gpt-4',
            'timestamp': datetime.now().isoformat()
        }))
        
        return response
        
    except Exception as e:
        # Log error
        logger.error(json.dumps({
            'event': 'query_error',
            'query_id': query_id,
            'error_type': type(e).__name__,
            'error_message': str(e),
            'timestamp': datetime.now().isoformat()
        }))
        raise
```

---

## Step 2: Track Key Metrics (10 min)

### What to Log

**Essential:**
- Query (anonymized if contains PII)
- Response length
- Latency (milliseconds)
- Cost (USD)
- Success/failure
- Timestamp

**Optional but useful:**
- Model/version used
- User ID (hashed)
- Session ID
- Feature flags active
- A/B test variant

### Metrics to Calculate

From logs, calculate:
- Average latency
- P50, P95, P99 latency
- Total cost
- Error rate
- Queries per hour/day

---

## Step 3: Create Metrics Dashboard (20 min)

### Simple Python Dashboard

```python
# metrics_dashboard.py
import json
from pathlib import Path
from datetime import datetime, timedelta
from collections import defaultdict

def load_logs(log_file='logs/application.log', hours=24):
    """Load recent logs"""
    cutoff = datetime.now() - timedelta(hours=hours)
    logs = []
    
    with open(log_file) as f:
        for line in f:
            try:
                log = json.loads(line.split(' - ')[-1])
                log_time = datetime.fromisoformat(log['timestamp'])
                if log_time >= cutoff:
                    logs.append(log)
            except:
                continue
    
    return logs

def calculate_metrics(logs):
    """Calculate aggregate metrics"""
    successes = [l for l in logs if l['event'] == 'query_success']
    errors = [l for l in logs if l['event'] == 'query_error']
    
    if not successes:
        return None
    
    latencies = [l['latency_ms'] for l in successes]
    costs = [l['cost_usd'] for l in successes]
    
    return {
        'total_queries': len(successes) + len(errors),
        'successful_queries': len(successes),
        'error_rate': len(errors) / (len(successes) + len(errors)),
        'avg_latency_ms': sum(latencies) / len(latencies),
        'p50_latency_ms': sorted(latencies)[len(latencies) // 2],
        'p95_latency_ms': sorted(latencies)[int(len(latencies) * 0.95)],
        'total_cost_usd': sum(costs),
        'avg_cost_per_query': sum(costs) / len(costs)
    }

def print_dashboard(hours=24):
    """Print metrics dashboard"""
    logs = load_logs(hours=hours)
    metrics = calculate_metrics(logs)
    
    if not metrics:
        print("No data available")
        return
    
    print("=" * 60)
    print(f"METRICS DASHBOARD (Last {hours} hours)")
    print("=" * 60)
    print(f"\n📊 Volume")
    print(f"  Total queries: {metrics['total_queries']}")
    print(f"  Successful: {metrics['successful_queries']}")
    print(f"  Error rate: {metrics['error_rate']:.1%}")
    
    print(f"\n⚡ Performance")
    print(f"  Avg latency: {metrics['avg_latency_ms']:.0f}ms")
    print(f"  P50 latency: {metrics['p50_latency_ms']:.0f}ms")
    print(f"  P95 latency: {metrics['p95_latency_ms']:.0f}ms")
    
    print(f"\n💰 Cost")
    print(f"  Total: ${metrics['total_cost_usd']:.2f}")
    print(f"  Per query: ${metrics['avg_cost_per_query']:.4f}")
    
    print("\n" + "=" * 60)

if __name__ == '__main__':
    print_dashboard(hours=24)
```

Run with:
```bash
python metrics_dashboard.py
```

---

## Step 4: Set Up Alerts (15 min)

### Email Alerts (Simple)

```python
import smtplib
from email.mime.text import MIMEText

def send_alert(subject, body, to_email):
    """Send email alert"""
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'alerts@yourapp.com'
    msg['To'] = to_email
    
    # Configure your SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('your_email@gmail.com', 'your_password')
        server.send_message(msg)

def check_alerts():
    """Check if alerts should fire"""
    metrics = calculate_metrics(load_logs(hours=1))
    
    if metrics['error_rate'] > 0.10:
        send_alert(
            subject='🚨 High Error Rate Alert',
            body=f"Error rate is {metrics['error_rate']:.1%} (threshold: 10%)",
            to_email='team@yourapp.com'
        )
    
    if metrics['avg_latency_ms'] > 5000:
        send_alert(
            subject='⚠️ High Latency Alert',
            body=f"Avg latency is {metrics['avg_latency_ms']:.0f}ms (threshold: 5000ms)",
            to_email='team@yourapp.com'
        )
```

### Slack Alerts (Better)

```python
import requests

def send_slack_alert(message, webhook_url):
    """Send Slack message"""
    requests.post(webhook_url, json={'text': message})

def check_alerts_slack():
    """Check and send Slack alerts"""
    metrics = calculate_metrics(load_logs(hours=1))
    webhook_url = 'https://hooks.slack.com/services/YOUR/WEBHOOK/URL'
    
    if metrics['error_rate'] > 0.10:
        send_slack_alert(
            f"🚨 High error rate: {metrics['error_rate']:.1%}",
            webhook_url
        )
```

---

## Step 5: Review Schedule (10 min)

### Daily Review (5 min)

Check:
- Error rate
- Average latency
- Total cost
- Any alerts fired

### Weekly Review (20 min)

Analyze:
- Trends over time
- Which queries fail most
- Cost patterns
- Performance degradation

### Monthly Review (1 hour)

Deep dive:
- Full quality assessment
- Run golden set regression
- Update thresholds
- Plan improvements

---

## Privacy Considerations

### What NOT to Log

- Full query if contains PII (names, emails, etc.)
- API keys or secrets
- User passwords
- Credit card numbers
- Personal health information

### Best Practices

**Anonymize queries:**
```python
def anonymize_query(query: str) -> str:
    """Remove PII from query"""
    # Just log first 100 characters
    # Or hash the entire query
    import hashlib
    return hashlib.sha256(query.encode()).hexdigest()[:16]
```

**Aggregate data:**
```python
# Don't log: "User John Smith queried..."
# Do log: "Anonymous user queried..."
```

**Retention policy:**
```python
# Delete logs older than 30 days
def cleanup_old_logs():
    cutoff = datetime.now() - timedelta(days=30)
    # Delete logs older than cutoff
```

---

## Common Issues

### Issue 1: Logs too large

**Problem:** Log files grow to gigabytes

**Solution:**
- Rotate logs daily
- Compress old logs
- Delete after 30 days

```python
# Use RotatingFileHandler
from logging.handlers import RotatingFileHandler

handler = RotatingFileHandler(
    'logs/app.log',
    maxBytes=10*1024*1024,  # 10MB
    backupCount=5  # Keep 5 old files
)
```

### Issue 2: Performance impact

**Problem:** Logging slows down system

**Solution:**
- Use async logging
- Sample queries (log 10%, not 100%)
- Batch writes

---

## Checklist

**Setup:**
- [ ] Added structured logging to main query handler
- [ ] Logging query, response, latency, cost, errors
- [ ] Logs saved to file
- [ ] Privacy considerations addressed

**Dashboard:**
- [ ] Created metrics dashboard script
- [ ] Can calculate key metrics
- [ ] Easy to run and understand

**Alerts:**
- [ ] Set up alert mechanism (email/Slack)
- [ ] Defined alert thresholds
- [ ] Tested alerts work

**Process:**
- [ ] Scheduled daily reviews
- [ ] Scheduled weekly reviews
- [ ] Team knows where to find logs

---

## Summary

**Telemetry tracks production quality:**
1. Add structured logging (15 min)
2. Track key metrics (10 min)
3. Create dashboard (20 min)
4. Set up alerts (15 min)
5. Review regularly (ongoing)

**Result:** Know immediately when quality degrades.

**Good luck with telemetry! 📊**
