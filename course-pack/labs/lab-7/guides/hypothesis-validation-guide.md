# Hypothesis Validation Guide

This guide teaches you how to test design assumptions with real data before committing to Week 8 complexity.

## Why Validate Hypotheses?

You made design decisions in Week 2:
- "RAG will improve accuracy"
- "Function calling will reduce errors"
- "GPT-4 is worth the extra cost"
- "Caching will significantly reduce costs"

But were you right? Week 7 is your chance to find out with data.

## The Scientific Method for AI

1. **State hypothesis** - What you believe and why
2. **Design test** - How to measure it
3. **Collect data** - Run experiments
4. **Analyze results** - What does data say?
5. **Draw conclusions** - Was hypothesis supported?

## Good Hypotheses

### Hypothesis Formula

"We hypothesize that [intervention] will [effect] by [magnitude] because [reasoning]."

### Examples

✅ **Good:**
"We hypothesize that implementing RAG will improve answer accuracy from 65% to >85% (measured by human evaluation) because relevant context reduces hallucinations."

✅ **Good:**
"We hypothesize that GPT-4 will provide >20% better responses than GPT-3.5 (measured by user satisfaction scores) despite 10x higher cost, making it worthwhile."

✅ **Good:**
"We hypothesize that caching responses will reduce costs by >50% for our use case because 70% of queries are repeated within 24 hours."

❌ **Bad:**
"RAG is better" - No measurement, no magnitude, no reasoning

❌ **Bad:**
"Users will prefer our system" - Not testable, too vague

## Test Design

### Control vs Treatment

**Control group:** Baseline (without your intervention)  
**Treatment group:** With your intervention

Example:
- Control: LLM without RAG
- Treatment: LLM with RAG
- Measure: Answer accuracy on same 50 test questions

### Sample Size

**Minimum:** 20 test cases  
**Better:** 50 test cases  
**Best:** 100+ test cases

Why? Small samples hide patterns. Larger samples reveal truth.

### Evaluation Methods

#### 1. Automated Metrics
- Exact match accuracy
- BLEU/ROUGE scores (for text generation)
- Semantic similarity
- Response time
- Cost per request

#### 2. Human Evaluation
- Correctness (right answer?)
- Helpfulness (useful to user?)
- Relevance (on topic?)
- Quality (well-written?)

Rating scale: 1-5 or "Poor/Fair/Good/Excellent"

#### 3. User Testing
- A/B testing (50% see control, 50% see treatment)
- User satisfaction surveys
- Task completion rates
- Time on task

## Example: Testing RAG Effectiveness

### 1. Hypothesis
"We hypothesize that RAG will improve answer accuracy from 65% to >85% because relevant document context reduces hallucinations."

### 2. Test Design
- **Control:** GPT-4 with no retrieval
- **Treatment:** GPT-4 with top-3 document retrieval
- **Test set:** 50 questions about our documentation
- **Evaluation:** Human judges rate correctness (0-5 scale)
- **Success criteria:** Treatment accuracy >85% AND >20% improvement over control

### 3. Data Collection
```python
results = []
for question in test_questions:
    # Control
    control_response = llm_call(question, context=None)
    control_score = human_evaluate(control_response)
    
    # Treatment
    docs = retrieve_documents(question, top_k=3)
    treatment_response = llm_call(question, context=docs)
    treatment_score = human_evaluate(treatment_response)
    
    results.append({
        "question": question,
        "control_score": control_score,
        "treatment_score": treatment_score
    })
```

### 4. Analysis
```python
import pandas as pd

df = pd.DataFrame(results)
control_accuracy = (df['control_score'] >= 4).mean() * 100
treatment_accuracy = (df['treatment_score'] >= 4).mean() * 100
improvement = treatment_accuracy - control_accuracy

print(f"Control accuracy: {control_accuracy}%")
print(f"Treatment accuracy: {treatment_accuracy}%")
print(f"Improvement: +{improvement}%")
```

Results:
- Control (no RAG): 68% accuracy (34/50 correct)
- Treatment (with RAG): 88% accuracy (44/50 correct)
- Improvement: +20%

### 5. Conclusion
**Hypothesis SUPPORTED.** RAG improved accuracy from 68% to 88% (+20%), meeting our >85% target. Cost increased by 2x (retrieval overhead) but quality gain justifies it.

**Implication for Week 8:** Continue with RAG. Optimize retrieval to reduce overhead.

## Common Hypotheses to Test

### 1. Model Selection
**Hypothesis:** "GPT-4 quality justifies 10x cost vs GPT-3.5"

**Test:**
- Same 30 prompts to both models
- Blind evaluation: which response is better?
- Calculate quality improvement per dollar spent

### 2. Caching Value
**Hypothesis:** "Caching will reduce costs by >40%"

**Test:**
- Analyze query logs for duplicates
- Calculate hit rate: repeated queries / total queries
- Project cost savings

### 3. Function Calling Reliability
**Hypothesis:** "Function calling succeeds >90% of the time"

**Test:**
- 50 queries that should trigger functions
- Measure: correct function called? Valid arguments? Successful execution?
- Calculate success rate

### 4. Response Time Acceptability
**Hypothesis:** "Users accept <5s response time"

**Test:**
- User testing with different latencies (2s, 5s, 10s)
- Measure satisfaction and completion rates
- Find threshold where users complain

## Documenting Results

### Template

```markdown
## Hypothesis Validation: [Topic]

### 1. Hypothesis Statement
"We hypothesized that [intervention] would [effect] by [magnitude]."

### 2. Test Methodology
- **Control:** [Description]
- **Treatment:** [Description]
- **Sample size:** [Number]
- **Evaluation method:** [How measured]
- **Success criteria:** [What counts as "supported"]

### 3. Results

| Metric | Control | Treatment | Delta |
|--------|---------|-----------|-------|
| Accuracy | 68% | 88% | +20% |
| Latency | 2.1s | 3.5s | +1.4s |
| Cost | $0.003 | $0.006 | +$0.003 |

### 4. Analysis
[Detailed findings]

Key observations:
- [Finding 1]
- [Finding 2]
- [Finding 3]

### 5. Conclusion
**Hypothesis:** [ ] Supported  [ ] Partially Supported  [ ] Not Supported

[Explanation with data]

### 6. Implications for Week 8
- [What you'll change or keep]
- [What you'll optimize]
- [What you learned]

### 7. Limitations
- [What this test didn't measure]
- [Potential biases]
- [Follow-up tests needed]
```

## Statistical Significance

### Do Differences Matter?

You found: Control 68%, Treatment 88% (+20%)

But is 20% meaningful or just luck?

**Simple test:** If you repeated the experiment, would you get similar results?

**Rules of thumb:**
- Difference >10% with n>30: Probably real
- Difference >20% with n>20: Very likely real
- Difference <5% with n<30: Could be noise

### When to Care About Significance

**Academic research:** Yes, calculate p-values  
**Production systems:** Focus on practical impact

If RAG improves accuracy 20% but costs 2x more, the business question is: "Is 20% worth 2x cost?" Not "Is p<0.05?"

## Common Mistakes

❌ Testing without baseline (no control group)  
✅ Always compare treatment vs control

❌ Sample size = 5  
✅ Minimum 20, preferably 50+

❌ "It seems better" (no measurements)  
✅ Quantitative results with numbers

❌ Testing only success cases  
✅ Include failure cases and edge cases

❌ Ignoring limitations  
✅ Acknowledge what you didn't test

## Checklist

- [ ] Clear hypothesis statement
- [ ] Defined control and treatment
- [ ] Sample size ≥20
- [ ] Quantitative measurements
- [ ] Results documented with data
- [ ] Honest analysis (even if hypothesis fails)
- [ ] Implications for Week 8 identified
- [ ] Limitations acknowledged

## What If Hypothesis Fails?

**That's valuable data!**

Failed hypothesis: "RAG would improve accuracy to >85%"  
Actual result: Improved from 68% to 72% (+4%)

**Conclusion:** RAG helps but not enough to justify cost. Try different approach:
- Better retrieval (semantic search vs keyword)
- More documents (top-3 vs top-10)
- Better prompt engineering
- Or: Accept 72% accuracy for this use case

Failing fast with data > Shipping broken assumptions.

## Example: Failed Hypothesis

### Hypothesis
"We hypothesized that using GPT-4 would improve response quality by >30% over GPT-3.5, justifying the 10x cost increase."

### Results
- GPT-3.5: 78% user satisfaction
- GPT-4: 84% user satisfaction
- Improvement: +6%

### Conclusion
**Hypothesis NOT SUPPORTED.** GPT-4 is better but only by 6%, not 30%. The 10x cost increase is not justified for our use case.

### Implication
Switch to GPT-3.5 as default. Use GPT-4 only for complex queries where quality matters most. Saved $0.03 per request (75% cost reduction).

**This is a win.** We discovered this in Week 7, not Week 12.

---

Good experiments change your mind.  
Bad experiments confirm your assumptions.  
No experiments leave you guessing.
