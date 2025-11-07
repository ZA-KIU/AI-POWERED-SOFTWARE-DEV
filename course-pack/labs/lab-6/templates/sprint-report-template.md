# Sprint 1 Report

**Team Name:** [Your Team Name]  
**Project Title:** [Your Project Title]  
**Sprint Duration:** Week 6  
**Date Submitted:** [Date]

---

## Sprint Goal

**Goal:** [Your 1-2 sentence sprint goal from lab]

**Example:** "Enable users to ask questions about our product documentation and receive accurate answers with source citations from our knowledge base."

**Status:** [ ] Fully Achieved | [ ] Partially Achieved | [ ] Not Achieved

---

## Features Implemented

###  1. [Feature Name]

**Description:** [What is this feature? 1-2 sentences]

**Implementation Details:**
- Technology used: [e.g., OpenAI text-embedding-3-small + FAISS]
- Key components: [e.g., Embedding service, Vector store, Retrieval endpoint]
- Integration points: [e.g., Connects to backend API at /api/search]

**Status:** ✅ Complete | 🟡 Partially Complete | ❌ Not Started

**Evidence:**
- Code: [Link to GitHub file/commit]
- Demo: [Timestamp in demo video, e.g., 0:45-1:20]
- Test result: [Screenshot or description]

**Challenges:**
- [What was hard about implementing this?]
- [How did you overcome it?]

---

### 2. [Feature Name]

[Repeat structure above for each feature - aim for 2-4 key features]

---

## Technical Decisions

### Architecture Choices

**Frontend:**
- Framework: [e.g., React with Vite]
- Why: [1-2 sentence justification]
- Alternative considered: [What else did you consider?]

**Backend:**
- Framework: [e.g., FastAPI]
- Why: [1-2 sentence justification]
- Alternative considered: [What else did you consider?]

**LLM Provider:**
- Model: [e.g., GPT-4o-mini]
- Why: [Balance of cost, speed, quality]
- Fallback: [What if this doesn't work?]

**Vector Database:**
- Technology: [e.g., FAISS local index]
- Why: [Justification]
- Migration path: [How would you move to production?]

### Design Patterns Used

**[Pattern 1: e.g., RAG with Citations]**
- **What:** [Brief description]
- **Why:** [Why this approach?]
- **Implementation:** [How did you implement it?]

**[Pattern 2: e.g., Function Calling with Pydantic Validation]**
- **What:** [Brief description]
- **Why:** [Why this approach?]
- **Implementation:** [How did you implement it?]

---

## Metrics & Performance

### Latency
- Average end-to-end response time: [X seconds]
- Embedding generation: [X ms]
- Vector search: [X ms]
- LLM inference: [X ms]
- UI render: [X ms]

**Target:** <5 seconds for 90% of queries  
**Actual:** [Your measurement]  
**Status:** [ ] Meeting target | [ ] Need optimization

### Cost
- Cost per query (estimated): [$X]
- Daily budget estimate (100 queries): [$X]
- Monthly budget estimate: [$X]

**Breakdown:**
- Embedding cost: [$X per query]
- LLM cost: [$X per query]
- Vector DB cost: [$X/month]
- Hosting cost: [$X/month]

### Quality
- Retrieval relevance (informal testing): [X/10 queries returned relevant documents]
- Response accuracy (informal testing): [X/10 responses were accurate]
- Citation accuracy: [X/10 citations were correct]

**Method:** [How did you measure? e.g., "Tested with 10 sample queries manually"]

---

## Challenges & Solutions

### Challenge 1: [Title]

**Problem:**  
[Detailed description of the problem you faced]

**Impact:**  
[How did this affect your progress?]

**Solution:**  
[What did you do to solve it?]

**Learning:**  
[What did you learn from this?]

**Example:**
- **Problem:** FAISS was returning irrelevant documents for 7/10 queries
- **Impact:** Delayed RAG integration by 1 day
- **Solution:** Changed chunk size from 1000 to 500 tokens with 50-token overlap
- **Learning:** Smaller chunks with overlap preserve more context for semantic search

---

### Challenge 2: [Title]

[Repeat structure for each major challenge - aim for 2-3]

---

## Known Issues & Limitations

### Issue 1: [Title]

**Description:** [What doesn't work or work well?]

**Severity:** [ ] Critical (blocks core functionality) | [ ] Major (limits usefulness) | [ ] Minor (cosmetic/edge case)

**Workaround:** [Is there a way to work around it?]

**Plan:** [How will you fix this? When?]

**Example:**
- **Description:** Error handling shows generic "Something went wrong" message
- **Severity:** Minor
- **Workaround:** Check console logs for actual error
- **Plan:** Implement proper error messages and user feedback in Sprint 2

---

### Issue 2: [Title]

[Repeat for 2-3 known issues]

---

## What We Learned

### Technical Learnings

**[Team Member 1 Name]**
- [Learning 1: e.g., "Learned how cosine similarity works for semantic search"]
- [Learning 2: e.g., "Discovered importance of chunking strategy for RAG"]
- [Learning 3]

**[Team Member 2 Name]**
- [Learning 1]
- [Learning 2]
- [Learning 3]

**[Team Member 3 Name]** (if applicable)
- [Learning 1]
- [Learning 2]
- [Learning 3]

### Process Learnings

**What Worked Well:**
- [e.g., "Daily 15-minute standups kept us aligned"]
- [e.g., "Pair programming on complex integration helped us learn faster"]
- [e.g., "Testing each component before integrating saved debugging time"]

**What Didn't Work:**
- [e.g., "Waiting until Thursday to integrate - should have started earlier"]
- [e.g., "Not documenting as we coded - had to recreate docs at end"]
- [e.g., "Unclear task ownership led to duplicated work"]

**What We'll Change Next Sprint:**
- [e.g., "Integrate continuously, not just at the end"]
- [e.g., "Document in code comments as we write"]
- [e.g., "More specific task descriptions in issues"]

---

## Sprint Statistics

### Time Breakdown

| Activity | Hours Spent | % of Total |
|----------|-------------|------------|
| Planning & Architecture | [X] | [Y%] |
| RAG Implementation | [X] | [Y%] |
| Function Calling | [X] | [Y%] |
| UI Development | [X] | [Y%] |
| Integration & Testing | [X] | [Y%] |
| Debugging | [X] | [Y%] |
| Documentation | [X] | [Y%] |
| **Total** | **[X]** | **100%** |

### Code Statistics

- Total lines of code written: [X]
- Files created: [X]
- GitHub commits: [X]
- Pull requests: [X]
- Issues closed: [X]

### Team Contribution

| Team Member | Commits | Lines Changed | Primary Contributions |
|-------------|---------|---------------|----------------------|
| [Name 1] | [X] | [+X / -Y] | [e.g., RAG pipeline, backend API] |
| [Name 2] | [X] | [+X / -Y] | [e.g., Function calling, Pydantic models] |
| [Name 3] | [X] | [+X / -Y] | [e.g., UI, integration, testing] |

---

## Next Sprint (Week 7-8) Priorities

### Must Have
1. **[Priority 1]**
   - Why: [Why is this critical?]
   - Who: [Who's responsible?]
   - When: [Deadline]

2. **[Priority 2]**
   - Why: [Why is this critical?]
   - Who: [Who's responsible?]
   - When: [Deadline]

3. **[Priority 3]**
   - Why: [Why is this critical?]
   - Who: [Who's responsible?]
   - When: [Deadline]

### Should Have
- [Feature or improvement]
- [Feature or improvement]
- [Feature or improvement]

### Nice to Have
- [Feature or improvement]
- [Feature or improvement]

### Won't Have (Cut from Scope)
- [What are you explicitly not doing?]
- [Why are you cutting this?]

---

## User Testing Prep (Week 7)

### Test Scenarios
1. **Scenario 1:** [What will you ask test users to do?]
   - Expected outcome: [What should happen?]
   - Success criteria: [How do you know if it worked?]

2. **Scenario 2:** [Second test scenario]
   - Expected outcome: [What should happen?]
   - Success criteria: [How do you know if it worked?]

3. **Scenario 3:** [Third test scenario]
   - Expected outcome: [What should happen?]
   - Success criteria: [How do you know if it worked?]

### What We're Testing For
- [ ] Does core functionality work as expected?
- [ ] Is the UI intuitive?
- [ ] Are responses accurate and helpful?
- [ ] Are error messages clear?
- [ ] Is response time acceptable?
- [ ] Would users actually use this?

### Participant Recruitment
- Target: [X] participants
- Recruiting method: [How will you find them?]
- Incentive: [What are you offering?]
- Schedule: [When will testing happen?]

---

## Appendix

### Links
- **Live Demo:** [URL]
- **GitHub Repo:** [URL]
- **Demo Video:** [URL]
- **Lovable Project:** [URL]

### Screenshots

**[Screenshot 1 Title]**
![Screenshot description](path/to/screenshot1.png)
[1-2 sentence explanation]

**[Screenshot 2 Title]**
![Screenshot description](path/to/screenshot2.png)
[1-2 sentence explanation]

---

## Sign-Off

**Prepared by:** [Team member names]  
**Date:** [Date]  
**Review status:** [ ] Draft | [ ] Final

**Team Agreement:**
We certify that this report accurately represents our Sprint 1 work and all team members contributed to this sprint.

- [Name 1] - [Date]
- [Name 2] - [Date]
- [Name 3] - [Date]

---

## Instructor Use Only

**Grade: _____ / 15**

**Strengths:**
- [What did this team do well?]

**Areas for Improvement:**
- [What should they focus on?]

**Notes:**
- [Any other feedback]
