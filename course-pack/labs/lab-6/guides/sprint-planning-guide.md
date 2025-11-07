# Sprint Planning Guide for Agile Development

**Learn how to plan and execute effective development sprints**

---

## 🎯 What is a Sprint?

A sprint is a **short, focused development cycle** (typically 1-2 weeks) where you:
1. **Plan** what you'll build
2. **Build** it
3. **Review** what you built
4. **Reflect** on how it went

**Your Sprint 1 is 7 days:** This Thursday → Next Thursday

---

## 🔄 The Sprint Cycle

```
┌─────────────────────────────────────────────┐
│                                             │
│  Sprint Planning (Today in Lab)            │
│  ↓                                          │
│  Daily Work (This Week)                     │
│  ↓                                          │
│  Sprint Review (Demo - Next Thursday)       │
│  ↓                                          │
│  Sprint Retrospective (Reflection)          │
│  ↓                                          │
│  → Next Sprint Planning...                  │
│                                             │
└─────────────────────────────────────────────┘
```

---

## 📋 Part 1: Sprint Planning (Today)

### Step 1: Define Sprint Goal (5 minutes)

**Format:** ONE clear sentence

**Examples:**
- ✅ "Implement function calling for quiz generation"
- ✅ "Integrate RAG with function calling for Q&A system"
- ❌ "Work on features" (too vague)
- ❌ "Build entire app and deploy to production" (too ambitious)

**Test:** Can you explain this goal to someone in one breath?

---

### Step 2: Write User Stories (10 minutes)

**Format:** "As a [user], I want [feature] so that [benefit]"

**Example User Stories:**

**Story 1: Quiz Generation**
- As a student, I want to generate quizzes on any topic so that I can practice
- Acceptance Criteria:
  - User can input topic, number of questions, difficulty
  - System returns structured quiz with questions and answers
  - Quiz follows Pydantic model validation

**Story 2: Progress Tracking**
- As a student, I want my quiz results saved so that I can track improvement
- Acceptance Criteria:
  - Quiz results saved to database
  - User can view past attempts
  - System calculates improvement metrics

**Why user stories?**
- Keeps focus on USER VALUE (not just technical tasks)
- Helps prioritize (which story matters most to users?)
- Makes demos easier ("Here's the story we implemented...")

---

### Step 3: Break Into Tasks (15 minutes)

**Each task should be:**
- **Specific:** "Implement generate_quiz() function" not "Work on functions"
- **Small:** <8 hours of work
- **Testable:** Clear "done" criteria

**Example Task Breakdown:**

**User Story:** Quiz generation

**Tasks:**
1. Define quiz function schema (JSON) - 2 hours
2. Create Pydantic models for quiz output - 2 hours
3. Implement generate_quiz() with hardcoded data - 3 hours
4. Connect to OpenAI function calling - 3 hours
5. Write unit tests (3+ tests) - 2 hours
6. Integrate with RAG for topic-specific questions - 4 hours

**Total: 16 hours** (reasonable for 2-person team over 7 days)

---

### Step 4: Estimate & Assign (10 minutes)

**Estimation techniques:**

**T-shirt sizing:**
- S (Small): 1-2 hours
- M (Medium): 3-5 hours
- L (Large): 6-8 hours

**Never estimate larger than L!** If task is >8 hours, break it down further.

**Assignment:**
- Each person picks tasks based on their strengths
- Balance workload (each person ~10-15 hours for week)
- Consider dependencies (Task B can't start until Task A done)

**Example:**
- Person A (Backend): Implement functions, write tests, connect to LLM
- Person B (Frontend): Build Lovable UI, integrate API, documentation

---

### Step 5: Check Capacity (5 minutes)

**Be realistic!**

**Calculate available hours:**
- How many hours THIS WEEK can you dedicate to capstone?
- Account for: other classes, exams, work, sleep, life
- Be honest! Better to underpromise and overdeliver

**Example calculation (2-person team):**
- Person A: 12 hours available
- Person B: 10 hours available
- **Total capacity: 22 hours**

**Planned work:** 18 hours  
**Buffer (20%):** 3.6 hours  
**Total needed:** 21.6 hours

✅ This fits! Proceed with sprint.

**If total needed > capacity:** Cut tasks or move to Sprint 2

---

## 🏃 Part 2: During Sprint (This Week)

### Daily Check-ins (5 minutes each day)

Even if you don't meet in person, do async standup:

**Three questions:**
1. What did I complete yesterday?
2. What am I working on today?
3. Any blockers?

**Example (in Slack/Discord):**
```
Nov 3 Standup:
✅ Completed: Function schemas defined
🚧 Today: Implementing Pydantic models
⚠️  Blocker: None
```

---

### Work Smart, Not Just Hard

**Avoid these traps:**

❌ **Trap 1: No communication**
- Team members work in silos
- Discover conflicts/duplicates late

✅ **Solution:** Quick daily check-ins

❌ **Trap 2: Perfectionism**
- Spending 8 hours making one function perfect
- Not leaving time for testing/integration

✅ **Solution:** "Good enough for MVP" mindset

❌ **Trap 3: Scope creep**
- "Let's just add this one more feature..."
- Sprint goal keeps expanding

✅ **Solution:** Stick to plan. New ideas go to Sprint 2.

---

### When to Pivot

**Sometimes you need to adjust mid-sprint:**

**Scenario 1:** Task taking way longer than estimated
- **Action:** Simplify the task OR move to next sprint
- **Don't:** Keep grinding and miss everything else

**Scenario 2:** Blocker you can't unblock
- **Action:** Switch to different task, ask for help
- **Don't:** Stay stuck for days

**Scenario 3:** Realize feature isn't needed
- **Action:** Cut it! Focus on essentials
- **Don't:** Build it anyway out of obligation

---

## 🎬 Part 3: Sprint Review (Next Thursday)

**Demo what you built!**

**Structure (5 minutes per team):**
1. **Remind of goal:** "Our goal was to..."
2. **Demo working features:** Show live, not slides
3. **Highlight challenges:** "We struggled with X but solved it by..."
4. **Show metrics:** "Our quiz generation works 90% of the time"

**Tips:**
- Test your demo beforehand
- Have backup plan if live demo fails
- Focus on what WORKS, acknowledge what doesn't

---

## 🔍 Part 4: Sprint Retrospective (After Demo)

**Three questions:**

### 1. What went well?
Examples:
- "Our daily check-ins kept us in sync"
- "Pydantic models saved us from bugs"
- "Pair programming on the hard parts worked great"

### 2. What didn't go well?
Examples:
- "Underestimated integration complexity (3 hrs → 8 hrs)"
- "CORS issues took a day to debug"
- "Didn't write tests until end (should do as we go)"

### 3. What will we do differently?
Examples:
- "Write tests WHILE coding, not after"
- "Add 50% buffer to estimates for new technologies"
- "Ask instructor earlier when stuck (don't wait 2 days)"

**Important:** Be honest! This is for learning, not blame.

---

## 📊 Measuring Success

**Sprint 1 is successful if:**
- ✅ Sprint goal achieved (even if not all tasks done)
- ✅ Working code committed to GitHub
- ✅ MVP is demo-able
- ✅ Team learned something
- ✅ Foundation set for Sprint 2

**Sprint 1 is NOT necessarily successful if:**
- ❌ All tasks completed but goal not achieved
- ❌ Code works locally but not deployed
- ❌ Features built but untested
- ❌ Team burned out and dreading Sprint 2

**Quality > Quantity** for Sprint 1

---

## 🎯 Sprint 2 Preview (Week 7)

Based on Sprint 1, plan Sprint 2:

**Consider:**
1. What didn't finish in Sprint 1?
2. What user feedback did you get?
3. What's the next priority feature?
4. What will make the biggest impact for users?

**Sprint 2 will focus on:**
- User testing and feedback integration
- Streaming APIs for better UX
- Performance optimization
- Preparing for Week 11 milestone

---

## ✅ Sprint Planning Checklist

Before starting Sprint 1, verify:

- [ ] Sprint goal is ONE clear sentence
- [ ] 2-3 user stories written
- [ ] User stories broken into <8 hour tasks
- [ ] All tasks have estimates
- [ ] Tasks assigned to team members
- [ ] Total estimated hours <= team capacity
- [ ] Everyone understands what they're building
- [ ] Sprint backlog documented in `docs/sprint-1-backlog.md`

---

## 📚 Resources

**Agile Methodology:**
- Atlassian Agile Guide: https://www.atlassian.com/agile/scrum/sprints
- Mountain Goat Software: https://www.mountaingoatsoftware.com/agile/scrum/sprints

**Sprint Planning:**
- Scrum.org Sprint Planning: https://www.scrum.org/resources/what-is-sprint-planning

**User Stories:**
- User Story Template: https://www.atlassian.com/agile/project-management/user-stories

---

**Remember:** This is your FIRST sprint. It won't be perfect. The goal is to learn the process, ship something working, and improve for Sprint 2. You've got this! 🚀
