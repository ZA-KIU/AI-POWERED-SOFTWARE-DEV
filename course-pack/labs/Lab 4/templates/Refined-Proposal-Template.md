# Refined Capstone Proposal (Version 2)

**Project Name:** [Your Project Name]  
**Team Members:** [Name 1], [Name 2], [Name 3]  
**Date:** Week 4, [Date]  
**Version:** 2.0 (Updated from Week 2 submission)

---

## 📋 Document Change Log

### What Changed Since Week 2?

| Section | Change Type | Summary |
|---------|-------------|---------|
| Problem Statement | **Refined** | Made problem more specific based on user conversations |
| Technical Architecture | **Major Update** | Switched from X to Y due to [reason] |
| Success Criteria | **Enhanced** | Added measurable metrics with specific targets |
| Risk Assessment | **Expanded** | Added 3 new risks discovered during prototyping |
| Timeline | **Realistic** | Adjusted based on Week 3-4 velocity |

---

## 1. Problem Statement (Updated)

### The Problem

**Original (Week 2):**
> [Your original problem statement from Week 2]

**Refined (Week 4):**
[Your updated, more specific problem statement. Should be 2-3 paragraphs addressing:]

- **What is the specific problem?** Be concrete and narrow.
- **Who experiences this problem?** Define your target users precisely.
- **Why is this problem significant?** Include any validation from Week 3-4 (e.g., "Interviewed 5 potential users, all confirmed this is a daily pain point")
- **What are current solutions and their limitations?** Explain gaps in existing tools.
- **Why is AI appropriate for this problem?** Justify why AI adds value over traditional approaches.

**Example (Good):**
> Small business owners (1-10 employees) who file quarterly taxes waste 3-5 hours per week manually entering receipt data into spreadsheets. Current solutions like Expensify ($15/month) are too expensive for businesses with <$100K revenue and require complex setup. In conversations with 6 local business owners, 5 reported losing receipts and missing tax deductions because tracking is too tedious. AI-powered OCR can extract receipt data in <3 seconds with 85%+ accuracy, reducing data entry time by 80% while costing <$10/month at our expected usage volume.

---

## 2. Target Users (Updated)

### User Personas

**Primary User: [Name] the [Role]**
- **Demographics:** Age range, location, education, tech comfort
- **Role/Context:** Job title, company size, daily responsibilities
- **Goals:** What they want to achieve with your app
- **Pain Points:** Current frustrations (validated with real users if possible)
- **Behaviors:** How they currently solve this problem
- **Success Metrics:** What would make them love your app?

**Example:**
> **Primary User: Maria the Freelance Consultant**
> - Demographics: 32 years old, Atlanta, MBA, moderate tech comfort (uses Google Workspace, struggles with complex software)
> - Role: Self-employed management consultant, $80K/year revenue, tracks ~200 receipts/year for taxes
> - Goals: Quickly categorize business expenses, generate quarterly tax reports, never miss a deduction
> - Pain Points: Loses paper receipts, forgets to log expenses until tax time, can't afford Expensify, finds QuickBooks overwhelming
> - Current Behavior: Takes photos with phone camera, saves to Google Drive folder, manually enters into Excel quarterly
> - Success: Would pay $10/month if it saves her 2+ hours/week and increases tax deductions by $500+/year

**Secondary User: [Name] the [Role]** (if applicable)
[Same structure as above]

### User Validation

**How We Validated Our Users:**
- [ ] Interviewed [X] potential users (Week 3-4)
- [ ] Observed [X] users with current tools
- [ ] Surveyed [X] people in target demographic
- [ ] Analyzed competitors' user reviews
- [ ] Posted in relevant communities and got [X] responses

**Key Insights from Validation:**
1. [Specific insight from user research]
2. [Specific insight from user research]
3. [Specific insight from user research]

---

## 3. Success Criteria (Updated & Measurable)

### Product Success Metrics

| Metric | Target (Week 15) | Measurement Method | Current Baseline (Week 4) |
|--------|------------------|-------------------|---------------------------|
| **Task Completion Rate** | >70% | User testing: % who complete core workflow without help | Not yet measured |
| **Time to Complete Core Task** | <3 minutes | Timed during user testing | Not yet measured |
| **User Satisfaction (Post-Task)** | >4.0/5.0 | Survey after Week 7 & 14 testing | Not yet measured |
| **Would Recommend** | >60% | "Would you recommend to a friend?" | Not yet measured |
| **Daily Active Users (if applicable)** | 10 users | Analytics tracking | 3 users (team members) |

### Technical Success Metrics

| Metric | Target | Measurement Method | Current Performance |
|--------|--------|-------------------|---------------------|
| **AI Accuracy** | >85% | Golden set (50 test cases) | ~75% (tested on 10 cases) |
| **Response Latency (P95)** | <3 seconds | Backend logging | ~4.5 seconds |
| **API Uptime** | >99% | Monitoring dashboard | Not yet deployed |
| **Cost per Query** | <$0.05 | Cost tracking logs | ~$0.013 (current, without optimization) |
| **Token Usage per Query** | <1000 tokens | API response tracking | ~1300 tokens (can optimize) |

### Learning Goals (Team Member Level)

| Team Member | Learning Goal | Success Criteria | Progress (Week 4) |
|-------------|---------------|------------------|-------------------|
| [Name 1] | Master RAG implementation | Successfully integrate FAISS, <300ms search latency | Not started (planned Week 5) |
| [Name 2] | Build production-ready FastAPI backend | Deployed API with >99% uptime, proper error handling | Basic API working, not deployed |
| [Name 3] | Implement comprehensive testing | >80% code coverage, golden set with 50+ cases | No automated tests yet |

**Why These Metrics Matter:**
- **Task completion >70%** → Users can actually use the app (validates UX)
- **Latency <3s** → Users won't abandon due to slowness
- **Accuracy >85%** → Users trust results (critical for adoption)
- **Cost <$0.05/query** → Economically viable at scale
- **Satisfaction >4.0/5.0** → High quality experience

---

## 4. Technical Architecture (Updated)

### Architecture Evolution

**What Changed Since Week 2:**

| Component | Week 2 Plan | Week 4 Reality | Why We Changed |
|-----------|-------------|----------------|----------------|
| **Frontend** | React on Netlify | React (Vite) on Vercel | Vercel has better FastAPI integration |
| **Backend** | Flask | FastAPI | Async support needed for streaming responses |
| **Database** | MongoDB | PostgreSQL | Relational structure better fits our data model |
| **AI Model** | GPT-4 | GPT-4o-mini (80%) + GPT-4o (20%) | Cost optimization: mini works for clear cases |
| **Deployment** | Heroku | Railway | Free tier more generous, better developer experience |

### Current Architecture Diagram

[Insert your architecture diagram here - can be image, ASCII, or Mermaid]

**Key Components:**

1. **Frontend (React + Vite)**
   - User interface for uploading, reviewing, categorizing
   - Deployed on Vercel
   - Communicates with backend via REST API

2. **Backend (FastAPI + Python)**
   - Receives images from frontend
   - Preprocesses images (resize, compress)
   - Calls OpenAI Vision API
   - Stores results in PostgreSQL
   - Returns structured JSON to frontend
   - Deployed on Railway

3. **Database (PostgreSQL on Railway)**
   - Tables: users, receipts, categories
   - Stores receipt metadata and extracted data
   - No image storage (images stored in Cloudinary)

4. **AI Services (OpenAI APIs)**
   - GPT-4o-mini for clear, standard receipts (80% of cases)
   - GPT-4o for poor quality or complex receipts (20% of cases)
   - Decision based on image quality score

5. **Authentication (Clerk)**
   - Handles user signup/login
   - OAuth integration (Google)
   - JWT tokens for API authentication

6. **Image Storage (Cloudinary)**
   - Stores uploaded receipt images
   - Auto-optimization and CDN
   - 7-day retention policy (privacy)

### Data Flow for Core User Action

**User Flow: Upload Receipt**

```
1. User uploads image in React frontend
   ↓
2. Frontend validates file (size, type) + shows loading state
   ↓
3. POST request to /api/receipts with image
   ↓
4. Backend (FastAPI):
   a. Authenticates user (Clerk JWT)
   b. Uploads image to Cloudinary
   c. Preprocesses image (resize to 1024x1024, compress)
   d. Assesses image quality (0-1 score)
   e. Chooses model: quality >0.7 → GPT-4o-mini, else → GPT-4o
   f. Calls OpenAI Vision API with structured output
   g. Receives JSON: {merchant, date, amount, items, confidence}
   h. Stores in PostgreSQL (receipts table)
   i. Returns JSON to frontend
   ↓
5. Frontend displays extracted data with confidence indicator
   ↓
6. User reviews and confirms/edits
   ↓
7. Frontend sends PUT request to update receipt (if edited)
   ↓
8. Backend updates PostgreSQL
```

**Latency Budget:**

| Step | Target Latency | Current Performance | Notes |
|------|----------------|---------------------|-------|
| Frontend validation | <100ms | ~50ms | ✅ On track |
| Image upload to Cloudinary | <500ms | ~800ms | ⚠️ Need CDN optimization |
| Image preprocessing | <200ms | ~150ms | ✅ On track |
| OpenAI API call | <2000ms | ~2500ms | ⚠️ Optimize prompt |
| Database write | <100ms | ~80ms | ✅ On track |
| Frontend render | <200ms | ~300ms | ⚠️ Optimize React rendering |
| **Total (P95)** | **<3000ms** | **~4500ms** | 🔴 Must optimize |

### Technology Stack Justification

| Technology | Why We Chose It | Alternatives Considered | Tradeoff |
|------------|-----------------|-------------------------|----------|
| **FastAPI** | Async support, automatic API docs, type safety | Flask, Django | Pro: Modern, fast; Con: Smaller community |
| **PostgreSQL** | Relational data fits our model, strong consistency | MongoDB, Firebase | Pro: ACID guarantees; Con: Less flexible schema |
| **Vercel** | Excellent DX, free tier, fast deployments | Netlify, Render | Pro: Speed; Con: Vendor lock-in |
| **Railway** | Free tier, PostgreSQL included, easy setup | Heroku, Fly.io | Pro: All-in-one; Con: Less mature |
| **GPT-4o-mini** | 90% cheaper than GPT-4, good for clear images | Claude, Gemini | Pro: Cost; Con: Slightly lower accuracy |
| **Clerk** | Drop-in auth, OAuth built-in, free tier | Auth0, Firebase Auth | Pro: Easy; Con: Vendor lock-in |

### Security & Privacy Considerations

**Implemented:**
- [x] HTTPS for all API requests
- [x] JWT authentication via Clerk
- [x] Environment variables for API keys (not committed to Git)
- [x] CORS configured to allow only frontend domain
- [x] Input validation on all API endpoints

**Planned (Week 5-6):**
- [ ] Rate limiting (100 requests/hour per user)
- [ ] API cost caps ($50/day hard limit)
- [ ] Image deletion after 7 days (privacy)
- [ ] Encryption at rest for sensitive data
- [ ] SQL injection protection (using ORMs with parameterized queries)

### Known Technical Debt

1. **No caching layer** (planned Week 6: Redis for repeated queries)
2. **No automated testing** (planned Week 6: pytest + GitHub Actions)
3. **No monitoring/logging** (planned Week 8: Sentry for error tracking)
4. **No database backups** (planned Week 7: daily automated backups)
5. **Hardcoded prompts** (planned Week 6: move to config file for A/B testing)

---

## 5. Risk Assessment (Updated & Expanded)

### Risk Matrix

| Risk ID | Risk | Likelihood | Impact | Severity | Status |
|---------|------|------------|--------|----------|--------|
| R1 | API cost overruns | HIGH | HIGH | 🔴 CRITICAL | Mitigating |
| R2 | Amount extraction accuracy <95% | MEDIUM | HIGH | 🔴 CRITICAL | Monitoring |
| R3 | Team member unavailability | HIGH | MEDIUM | 🟡 HIGH | Planning |
| R4 | Poor quality receipt photos | HIGH | MEDIUM | 🟡 HIGH | Not addressed |
| R5 | No production deployment experience | HIGH | MEDIUM | 🟡 HIGH | In progress |
| R6 | Scope creep | MEDIUM | MEDIUM | 🟢 MEDIUM | Controlled |
| R7 | User adoption (no one uses it) | MEDIUM | MEDIUM | 🟢 MEDIUM | Validating |
| R8 | Database performance at scale | LOW | MEDIUM | 🟢 MEDIUM | Not urgent |
| R9 | Receipt image storage costs | LOW | LOW | ⚪ LOW | Monitoring |
| R10 | Privacy/GDPR compliance gaps | MEDIUM | HIGH | 🟡 HIGH | Planning (Week 11) |

### Critical Risks (Detailed)

#### 🔴 Risk R1: API Cost Overruns

**Description:** Without proper cost controls, API costs could exhaust semester budget in days.

**Likelihood:** HIGH (60-80%)  
**Impact:** HIGH (Blocks development and testing)  
**Severity:** CRITICAL

**Triggers:**
- Inefficient prompts (too many tokens)
- No caching for repeated queries
- Testing without cost tracking
- Batch processing without rate limits

**Preventive Mitigation:**
1. ✅ **DONE (Week 4):** Set up cost tracking dashboard
2. ✅ **DONE (Week 4):** Implement rate limiting (100 req/hour per user)
3. ⏳ **IN PROGRESS (Week 4):** Switch to GPT-4o-mini for 80% of queries
4. 📅 **PLANNED (Week 5):** Add Redis caching (40% cost reduction expected)
5. 📅 **PLANNED (Week 5):** Optimize prompts (reduce from 500 to 200 tokens)

**Contingency Plan (If Risk Occurs):**
- Immediate: Pause all non-essential API calls
- Week 5+: Switch to GPT-4o-mini exclusively, apply for OpenAI credits, reduce scope

**Monitoring:**
- Daily cost dashboard (check every morning)
- Alert if daily cost >$5
- Weekly budget review in standup

**Owner:** [Backend Lead]  
**Next Review:** Every Monday

---

#### 🔴 Risk R2: Amount Extraction Accuracy <95%

**Description:** If amount extraction is inaccurate, users could claim wrong tax deductions (legal liability).

**Likelihood:** MEDIUM (40-60%)  
**Impact:** HIGH (User trust destroyed, potential legal issues)  
**Severity:** CRITICAL

**What We've Learned (Week 3-4):**
- Tested on 10 receipts: 7/10 perfect, 2/10 off by pennies, 1/10 completely wrong (faded receipt)
- Faded receipts are the biggest problem
- Decimal point detection is fragile

**Preventive Mitigation:**
1. ✅ **DONE (Week 4):** User confirmation workflow (always require manual review)
2. 📅 **PLANNED (Week 5):** Create golden set with 50 diverse receipts
3. 📅 **PLANNED (Week 6):** Implement multi-pass verification (extract amount twice, compare)
4. 📅 **PLANNED (Week 6):** Add image preprocessing (enhance contrast for faded receipts)
5. 📅 **PLANNED (Week 7):** Add confidence scoring (flag <0.8 for human review)

**Contingency Plan:**
- If golden set shows <95%: Add preprocessing, try GPT-4o exclusively for amounts, consider hybrid OCR+LLM
- If production accuracy drops: Add "Beta" warning, require human review for amounts >$100

**Monitoring:**
- Golden set regression tests (weekly)
- User edit rate for amounts
- Production accuracy dashboard

**Owner:** [AI/ML Lead]  
**Next Review:** Week 5 (after golden set created)

---

### High Priority Risks (Summary)

**🟡 R3: Team Member Unavailability**
- Mitigation: Cross-training (Week 4-5), frontload critical work, buffer time in schedule
- Contingency: Redistribute tasks, reduce scope

**🟡 R4: Poor Quality Receipt Photos**
- Mitigation: Add image preprocessing (Week 6), user guidance ("Take clear photos"), provide examples
- Contingency: Manual review workflow, set expectations

**🟡 R5: No Production Deployment Experience**
- Mitigation: Deploy to staging NOW (Week 4), practice deployment, document process
- Contingency: Allocate extra time Week 13-14, instructor support

**🟡 R10: Privacy/GDPR Compliance**
- Mitigation: Review GDPR requirements (Week 5), implement data deletion (Week 6), privacy policy (Week 10)
- Contingency: Consult legal resources, scope down data collection

### Risk Mitigation Roadmap

**Week 4 (This Week):**
- [x] Cost tracking dashboard (R1)
- [x] Rate limiting (R1)
- [x] User confirmation for amounts (R2)
- [ ] Deploy to staging (R5)
- [ ] Cross-training session (R3)

**Week 5-6:**
- [ ] Create golden set (R2)
- [ ] Implement caching (R1)
- [ ] Image preprocessing (R4)
- [ ] Optimize prompts (R1)
- [ ] Review GDPR requirements (R10)

**Week 7-8:**
- [ ] User testing (R7)
- [ ] Iterate based on feedback (R4, R7)
- [ ] Multi-pass amount verification (R2)

**Week 9-11:**
- [ ] Buffer for midterms (R3)
- [ ] Safety audit (R10)
- [ ] Performance testing (R8)

---

## 6. Research Plan (Updated)

### Technical Questions We Need to Answer

#### Q1: How do we optimize image preprocessing to improve accuracy on faded receipts?

**Status:** 🔴 Not Started  
**Deadline:** Week 5  
**Approach:**
1. Research image enhancement techniques (contrast adjustment, sharpening, noise reduction)
2. Test with Python libraries: Pillow, OpenCV, scikit-image
3. Create A/B test: raw images vs. enhanced images
4. Measure accuracy improvement on faded receipts

**Resources:**
- OpenCV documentation on image enhancement
- Research papers on receipt OCR preprocessing
- Stack Overflow: "improve OCR accuracy on faded documents"

**Success Criteria:** 10%+ accuracy improvement on faded receipts

---

#### Q2: What's the optimal chunking strategy for RAG (if we add RAG)?

**Status:** ⏸️ Deprioritized (Not in MVP scope)  
**Deadline:** Post-course  
**Note:** RAG is not essential for MVP. May add later if users request "search my past receipts."

---

#### Q3: How do we prevent prompt injection attacks?

**Status:** 📅 Planned (Week 6)  
**Deadline:** Week 6 (before user testing)  
**Approach:**
1. Research OWASP Top 10 for LLMs
2. Implement input sanitization
3. Test with adversarial inputs (e.g., "Ignore previous instructions and...")
4. Add system prompt guardrails

**Resources:**
- OWASP LLM Top 10
- OpenAI safety best practices
- LangChain prompt injection defenses

**Success Criteria:** Block 100% of obvious injection attempts in testing

---

### Product Questions We Need to Answer

#### Q4: Do users trust AI extractions enough to skip manual review?

**Status:** 📅 Planned (Week 7)  
**Deadline:** Week 7 (during user testing)  
**Approach:**
1. Ask in user testing: "Would you confirm every receipt or only suspicious ones?"
2. Track: How often do users edit extracted data?
3. Measure: Confidence score correlation with user edits

**Success Criteria:** >50% of users say they'd trust results without manual review (if confidence >0.8)

---

#### Q5: What error messages are most helpful when extraction fails?

**Status:** 📅 Planned (Week 7)  
**Deadline:** Week 7 (during user testing)  
**Approach:**
1. Observe users when errors occur
2. Test multiple error message variations
3. Ask: "What would you do next?" when error appears

**Success Criteria:** Users understand error and know how to recover

---

### Experiments & Prototypes

**Week 4-5: Enhanced Image Preprocessing**
- Goal: Improve accuracy on poor quality receipts
- Success: 10%+ accuracy improvement on golden set (faded receipts subset)

**Week 5-6: GPT-4o vs GPT-4o-mini Quality Comparison**
- Goal: Validate that GPT-4o-mini is acceptable for clear receipts
- Success: <5% accuracy difference on clear receipts, 50% cost savings

**Week 7-8: User Testing Round 1**
- Goal: Validate core UX and AI accuracy
- Success: >70% task completion rate, >4.0/5.0 satisfaction

**Week 11-12: Red Team Testing (Safety Audit)**
- Goal: Identify security vulnerabilities
- Success: Find and fix all critical issues before Week 15

---

## 7. User Study Plan (Updated)

### Research Ethics

**Do we need IRB approval?**  
✅ **No** - Our project qualifies for IRB exemption (educational, minimal risk, no sensitive data)

**IRB Light Checklist:**
- [x] Informed consent will be obtained (verbal consent via Zoom)
- [x] Participants can withdraw at any time
- [x] Data will be anonymized (Participant 1, Participant 2, etc.)
- [x] Recordings will be deleted after analysis (within 2 weeks)
- [x] No collection of sensitive personal information
- [x] Minimal risk to participants (just testing a receipt app)

### User Testing Round 1: Week 7

**Participants:**
- Sample size: 5 participants
- Criteria: Freelancers or small business owners who track expenses
- Recruitment: Facebook groups, LinkedIn, local coworking spaces, personal network
- Incentive: $25 Amazon gift card per participant
- Format: Remote (Zoom), 45 minutes per session

**Testing Goals:**
1. Validate that users can successfully upload and process receipts
2. Measure perceived accuracy of AI extractions
3. Identify UX pain points and confusion
4. Assess whether users trust the AI results
5. Determine if categorization feature is useful
6. Understand whether users would pay for this

**Testing Tasks:**
1. Upload and process first receipt (5 min)
2. Review and confirm accuracy (3 min)
3. Categorize expense (3 min)
4. Batch upload multiple receipts (7 min)
5. Export data (3 min)

**Data Collection:**
- Task completion rate (per task)
- Time on task
- Errors or confusion moments
- Think-aloud observations
- Post-task survey (10 questions)
- System Usability Scale (SUS) score

**Success Criteria:**
- >70% task completion rate
- >4.0/5.0 average satisfaction score
- At least 3 actionable insights for improvement
- Validation that users would pay $10-15/month

**Timeline:**
- Days 1-2: Recruit participants
- Days 3-6: Conduct 5 sessions
- Day 7: Analyze and synthesize findings

**Deliverable:** User Testing Report (due end of Week 7)

### User Testing Round 2: Week 14

**Participants:** 5 NEW participants (different from Round 1)  
**Goal:** Validate that improvements from Round 1 worked  
**Success Criteria:** >85% task completion, >4.5/5.0 satisfaction

---

## 8. Project Timeline & Milestones (Realistic)

### Weekly Breakdown

| Week | Focus | Deliverables | Owner | Status |
|------|-------|-------------|--------|--------|
| 1 | Setup | Team formation, initial ideas | All | ✅ Complete |
| 2 | Planning | Proposal v1, team contract, dev environment | All | ✅ Complete |
| 3 | Core Flow | Basic query → LLM → response | [Name] | ✅ Complete |
| 4 | **Design Review** | **Proposal v2, architecture v2, eval plan** | **All** | **🔄 In Progress** |
| 5 | Retrieval (Skip) | RAG not needed for MVP | - | ⏸️ Deprioritized |
| 5 | Optimization | Golden set creation, caching, prompt optimization | [Name] | 📅 Planned |
| 6 | Safety | Input validation, rate limiting, error handling | [Name] | 📅 Planned |
| 7 | User Testing 1 | First user feedback round (5 participants) | All | 📅 Planned |
| 8 | Iteration | Implement feedback from Week 7 | All | 📅 Planned |
| 9 | **Midterm Exam** | Study week (reduced project work) | All | 📅 Planned |
| 10 | Deployment | Deploy to production, monitoring, CI/CD | [Name] | 📅 Planned |
| 11 | **Safety Audit** | Red teaming, bias testing, privacy review | All | 📅 Planned |
| 12 | Evaluation | Regression testing on golden set | [Name] | 📅 Planned |
| 13 | Production Polish | Bug fixes, performance optimization | All | 📅 Planned |
| 14 | User Testing 2 | Final validation round (5 participants) | All | 📅 Planned |
| 15 | **Final Demo** | Presentation, video, case study | All | 📅 Planned |

### Major Milestones (Updated)

**✅ Milestone 1: Proposal v1 (Week 2)** - COMPLETE
- Submitted: [Date]
- Points: 10/10
- Feedback: [Instructor feedback summary]

**🔄 Milestone 2: Design Review (Week 4)** - IN PROGRESS
- Due: [Date]
- Points: 5
- Deliverables: This document, architecture diagram, evaluation plan, cost model, backlog

**🎯 Milestone 3: Safety & Evaluation Audit (Week 11)**
- Due: [Date]
- Points: 3
- Deliverables: Red team results, bias checks, golden set regression, error taxonomy, telemetry plan

**🎯 Milestone 4: Final Demo (Week 15)**
- Due: [Date]
- Points: 7
- Deliverables: Working product, CI/CD, public README, demo video, case study

### Dependency Map

**Critical Path (Must Complete in Order):**
1. Week 4: Finalize architecture → Blocks everything else
2. Week 5: Create golden set → Blocks Week 12 evaluation
3. Week 6: Basic features complete → Blocks Week 7 user testing
4. Week 7: User testing → Informs Week 8 iterations
5. Week 10: Deploy to production → Blocks Week 11 safety audit
6. Week 11: Safety audit → Must pass before Week 15 demo

**Parallel Tracks (Can Work Simultaneously):**
- Week 5-6: One person on golden set, another on caching
- Week 7-8: One person recruiting testers, another implementing features

### Backup Plan (Scope Cuts if Behind)

**If we fall behind, we'll cut in this order:**

**Priority 3: Cut First (Nice-to-Have)**
1. Batch upload feature → Users can upload one at a time
2. Multiple export formats → Just CSV is fine
3. Expense charts/analytics → Not essential for MVP
4. Email forwarding → Can add post-course

**Priority 2: Cut if Desperate (Should Have)**
5. Categorization feature → Users can categorize manually later
6. Image preprocessing → Rely on base GPT-4V accuracy

**Priority 1: Never Cut (Must Have)**
- Core upload + extraction flow
- User authentication
- Amount extraction (must be accurate!)
- Basic export to CSV
- Safety features (rate limiting, input validation)

### Velocity Tracking (Week 3-4 Reality Check)

**Week 3 Planned vs. Actual:**
- Planned: 30 hours team effort, basic prototype working
- Actual: 25 hours team effort, basic prototype working (but slower than expected)
- Lesson: We underestimated debugging time by 30%

**Week 4 Adjusted Expectations:**
- Plan: 30 hours → Expect 20 hours of real progress
- Account for: Midterm prep, other course deadlines, debugging overhead

**Realistic Capacity per Week:**
- Team member 1: 12 hours/week (consistent)
- Team member 2: 10 hours/week (has heavier course load)
- Team member 3: 15 hours/week (most available)
- Total: ~37 hours/week team capacity

---

## 9. Team Health & Collaboration (New Section)

### What's Working Well (Week 4 Assessment)

✅ **Communication:**
- Daily Slack check-ins working well
- Quick responses (usually <2 hours)
- Good use of voice calls for complex discussions

✅ **Technical Collaboration:**
- Pair programming sessions effective (2x/week)
- Code reviews happening consistently
- Shared knowledge of codebase

✅ **Task Ownership:**
- Clear division of responsibilities
- Everyone contributing meaningfully
- No major conflicts over decisions

### What Needs Improvement

⚠️ **Documentation:**
- Need better inline code comments
- Setup instructions incomplete (new team members would struggle)
- Architecture decisions not documented

🔧 **Fix:** Spend 2 hours in Week 5 documenting everything

---

⚠️ **Testing:**
- No automated tests yet
- Manual testing is time-consuming
- Hard to catch regressions

🔧 **Fix:** Allocate Week 6 to writing tests, aim for >50% coverage

---

⚠️ **Workload Balance:**
- Team member 2 has heavier course load (will worsen near midterms)
- Team member 1 doing disproportionate amount of backend work

🔧 **Fix:** Cross-train on backend (Week 5), frontload critical work before Week 9

---

### Updated Team Contract (Changes from Week 2)

**Adjusted Meeting Schedule:**
- ~~3x/week~~ → **2x/week in-person** (Wed 6-8pm, Sat 10am-12pm)
- Daily async Slack check-ins
- Ad-hoc pair programming as needed

**Adjusted Roles:**
- Team member 1: Backend + Architecture (expanded role)
- Team member 2: Frontend + UX (reduced hours Week 9)
- Team member 3: Testing + DevOps (new focus)

**Decision-Making Process:**
- Technical decisions: Majority vote after trying both approaches in prototype
- Scope cuts: Unanimous agreement required
- Urgent issues: Any team member can make call, document rationale

### Risk Mitigation Plan (Team-Level)

**Risk:** Team member 2 unavailable during midterms (Week 9)

**Mitigation:**
- Frontload all critical work to Week 5-8
- Cross-train team members 1 & 3 on frontend (Week 5)
- Schedule buffer time in Week 9 (only non-blocking tasks)
- Team member 2 can contribute documentation/testing during Week 9

**Early Warning Signs:**
- Team member 2 missing 2+ meetings in a row
- Declining code contributions
- Not responding to Slack within 24 hours

**Escalation Plan:**
- Week 1 of absence: Friendly check-in
- Week 2 of absence: Team meeting to redistribute work
- Week 3 of absence: Contact instructor, formally adjust scope

---

## 10. Summary: Key Changes Since Week 2

### Problem & Solution
- ✅ **Narrowed target user** from "all small businesses" to "freelancers with <$100K revenue"
- ✅ **Validated problem** with 6 user interviews
- ✅ **Refined solution** to focus on MVP features only

### Technical Architecture
- ✅ **Switched Flask → FastAPI** for async support
- ✅ **Switched MongoDB → PostgreSQL** for relational data
- ✅ **Added GPT-4o-mini** for 80% of queries (cost optimization)
- ✅ **Added Cloudinary** for image storage
- ✅ **Deployed prototype** to Railway (staging environment)

### Success Metrics
- ✅ **Added specific targets** (>70% completion, <3s latency, >4.0/5.0 satisfaction)
- ✅ **Baseline measurements** from Week 3-4 testing
- ✅ **Cost tracking** ($0.013/query current, targeting <$0.05)

### Risk Management
- ✅ **Identified 5 new risks** from prototyping experience
- ✅ **Implemented cost controls** (dashboard, rate limiting)
- ✅ **Created mitigation roadmap** with weekly milestones

### Scope Adjustments
- ❌ **Removed RAG** from MVP (not essential, can add later)
- ❌ **Removed batch upload** (nice-to-have, cut if needed)
- ✅ **Kept core extraction + categorization** (essential)

### Team Dynamics
- ✅ **Realistic velocity** (~37 hours/week team capacity)
- ✅ **Cross-training plan** to mitigate availability risks
- ✅ **Adjusted meeting schedule** (3x/week → 2x/week)

---

## 📊 Appendix

### A. Technology Research Summary

**Why FastAPI over Flask?**
- Researched: Compared performance benchmarks, async capabilities, type safety
- Decision: FastAPI chosen for async support (needed for streaming) and automatic API docs
- Source: [Links to research]

**Why PostgreSQL over MongoDB?**
- Researched: Data model analysis, consistency requirements, query patterns
- Decision: Relational structure fits our data (users → receipts → categories)
- Source: [Links to research]

### B. User Interview Notes Summary

**Participant 1 (Freelance Designer):**
- Pain point: "I lose receipts all the time. Usually find them at tax time, crumpled in my bag."
- Need: "I just want to take a photo and forget about it until quarterly taxes."
- Would pay: "$10/month if it saves me 2+ hours"

**Participant 2 (Small Business Owner - Landscaping):**
- Pain point: "I'm terrible at categorizing. Is fertilizer 'supplies' or 'materials'? I never know."
- Need: "Auto-categorization would be huge. Most of my receipts are the same 3 places."
- Would pay: "$15/month if it integrates with QuickBooks"

[Include summaries from all 6 interviews]

### C. Cost Calculation Details

**Current Cost Model (Week 4, No Optimization):**
```
GPT-4o (current):
- System prompt: 500 tokens × $0.0025/1K = $0.00125
- User query: 200 tokens × $0.0025/1K = $0.0005
- Output: 600 tokens × $0.01/1K = $0.006
- Total per query: $0.00775
- Monthly (1000 queries): $7.75
```

**Projected Cost (Week 6, With Optimization):**
```
80% GPT-4o-mini, 20% GPT-4o:
- Mini (800 queries): 800 × $0.0002 = $0.16
- Full (200 queries): 200 × $0.003 = $0.60
- Total monthly: $0.76 (90% reduction!)
```

### D. Architecture Diagrams

[Include detailed diagrams here]

### E. Week 3-4 Prototype Screenshots

[Include screenshots showing current state of app]

---

**Document Version:** 2.0  
**Last Updated:** [Date], Week 4  
**Next Review:** Week 7 (after user testing)

---

## ✅ Review Checklist

Before submitting, verify:

- [ ] All sections updated from Week 2 version
- [ ] Specific changes documented with rationale
- [ ] Measurable success metrics with targets
- [ ] Architecture diagram included and explained
- [ ] All known risks documented with mitigation plans
- [ ] Realistic timeline based on Week 3-4 velocity
- [ ] Team health assessment completed
- [ ] All team members reviewed and approved
- [ ] Proofread for typos and clarity
- [ ] Links and references verified
