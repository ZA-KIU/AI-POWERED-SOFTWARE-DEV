# Lab 4: Design Review & AI-Powered Architecture Refinement
**Week 4 | Building AI-Powered Applications**

This lab serves a triple purpose: (1) refining and tightening your Week 2 capstone deliverables based on what you've learned in Weeks 3-4, (2) conducting a formal Design Review to validate your architecture, and (3) introducing AI-powered design frameworks that will accelerate your path to MVP prototyping and PRD development.

**Lab Duration:** 2 hours in-class + asynchronous team refinement work
**Due Date:** End of Week 4 (see course calendar for exact date/time)

---

## 🎯 Critical Context: Why This Lab Matters

**Where You Are Now:**

* ✅ **Week 2:** Submitted capstone proposal (possibly rushed, conceptual)
* ✅ **Week 3:** Built your first working prototype (learned what's actually hard)
* ✅ **Week 3 Lecture:** Covered image generation and content filtering
* 📍 **Week 4 (NOW):** Time to consolidate learnings and refine your foundation

**Why This Matters:**
By Week 4, most teams have discovered:

* Their initial tech stack choices need adjustment
* Their problem statement was too vague or too broad
* They underestimated certain risks
* They're unclear on how to evaluate success
* Their architecture diagram doesn't match reality

This lab is your opportunity to course-correct before it's too late.

**What's Coming After This:**

* **Week 5:** RAG implementation (requires solid architecture foundation)
* **Week 7:** First user testing round (needs clear success criteria)
* **Week 11:** Safety & Evaluation Audit (builds on evaluation plan from today)
* **Week 15:** Final demo (everything compounds from here)

---

## 🎓 Learning Objectives

By the end of this lab, you will:

**Refinement & Validation:**

* Audit and tighten your Week 2 capstone deliverables (proposal, team contract, architecture)
* Update your architecture to reflect Week 3-4 learnings
* Present and defend your refined design to peers and instructor
* Incorporate critical feedback before building scales

**AI-Powered Design Frameworks:**

* Use AI to generate comprehensive feature roadmaps (20 pillars → 200 functions)
* Apply AI-driven architecture analysis to identify gaps and risks
* Create data-driven evaluation plans using AI strategic frameworks
* Generate prioritized backlogs aligned with user needs and business goals

**Bridge to Next Milestones:**

* Establish clear success metrics for Week 7 user testing
* Create foundation for Week 11 safety audit requirements
* Build evaluation infrastructure that scales to Week 15 demo

---

## 📋 What's Due This Week

**Milestone 2: Design Review Submission (5 points)**

All deliverables must be in your team GitHub repository under `docs/`:

### 1. Refined Capstone Proposal (`docs/capstone-proposal-v2.md`) ⭐

**Why Refine?** Your Week 2 proposal was conceptual. Now you have implementation experience.

#### Required Updates:
* **Problem Statement:** More specific, validated with potential users
* **Technical Architecture:** Reflects actual tech decisions from Week 3-4
* **Success Criteria:** Concrete, measurable metrics (not "users will like it")
* **Risk Assessment:** Updated with risks you've discovered while building
* **Timeline:** Realistic milestones based on actual velocity

#### New Sections to Add:
* **Week 3-4 Learnings:** What changed since original proposal?
* **Technical Decisions Log:** Why you chose X over Y
* **Open Questions:** What you're still uncertain about

📄 **Template:** Refined Proposal Template

### 2. AI-Generated Feature Roadmap (`docs/feature-roadmap.md`) 🆕

**Objective:** Use AI frameworks to systematically explore your product's full potential.

#### Process:
1.  Run your current capstone idea through the **20-Pillar Design System** (see prompt below)
2.  Select 5-8 relevant design pillars for your project
3.  For each pillar, generate 10 specific implementation tasks
4.  Prioritize which features are MVP vs. future enhancements
5.  Document your full roadmap with implementation timeline

#### What to Include:
* **Strategic Design Pillars:** 5-8 selected from AI-generated 20
* **Feature Matrix:** All generated functions organized by pillar
* **MVP Features:** 10-15 functions you'll build by Week 15
* **Future Roadmap:** Additional features for post-course development
* **Feature Justification:** Why each MVP feature was prioritized

📄 **Template:** Feature Roadmap Template
🤖 **AI Prompt:** 20-Pillar Design System Prompt

### 3. Updated Architecture Diagram (`docs/architecture-v2.png` + explanation) 🏗️

#### Requirements:
Your architecture diagram must show:
* All system components (frontend, backend, database, APIs, vector stores, caches)
* Data flow with arrows showing request/response paths
* Latency budget annotations (e.g., "Vector search: <300ms")
* Technology stack for each component (specific versions)
* External dependencies (OpenAI, Redis, Postgres, etc.)
* Security boundaries (where auth happens, what's encrypted)
* Failure points (what happens when API is down?)

#### Changes Since Week 2:
* Highlight what changed from original proposal and why
* Use different colors or annotations to show evolution

📄 **Template:** Architecture Diagram Template
📄 **Guide:** Architecture Best Practices

**Accompanying Document (`docs/architecture-explanation.md`):**
* Explain each component's purpose
* Justify technology choices
* Document tradeoffs considered
* Identify potential bottlenecks

### 4. Comprehensive Evaluation Plan (`docs/evaluation-plan-v2.md`) 📊

**Critical:** This document will guide your Week 7 user testing, Week 11 safety audit, and Week 15 demo.

#### Required Sections:

**A. Success Metrics (Quantitative)**
* **Product metrics:** (e.g., task completion rate >70%, time on task <3 min)
* **Technical metrics:** (e.g., latency <3s, accuracy >85%, uptime >99%)
* **Business metrics:** (e.g., user satisfaction >4/5, would-recommend >60%)

**B. Evaluation Methods**
* **Golden Set:** 50+ test cases covering typical, edge, and adversarial inputs
* **User Testing Protocol:** Tasks, recruitment strategy, success criteria
* **A/B Testing Plan:** What variations you'll test (if applicable)
* **Regression Testing:** Automated tests to prevent quality degradation

**C. Evaluation Schedule**

| Week | Activity | Metric | Target |
| :--- | :--- | :--- | :--- |
| 4 | Baseline measurement | Initial accuracy | Document current state |
| 6 | Golden set creation | Test coverage | 50+ test cases |
| 7 | User testing round 1 | Task completion | >70% success rate |
| 11 | Safety audit | Red team pass rate | >90% blocked |
| 14 | User testing round 2 | Satisfaction | >4.0/5.0 |
| 15 | Final evaluation | All metrics | Hit all targets |

**D. Tools & Infrastructure**
* How you'll track metrics (logging, analytics, dashboards)
* Test data management strategy
* User feedback collection methods

📄 **Template:** Evaluation Plan Template
🤖 **AI Prompt:** Evaluation Strategy Generator

### 5. Token Usage & Cost Model (`docs/cost-model-v2.md`) 💰

**Update from Week 2:** Now that you've built something, you have real data.

#### Required Sections:

**A. Current Baseline (Based on Week 3-4 Usage)**
*Example:*
* Average input tokens per query: 1,200
    * System prompt: 400 tokens
    * User query: 200 tokens
    * Retrieved context (if RAG): 600 tokens
* Average output tokens: 500
* **Total per query:** 1,700 tokens
* **Cost per query:** $0.051 (using GPT-4o)
* **Current daily usage:** ~50 queries (testing)

**B. Production Projections**
* Expected queries per day/month
* Peak load scenarios
* Monthly cost estimate at scale
* Cost per user (if applicable)

**C. Optimization Strategies**
* **Model Selection**
    * Use GPT-4o-mini for 80% of queries → 50% cost reduction
    * Upgrade to GPT-4o only for complex queries
* **Prompt Engineering**
    * Reduce system prompt from 400 to 200 tokens → 12% savings
    * More concise retrieved context → 20% savings
* **Caching**
    * Cache common queries (50% hit rate) → 40% reduction in API calls
    * Cache embeddings for documents → one-time cost
* **Smart Batching**
    * Batch similar queries → reduce API overhead

**D. Budget Allocation**
* Development Phase (Weeks 3-9): $50
* Production Phase (Weeks 10-15): $100
* User Testing Buffer: $30
* Emergency/Overflow: $20
---
* **Total Semester Budget:** $200

📄 **Template:** Cost Model Template
📄 **Guide:** Token Optimization Strategies

### 6. Prioritized Backlog (`docs/backlog-v2.md`) 📝

**Update from Week 2:** Your initial backlog was speculative. Now prioritize based on:
* Technical dependencies (what blocks what)
* Risk mitigation (tackle unknowns early)
* User value (MVP features first)
* Milestone alignment (what's due when)

#### Required Structure:

**Priority 1: Critical Path (Must Have for MVP)**
* Issues that block future work
* Core features essential for Week 15 demo
* Technical infrastructure (auth, database, APIs)

**Priority 2: High Value (Should Have)**
* Features that significantly improve UX
* Evaluation infrastructure
* Error handling and edge cases

**Priority 3: Nice to Have (Could Have)**
* Polish and optimization
* Additional features if time permits
* Future roadmap items

**For Each Issue:**
```markdown
### Issue #15: Implement RAG with FAISS Vector Store

**Priority:** P1 (Critical Path - Week 5)

**User Story:**
As a user, I want relevant context retrieved from documents so that
answers are accurate and cited.

**Acceptance Criteria:**
- [ ] FAISS index created with 100+ document chunks
- [ ] Vector search returns top-5 results in <300ms
- [ ] Retrieved context successfully injected into prompt
- [ ] Citations displayed in response
- [ ] Handles documents without relevant content gracefully

**Technical Requirements:**
- Chunking strategy: 500 tokens, 50 token overlap
- Embedding model: text-embedding-3-small
- Storage: Local FAISS index (migrate to hosted if needed)

**Effort Estimate:** Large (8-12 hours)

**Assigned To:** [Team Member Name]

**Dependencies:**
- Blocks: #18 (User Testing Round 1)
- Depends on: #12 (Document ingestion pipeline)

**Definition of Done:**
- Code committed and reviewed
- Unit tests pass (>80% coverage)
- Integration test validates end-to-end flow
- Latency benchmark: <300ms for search
- Documentation updated

**Resources:**
- LangChain FAISS tutorial: [link]
- FAISS documentation: [link]
