# Grading Checklist - Week 6 & 7 Combined Homework

**Team Name:** [Your Team Name Here]  
**Project Title:** [Your Capstone Project Title]  
**Submission Date:** [Date of Submission]  
**Team Members:** [Name 1, Name 2, Name 3 (if applicable)]

---

## Part A: Week 6 - Function Calling Implementation (110 points)

### 1. Functions Implementation (40 points)

**Functions Implemented:**
- [ ] **Function 1 Name:** `[function_name_1]`
  - **Location:** [Direct GitHub link to file, e.g., `src/functions/tools.py#L10-L25`]
  - **Purpose:** [Brief description]
  - **Input:** [Input type/schema]
  - **Output:** [Output type/schema]

- [ ] **Function 2 Name:** `[function_name_2]`
  - **Location:** [Direct GitHub link to file]
  - **Purpose:** [Brief description]
  - **Input:** [Input type/schema]
  - **Output:** [Output type/schema]

- [ ] **Function 3 Name (if applicable):** `[function_name_3]`
  - **Location:** [Direct GitHub link to file]
  - **Purpose:** [Brief description]
  - **Input:** [Input type/schema]
  - **Output:** [Output type/schema]

**Supporting Files:**
- [ ] **Pydantic Models:** [Direct link to `src/models/function_models.py`]
- [ ] **JSON Schemas:** [Direct link to schema definitions]
- [ ] **Agent/Orchestration:** [Direct link to `src/ai/agent.py`]

**Quick Navigation:**
- Functions code: [Direct link]
- Models code: [Direct link]
- Agent code: [Direct link]

**Status Notes:**
[Add any notes about implementation status, known issues, or special considerations]

---

### 2. Tests & Demo Video (30 points)

#### Test Suite (20 points)
- [ ] **Test File Location:** [Direct link to `tests/test_functions.py`]
- [ ] **Test Coverage:**
  - Function 1: [X] tests implemented
  - Function 2: [X] tests implemented
  - Function 3: [X] tests implemented (if applicable)
  - Pydantic validation: [X] tests
  - End-to-end LLM: [X] tests

- [ ] **All Tests Passing:** ✅ Yes / ❌ No (if no, explain below)

**Test Results Evidence:**
- Screenshot/log showing tests passing: [Direct link to image in `docs/evidence/` or describe]
- Command used: `[e.g., python -m pytest tests/ -v]`

**If tests are not all passing:**
[Explain which tests are failing and why, or remove this section if all passing]

#### Demo Video (10 points)
- [ ] **Video Link:** [YouTube/Google Drive URL]
- [ ] **Video Duration:** [X minutes, X seconds]
- [ ] **Video Shows:**
  - ✅ System running
  - ✅ User asking questions
  - ✅ AI calling functions
  - ✅ AI responding with results
  - ✅ Multiple scenarios (at least 2-3)
  - ✅ Error handling demonstration

**Video Description:**
[Brief 2-3 sentence summary of what the video demonstrates]

---

### 3. Documentation & Code Quality (20 points)

#### README Update (5 points)
- [ ] **Week 6 Section Location:** [Direct link to README section, e.g., `README.md#week-6-function-calling`]
- [ ] **Documentation Includes:**
  - ✅ All functions listed
  - ✅ Input/output specifications
  - ✅ Use case descriptions
  - ✅ Usage examples

#### Docstrings (5 points)
- [ ] **All functions have docstrings:** ✅ Yes / ❌ No
- [ ] **Docstrings include:**
  - ✅ Function purpose
  - ✅ Parameter descriptions
  - ✅ Return value description
  - ✅ Example usage (where appropriate)

#### Type Hints (5 points)
- [ ] **Type hints present on all:**
  - ✅ Function parameters
  - ✅ Return types
  - ✅ Pydantic model fields

#### Error Handling (3 points)
- [ ] **Error handling implemented for:**
  - ✅ Invalid function inputs
  - ✅ API failures
  - ✅ Validation errors
  - ✅ Unexpected LLM responses
- [ ] **User-facing error messages:** ✅ Clear and helpful / ❌ Needs improvement

#### Security (2 points)
- [ ] **No hard-coded API keys:** ✅ Confirmed
- [ ] **Environment variables used:** ✅ Yes (via `.env`)
- [ ] **`.env.example` exists:** ✅ Yes - [Direct link]
- [ ] **`.env` in `.gitignore`:** ✅ Confirmed - [Direct link to `.gitignore#LX`]

---

### 4. GitHub Commits (10 points)

#### Commit Quality (8 points)
- [ ] **Example commit messages:**
  1. `[Most recent commit message]` - [link to commit]
  2. `[Another meaningful commit]` - [link to commit]
  3. `[Another meaningful commit]` - [link to commit]

- [ ] **Commits are descriptive:** ✅ Yes / ❌ Needs improvement
- [ ] **Commits follow conventions:** ✅ Yes (e.g., `feat:`, `fix:`, `docs:`)

#### Security (2 points)
- [ ] **Verified `.env` NOT in repository:** ✅ Confirmed
- [ ] **No secrets in commit history:** ✅ Confirmed
- [ ] **If secrets were accidentally committed:** [Explain remediation steps taken, or remove if N/A]

#### Repository Status
- [ ] **All files pushed to `main` branch:** ✅ Yes
- [ ] **Latest commit hash:** `[commit hash]` - [link]
- [ ] **Last push date/time:** [Date and time]

---

### 5. Evaluation & Safety Logs (10 points)

**All logs located in:** `course-pack/labs/lab-6/`

#### Evaluation Notes (4 points)
- [ ] **File:** [Direct link to `course-pack/labs/lab-6/evaluation_notes.md`]
- [ ] **Contains:**
  - ✅ Average latency measurements
  - ✅ 3-5 input/output test results
  - ✅ Performance observations
  - ✅ Comparison to expectations

**Key Finding:** [One-sentence summary of most important evaluation finding]

#### Safety Checklist (3 points)
- [ ] **File:** [Direct link to `course-pack/labs/lab-6/safety_checklist.md`]
- [ ] **Confirmed:**
  - ✅ API keys removed/secured
  - ✅ No personal/private data exposed
  - ✅ Strange inputs handled safely
  - ✅ Fallback for unsafe model outputs

**Safety Status:** ✅ All items addressed / ⚠️ [List any concerns]

#### AI Use Log (2 points)
- [ ] **File:** [Direct link to `course-pack/labs/lab-6/ai_use_log.md`]
- [ ] **Tools used:**
  - [List AI tools: ChatGPT, Claude, Cursor, GitHub Copilot, etc.]
  - [Brief description of how each was used]

#### Capstone Link (1 point)
- [ ] **File:** [Direct link to `course-pack/labs/lab-6/capstone_link.md`]
- [ ] **Contains:**
  - ✅ Which function(s) will be reused
  - ✅ Improvement plan for next week

---

## Part B: Week 7 - Design Review (5 points)

### Main Documents

#### Design Review Document
- [ ] **File:** [Direct link to `docs/design-review-week7.md`]
- [ ] **Page count:** [X pages, target: 6-10]
- [ ] **Last updated:** [Date]

#### Event Schemas
- [ ] **File:** [Direct link to `docs/event-schemas.md`]
- [ ] **Number of schemas defined:** [X schemas]

#### Architecture Diagram
- [ ] **File:** [Direct link to `docs/architecture-week7.png` or `.pdf`]
- [ ] **Format:** [PNG/PDF/SVG]
- [ ] **Last updated:** [Date]

#### Evidence Folder
- [ ] **Location:** [Direct link to `docs/evidence/`]
- [ ] **Contains:**
  - [List key files: logs, screenshots, measurements, etc.]

#### README Update
- [ ] **Link to design review:** [Direct link to README section]
- [ ] **Architectural changes noted:** ✅ Yes / ❌ No changes since Week 2

---

### Design Review Sections (Check all 6 completed)

#### Section 1: Architecture Validation (1.0 point) [1-2 pages]
- [ ] **Status:** ✅ Complete / ⏳ In Progress / ❌ Incomplete
- [ ] **Contents:**
  - ✅ Updated architecture diagram embedded
  - ✅ Component descriptions with specific tech choices
  - ✅ Data flow diagram showing event movement
  - ✅ Explanation of changes from Week 2 proposal

**Key Changes from Week 2:**
[Brief summary of main architectural changes, or "No major changes"]

#### Section 2: Event Schema Documentation (1.5 points) [2-3 pages]
- [ ] **Status:** ✅ Complete / ⏳ In Progress / ❌ Incomplete
- [ ] **Schemas Documented:**
  - ✅ User input event
  - ✅ LLM request event
  - ✅ LLM response event
  - ✅ Error event
  - ✅ [If RAG] Document retrieval event
  - ✅ [If functions] Tool call & result events
  - ✅ [Other relevant events]

**Total Schemas:** [X schemas]

**Schema Quality:**
- ✅ JSON Schema format used
- ✅ All fields have descriptions and types
- ✅ Validation rules specified
- ✅ Example instances provided

#### Section 3: Smoke Test Results (1.0 point) [1-2 pages]
- [ ] **Status:** ✅ Complete / ⏳ In Progress / ❌ Incomplete
- [ ] **Smoke Test Checklist:** [Direct link to completed checklist]
- [ ] **Results Summary:**
  - ✅ Passed: [X/Y tests]
  - ⚠️ Failed: [X/Y tests]
  - 📋 Mitigation plans for failures: [✅ Yes / ❌ No]

**Critical Tests Status:**
- End-to-end request/response: ✅ PASS / ❌ FAIL
- Error handling: ✅ PASS / ❌ FAIL
- Performance acceptable (<5s p95): ✅ PASS / ❌ FAIL
- Cost tracking: ✅ PASS / ❌ FAIL
- Structured logs: ✅ PASS / ❌ FAIL

**Evidence Location:**
[Direct link to logs/screenshots in `docs/evidence/`]

#### Section 4: Performance Baseline (0.75 points) [1 page]
- [ ] **Status:** ✅ Complete / ⏳ In Progress / ❌ Incomplete
- [ ] **Measurements Completed:**
  - ✅ Latency (p50, p95, p99)
  - ✅ Token usage analysis
  - ✅ Cost per request
  - ✅ Bottleneck identification

**Performance Summary:**
- **p50 latency:** [X.X seconds]
- **p95 latency:** [X.X seconds]
- **p99 latency:** [X.X seconds]
- **Average cost per request:** [$X.XX]
- **Primary bottleneck:** [e.g., Database query, LLM call, etc.]

**Evidence Location:**
[Direct link to performance data in `docs/evidence/`]

#### Section 5: Hypothesis Validation (0.5 points) [1-2 pages]
- [ ] **Status:** ✅ Complete / ⏳ In Progress / ❌ Incomplete
- [ ] **Hypothesis Tested:** "[State your hypothesis]"
- [ ] **Methodology:** [Brief description]
- [ ] **Results:** [Quantitative data summary]
- [ ] **Conclusion:** [Hypothesis supported? What changes?]

**Key Finding:**
[One-sentence summary of validation result]

#### Section 6: Readiness Assessment (0.25 points) [1 page]
- [ ] **Status:** ✅ Complete / ⏳ In Progress / ❌ Incomplete
- [ ] **Assessment Questions Answered:**
  - ✅ Can system handle 5-20x more API calls?
  - ✅ Are error handlers robust for agent loops?
  - ✅ Is cost model sustainable at scale?
  - ✅ What must be fixed before Week 8?

**Action Plan:**
- [ ] **Action plan table created:** ✅ Yes
- [ ] **Action items assigned:** ✅ Yes
- [ ] **Deadlines set:** ✅ Yes

**Week 8 Readiness:** ✅ Ready / ⚠️ Ready with caveats / ❌ Not ready

---

## 🎯 Summary for Instructor

### Total Points: 115 (110 from Week 6 + 5 from Week 7)

### Quick Access Links (For Grader)

**Part A (Week 6):**
1. **Main functions:** [link]
2. **Test file:** [link]
3. **Demo video:** [link]
4. **Lab 6 logs folder:** [link]

**Part B (Week 7):**
1. **Design review document:** [link]
2. **Event schemas:** [link]
3. **Architecture diagram:** [link]
4. **Evidence folder:** [link]

### What's Working Well
[Provide 2-3 bullet points highlighting your strongest areas]
- 
- 
- 

### Known Issues / In Progress
[List any incomplete items or known problems]
- 
- 
- 

### Questions for Grader
[Any specific areas where you want feedback or have questions]
- 
- 
- 

### Time Spent on Assignment
- **Part A (Week 6):** Approximately [X] hours
- **Part B (Week 7):** Approximately [X] hours
- **Total:** Approximately [X] hours

---

## ✅ Pre-Submission Verification

Before submitting, verify these items:

### Final Checklist:
- [ ] This `GRADING_CHECKLIST.md` file is complete with all sections filled
- [ ] All direct links work (clicked through each one)
- [ ] Demo video plays correctly
- [ ] All tests pass locally
- [ ] No `.env` file in repository
- [ ] All team members reviewed and approved submission
- [ ] Repository URL ready to submit: `[your-repo-url]`
- [ ] Submitted before deadline: November 27th, 2025 at 11:59 PM

---

## 📝 Grader Notes Section

**[Leave this section blank - for instructor use only]**

---

**Submission Timestamp:** [Will be recorded upon submission]  
**Submitted By:** [Team member who submitted]  
**Repository URL:** [Your GitHub repo URL]
