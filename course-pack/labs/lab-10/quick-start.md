# Lab 10 Quick Start Guide

**Missed Lab? Start Here.**

This condensed guide gives you the essentials for Week 11's Evaluation & Observability lab.

---

## TL;DR - What You Need to Do This Week

**Due:** Safety & Evaluation Audit - Thursday December 18th, 2025 23:59


### 4 Critical Tasks:

1. Create golden set (30+ test queries)
2. Calculate baseline metrics
3. Set up regression testing
4. Complete Safety & Evaluation Audit (3 points!)

**Plus:** Implement 2-3 UI improvements

---

## Step 1: Create Golden Set (3 hours)

### What is a Golden Set?

A test suite of 30-50 queries representing real usage of your capstone, with expected outputs.

**Purpose:** Catch quality degradation before users do.

### Quick Setup

1. **Create file:** `tests/golden_set.json`

2. **Use template:** Copy from `templates/golden-set-template.json`

3. **Add 30+ queries:**

```json
{
  "golden_set": [
    {
      "id": "test_001",
      "query": "What is the capital of France?",
      "expected": "Paris",
      "category": "factual",
      "difficulty": "easy"
    },
    {
      "id": "test_002",
      "query": "Summarize this document in 3 bullet points",
      "expected_keywords": ["main points", "summary", "key findings"],
      "min_quality_score": 0.75,
      "category": "summarization",
      "difficulty": "medium"
    }
  ]
}
```

4. **Distribution:**
   - 40% easy queries
   - 40% medium queries
   - 20% hard queries

5. **Cover your use cases:**
   - Main functionality
   - Edge cases
   - Adversarial inputs (try to break it)

**Time budget:** 3 hours  
**Resource:** See `guides/creating-golden-sets.md`

---

## Step 2: Calculate Baseline Metrics (2 hours)

### What Metrics to Track

**For all projects:**
- **Latency:** Time from query to response
- **Cost:** API costs per query
- **Error rate:** % of queries that fail

**For QA/Chat systems:**
- **Accuracy:** % of correct answers
- **Hallucination rate:** % of false information

**For generation systems:**
- **BLEU/ROUGE:** Text similarity scores
- **Coherence:** Does output make sense?

### Quick Implementation

1. **Use evaluation script:** Copy `templates/evaluation-script-template.py`

2. **Run your golden set:**

```python
python templates/evaluation-script-template.py \
  --golden-set tests/golden_set.json \
  --output tests/metrics_baseline.json
```

3. **Calculate aggregate metrics:**

```
Results:
- Accuracy: 84.2% (25/30 correct)
- Avg Latency: 2.3s
- Avg Cost: $0.18/query
- Error Rate: 3.2% (1 failure)
```

4. **Set thresholds:**
   - Accuracy: > 80%
   - Latency: < 3s
   - Cost: < $0.25/query
   - Error rate: < 5%

**Time budget:** 2 hours  
**Resource:** See `guides/evaluation-metrics-guide.md`

---

## Step 3: Set Up Regression Testing (1 hour)

### What is Regression Testing?

Automated check that quality hasn't degraded. Run before every deployment.

### Quick Setup

1. **Create test script:** `tests/test_regression.py`

2. **Use template:** Copy from `templates/evaluation-script-template.py`

3. **Add threshold checks:**

```python
def check_thresholds(metrics):
    if metrics['accuracy'] < 0.80:
        print("❌ Accuracy too low")
        sys.exit(1)
    if metrics['avg_latency'] > 3.0:
        print("❌ Latency too high")
        sys.exit(1)
    # ... other checks
    
    print("✅ All checks passed")
    sys.exit(0)
```

4. **Test it:**

```bash
python tests/test_regression.py

Running golden set...
✅ Accuracy: 84.2% (threshold: 80%)
✅ Latency: 2.3s (threshold: 3s)
✅ Cost: $0.18 (threshold: $0.25)

All checks passed!
```

5. **Add basic logging** to your application:

```python
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info(f"Query: {query}, Latency: {latency}ms, Cost: ${cost}")
```

**Time budget:** 1 hour  
**Resource:** See `guides/regression-testing-guide.md`

---

## Step 4: Complete Safety & Evaluation Audit (4 hours)

### What is This?

Your **Week 11 capstone milestone** worth **3 points** (12% of capstone grade).

**Location:** `docs/safety-evaluation-audit.md`  
**Length:** 6-8 pages

### Required Sections

#### 1. Red Team Results (1 hour)

Try to break your system:
- Prompt injection attacks
- Jailbreaking attempts
- Over-reliance scenarios

Document:
- What you tried (10+ attacks)
- What worked/failed
- Mitigations implemented

#### 2. Bias & Privacy Checks (1 hour)

Test for biased outputs:
- Gender bias (male vs. female names)
- Race/ethnicity bias
- Age bias

Privacy audit:
- No PII in logs
- Data retention policy
- User deletion capability

#### 3. Golden Set & Regression Tests (30 min)

Link to your golden set and document:
- Total queries and distribution
- Baseline metrics
- Quality thresholds
- How to run regression tests

#### 4. Error Taxonomy (30 min)

Categorize your failures:
- API errors (timeouts, rate limits)
- Quality errors (hallucinations, off-topic)
- User input errors (malformed queries)
- System errors (database, memory)

For each, explain how you handle it.

#### 5. Telemetry Plan (1 hour)

Document what you log:
- Every query and response
- Latency, cost, model used
- Success/failure, error types
- How often you review metrics
- Alert thresholds

**Time budget:** 4 hours  
**Template:** See `examples/evaluation-audit-example.md`  
**Detailed requirements:** See `homework-assignment.md`

---

## Step 5: UI/UX Improvements (4 hours)

### The 5 Essential Quick Wins

**Context:** We haven't taught UI/UX formally. Standard is "functional and clear" NOT "beautiful and creative."

Pick 2-3 to implement:

#### 1. Visual Consistency (90 min)
- Pick 3 colors, use everywhere
- Use consistent spacing (8px, 16px, 24px)
- One font throughout

#### 2. Clear Error Messages (60 min)
Change:
- "Error 429" → "Rate limit exceeded. You've made 100 requests. Wait 15 minutes."

Formula: What happened + Why + What to do

#### 3. Loading States (60 min)
Add:
- Spinner or progress bar
- Text: "Processing... typically 3-5 seconds"
- Progress steps for long operations

#### 4. Clear Actions (45 min)
- Button labels: "Analyze Document" not "Submit"
- Disabled states: "Upload document first"

#### 5. Empty States (45 min)
Never show blank screens:
- "No documents yet. Upload PDF to get started."

**Time budget:** 4 hours total (pick 2-3)  
**Resource:** See `guides/ui-ux-quick-wins.md`

---

## Submission Checklist

**Before deadline:**
- [ ] Golden set: 30+ queries (`tests/golden_set.json`)
- [ ] Baseline metrics calculated (`tests/metrics_baseline.json`)
- [ ] Regression test script works (`tests/test_regression.py`)
- [ ] Logging added to application
- [ ] Safety & Evaluation Audit complete (`docs/safety-evaluation-audit.md`)
- [ ] 2-3 UI improvements implemented
- [ ] Everything committed to GitHub

**Submission:**
1. Push all code to GitHub
2. Submit audit document: `docs/safety-evaluation-audit.md`
3. Include link to GitHub repo

**Deadline:** End of Week 11 (check course calendar)

---

## What You Missed in Lab

**Part 1: Golden Set Workshop (30 min)**
- Teams brainstormed test queries together
- Categorized by difficulty and use case
- Created initial set of 15-20 queries

**You need to:** Create 30+ queries on your own

**Part 2: Evaluation Metrics (40 min)**
- Teams ran golden sets through their systems
- Calculated baseline metrics
- Set quality thresholds

**You need to:** Run evaluation script and calculate metrics

**Part 3: Regression Testing (30 min)**
- Teams created automated test scripts
- Added logging to their applications

**You need to:** Create test script and add logging

**Part 4: UI Audit (20 min)**
- Teams partnered to audit each other's UIs
- Gave feedback on improvements

**You need to:** Self-audit using checklist or ask teammate to review

---

## Common Questions

**Q: How do I know if my golden set is good enough?**  
A: 30+ queries, covers main use cases, mix of easy/medium/hard, realistic.

**Q: What if my metrics are terrible?**  
A: That's okay! Document honestly. This is about measurement, not perfection.

**Q: Can I use AI tools for the audit?**  
A: Yes for drafting, but all data and analysis must be your own.

**Q: How technical should the audit be?**  
A: Technical enough to be credible, but readable by non-technical stakeholders.

**Q: Do I need professional UI design?**  
A: No! Standard is "functional and clear." Follow the 5 quick wins.

---

## Getting Help

**Resources in this lab:**
- `homework-assignment.md` - Detailed requirements
- `templates/` - Copy-paste templates
- `guides/` - Step-by-step instructions
- `examples/` - Reference examples

**Office Hours:**
- See course announcement for schedule
- Bring specific questions
- Show your work so far

**Discussion Forum:**
- Post questions publicly
- Search for similar questions
- Help others if you can

**Email:** zeshan.ahmad@kiu.edu.ge (for sensitive issues)


---

## Tips for Success

1. **Start with golden set** - Foundation for everything else
2. **Be thorough on audit** - It's worth 3 points (12% of capstone)
3. **Be honest** - Admitting weaknesses shows maturity
4. **Use templates** - Don't start from scratch
5. **Document as you go** - Easier than reconstructing later
6. **Focus on clarity over beauty** - For UI/UX
7. **Ask for help early** - Don't wait until last minute

---

## Looking Ahead

**Next week (Week 13 - Lab 11):**
- Production engineering: CI/CD, secrets management, rate limiting
- Your golden sets will become automated quality gates
- Final push toward production-ready capstone

**Week 15:**
- Final Demo Day
- Your Safety & Evaluation Audit will be referenced in presentation

---

**Don't panic! This is doable. Start with the golden set and work through methodically. You've got this! 🎯**

**Questions? Review the full homework-assignment.md or reach out during office hours.**
