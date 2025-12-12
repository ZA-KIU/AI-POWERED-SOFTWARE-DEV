# Regression Testing Guide

**Purpose:** Automate quality checks to catch degradation before deployment.

---

## What is Regression Testing?

**Regression testing** means running your golden set automatically to ensure that changes (new features, optimizations, bug fixes) don't break existing functionality.

### Why Automate Testing?

**Manual testing problems:**
- Tedious and time-consuming
- Inconsistent (humans make mistakes)
- Doesn't scale
- Easy to skip when busy

**Automated testing benefits:**
- Runs in seconds/minutes
- Consistent every time
- Catches bugs immediately
- Runs before every deployment

---

## Step 1: Create Test Script (20 min)

### Basic Structure

```python
#!/usr/bin/env python3
"""
Regression test script - runs golden set and checks thresholds
"""

import sys
import json
from pathlib import Path

# Import your evaluation script
from evaluation_script import run_evaluation, calculate_metrics

def check_thresholds(metrics, thresholds):
    """
    Check if metrics meet minimum thresholds
    Returns (passed: bool, failures: list)
    """
    failures = []
    
    # Check accuracy
    if metrics['accuracy'] < thresholds['min_accuracy']:
        failures.append(
            f"Accuracy {metrics['accuracy']:.1%} < {thresholds['min_accuracy']:.1%}"
        )
    
    # Check latency
    if metrics['avg_latency_ms'] > thresholds['max_latency_ms']:
        failures.append(
            f"Latency {metrics['avg_latency_ms']:.0f}ms > {thresholds['max_latency_ms']:.0f}ms"
        )
    
    # Check cost
    if metrics['avg_cost_per_query'] > thresholds['max_cost_per_query']:
        failures.append(
            f"Cost ${metrics['avg_cost_per_query']:.4f} > ${thresholds['max_cost_per_query']:.4f}"
        )
    
    # Check error rate
    if metrics['error_rate'] > thresholds['max_error_rate']:
        failures.append(
            f"Error rate {metrics['error_rate']:.1%} > {thresholds['max_error_rate']:.1%}"
        )
    
    return len(failures) == 0, failures

def main():
    # Load configuration
    GOLDEN_SET_PATH = "tests/golden_set.json"
    
    # Define thresholds
    thresholds = {
        'min_accuracy': 0.80,
        'max_latency_ms': 3000,
        'max_cost_per_query': 0.25,
        'max_error_rate': 0.05
    }
    
    print("Running regression tests...")
    print(f"Golden set: {GOLDEN_SET_PATH}")
    print(f"Thresholds: {json.dumps(thresholds, indent=2)}\n")
    
    # Run evaluation
    metrics, results = run_evaluation(GOLDEN_SET_PATH)
    
    # Print results
    print(f"\nResults:")
    print(f"  Accuracy: {metrics['accuracy']:.1%}")
    print(f"  Avg Latency: {metrics['avg_latency_ms']:.0f}ms")
    print(f"  Avg Cost: ${metrics['avg_cost_per_query']:.4f}")
    print(f"  Error Rate: {metrics['error_rate']:.1%}")
    
    # Check thresholds
    passed, failures = check_thresholds(metrics, thresholds)
    
    if passed:
        print("\n✅ All regression tests PASSED")
        sys.exit(0)
    else:
        print("\n❌ Regression tests FAILED:")
        for failure in failures:
            print(f"  - {failure}")
        sys.exit(1)

if __name__ == '__main__':
    main()
```

### Save as `tests/test_regression.py`

---

## Step 2: Run Locally (5 min)

### First Run

```bash
cd your-project/
python tests/test_regression.py
```

**Expected output:**
```
Running regression tests...
Golden set: tests/golden_set.json
Thresholds: {
  "min_accuracy": 0.8,
  "max_latency_ms": 3000,
  "max_cost_per_query": 0.25,
  "max_error_rate": 0.05
}

[1/30] Running test: test_001
Query: What is the capital of France?
  ✅ PASS | Quality: 100.0% | Latency: 1.23s | Cost: $0.0021

[2/30] Running test: test_002
...

Results:
  Accuracy: 84.2%
  Avg Latency: 2341ms
  Avg Cost: $0.1834
  Error Rate: 3.2%

✅ All regression tests PASSED
```

### Interpreting Results

**If tests pass:**
- System meets minimum quality standards
- Safe to deploy

**If tests fail:**
- Don't deploy!
- Investigate which queries failed
- Fix issues
- Re-run tests

---

## Step 3: Configure Thresholds (10 min)

### Threshold Strategy

**Conservative (Safe but might fail often):**
```python
thresholds = {
    'min_accuracy': 0.85,      # High bar
    'max_latency_ms': 2000,    # Strict timing
    'max_cost_per_query': 0.15, # Tight budget
    'max_error_rate': 0.02      # Very reliable
}
```

**Balanced (Recommended):**
```python
thresholds = {
    'min_accuracy': 0.80,      # Reasonable quality
    'max_latency_ms': 3000,    # Acceptable UX
    'max_cost_per_query': 0.25, # Sustainable cost
    'max_error_rate': 0.05      # Some tolerance
}
```

**Lenient (Initial development):**
```python
thresholds = {
    'min_accuracy': 0.70,      # Work in progress
    'max_latency_ms': 5000,    # Slow but functional
    'max_cost_per_query': 0.50, # Will optimize later
    'max_error_rate': 0.10      # Catching major issues only
}
```

### Adjusting Over Time

**Week 11:** Start lenient, establish baseline  
**Week 13:** Tighten thresholds as system improves  
**Week 15:** Production-ready thresholds

---

## Step 4: Make it Executable (5 min)

### Add to package.json (if using Node.js)

```json
{
  "scripts": {
    "test": "python tests/test_regression.py",
    "test:quick": "pytest tests/ -k 'not slow'"
  }
}
```

### Or create Makefile

```makefile
test:
	python tests/test_regression.py

test-quick:
	python tests/test_regression.py --limit 10

test-coverage:
	python tests/test_regression.py --verbose
```

### Make executable

```bash
chmod +x tests/test_regression.py
```

Now run with:
```bash
./tests/test_regression.py
```

---

## Step 5: Integrate with Git Workflow (10 min)

### Pre-commit Hook (Optional)

Run tests before allowing commit:

```bash
# .git/hooks/pre-commit
#!/bin/bash
echo "Running regression tests..."
python tests/test_regression.py

if [ $? -ne 0 ]; then
    echo "❌ Regression tests failed. Commit aborted."
    exit 1
fi

echo "✅ Tests passed. Proceeding with commit."
```

Make executable:
```bash
chmod +x .git/hooks/pre-commit
```

**Note:** This can slow down commits. Alternative: run tests before push.

---

## Advanced: Pytest Integration (Optional)

### Convert to pytest

```python
# tests/test_regression.py
import pytest
from evaluation_script import run_evaluation

@pytest.fixture
def golden_set_results():
    """Run golden set once for all tests"""
    metrics, results = run_evaluation("tests/golden_set.json")
    return metrics

def test_accuracy(golden_set_results):
    """Test accuracy meets minimum threshold"""
    assert golden_set_results['accuracy'] >= 0.80, \
        f"Accuracy {golden_set_results['accuracy']:.1%} below 80%"

def test_latency(golden_set_results):
    """Test average latency is acceptable"""
    assert golden_set_results['avg_latency_ms'] <= 3000, \
        f"Latency {golden_set_results['avg_latency_ms']:.0f}ms exceeds 3000ms"

def test_cost(golden_set_results):
    """Test cost per query is within budget"""
    assert golden_set_results['avg_cost_per_query'] <= 0.25, \
        f"Cost ${golden_set_results['avg_cost_per_query']:.4f} exceeds $0.25"

def test_error_rate(golden_set_results):
    """Test error rate is acceptable"""
    assert golden_set_results['error_rate'] <= 0.05, \
        f"Error rate {golden_set_results['error_rate']:.1%} exceeds 5%"

def test_easy_queries_high_accuracy(golden_set_results):
    """Easy queries should have very high accuracy"""
    assert golden_set_results['accuracy_easy'] >= 0.90, \
        f"Easy query accuracy {golden_set_results['accuracy_easy']:.1%} below 90%"
```

Run with:
```bash
pytest tests/test_regression.py -v
```

---

## Testing Workflow

### Development Cycle

```
1. Make changes to your code
   ↓
2. Run regression tests locally
   ↓
3. If tests pass:
   - Commit changes
   - Push to GitHub
   - Tests run in CI/CD (Week 12)
   
4. If tests fail:
   - Debug issues
   - Fix code
   - Go to step 2
```

### When to Run Tests

**Always run before:**
- Committing code
- Merging branches
- Deploying to production
- Demo/presentation

**Run regularly:**
- Daily during active development
- After each feature implementation
- When changing prompts/models
- When updating dependencies

---

## Common Issues

### Issue 1: Tests take too long

**Problem:** Running 50 queries takes 5 minutes

**Solutions:**
- Cache responses for deterministic queries
- Run subset of tests locally (full suite in CI)
- Parallelize test execution
- Use faster test data

```python
# Run quick test with 10 queries
python tests/test_regression.py --limit 10
```

### Issue 2: Flaky tests (pass/fail randomly)

**Problem:** Tests pass sometimes, fail others

**Causes:**
- Network issues
- API rate limiting
- Non-deterministic model outputs
- Timing-dependent tests

**Solutions:**
- Add retries for network errors
- Set temperature=0 for deterministic outputs
- Use mock responses for unit tests
- Increase timeout thresholds

### Issue 3: Tests always fail on one metric

**Problem:** Accuracy always 75%, threshold is 80%

**Solutions:**
- Improve your system (best option!)
- Lower threshold temporarily
- Exclude problematic queries
- Document known limitations

---

## Best Practices

### 1. Fast Feedback

Tests should run in <5 minutes ideally. If longer:
- Run subset locally
- Full suite in CI/CD
- Provide progress indicators

### 2. Clear Failure Messages

Bad:
```
AssertionError: Assertion failed
```

Good:
```
Accuracy 76.5% is below threshold of 80%
Failed queries: test_003, test_012, test_024
See tests/latest_results.json for details
```

### 3. Save Test Results

```python
# Save results for debugging
with open('tests/latest_results.json', 'w') as f:
    json.dump({
        'timestamp': datetime.now().isoformat(),
        'metrics': metrics,
        'results': results
    }, f, indent=2)
```

### 4. Version Thresholds

Track threshold changes over time:

```python
# tests/thresholds_history.json
{
  "v1.0": {"min_accuracy": 0.70, "date": "2025-11-15"},
  "v1.1": {"min_accuracy": 0.75, "date": "2025-11-29"},
  "v1.2": {"min_accuracy": 0.80, "date": "2025-12-11"}
}
```

### 5. Categorize Tests

```python
# Mark slow tests
@pytest.mark.slow
def test_all_golden_set():
    # Full regression suite
    pass

# Mark critical tests
@pytest.mark.critical
def test_basic_functionality():
    # Must pass for system to work at all
    pass

# Run only critical tests quickly
pytest -m critical
```

---

## Next Week: CI/CD Integration

In Week 12 (Lab 11), you'll integrate these regression tests into GitHub Actions:

```yaml
# .github/workflows/test.yml
name: Regression Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run regression tests
        run: python tests/test_regression.py
```

This automatically runs tests on every commit!

---

## Checklist

**Setup:**
- [ ] Created test_regression.py
- [ ] Set thresholds based on baseline
- [ ] Test script runs successfully
- [ ] Results are clear and actionable

**Integration:**
- [ ] Added to project documentation
- [ ] Team knows how to run tests
- [ ] Decided when to run (pre-commit, pre-deploy)

**Optional:**
- [ ] Converted to pytest
- [ ] Set up pre-commit hook
- [ ] Created quick test variant
- [ ] Saved test results history

---

## Summary

**Regression testing automates quality checks:**
1. Create test script (20 min)
2. Set thresholds (10 min)
3. Run before commits/deployments
4. Fix failures immediately
5. Track improvements over time

**Result:** Confidence that changes don't break your system.

**Next:** Week 12 - these tests will run automatically in CI/CD!

**Good luck with regression testing! ✅**
