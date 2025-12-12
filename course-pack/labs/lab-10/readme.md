# Lab 10: Evaluation, Observability & UX Polish

**Week:** 11  
**Topic:** Evaluation and Observability + UI/UX Quick Wins  
**Duration:** 2 hours in-lab + 9-13 hours homework  
**Due:** Safety & Evaluation Audit (3 points) - End of Week 11

---

## Overview

This week, you'll learn to **measure and maintain quality** in AI systems. You'll create golden sets to test your capstone, calculate evaluation metrics, set up regression testing, and add telemetry for production monitoring. You'll also apply UI/UX quick wins to polish your application before the final stretch.

**Why this matters:** Last week you optimized for cost and speed. This week, you ensure quality doesn't degrade. Without measurement, you're flying blind—you might ship a broken system and only discover it from user complaints.

---

## This Week's Lecture (Week 11)

**Topics covered in lecture:**
- Golden sets: Creating test data that represents real usage
- Evaluation metrics: Accuracy, BLEU, ROUGE, F1, latency, cost
- Regression testing: Catching quality degradation early
- Telemetry: Tracking quality in production
- A/B testing: Comparing model versions
- User feedback loops: Thumbs up/down, reports

**What you'll build in lab:**
- Golden set for your capstone (20-50 test queries)
- Evaluation script that calculates metrics
- Regression test suite
- Basic telemetry/logging
- UI/UX improvements (consistency, errors, loading states)

---

## Learning Objectives

By the end of this lab, you will:

1. **Create golden sets** - Build a test suite of 20-50 queries representing real usage
2. **Calculate evaluation metrics** - Measure accuracy, latency, cost for your system
3. **Set up regression testing** - Automate quality checks to catch degradation
4. **Implement telemetry** - Add logging to track quality in production
5. **Apply UI/UX quick wins** - Polish interface with consistency, clear errors, loading states

---

## In-Class Activities (2 Hours)

### Part 1: Golden Set Workshop (30 min)

**Goal:** Create 15-20 test queries that represent real usage of your capstone.

**What makes a good golden set:**
- **Representative:** Covers the main use cases and edge cases
- **Diverse:** Mix of easy, medium, hard queries
- **Realistic:** Actual queries users would ask
- **Stable:** Expected outputs don't change frequently
- **Measurable:** You can evaluate quality objectively

**Activity:**
1. As a team, brainstorm 20-30 potential test queries (10 min)
2. Categorize by difficulty and use case (5 min)
3. Select top 15-20 most important queries (5 min)
4. For each query, define expected output or quality criteria (10 min)

**Deliverable:** `tests/golden_set.json` with 15-20 queries

**Resource:** See `templates/golden-set-template.json` and `guides/creating-golden-sets.md`

---

### Part 2: Evaluation Metrics Implementation (40 min)

**Goal:** Calculate baseline metrics for your capstone.

**Metrics to implement:**

**For all projects:**
- **Latency:** Time from query to response
- **Cost:** API costs per query
- **Error rate:** % of queries that fail

**For QA/chat systems:**
- **Accuracy:** % of correct answers
- **Citation quality:** Do responses cite sources correctly?
- **Hallucination rate:** % of responses with false information

**For generation systems:**
- **BLEU/ROUGE:** Text similarity to expected output
- **Coherence:** Does output make sense?
- **Relevance:** Does output match the query?

**For classification/extraction:**
- **Precision/Recall/F1:** Standard classification metrics
- **Confusion matrix:** Where does your system fail?

**Activity:**
1. Run your system on all golden set queries (15 min)
2. Calculate metrics using evaluation script (15 min)
3. Set quality thresholds (e.g., accuracy > 80%) (5 min)
4. Document baseline results (5 min)

**Deliverable:** `tests/metrics_baseline.json` with calculated metrics

**Resource:** See `templates/evaluation-script-template.py` and `guides/evaluation-metrics-guide.md`

---

### Part 3: Regression Testing & Telemetry (30 min)

**Goal:** Automate quality checks and add production monitoring.

**Regression Testing (15 min):**
- Create test script that runs golden set automatically
- Fails if quality drops below threshold
- Can run locally or in CI/CD (we'll add CI/CD in Lab 11)

**Telemetry Setup (15 min):**
- Add structured logging to your application
- Log every query, response, latency, cost
- Track metrics over time
- Set up basic alerting (optional)

**Activity:**
1. Create `tests/test_regression.py` (10 min)
2. Add logging to your main application code (10 min)
3. Test that logs capture key metrics (5 min)
4. Run regression test and verify it works (5 min)

**Deliverable:** 
- `tests/test_regression.py` 
- Logging added to application code

**Resource:** See `guides/regression-testing-guide.md` and `guides/telemetry-setup-guide.md`

---

### Part 4: UI/UX Quick Wins (20 min)

**Goal:** Apply 2-3 quick UI/UX improvements to make your capstone look intentional.

**Context:** We haven't taught UI/UX design in this course. This section provides minimal viable guidance so your demo doesn't look broken. Standard is "functional and clear" NOT "beautiful and creative."

**The 5 Essential Quick Wins:**

1. **Visual Consistency (5 min audit)**
   - Pick 3 colors (primary, success, error) and use everywhere
   - Use consistent spacing (e.g., 8px, 16px, 24px)
   - Use one font throughout

2. **Clear Error Messages (5 min audit)**
   - Change "Error 429" → "Rate limit exceeded. You've made 100 requests. Wait 15 min."
   - Format: What went wrong + Why + What user should do

3. **Loading States (5 min audit)**
   - Add spinner or progress indicator when processing
   - Add text: "Processing... typically 3-5 seconds"
   - Show progressive feedback for long operations

4. **Clear Actions (3 min audit)**
   - Button labels are descriptive: "Analyze Document" not "Submit"
   - Disabled states are explained: "Upload document first"

5. **Empty States (2 min audit)**
   - Never show blank screens
   - Show: "No documents yet. Upload PDF to get started."

**Activity:**
1. Partner with another team (5 min)
2. Each team audits the other using checklist (10 min)
3. Give 2-3 specific improvement suggestions (5 min)

**Deliverable:** List of 2-3 UI improvements to implement this week

**Resource:** See `templates/ui-checklist-template.md` and `guides/ui-ux-quick-wins.md`

---

## Homework Assignment (Due: End of Week 11)

**Total Time Estimate:** 9-13 hours

### Task 1: Expand Golden Set (2-3 hours)

**Goal:** Expand from 15-20 queries (from lab) to 30-50 queries.

**Requirements:**
- [ ] At least 30 test queries total
- [ ] Mix of difficulties: 40% easy, 40% medium, 20% hard
- [ ] Cover all major use cases of your application
- [ ] Include edge cases and adversarial examples
- [ ] For each query, define expected output or quality criteria

**Deliverable:** `tests/golden_set.json` with 30+ queries

---

### Task 2: Complete Safety & Evaluation Audit (3-4 hours)

**Goal:** Submit the Safety & Evaluation Audit milestone (3 points).

This is your Week 11 capstone milestone. Create `docs/safety-evaluation-audit.md` with:

**Required Sections:**

1. **Red Team Results** (1 hour)
   - Attempt to break your system (prompt injection, jailbreaking)
   - Document what worked, what failed
   - Mitigations implemented

2. **Bias & Privacy Checks** (1 hour)
   - Test for biased outputs (gender, race, age, etc.)
   - Verify no PII is logged or exposed
   - Data retention policy

3. **Golden Set & Regression Tests** (30 min)
   - Link to your golden set
   - Baseline metrics
   - Quality thresholds
   - How you run regression tests

4. **Error Taxonomy** (30 min)
   - Categorize types of failures (API errors, bad outputs, timeouts)
   - Frequency of each error type
   - How you handle each type

5. **Telemetry Plan** (1 hour)
   - What metrics you track
   - How often you review them
   - Alert thresholds
   - Incident response process

**Deliverable:** `docs/safety-evaluation-audit.md` (6-8 pages)

**Worth:** 3 points (part of 25-point Capstone grade)

**Template:** See `examples/evaluation-audit-example.md`

---

### Task 3: UI/UX Improvements (4-6 hours)

**Goal:** Implement 2-3 UI/UX improvements from lab feedback.

**Time Budget by Quick Win:**
- Visual consistency: 90 min
- Error messages: 60 min
- Loading states: 60 min
- Clear actions: 45 min
- Empty states: 45 min

**Pick your top 2-3 priorities** based on lab partner feedback.

**Requirements:**
- [ ] Visual consistency: Same colors, spacing, fonts throughout
- [ ] Error messages: User-friendly, explain what happened and what to do
- [ ] Loading states: Show progress, don't leave users wondering
- [ ] Clear actions: Descriptive button labels, explained disabled states
- [ ] Empty states: Helpful guidance, never blank screens

**Deliverable:** Updated application with UI improvements

**Resource:** See `guides/ui-ux-quick-wins.md` for detailed implementation guidance

---

## Grading

**This week contributes to two grading components:**

### 1. Participation & Lab Work (ongoing, total 15 points, inclusive of peer review)

**Lab 10 Participation 2 points:**
- Completed in-lab deliverables:
  * Initial golden set (15-20 queries)
  * Baseline metrics calculated
  * Regression test created
  * Telemetry added
  * UI audit completed

---

### 2. Safety & Evaluation Audit (3 points, due end of Week 11)

See `grading-rubric.md` for detailed rubric.

**Summary:**
- Red team results (0.6 pts)
- Bias & privacy checks (0.6 pts)
- Golden set & regression tests (0.9 pts)
- Error taxonomy (0.3 pts)
- Telemetry plan (0.6 pts)

---

## What You'll Need

### Before Lab
- [ ] Working capstone application (from previous weeks)
- [ ] Laptop with dev environment set up
- [ ] API keys configured
- [ ] Access to your team's GitHub repository

### During Lab
- [ ] Notebook for brainstorming test queries
- [ ] Calculator or spreadsheet for metrics
- [ ] Test data for your application

### For Homework
- [ ] Time to run your system on 30+ test queries
- [ ] Tools: Python, pytest (for regression tests), logging library
- [ ] Template files from this lab

---

## Resources

### In This Lab
- **Templates:** `templates/` - Copy-paste templates for golden sets, evaluation scripts
- **Guides:** `guides/` - Step-by-step instructions for each task
- **Examples:** `examples/` - Reference examples from past projects

### External Resources
- [BLEU Score Explanation](https://en.wikipedia.org/wiki/BLEU)
- [ROUGE Metrics](https://en.wikipedia.org/wiki/ROUGE_(metric))
- [Precision, Recall, F1](https://en.wikipedia.org/wiki/Precision_and_recall)
- [Structured Logging Best Practices](https://www.loggly.com/ultimate-guide/python-logging-basics/)

### Related Course Materials
- Week 11 Lecture Slides
- Week 11 Lecture Script
- Week 10 Lab (Optimization) - for baseline performance numbers

---

## Common Questions

**Q: How many test queries is enough?**  
A: Minimum 30 for this assignment. More is better. Aim for 50+ if you have time.

**Q: Can we use the same queries from Week 4 Design Review?**  
A: Yes, if they're still relevant! But expand and refine them.

**Q: Do we need to achieve high accuracy/scores?**  
A: No! This is about measurement, not perfection. Document current performance honestly.

**Q: What if our system performs poorly on golden sets?**  
A: Good! Now you know. This is the point—find problems before users do. Document the issues and plan improvements.

**Q: How long should our Safety & Evaluation Audit be?**  
A: 6-8 pages typically. Quality > quantity. Be thorough but concise.

**Q: Do we need professional UI/UX design?**  
A: No. Standard is "functional and clear" not "beautiful." Focus on consistency and clarity.

**Q: Can we skip UI/UX since it wasn't taught?**  
A: No, but expectations are realistic. Follow the 5 quick wins and you'll be fine. It's 4-6 hours max.

**Q: Will we use these golden sets in Lab 11?**  
A: Yes! Lab 11 (Week 12) will connect your golden sets to CI/CD pipelines as quality gates.

---

## Getting Help

### During Lab
- Ask instructor or TAs
- Discuss with your team
- Collaborate with other teams

### Office Hours
- See course announcement for schedule
- Bring specific questions
- Show your work so far

### Online
- Course discussion forum (preferred)
- Email: zeshan.ahmad@kiu.edu.ge (for sensitive issues)
- GitHub Issues on your project repo

---

## Looking Ahead

**Next Week (Week 12 - Lab 11):**
- Production Engineering: CI/CD, secrets management, rate limiting
- Your golden sets will become automated quality gates
- Final push toward production-ready capstone

**Week 13 (Lab 12):**
- Multi-vendor & OSS models
- Portability and fallbacks

**Week 15:**
- Final Demo Day!
- Your Safety & Evaluation Audit will be referenced in your presentation

---

## Lab Checklist

**Before Lab:**
- [ ] Bring working laptop
- [ ] Have capstone code accessible
- [ ] Review Week 11 lecture slides

**During Lab:**
- [ ] Create initial golden set (15-20 queries)
- [ ] Calculate baseline metrics
- [ ] Write regression test script
- [ ] Add telemetry/logging
- [ ] Complete UI audit with partner team

**After Lab:**
- [ ] Expand golden set to 30+ queries
- [ ] Complete Safety & Evaluation Audit (3 points)
- [ ] Implement 2-3 UI improvements
- [ ] Commit everything to GitHub
- [ ] Submit audit document before deadline

---

## Tips for Success

1. **Start with representative queries** - Use real or realistic examples
2. **Document everything** - Your audit needs evidence, not just claims
3. **Be honest about weaknesses** - Finding problems now is better than later
4. **Keep UI improvements focused** - 2-3 quick wins is better than 10 half-done changes
5. **Test your metrics code** - Make sure calculations are correct
6. **Ask for help early** - Don't wait until the last minute
7. **Learn from other teams** - See how they approach evaluation

---

**Remember:** You can't improve what you don't measure. This week is about building the measurement infrastructure that will carry you through the final weeks.

**Let's build systems we can trust! 🎯**
