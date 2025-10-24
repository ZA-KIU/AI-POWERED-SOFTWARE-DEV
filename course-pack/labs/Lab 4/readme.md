# Lab 4: Design Review & AI-Powered Architecture Refinement

**Week 4 | Building AI-Powered Applications**

This lab serves a **triple purpose**: (1) refining and tightening your Week 2 capstone deliverables based on what you've learned in Weeks 3-4, (2) conducting a formal Design Review to validate your architecture, and (3) introducing AI-powered design frameworks that will accelerate your path to MVP prototyping and PRD development.

**Lab Duration:** 2 hours in-class + asynchronous team refinement work  
**Due Date:** End of Week 4 (see course calendar for exact date/time)

---

## 🎯 Critical Context: Why This Lab Matters

**Where You Are Now:**
- ✅ Week 2: Submitted capstone proposal (possibly rushed, conceptual)
- ✅ Week 3: Built your first working prototype (learned what's actually hard)
- ✅ Week 3 Lecture: Covered image generation and content filtering
- 📍 **Week 4 (NOW)**: Time to consolidate learnings and refine your foundation

**Why This Matters:**

By Week 4, most teams have discovered:
- Their initial tech stack choices need adjustment
- Their problem statement was too vague or too broad
- They underestimated certain risks
- They're unclear on how to evaluate success
- Their architecture diagram doesn't match reality

**This lab is your opportunity to course-correct before it's too late.**

**What's Coming After This:**
- Week 5: RAG implementation (requires solid architecture foundation)
- Week 7: First user testing round (needs clear success criteria)
- Week 11: Safety & Evaluation Audit (builds on evaluation plan from today)
- Week 15: Final demo (everything compounds from here)

---

## 🎓 Learning Objectives

By the end of this lab, you will:

### **Refinement & Validation:**
1. Audit and tighten your Week 2 capstone deliverables (proposal, team contract, architecture)
2. Update your architecture to reflect Week 3-4 learnings
3. Present and defend your refined design to peers and instructor
4. Incorporate critical feedback before building scales

### **AI-Powered Design Frameworks:**
5. Use AI to generate comprehensive feature roadmaps (20 pillars → 200 functions)
6. Apply AI-driven architecture analysis to identify gaps and risks
7. Create data-driven evaluation plans using AI strategic frameworks
8. Generate prioritized backlogs aligned with user needs and business goals

### **Bridge to Next Milestones:**
9. Establish clear success metrics for Week 7 user testing
10. Create foundation for Week 11 safety audit requirements
11. Build evaluation infrastructure that scales to Week 15 demo

---

## 📋 What's Due This Week

All due end of Week 4 in team GitHub repo (`docs/` folder):

| # | File Name | Template/Guide | AI Prompt Used |
| :--- | :--- | :--- | :--- |
| 1 | `capstone-proposal-v2.md` | `templates/refined-proposal-template.md` | #5 Risk Assessment |
| 2 | `feature-roadmap.md` | Use AI prompts directly | #1 20-Pillar + #2 Prioritization |
| 3 | `architecture-v2.md` + diagram | README Section 4 | #3 Architecture Gap |
| 4 | `evaluation-plan-v2.md` | README Section 5 | #4 Evaluation + #7 User Testing |
| 5 | `cost-model-v2.md` | README Section 6 | #6 Token Optimization |
| 6 | `backlog-v2.md` | README Section 7 | #2 Prioritization |
| 7 | `team-health-week4.md` | README Section 8 | `N/A` |

**Grading:** 5 points total (Design Review Milestone)

### **Milestone 2: Design Review Submission (5 points)**

All deliverables must be in your team GitHub repository under `docs/`:

#### **1. Refined Capstone Proposal (`docs/capstone-proposal-v2.md`)** ⭐

**Why Refine?** Your Week 2 proposal was conceptual. Now you have implementation experience.

**Required Updates:**
- [ ] **Problem Statement:** More specific, validated with potential users
- [ ] **Technical Architecture:** Reflects actual tech decisions from Week 3-4
- [ ] **Success Criteria:** Concrete, measurable metrics (not "users will like it")
- [ ] **Risk Assessment:** Updated with risks you've discovered while building
- [ ] **Timeline:** Realistic milestones based on actual velocity

**New Sections to Add:**
- [ ] **Week 3-4 Learnings:** What changed since original proposal?
- [ ] **Technical Decisions Log:** Why you chose X over Y
- [ ] **Open Questions:** What you're still uncertain about

📄 **Template:** [Refined Proposal Template]

---

#### **2. AI-Generated Feature Roadmap (`docs/feature-roadmap.md`)** 🆕

**Objective:** Use AI frameworks to systematically explore your product's full potential.

**Process:**
1. Run your current capstone idea through the **20-Pillar Design System** (see prompt below)
2. Select 5-8 relevant design pillars for your project
3. For each pillar, generate 10 specific implementation tasks
4. Prioritize which features are MVP vs. future enhancements
5. Document your full roadmap with implementation timeline

**What to Include:**
- [ ] **Strategic Design Pillars:** 5-8 selected from AI-generated 20
- [ ] **Feature Matrix:** All generated functions organized by pillar
- [ ] **MVP Features:** 10-15 functions you'll build by Week 15
- [ ] **Future Roadmap:** Additional features for post-course development
- [ ] **Feature Justification:** Why each MVP feature was prioritized

📄 **Template:** [Feature Roadmap Template]
🤖 **AI Prompt:** [20-Pillar Design System Prompt]

---

#### **3. Updated Architecture Diagram (`docs/architecture-v2.png` + explanation)** 🏗️

**Requirements:**

Your architecture diagram must show:
- [ ] **All system components** (frontend, backend, database, APIs, vector stores, caches)
- [ ] **Data flow** with arrows showing request/response paths
- [ ] **Latency budget annotations** (e.g., "Vector search: <300ms")
- [ ] **Technology stack** for each component (specific versions)
- [ ] **External dependencies** (OpenAI, Redis, Postgres, etc.)
- [ ] **Security boundaries** (where auth happens, what's encrypted)
- [ ] **Failure points** (what happens when API is down?)

**Changes Since Week 2:**
- Highlight what changed from original proposal and why
- Use different colors or annotations to show evolution

📄 **Template:** [Architecture Diagram Template]
📄 **Guide:** [Architecture Best Practices]

**Accompanying Document (`docs/architecture-explanation.md`):**
- Explain each component's purpose
- Justify technology choices
- Document tradeoffs considered
- Identify potential bottlenecks

---

#### **4. Comprehensive Evaluation Plan (`docs/evaluation-plan-v2.md`)** 📊

**Critical:** This document will guide your Week 7 user testing, Week 11 safety audit, and Week 15 demo.

**Required Sections:**

**A. Success Metrics (Quantitative)**
- Product metrics (e.g., task completion rate >70%, time on task <3 min)
- Technical metrics (e.g., latency <3s, accuracy >85%, uptime >99%)
- Business metrics (e.g., user satisfaction >4/5, would-recommend >60%)

**B. Evaluation Methods**
- **Golden Set:** 50+ test cases covering typical, edge, and adversarial inputs
- **User Testing Protocol:** Tasks, recruitment strategy, success criteria
- **A/B Testing Plan:** What variations you'll test (if applicable)
- **Regression Testing:** Automated tests to prevent quality degradation

**C. Evaluation Schedule**
| Week | Activity | Metric | Target |
|------|----------|--------|--------|
| 4 | Baseline measurement | Initial accuracy | Document current state |
| 6 | Golden set creation | Test coverage | 50+ test cases |
| 7 | User testing round 1 | Task completion | >70% success rate |
| 11 | Safety audit | Red team pass rate | >90% blocked |
| 14 | User testing round 2 | Satisfaction | >4.0/5.0 |
| 15 | Final evaluation | All metrics | Hit all targets |

**D. Tools & Infrastructure**
- How you'll track metrics (logging, analytics, dashboards)
- Test data management strategy
- User feedback collection methods

📄 **Template:** [Evaluation Plan Template] 
🤖 **AI Prompt:** [Evaluation Strategy Generator]

---

#### **5. Token Usage & Cost Model (`docs/cost-model-v2.md`)** 💰

**Update from Week 2:** Now that you've built something, you have real data.

**Required Sections:**

**A. Current Baseline (Based on Week 3-4 Usage)**
```
Example:
- Average input tokens per query: 1,200
  - System prompt: 400 tokens
  - User query: 200 tokens
  - Retrieved context (if RAG): 600 tokens
- Average output tokens: 500
- Total per query: 1,700 tokens
- Cost per query: $0.051 (using GPT-4o)
- Current daily usage: ~50 queries (testing)
```

**B. Production Projections**
- Expected queries per day/month
- Peak load scenarios
- Monthly cost estimate at scale
- Cost per user (if applicable)

**C. Optimization Strategies**
1. **Model Selection**
   - Use GPT-4o-mini for 80% of queries → 50% cost reduction
   - Upgrade to GPT-4o only for complex queries

2. **Prompt Engineering**
   - Reduce system prompt from 400 to 200 tokens → 12% savings
   - More concise retrieved context → 20% savings

3. **Caching**
   - Cache common queries (50% hit rate) → 40% reduction in API calls
   - Cache embeddings for documents → one-time cost

4. **Smart Batching**
   - Batch similar queries → reduce API overhead

**D. Budget Allocation**
```
Development Phase (Weeks 3-9):    $50
Production Phase (Weeks 10-15):   $100
User Testing Buffer:              $30
Emergency/Overflow:               $20
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Total Semester Budget:            $200
```

📄 **Template:** [Cost Model Template]
📄 **Guide:** [Token Optimization Strategies]

---

#### **6. Prioritized Backlog (`docs/backlog-v2.md`)** 📝

**Update from Week 2:** Your initial backlog was speculative. Now prioritize based on:
- Technical dependencies (what blocks what)
- Risk mitigation (tackle unknowns early)
- User value (MVP features first)
- Milestone alignment (what's due when)

**Required Structure:**

**Priority 1: Critical Path (Must Have for MVP)**
- Issues that block future work
- Core features essential for Week 15 demo
- Technical infrastructure (auth, database, APIs)

**Priority 2: High Value (Should Have)**
- Features that significantly improve UX
- Evaluation infrastructure
- Error handling and edge cases

**Priority 3: Nice to Have (Could Have)**
- Polish and optimization
- Additional features if time permits
- Future roadmap items

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
```

📄 **Template:** [Backlog Template](./templates/backlog-template.md)  
🤖 **AI Prompt:** [Feature Prioritization Framework]
---

#### **7. Team Health Check (`docs/team-health-week4.md`)** 🤝

**New Requirement:** After 2 weeks of working together, assess team dynamics.

**Required Sections:**

**A. What's Working Well**
- Effective communication patterns
- Successful collaboration strategies
- Individual strengths being leveraged

**B. What Needs Improvement**
- Communication gaps
- Workload imbalances
- Technical skill gaps

**C. Updated Team Contract (if needed)**
- Any role reassignments
- Adjusted meeting schedules
- Refined decision-making processes

**D. Risk Mitigation**
- Early warning signs (e.g., someone falling behind)
- Backup plans for key risks
- Escalation paths if problems arise

📄 **Template:** [Team Health Check Template]

---

## 🔬 In-Class Lab Activities (2 Hours)

### **Part 1: AI-Powered Feature Discovery Workshop (45 minutes)**

**Objective:** Use AI frameworks to systematically explore your product space and identify high-impact features.

#### **Activity 1A: Run the 20-Pillar Design System (20 min)**

**Step-by-Step Process:**

1. **Open your AI assistant** (Claude, ChatGPT, etc.)

2. **Paste the 20-Pillar Design System prompt** (see [AI Prompts Guide]

3. **Input your refined capstone idea:**
   ```
   Example:
   "I'm building a mobile app for small business owners to extract 
   data from receipts using AI. Users upload photos of receipts, 
   the AI extracts merchant name, date, amount, and items, then 
   categorizes them for tax purposes. Currently, we have basic 
   OCR working but want to expand features."
   ```

4. **AI generates 20 strategic design pillars** like:
   - User-Centered Experience
   - Accessibility-First Design
   - Data Security & Privacy
   - Offline Capability
   - Export & Integration Features
   - Cost Optimization
   - Error Recovery & Support
   - Personalization Engine
   - (12 more...)

5. **Select 5-8 pillars most relevant to your project**
   ```
   Example selection:
   "I want to work with pillars 1 (User-Centered Experience), 
   3 (Data Security), 5 (Export Features), 7 (Error Recovery), 
   and 8 (Personalization)"
   ```

6. **For each selected pillar, AI generates 10 implementation tasks**
   ```
   Example for "Data Security & Privacy":
   1. End-to-end encryption for receipt images
   2. Secure cloud storage with automatic deletion
   3. GDPR/CCPA compliance framework
   4. User data export functionality
   5. Anonymization for analytics
   6. Biometric authentication (fingerprint/face)
   7. Secure API key management
   8. Privacy-first analytics
   9. Data breach notification system
   10. Third-party security audits
   ```

7. **Select which tasks are MVP vs. future roadmap**

8. **AI generates final blueprint** organizing all selected features

**Deliverable:** Complete feature roadmap with 40-80 potential functions, prioritized for implementation.

---

#### **Activity 1B: Run Feature Prioritization Framework (15 min)**

**Now that you have 40-80 features, how do you decide what to build first?**

1. **Paste the Feature Prioritization prompt** (see guide)

2. **Provide your context:**
   ```
   - Core purpose: [Your app's main function]
   - Target users: [Who uses it]
   - Current features: [What you've built in Week 3-4]
   - Business model: [How you monetize, if applicable]
   - Main pain points: [User frustrations]
   ```

3. **AI recommends 10 high-impact features** across categories:
   - 🚀 Growth Engine (acquire users)
   - ♻️ Retention Loop (keep users coming back)
   - 💰 Revenue Generator (improve monetization)
   - 🔄 Workflow Enhancer (improve core UX)
   - 🛡️ Trust Amplifier (increase security/credibility)

4. **For each feature, AI provides:**
   - User need it addresses
   - Implementation complexity
   - Impact potential
   - Success metrics

5. **AI generates priority matrix:**
   ```
   High Impact, Low Effort (DO FIRST):
   - Feature A
   - Feature B
   
   High Impact, High Effort (PLAN CAREFULLY):
   - Feature C
   - Feature D
   
   Low Impact, Low Effort (QUICK WINS):
   - Feature E
   
   Low Impact, High Effort (AVOID):
   - Feature F
   ```

**Deliverable:** Prioritized feature list aligned with user needs and team capacity.

---

#### **Activity 1C: Team Discussion & Alignment (10 min)**

**As a team, discuss:**

1. **Which AI-generated features resonate most with your vision?**
2. **Which features are essential for MVP (Week 15 demo)?**
3. **Which features address your biggest technical risks?**
4. **Which features are most feasible given your skill set?**

**Output:** Consensus on your MVP feature set (10-15 functions max)

---

### **Part 2: Architecture Review & Feedback (50 minutes)**

**Format:** Each team presents their refined architecture for peer and instructor feedback.

#### **Presentation Structure (5 minutes per team)**

**Slide 1: Problem & Solution (1 min)**
- What problem you're solving (updated from Week 2)
- Who your users are
- Your solution in one sentence

**Slide 2: Architecture Diagram (2 min)**
- Show your updated architecture diagram
- Walk through data flow for one core user action
- Highlight what changed since Week 2 and why

**Slide 3: Critical Design Decisions (1.5 min)**
- **Model choice:** "We're using GPT-4o-mini because [cost/speed tradeoff]"
- **Data storage:** "We chose Postgres + FAISS because [reasons]"
- **Deployment:** "We're deploying on Vercel because [developer experience]"

**Slide 4: Biggest Concerns & Questions (0.5 min)**
- "We're worried about [specific risk]"
- "We're unsure about [technical decision]"
- "We need advice on [specific challenge]"

#### **Feedback Session (3 minutes per team)**

**Instructor provides:**
- ✅ What's strong about this architecture
- ⚠️ Red flags or potential issues
- 💡 Suggestions for improvement
- 🎯 Focus areas for next 2 weeks

**Peers provide:**
- Questions about design choices
- Similar challenges they're facing
- Suggestions based on their experience

**Team takes notes** for post-lab refinement.

---

### **Part 3: Evaluation Planning Workshop (20 minutes)**

**Objective:** Define concrete success metrics and testing protocols.

#### **Activity 3A: Define Your Golden Set (10 min)**

**Golden Set = Your standard test cases for measuring quality**

**Step-by-Step:**

1. **Brainstorm test scenarios:**
   - Typical use cases (70% of test cases)
   - Edge cases (20% of test cases)
   - Adversarial inputs (10% of test cases)

2. **Example for Receipt Scanner App:**
   
   **Typical Cases:**
   - Standard grocery receipt
   - Restaurant receipt with tip
   - Gas station receipt
   - Online order confirmation
   
   **Edge Cases:**
   - Crumpled receipt
   - Faded ink
   - Receipt with multiple languages
   - Partial receipt (torn)
   
   **Adversarial Cases:**
   - Random text document
   - Blank image
   - Image of non-receipt (credit card, ID)
   - Deliberately obfuscated receipt

3. **Define success criteria for each case:**
   ```
   Test Case #1: Standard Grocery Receipt
   ✅ Extracts merchant name (>90% accuracy)
   ✅ Extracts date (>95% accuracy)
   ✅ Extracts total amount (>99% accuracy)
   ✅ Extracts 80%+ of line items
   ✅ Response time <3 seconds
   ✅ Confidence score calculated correctly
   ```

4. **Document in your evaluation plan**

**By Week 6, you'll have 50+ test cases ready.**

---

#### **Activity 3B: Plan User Testing Protocol (10 min)**

**For Week 7 user testing, you need:**

1. **Participant Profile**
   - Who are you recruiting? (demographics, experience level)
   - How many? (minimum 3, recommended 5)
   - How will you recruit them?

2. **Testing Tasks**
   - 3-5 specific tasks users will complete
   - Clear success criteria for each task
   
   Example:
   ```
   Task 1: Upload and Process a Receipt
   - Success: User uploads receipt, sees extracted data, confirms accuracy
   - Time limit: 5 minutes
   - Success criteria: Completes without assistance
   
   Task 2: Categorize Expense
   - Success: User correctly categorizes receipt as "Meals" or "Office Supplies"
   - Time limit: 2 minutes
   - Success criteria: Uses correct category
   ```

3. **Data Collection**
   - What metrics will you track? (completion rate, time on task, errors, satisfaction)
   - How will you collect feedback? (survey, interview, observation notes)

4. **Consent & Ethics**
   - How will you get informed consent?
   - How will you protect participant data?
   - IRB light checklist completed?

**Document this in your evaluation plan.**

---

### **Part 4: Rapid Refinement Session (5 minutes)**

**Quick team huddle to plan post-lab work:**

1. **Who is responsible for each deliverable?**
2. **What feedback from today needs to be incorporated?**
3. **What are your blockers?**
4. **When will you meet to finalize everything?**

**Instructor available for quick check-ins.**

---

## 🤖 AI Framework Prompts

All AI prompts are provided in the [AI Design Framework Prompts Guide](./guides/ai-design-framework-prompts.md):

### **Available Frameworks:**

1. **20-Pillar Design System**
   - Generates comprehensive feature roadmap
   - 20 strategic pillars → 200+ potential functions
   - Systematic exploration of product space

2. **Feature Prioritization Framework**
   - Identifies 10 high-impact features users actually want
   - Organizes by business impact (growth, retention, revenue)
   - Provides implementation complexity analysis
   - Generates priority matrix

3. **Architecture Gap Analysis**
   - Analyzes your current architecture for missing components
   - Identifies scalability bottlenecks
   - Suggests improvements with tradeoff analysis

4. **Evaluation Strategy Generator**
   - Creates comprehensive test plans
   - Suggests metrics aligned with your goals
   - Provides testing timeline and protocols

5. **Risk Assessment Framework**
   - Systematically identifies technical, product, and team risks
   - Generates mitigation strategies
   - Prioritizes risks by likelihood and impact

**How to Use These Prompts:**

1. Copy prompt from guide
2. Paste into your preferred AI assistant (Claude, ChatGPT, etc.)
3. Provide your project context
4. Iterate on AI suggestions
5. Document final decisions in your deliverables

**Pro Tips:**
- Run multiple iterations: "Give me 10 more feature ideas"
- Challenge AI suggestions: "Why is feature X higher priority than Y?"
- Combine frameworks: Use 20-Pillar System, then Feature Prioritization, then Risk Assessment
- Use AI to review your work: Paste your architecture diagram and ask "What's missing?"

---

## 📊 Grading Rubric (5 points total)

| Component | Points | Criteria |
|-----------|--------|----------|
| **Refined Proposal** | 1.0 | Updated with Week 3-4 learnings, specific improvements documented, realistic scope |
| **Feature Roadmap (AI-Generated)** | 1.0 | Used AI frameworks systematically, prioritized features clearly, MVP defined |
| **Architecture Diagram v2** | 1.0 | Complete, accurate, shows evolution from Week 2, all components documented |
| **Evaluation Plan** | 1.0 | Concrete metrics, golden set defined, user testing protocol clear, timeline realistic |
| **Cost Model** | 0.5 | Based on real data, optimizations identified, budget allocated |
| **Presentation Quality** | 0.5 | Clear communication, defends design decisions, incorporates feedback professionally |

**Bonus (up to +0.5):**
- Exceptionally thorough AI framework exploration
- Creative use of AI for architecture analysis
- Evidence of deep iteration and refinement

---

## 🚀 After This Lab: Your Path Forward

### **Week 5: RAG Implementation**
Your refined architecture and evaluation plan will guide:
- Which documents to index
- How to chunk and embed
- What metrics to track
- How to measure retrieval quality

### **Week 7: User Testing Round 1**
Your evaluation plan provides:
- Participant recruitment strategy
- Testing tasks and success criteria
- Data collection methods
- Feedback analysis framework

### **Week 11: Safety & Evaluation Audit**
Your golden set and risk assessment form the foundation for:
- Red team testing
- Bias and privacy checks
- Error taxonomy
- Safety telemetry

### **Week 15: Final Demo**
Everything compounds:
- Feature roadmap → What you built
- Evaluation plan → How you measured success
- Architecture → What you'll present
- Cost model → Business viability

**This lab is your foundation. Build it well.**

---

## 💡 Tips for Success

### **For Refinement**

1. **Be honest about what changed**
   - Don't hide Week 2 mistakes, show growth
   - "We initially chose X, but learned Y, so switched to Z"

2. **Use data, not opinions**
   - "Our Week 3 testing showed latency of 5s, so we optimized to 2.5s"
   - Not: "We think it's fast enough"

3. **Document tradeoffs**
   - "We chose Postgres over MongoDB because relational queries are more important than schema flexibility for our use case"

4. **Identify unknowns**
   - "We're still unsure about optimal chunk size for RAG, will experiment in Week 5"

### **For AI Framework Usage**

1. **Iterate multiple times**
   - Don't stop at first set of suggestions
   - "Give me 10 more features focusing on enterprise users"

2. **Cross-validate**
   - Run same project through different AI frameworks
   - Compare Feature Prioritization results with 20-Pillar System output

3. **Challenge AI suggestions**
   - "Why is this feature higher priority?"
   - "What's the implementation risk you're not mentioning?"

4. **Use AI for review**
   - Paste your architecture: "What's missing? What are the weak points?"
   - Paste your evaluation plan: "What metrics am I not considering?"

### **For Presentations**

1. **Practice your 5-minute pitch**
   - Time yourself
   - Focus on key decisions, not details

2. **Prepare for tough questions**
   - "Why not use a different model?"
   - "How will you handle [specific edge case]?"

3. **Show vulnerability**
   - "We're worried about X, any suggestions?"
   - Builds trust and gets better feedback

4. **Take notes**
   - Assign someone to document all feedback
   - You'll forget important points otherwise

---

## ❓ Frequently Asked Questions

**Q: Our architecture changed completely since Week 2. Is that bad?**

A: No! That's **expected and good**. Show what you learned. Teams that don't adapt their architecture by Week 4 often struggle later.

**Q: The AI frameworks generated 200+ features. We can't build all of them.**

A: Correct! That's the point. Pick 10-15 for MVP. The rest inform your future roadmap and help you think comprehensively.

**Q: Can we use AI to write our evaluation plan?**

A: AI can suggest structure and metrics, but YOU must customize it to your specific project. Copy-paste without adaptation will be obvious and penalized.

**Q: Our team is behind. Can we skip some deliverables?**

A: NO. This lab is specifically designed to catch you up. Skipping now means you'll be more behind later. Use the AI frameworks to accelerate your work.

**Q: What if we get critical feedback that requires major changes?**

A: That's the point of Week 4! Better to pivot now than at Week 10. You have time to adjust.

**Q: Should we run the AI prompts individually or as a team?**

A: **Both.** Run individually first to get diverse ideas, then discuss as a team to reach consensus.

**Q: Can we change our capstone project entirely based on AI suggestions?**

A: Only with instructor approval. Small pivots are fine, complete project changes need discussion.

---

## 📚 Resources

### **Templates** (All in `/templates/`)
- [Refined Proposal Template](./templates/refined-proposal-template.md)
- [Feature Roadmap Template](./templates/feature-roadmap-template.md)
- [Architecture Diagram Template](./templates/architecture-diagram-template.md)
- [Evaluation Plan Template](./templates/evaluation-plan-template.md)
- [Cost Model Template](./templates/cost-model-template.md)
- [Backlog Template](./templates/backlog-template.md)
- [Team Health Check Template](./templates/team-health-template.md)

### **Guides** (All in `/guides/`)
- [AI Design Framework Prompts](./guides/ai-design-framework-prompts.md) ⭐
- [Architecture Design Best Practices](./guides/architecture-design-guide.md)
- [Token Optimization Strategies](./guides/token-optimization-guide.md)
- [Evaluation Planning Guide](./guides/evaluation-planning-guide.md)
- [Feature Prioritization Guide](./guides/feature-prioritization-guide.md)

### **Examples** (All in `/examples/`)
- [Example Refined Proposal](./examples/example-refined-proposal.md)
- [Example Feature Roadmap](./examples/example-feature-roadmap.md)
- [Example Architecture Diagram](./examples/example-architecture-diagram.png)
- [Example Evaluation Plan](./examples/example-evaluation-plan.md)

### **External Resources**
- OpenAI Token Optimization: https://platform.openai.com/docs/guides/optimization
- System Design Primer: https://github.com/donnemartin/system-design-primer
- OWASP AI Security Top 10: https://owasp.org/www-project-ai-security-and-privacy-guide/

---

## 🎯 Success Checklist

Before you submit, verify:

### **Refinement**
- [ ] Week 2 proposal updated with specific learnings
- [ ] Architecture diagram reflects current reality
- [ ] All technical decisions documented with rationale
- [ ] Risks updated based on implementation experience

### **AI Frameworks**
- [ ] Ran 20-Pillar Design System and selected relevant pillars
- [ ] Generated comprehensive feature roadmap (40-80 functions)
- [ ] Used Feature Prioritization to identify MVP features
- [ ] Applied Risk Assessment framework to identify gaps

### **Evaluation**
- [ ] Defined 5+ concrete success metrics
- [ ] Created plan for 50+ golden set test cases
- [ ] Documented user testing protocol for Week 7
- [ ] Established evaluation timeline through Week 15

### **Cost Model**
- [ ] Calculated baseline from Week 3-4 usage
- [ ] Projected production costs
- [ ] Identified 3+ optimization strategies
- [ ] Allocated semester budget

### **Team Health**
- [ ] Assessed what's working well
- [ ] Identified improvement areas
- [ ] Updated team contract if needed
- [ ] Established risk mitigation plans

### **Quality**
- [ ] All documents proofread
- [ ] All links work
- [ ] All images render correctly
- [ ] Git history shows team collaboration

---

## 🔥 Final Reminder

**This lab is your course correction opportunity.**

Teams that invest deeply in Week 4 refinement:
- Have clearer direction for Weeks 5-15
- Make better technical decisions
- Build more cohesive products
- Stress less during final weeks
- Deliver stronger demos

Teams that rush through Week 4:
- Struggle with Week 5 RAG implementation
- Lack clear evaluation criteria for Week 7 testing
- Scramble during Week 11 safety audit
- Deliver incomplete Week 15 demos

**The choice is yours. Make Week 4 count.**

---

**Questions?** Come to office hours, post in the forum, or email: zeshan.ahmad@kiu.edu.ge

**Good luck! 🚀**
