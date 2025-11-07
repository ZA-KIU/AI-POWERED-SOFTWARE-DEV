# Feature Prioritization Matrix

**Team:** [Team Name]  
**Date:** [Date]  
**Method:** Value vs. Effort Matrix

---

## Scoring Guide

### Value Score (1-5)
- **5 = Critical:** Mentioned by 8+ interviews, high pain intensity
- **4 = High:** Mentioned by 5-7 interviews, significant pain
- **3 = Medium:** Mentioned by 3-4 interviews, moderate pain
- **2 = Low:** Mentioned by 1-2 interviews, minor pain
- **1 = Minimal:** No strong evidence, nice-to-have

### Effort Score (1-5)
- **1 = Trivial:** < 1 day, simple implementation
- **2 = Easy:** 1-2 days, straightforward
- **3 = Medium:** 3-5 days, moderate complexity
- **4 = Hard:** 1-2 weeks, significant complexity
- **5 = Very Hard:** > 2 weeks, requires new skills/tech

---

## All Features with Scores

| ID | Feature | Value | Effort | Score | Quadrant | MVP? |
|----|---------|-------|--------|-------|----------|------|
| F1 | [Feature name] | 5 | 2 | 10 | Quick Win | ✅ Yes |
| F2 | [Feature name] | 5 | 3 | 8.3 | Quick Win | ✅ Yes |
| F3 | [Feature name] | 4 | 2 | 8 | Quick Win | ✅ Yes |
| F4 | [Feature name] | 4 | 3 | 6.7 | Strategic | ✅ Yes |
| F5 | [Feature name] | 4 | 4 | 5 | Strategic | ⚠️ Maybe |
| F6 | [Feature name] | 3 | 2 | 6 | Fill-In | ⚠️ Maybe |
| F7 | [Feature name] | 3 | 4 | 3.75 | Fill-In | ❌ No |
| F8 | [Feature name] | 2 | 1 | 8 | Fill-In | ❌ No |
| F9 | [Feature name] | 5 | 5 | 5 | Avoid | ❌ No |
| F10 | [Feature name] | 1 | 5 | 1 | Avoid | ❌ No |

**Score Calculation:** Value ÷ Effort (higher = better priority)

---

## Visual Matrix

```
         HIGH VALUE
              ↑
    ╔═════════╦═════════╗
    ║ STRATEGIC║QUICK WIN║ → Include in MVP
    ║  (Maybe)║  (YES!) ║
  E ║─────────╫─────────║
  F ║         ║         ║
  F ║  AVOID  ║ FILL-IN ║
  O ║  (NO)   ║ (Maybe) ║
  R ╚═════════╩═════════╝
  T         LOW VALUE
```

**Quick Wins:** F1, F2, F3 → Definitely in MVP  
**Strategic:** F4, F5 → Include if capacity allows  
**Fill-Ins:** F6, F7, F8 → Post-MVP  
**Avoid:** F9, F10 → Not worth effort

---

## Feature Details

### F1: [Feature Name] - MVP: ✅ YES

**Description:** [What this feature does]

**Value Justification (Score: 5):**
- Interview #3: "[Quote showing high value]"
- Interview #7: "[Quote showing pain point]"
- Interview #12: "[Quote showing impact]"
- Pattern: 9 out of 10 interviews mentioned this
- Quantified impact: [Users waste X hours/week without this]

**Effort Justification (Score: 2):**
- Implementation: Basic CRUD operation
- Technology: Using familiar frameworks
- Dependencies: None, can start immediately
- Estimated time: 1.5 days
- Risk: Low, straightforward implementation

**Prioritization Decision:**
✅ **INCLUDE IN MVP** - High value, low effort = quick win

---

### F2: [Feature Name] - MVP: ✅ YES

[Repeat structure for each feature]

---

## MVP Feature Selection Summary

**Selected Features (5-8 total):**
1. F1: [Name] - Quick Win
2. F2: [Name] - Quick Win
3. F3: [Name] - Quick Win
4. F4: [Name] - Strategic
5. F5: [Name] - Strategic (if time allows)

**Total Estimated Effort:** [X weeks]  
**Available Time:** 6 weeks  
**Buffer:** [Y weeks for testing, iteration, unexpected issues]

---

## Deferred Features

### Post-MVP (Sprint 4+)
- F6: [Name] - Good value but not essential for core experience
- F7: [Name] - Nice-to-have, not backed by strong evidence

### Future (After Course)
- F9: [Name] - High effort, requires more research
- F10: [Name] - Low value, low priority

---

## Feature Dependencies

**Must Build First:**
- [Feature] depends on [Feature]
- [Feature] requires [Infrastructure]

**Can Build in Parallel:**
- [Feature] and [Feature] are independent
- [Feature] and [Feature] can be developed simultaneously

---

## Validation Plan

For each MVP feature, how will we know if it's successful?

**F1: [Feature Name]**
- **Metric:** [What we'll measure]
- **Target:** [Specific number/percentage]
- **Method:** [How we'll track it]

**F2: [Feature Name]**
[Repeat for each MVP feature]

---

## Change Log

| Date | Feature | Change | Reason |
|------|---------|--------|--------|
| [Date] | F5 | Added to MVP | Strong user feedback |
| [Date] | F8 | Removed from MVP | Technical constraint |

---

## Notes & Assumptions

**Assumptions:**
- [Assumption 1 affecting prioritization]
- [Assumption 2 affecting estimates]

**Constraints:**
- [Time constraint]
- [Technical constraint]
- [Resource constraint]

**Open Questions:**
- [ ] [Question affecting F5 prioritization]
- [ ] [Question affecting implementation approach]

---

**File:** `/03-build/roadmap/feature-prioritization.md`  
**Related:** MVP Definition, Product Roadmap, Sprint Plans
