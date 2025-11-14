# Week 6 & 7 Combined Homework: Function Calling + Design Review

**Building AI-Powered Applications | Due: November 27th, 2025 at 11:59 PM**

This is a **combined assignment** worth 115 points total that represents two major capstone milestones:
- **Week 6 Milestone:** Function Calling Implementation (110 points)
- **Week 7 Milestone:** Design Review & Architecture Validation (5 points)

These assignments build on each other—your Week 6 functions feed into your Week 7 architecture validation. Complete both parts to demonstrate your system is ready for agent orchestration (Week 8).

---

## 📋 Submission Checklist (REQUIRED)

**Before you submit, you MUST complete this grading checklist to help your instructor efficiently evaluate your work.**

Create a file called `GRADING_CHECKLIST.md` in the root of your repository with the following format:

```markdown
# Grading Checklist - Week 6 & 7 Combined Homework

**Team Name:** [Your Team Name]  
**Project Title:** [Your Capstone Project Title]  
**Submission Date:** [Date]  
**Team Members:** [Name 1, Name 2, Name 3]

## Part A: Week 6 - Function Calling (110 points)

### Functions Implementation (40 points)
- [ ] **Function 1:** [Name] - Located at: [path/to/file.py]
- [ ] **Function 2:** [Name] - Located at: [path/to/file.py]
- [ ] **Function 3 (if applicable):** [Name] - Located at: [path/to/file.py]
- [ ] Pydantic models defined at: [path/to/models.py]
- [ ] JSON schemas defined at: [path/to/schemas or agent.py]

**Quick Navigation:**
- Functions code: [Direct link to GitHub file]
- Models code: [Direct link to GitHub file]
- Agent/orchestration: [Direct link to GitHub file]

### Tests & Demo (30 points)
- [ ] Test file located at: [path/to/test_functions.py]
- [ ] All tests pass (screenshot/evidence at: [path or link])
- [ ] Demo video link: [YouTube/Drive URL]
- [ ] Demo video shows: ✅ AI calling functions ✅ Multiple scenarios ✅ Error handling

### Documentation & Code Quality (20 points)
- [ ] README updated with Week 6 section: [Direct link to section]
- [ ] All functions have docstrings: ✅ Yes / ❌ No
- [ ] Type hints present: ✅ Yes / ❌ No
- [ ] Error handling implemented: ✅ Yes / ❌ No
- [ ] No hard-coded API keys: ✅ Confirmed / ❌ Found issues

### GitHub (10 points)
- [ ] Descriptive commit messages used: ✅ Yes
- [ ] .env is NOT in repo: ✅ Confirmed
- [ ] .env.example exists: ✅ Yes
- [ ] All files pushed to main branch: ✅ Confirmed

### Evaluation & Safety Logs (10 points)
Located in: `course-pack/labs/lab-6/`
- [ ] `evaluation_notes.md`: [Direct link]
- [ ] `safety_checklist.md`: [Direct link]
- [ ] `ai_use_log.md`: [Direct link]
- [ ] `capstone_link.md`: [Direct link]

---

## Part B: Week 7 - Design Review (5 points)

### Main Documents
- [ ] Design Review Document: `docs/design-review-week7.md` - [Direct link]
- [ ] Event Schemas: `docs/event-schemas.md` - [Direct link]
- [ ] Updated Architecture Diagram: `docs/architecture-week7.[png/pdf]` - [Direct link]

### Design Review Sections Completed (check all 6)
- [ ] Section 1: Architecture Validation (1-2 pages)
- [ ] Section 2: Event Schema Documentation (2-3 pages)
- [ ] Section 3: Smoke Test Results (1-2 pages)
- [ ] Section 4: Performance Baseline (1 page)
- [ ] Section 5: Hypothesis Validation (1-2 pages)
- [ ] Section 6: Readiness Assessment (1 page)

### Evidence Folder
- [ ] Evidence folder exists at: `docs/evidence/`
- [ ] Contains: Logs, screenshots, performance data, validation results

### README Update
- [ ] README links to design review: [Direct link to README section]
- [ ] README notes architectural changes (if any): ✅ Yes / ❌ No changes

---

## Part A: Week 6 - Function Calling Implementation (110 points)

By the end of Week 6, your capstone must demonstrate working function calling with proper validation, error handling, and integration.

### 1. Function Implementations (40 points)

Create **2–3 functions** that are specific to your project and integrate them into your capstone. Each function must have clearly defined inputs and outputs, validated with Pydantic.

**Requirements:**
- ✅ Functions are specific to your project (not generic examples)
- ✅ Located in your capstone repository (not in lab folders)
- ✅ Pydantic models defined for all inputs and outputs
- ✅ JSON schemas correctly defined for the LLM
- ✅ Functions execute without errors (mock data OK for Week 6)
- ✅ AI successfully calls your functions in conversations

**Recommended File Structure:**
```
your-capstone-repo/
├── src/
│   ├── models/
│   │   └── function_models.py      # Pydantic models
│   ├── functions/
│   │   └── tools.py                # Function implementations
│   └── ai/
│       └── agent.py                # LLM orchestration
```

**Example Implementation:**

```python
# src/models/function_models.py
from pydantic import BaseModel, Field
from typing import List, Literal

class OrderLookupRequest(BaseModel):
    order_id: str = Field(description="Order ID (format: ORD-XXXXX)")

class OrderStatus(BaseModel):
    order_id: str
    status: Literal["pending", "shipped", "delivered"]
    tracking_number: str | None = None
    items: List[str]

# src/functions/tools.py
from ..models.function_models import OrderLookupRequest, OrderStatus

def lookup_order_status(order_id: str) -> OrderStatus:
    """Retrieve status for a given order ID."""
    # Mock implementation for Week 6
    return OrderStatus(
        order_id=order_id,
        status="shipped",
        tracking_number="TRACK-12345",
        items=["Product A", "Product B"]
    )
```

**Function Ideas by Project Type:**
- **Customer Support:** `lookup_order_status`, `calculate_refund`, `create_support_ticket`
- **Recipe App:** `search_recipes`, `get_recipe_details`, `save_to_favorites`
- **Study Assistant:** `search_course_materials`, `generate_quiz`, `track_progress`
- **Document Q&A:** `search_docs`, `get_document`, `summarize_section`

**Grading (40 points):**
- 15 pts: 2–3 functions implemented and working
- 10 pts: Pydantic models with proper validation
- 10 pts: Integrated into your capstone (not standalone files)
- 5 pts: Error handling present

---

### 2. Test Cases & Demo Video (30 points)

#### A. Test File (20 points)

Create `tests/test_functions.py` in your capstone repo with at least **three test cases per function**. Include tests for Pydantic validation and an end-to-end test using your LLM.

**Requirements:**
- ✅ At least 3 test cases per function
- ✅ Test for Pydantic validation (valid and invalid inputs)
- ✅ End-to-end test with the LLM
- ✅ All tests pass when run

**Example Test Structure:**
```python
import pytest
from src.functions.tools import lookup_order_status
from src.models.function_models import OrderStatus

def test_lookup_order_valid():
    """Test with valid order ID"""
    result = lookup_order_status("ORD-12345")
    assert isinstance(result, OrderStatus)
    assert result.order_id == "ORD-12345"

def test_lookup_order_invalid_format():
    """Test with invalid order ID format"""
    with pytest.raises(ValueError):
        lookup_order_status("INVALID")

def test_end_to_end_llm_function_call():
    """Test that LLM can successfully call the function"""
    # Your end-to-end test here
    pass
```

#### B. Demo Video (10 points)

Record a **2–3 minute video** showing:
1. Your capstone running
2. A user asking a question
3. The AI calling your function
4. The AI responding with the result
5. Two or three different scenarios

**Upload:** YouTube (unlisted) or Google Drive  
**Link:** Include in your `GRADING_CHECKLIST.md` and README

**Grading (30 points):**
- 20 pts: Comprehensive test cases that pass
- 10 pts: Demo video clearly shows functions working

---

### 3. Documentation & Code Quality (20 points)

Your code should be clean, well documented, and safe.

**Requirements:**
- ✅ README updated with a Week 6 section listing each function (name, input, output, use case)
- ✅ Docstrings on all functions
- ✅ Type hints present on all parameters and return types
- ✅ Error handling implemented with clear user-facing messages
- ✅ No hard-coded API keys (use environment variables)

**README Example:**
```markdown
## Week 6: Function Calling Implementation

### Implemented Functions

#### 1. `lookup_order_status`
- **Input:** `order_id` (string, format: ORD-XXXXX)
- **Output:** `OrderStatus` object with status, tracking number, items
- **Use Case:** Allows users to check their order status through natural language

#### 2. `calculate_refund`
- **Input:** `order_id` (string), `reason` (string)
- **Output:** `RefundCalculation` object with amount, processing time
- **Use Case:** Calculates refund amount based on order and return reason
```

**Grading (20 points):**
- 5 pts: README updated with function documentation
- 5 pts: Docstrings on all functions
- 5 pts: Type hints present
- 3 pts: Error handling implemented
- 2 pts: No hard-coded secrets

---

### 4. GitHub Commit (10 points)

Ensure your work is committed and pushed to your capstone repository with descriptive messages.

**Requirements:**
- ✅ Descriptive commit message (not just "update")
- ✅ All required files included
- ✅ `.env` is NOT committed (check `.gitignore`)
- ✅ Code pushed to the main branch

**Good Commit Message Examples:**
- ✅ `feat: implement order lookup and refund calculation functions`
- ✅ `test: add comprehensive test suite for function calling`
- ❌ `update` (too vague)
- ❌ `changes` (not descriptive)

**Grading (10 points):**
- 5 pts: All required files committed
- 3 pts: Descriptive commit message
- 2 pts: `.env` not in repo (security)

---

### 5. Evaluation & Safety Logs (10 points)

Create the following files in your `course-pack/labs/lab-6/` folder:

#### Required Files:

**`evaluation_notes.md`**
- Record average latency of your function calls
- Results from 3–5 simple input/output checks
- See `examples/evaluation-notes.md` for sample format

**`safety_checklist.md`**
- Confirm you removed API keys
- Avoided personal or private data
- Handled strange inputs safely
- Return fallback when model produces unsafe content

**`ai_use_log.md`**
- List any AI tools (ChatGPT, Claude, Cursor, etc.) you used
- Briefly describe how they helped you

**`capstone_link.md`**
- Explain which Lab 6 function you will reuse in your capstone
- What improvement you plan for next week

**Grading (10 points):**
- 4 pts: Complete and clear evaluation notes
- 3 pts: Safety checklist fully addressed
- 2 pts: AI use log filled out
- 1 pt: Capstone link written

---

## Part B: Week 7 - Design Review (5 points)

This is your **Design Review** milestone that validates your system is ready for agent orchestration (Week 8+). It builds directly on your Week 6 function implementations.

### Core Deliverable: `docs/design-review-week7.md`

Create this document with all 6 sections. Use the [Design Review Template](./templates/design-review-template.md) as your starting point.

#### Section 1: Architecture Validation (1 point) [1-2 pages]
- ✅ Updated architecture diagram (reflects actual implementation, not proposal)
- ✅ Component descriptions with specific technology choices
- ✅ Data flow diagram showing how events move through your system
- ✅ Explanation of any changes from your Week 2 proposal

#### Section 2: Event Schema Documentation (1.5 points) [2-3 pages]
- ✅ JSON schemas for ALL critical events in your system
- ✅ At minimum: user input, LLM request, LLM response, error events
- ✅ If applicable: RAG retrieval events, function call events, database events
- ✅ Clear field descriptions and type specifications
- ✅ Example instances for each schema

#### Section 3: Smoke Test Results (1 point) [1-2 pages]
- ✅ Completed [Smoke Test Checklist](./templates/smoke-test-checklist.md) (pass/fail for each item)
- ✅ Evidence for each test: logs, screenshots, measurements
- ✅ Failed items with mitigation plans
- ✅ Timeline for addressing gaps

#### Section 4: Performance Baseline (0.75 points) [1 page]
- ✅ Latency measurements (p50, p95, p99) for typical requests
- ✅ Token usage analysis (input tokens, output tokens, cost)
- ✅ Cost per request calculations with breakdown
- ✅ Bottleneck identification and optimization plan

#### Section 5: Hypothesis Validation (0.5 points) [1-2 pages]
- ✅ One core design assumption tested with real data
- ✅ Methodology: what you tested and how
- ✅ Results: quantitative data with analysis
- ✅ Implications: what you learned and what changes

#### Section 6: Readiness Assessment (0.25 points) [1 page]
- ✅ Can your system handle 5-20x more API calls? Analysis
- ✅ Are error handlers robust enough for agent loops?
- ✅ Is cost model sustainable at scale?
- ✅ What must be fixed before Week 8?
- ✅ Action plan with owners and deadlines

---

### Additional Required Files:

**`docs/event-schemas.md`**
- Separate file with all JSON schemas
- Well-formatted and documented
- Referenced from main document

**`docs/evidence/` folder**
- Logs from smoke test runs
- Performance measurement screenshots
- Hypothesis validation data
- Any supporting materials

**`docs/architecture-week7.png` (or .pdf)**
- Reflects actual implementation
- Shows event flows
- Labels all components

**Updated README:**
- Link to design review document
- Note any architectural changes since Week 2

---

### Event Schema Example (What Good Looks Like):

```json
// docs/event-schemas.md

## Function Call Event Schema

{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["function_name", "arguments", "timestamp"],
  "properties": {
    "function_name": {
      "type": "string",
      "description": "Name of the function being called",
      "enum": ["lookup_order_status", "calculate_refund", "create_ticket"]
    },
    "arguments": {
      "type": "object",
      "description": "Function-specific arguments passed to the call"
    },
    "timestamp": {
      "type": "string",
      "format": "date-time",
      "description": "ISO 8601 timestamp of when function was called"
    },
    "user_id": {
      "type": "string",
      "description": "Identifier of the user who initiated the call"
    }
  }
}

### Example Instance:
{
  "function_name": "lookup_order_status",
  "arguments": {
    "order_id": "ORD-12345"
  },
  "timestamp": "2025-11-20T14:30:00Z",
  "user_id": "user-789"
}
```

---

### Performance Baseline Example (What Good Looks Like):

```markdown
## Performance Baseline - Week 7

### Test Methodology
- Ran 25 typical requests through the system
- Measured end-to-end latency from user input to final response
- Tracked token usage for each request
- Calculated costs based on OpenAI pricing

### Latency Results
| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| p50 (median) | 2.1s | <3s | ✅ PASS |
| p95 | 4.8s | <5s | ✅ PASS |
| p99 | 6.2s | <8s | ✅ PASS |

### Token Usage
- Average Input Tokens: 420
- Average Output Tokens: 180
- Average Total Tokens: 600

### Cost Analysis
- Cost per request: $0.018
- Projected cost for 100 users/day: $1.80/day = $54/month
- Projected cost for 1000 users/day: $18/day = $540/month

### Bottleneck Analysis
**Slowest Component:** Database query for RAG retrieval (1.8s average)
**Optimization Plan:** Add Redis caching layer for common queries (target: reduce to 0.3s)
```

---

## 🚚 Submission Instructions

### Before You Submit - Final Checklist

#### Part A (Week 6) Files:
- [ ] `src/models/function_models.py` exists
- [ ] `src/functions/tools.py` exists
- [ ] `src/ai/agent.py` exists
- [ ] `tests/test_functions.py` exists
- [ ] README.md updated with Week 6 section
- [ ] `.env.example` exists (no real keys!)
- [ ] `.env` is in `.gitignore`
- [ ] `course-pack/labs/lab-6/evaluation_notes.md`
- [ ] `course-pack/labs/lab-6/safety_checklist.md`
- [ ] `course-pack/labs/lab-6/ai_use_log.md`
- [ ] `course-pack/labs/lab-6/capstone_link.md`

#### Part B (Week 7) Files:
- [ ] `docs/design-review-week7.md` exists (6-10 pages)
- [ ] `docs/event-schemas.md` exists
- [ ] `docs/evidence/` folder with files
- [ ] `docs/architecture-week7.png` (or .pdf) exists
- [ ] README links to design review

#### Required for Both:
- [ ] **`GRADING_CHECKLIST.md` in root directory** (MUST HAVE!)
- [ ] All sections filled out with direct links
- [ ] Demo video uploaded and linked
- [ ] All tests pass (`python -m pytest tests/`)
- [ ] No hard-coded secrets in code

### How to Submit

**1. Push to GitHub:**
```bash
git add .
git commit -m "feat: complete week 6 & 7 combined homework - function calling + design review"
git push origin main
```

**2. Verify on GitHub:**
- Go to your repo on GitHub.com
- Check all files are there
- Verify `.env` is NOT visible
- Click through links in your `GRADING_CHECKLIST.md` to ensure they work

**3. Submit via Course System:**
- **Repository URL:** `https://github.com/username/capstone-project`
- **Demo Video:** [YouTube/Drive link]
- **Team:** [Member names]
- **Project:** [Project title]
- **Notes:** [Any special notes for grader]

**Deadline:** November 27th, 2025 at 11:59 PM

---

## 📊 Grading Rubric (115 Points Total)

### Part A: Week 6 - Function Calling (110 points)

| Component | Points | Criteria |
|-----------|--------|----------|
| **Functions** | 40 | 2–3 working functions with Pydantic, integrated into capstone |
| **Tests & Demo** | 30 | Test suite passes, demo video shows functions working |
| **Code Quality** | 20 | Docstrings, type hints, error handling, no secrets |
| **GitHub** | 10 | Descriptive commit, all files included, pushed properly |
| **Logs & Safety** | 10 | Evaluation notes, safety checklist, AI use log, capstone link |

### Part B: Week 7 - Design Review (5 points)

| Component | Points | Criteria |
|-----------|--------|----------|
| **Architecture Validation** | 1.0 | Diagram clarity, completeness, accuracy |
| **Event Schemas** | 1.5 | Completeness, correctness, documentation quality |
| **Smoke Test** | 1.0 | Evidence provided, gaps identified, mitigation plans |
| **Performance Baseline** | 0.75 | Measurements complete, analysis sound |
| **Hypothesis Validation** | 0.5 | Clear methodology, quantitative results |
| **Readiness Assessment** | 0.25 | Honest, actionable, realistic plan |

### Deductions:

**Late Penalties:**
- 1 day late: −10%
- 2 days late: −20%
- 3 days late: −30%
- After 3 days: Requires instructor approval

**Quality Issues:**
- Code doesn't run: −20 points
- API keys in repo: −10 points
- Functions not in capstone: −20 points
- No tests: −10 points
- No demo video: −10 points
- Missing `GRADING_CHECKLIST.md`: −5 points
- Incomplete design review: −5 points per missing section

---

## ❓ FAQ

### General Questions

**Q: Can I use examples from lecture?**  
A: Yes, but adapt them to your project. Don't submit generic examples.

**Q: Do I need real database integration?**  
A: Not yet. Mock data is fine for Week 6.

**Q: What if I only have 2 functions?**  
A: That's fine if they're substantial and working well.

**Q: Can I use Claude instead of OpenAI?**  
A: Yes, but adapt the function calling syntax accordingly.

**Q: How long should the demo video be?**  
A: 2–3 minutes. Just show it working—no need for fancy editing.

**Q: Can I submit late?**  
A: Up to 3 days with deductions. After that you need instructor approval.

### Design Review Questions

**Q: Is this just copying my Week 2 proposal?**  
A: No! This should reflect your ACTUAL implementation, not your proposal.

**Q: What if my architecture changed since Week 2?**  
A: That's normal and expected. Document what changed and why.

**Q: Do I need to fix everything before submitting?**  
A: No, but you must identify issues and have a realistic plan to fix them.

**Q: What if something doesn't work yet?**  
A: Be honest! That's what this checkpoint is for. Better to identify problems now.

**Q: How detailed should the event schemas be?**  
A: Very detailed. Every field needs a type, description, and validation rules.

### Team Questions

**Q: What if my teammate isn't helping?**  
A: Document attempts to contact them. Continue solo if needed; this will be considered in peer reviews.

**Q: Can we split the work?**  
A: Yes, but everyone should understand all parts. Use your `GRADING_CHECKLIST.md` to coordinate.

**Q: Where do I get help?**  
A: Resources in this repository, office hours, or email instructor.

---

## 💡 Tips for Success

### For Week 6 (Functions):

1. **Start with one function** that works perfectly, then add more
2. **Test incrementally** - don't wait until the end
3. **Use print statements** to debug function calling
4. **Mock data is OK** - you don't need real databases yet
5. **Record your demo early** - it often reveals bugs

### For Week 7 (Design Review):

1. **Be honest about problems** - this is a checkpoint, not a final exam
2. **Use real measurements** - "system is fast" is meaningless without data
3. **Start the smoke test early** - it often reveals issues
4. **Document as you go** - don't try to remember everything at the end
5. **Ask questions** - stuck on schemas? Not sure how to measure? Ask!

### For Both:

1. **Fill out `GRADING_CHECKLIST.md` first** - it helps you organize
2. **Use direct GitHub links** - makes grading much faster
3. **Commit frequently** with descriptive messages
4. **Test from a fresh clone** - if your teammate can't run it, neither can the grader
5. **Read the rubric carefully** - it tells you exactly what we're looking for

---

## 🎯 What Happens Next

### Week 9: Agent Orchestration Lab (November 28th, 2025
With validated foundations, you'll implement:
- ReAct agent loops
- Multi-tool orchestration
- Retry and fallback logic
- Production-grade error handling
- Automation

Your Week 6 functions become the tools your agents use!

### Week 9: Midterm Exam
Covers material from Weeks 1-7, including:


---

## 📚 Resources & Templates

### Week 6 Resources:
- [Function Examples](./examples/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [OpenAI Function Calling Guide](https://platform.openai.com/docs/guides/function-calling)

### Week 7 Resources:
- [Design Review Template](./templates/design-review-template.md)
- [Smoke Test Checklist](./templates/smoke-test-checklist.md)
- [Event Schema Examples](./examples/event-schemas.md)

### Help & Support:
- **Office Hours:** Check course calendar
- **Forum:** Post technical questions with error logs
- **Email:** Zeshan.ahmad@kiu.edu.ge (24-hour response weekdays)

---

## 🎓 Final Note

This combined assignment is **not busy work**. These are genuine forcing functions:

- **Week 6** ensures you can build working AI functions
- **Week 7** validates your system can handle the complexity ahead

Teams that take both seriously ship better capstones. Teams that rush through struggle in Weeks 8-15.

**Invest the time. Be thorough. Be honest. Build something robust.**

Good luck! 🚀
