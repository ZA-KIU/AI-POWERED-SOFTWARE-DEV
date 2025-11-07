# Sprint 1 Backlog

**Project:** [Your Project Name]  
**Team:** [Team Member Names]  
**Sprint Duration:** Week 6 → Week 7 (7 days)  
**Sprint Start:** [Date]  
**Sprint End:** [Date - next Thursday]

---

## 🎯 Sprint Goal

[ONE clear sentence describing what you want to achieve this sprint]

**Example:** "Implement function calling for quiz generation and integrate with RAG system"

---

## 📖 User Stories

User stories describe features from the user's perspective. Format: "As a [user], I want [feature] so that [benefit]"

### Story 1: [Story Title]
**As a** [type of user]  
**I want** [some feature]  
**So that** [some benefit]

**Acceptance Criteria:**
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

**Story Points:** [S/M/L or 1-8]

---

### Story 2: [Story Title]
**As a** [type of user]  
**I want** [some feature]  
**So that** [some benefit]

**Acceptance Criteria:**
- [ ] Criterion 1
- [ ] Criterion 2

**Story Points:** [S/M/L or 1-8]

---

## ✅ Tasks

Break each story into concrete, technical tasks. Each task should be:
- **Specific:** No vague descriptions
- **Small:** <8 hours of work
- **Testable:** Clear "done" criteria

### Function Implementation Tasks

- [ ] **Task 1:** Define function schemas (JSON)
  - **Assignee:** [Name]
  - **Estimate:** 2 hours
  - **Done when:** 2-3 function schemas in `functions/schemas.json`

- [ ] **Task 2:** Create Pydantic models
  - **Assignee:** [Name]
  - **Estimate:** 3 hours
  - **Done when:** Models in `functions/models.py`, all fields validated

- [ ] **Task 3:** Implement function logic
  - **Assignee:** [Name]
  - **Estimate:** 4 hours
  - **Done when:** Functions work with hardcoded data, return Pydantic models

- [ ] **Task 4:** Write unit tests
  - **Assignee:** [Name]
  - **Estimate:** 2 hours
  - **Done when:** 3+ tests passing, cover happy + error paths

---

### Integration Tasks

- [ ] **Task 5:** Connect functions to LLM
  - **Assignee:** [Name]
  - **Estimate:** 3 hours
  - **Done when:** LLM successfully calls functions, loop closes

- [ ] **Task 6:** Integrate with RAG from Lab 5
  - **Assignee:** [Name]
  - **Estimate:** 4 hours
  - **Done when:** RAG + functions work together end-to-end

- [ ] **Task 7:** Add error handling
  - **Assignee:** [Name]
  - **Estimate:** 2 hours
  - **Done when:** Invalid inputs handled gracefully, errors logged

---

### UI Tasks

- [ ] **Task 8:** Build Lovable UI
  - **Assignee:** [Name]
  - **Estimate:** 3 hours
  - **Done when:** UI deployed, functions callable from frontend

- [ ] **Task 9:** Connect frontend to backend
  - **Assignee:** [Name]
  - **Estimate:** 2 hours
  - **Done when:** API calls work, data flows both ways

---

### Testing & Documentation Tasks

- [ ] **Task 10:** Create evaluation golden set
  - **Assignee:** [Name]
  - **Estimate:** 2 hours
  - **Done when:** 10-15 test cases in `tests/golden-set.json`

- [ ] **Task 11:** Update PRD architecture
  - **Assignee:** [Name]
  - **Estimate:** 2 hours
  - **Done when:** Architecture diagrams + description reflect function calling

- [ ] **Task 12:** Write sprint retrospective
  - **Assignee:** [All]
  - **Estimate:** 1 hour
  - **Done when:** Retrospective in `docs/sprint-1-retrospective.md`

---

## 📊 Capacity Planning

**Team Size:** [2 or 3 people]  
**Available Hours per Person:** [Be realistic! Account for other classes, work, life]  
**Total Team Capacity:** [Team size × hours per person]

**Example for 2-person team:**
- Person A: 12 hours available
- Person B: 10 hours available
- **Total:** 22 hours

**Planned Work:** [Sum of all task estimates]  
**Buffer:** [10-20% for unexpected issues]  
**Adjusted Estimate:** [Planned work + buffer]

**Velocity Check:**
- If Adjusted Estimate > Total Capacity → Cut scope (move tasks to Sprint 2)
- If Adjusted Estimate < 80% of Capacity → Add stretch goals

---

## 🚨 Risks & Mitigation

### Risk 1: [Risk description]
**Likelihood:** High/Medium/Low  
**Impact:** High/Medium/Low  
**Mitigation:** [How will you prevent or minimize this risk?]

### Risk 2: [Risk description]
**Likelihood:** High/Medium/Low  
**Impact:** High/Medium/Low  
**Mitigation:** [How will you prevent or minimize this risk?]

---

## 📅 Daily Progress Tracking

Track progress each day (or every other day):

### Monday [Date]
- **Completed:** [List completed tasks]
- **In Progress:** [List current tasks]
- **Blockers:** [Any issues?]

### Tuesday [Date]
- **Completed:**
- **In Progress:**
- **Blockers:**

### Wednesday [Date]
- **Completed:**
- **In Progress:**
- **Blockers:**

### Thursday [Date] - Due Date!
- **Final Status:** [All done? What's remaining?]
- **Deployed URL:** [Lovable deployment link]
- **Demo Ready:** Yes/No

---

## ✅ Definition of Done

Before marking Sprint 1 as complete, verify:

- [ ] All planned tasks completed (or explicitly moved to Sprint 2)
- [ ] All code committed to GitHub
- [ ] All unit tests passing
- [ ] Lovable MVP deployed and accessible
- [ ] PRD updated with architecture changes
- [ ] Golden set created (10-15 test cases)
- [ ] Sprint retrospective written
- [ ] Homework submitted on LMS

---

## 🔄 Sprint Review Notes

*(Fill this out next Thursday during Lab 7)*

**What we accomplished:**
- [List completed features]

**What we didn't finish:**
- [List incomplete items + why]

**Demo highlights:**
- [What worked well in the demo]

**Feedback received:**
- [From instructor, peers, or users]

---

## 🎯 Next Sprint Preview

*(Fill this out next Thursday)*

Based on this sprint, what should Sprint 2 focus on?

**Sprint 2 Goal Ideas:**
1. [Idea 1]
2. [Idea 2]
3. [Idea 3]

**Tasks to carry over from Sprint 1:**
- [Task that didn't get done]

---

**Version:** 1.0  
**Last Updated:** [Date]
