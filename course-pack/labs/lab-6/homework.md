# Week 6 Homework: Function Calling Implementation

**Building AI‑Powered Applications | Due: End of Week 6**

Implement function calling and structured outputs into your capstone project. This is a **project milestone**—your AI must be able to take real actions by Friday.

**Points:** 10 (Project milestone)  
**Due:** Friday, Friday November 13th 23:59  
**Submission:** GitHub repo URL + demo video link

---

## 📌 What You’re Building

By the end of Week 6, your capstone must have:

- ✅ 2–3 working functions the AI can call
- ✅ Pydantic models validating all inputs/outputs
- ✅ Multi‑turn conversations with tool usage
- ✅ Error handling for function failures
- ✅ Code committed to GitHub

---

## 📦 Required Deliverables

### 1. Function Implementations (40 points)

Create 2–3 functions that are specific to **your** project—not generic examples—and integrate them into your capstone. Each function must have clearly defined inputs and outputs, validated with Pydantic.

**Requirements:**

- [ ] Functions are specific to your project
- [ ] Located in your capstone repository (not in this lab folder)
- [ ] Pydantic models defined for all inputs and outputs
- [ ] JSON schemas correctly defined for the LLM
- [ ] Functions execute without errors (mock data OK for Week 6)
- [ ] AI successfully calls your functions in conversations

**Where to put it:**

```
your‑capstone‑repo/
├── src/
│   ├── models/
│   │   └── function_models.py      # Pydantic models
│   ├── functions/
│   │   └── tools.py                # Function implementations
│   └── ai/
│       └── agent.py                # LLM orchestration
```

**Example models and function:**

```python
# src/models/function_models.py
from pydantic import BaseModel, Field
from typing import List, Literal

class OrderLookupRequest(BaseModel):
    order_id: str = Field(description="Order ID (format: ORD‑XXXXX)")

class OrderStatus(BaseModel):
    order_id: str
    status: Literal["pending", "shipped", "delivered"]
    tracking_number: str | None = None
    items: List[str]

# src/functions/tools.py
from ..models.function_models import OrderLookupRequest, OrderStatus

def lookup_order_status(order_id: str) -> OrderStatus:
    """Retrieve status for a given order ID."""
    return OrderStatus(order_id=order_id, status="shipped", items=["Product A", "Product B"])
```

**Function ideas by project type:**

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

Create `tests/test_functions.py` in your capstone repo with at least three test cases per function. Include tests for Pydantic validation and an end‑to‑end test using your LLM.

**Requirements:**

- [ ] At least 3 test cases per function
- [ ] Test for Pydantic validation
- [ ] End‑to‑end test with the LLM
- [ ] All tests pass when run

#### B. Demo Video (10 points)

Record a 2–3 minute video showing:

1. Your capstone running
2. A user asking a question
3. The AI calling your function
4. The AI responding with the result
5. Two or three different scenarios

Upload the video to YouTube (unlisted) or Google Drive and link it in your README.

**Grading (30 points):**

- 20 pts: Comprehensive test cases that pass
- 10 pts: Demo video clearly shows functions working

---

### 3. Documentation & Code Quality (20 points)

Your code should be clean, well documented and safe. Include docstrings and type hints, implement error handling, and avoid hard‑coded secrets.

**Requirements:**

- [ ] README updated with a Week 6 section listing each implemented function (name, input, output, use case)
- [ ] Docstrings on all functions
- [ ] Type hints present on all parameters and return types
- [ ] Error handling implemented with clear user‑facing messages
- [ ] No hard‑coded API keys (use environment variables)

**Grading (20 points):**

- 5 pts: README updated with function docs
- 5 pts: Docstrings on all functions
- 5 pts: Type hints present
- 3 pts: Error handling implemented
- 2 pts: No hard‑coded secrets

---

### 4. GitHub Commit (10 points)

Make sure your work is committed and pushed to your capstone repository with a descriptive message. Do not commit your actual `.env` file—use `.env.example` instead and ensure `.env` is listed in `.gitignore`.

**Requirements:**

- [ ] Descriptive commit message (not just “update”)
- [ ] All required files included
- [ ] `.env` is NOT committed (check `.gitignore`)
- [ ] Code pushed to the main branch

**Grading (10 points):**

- 5 pts: All required files committed
- 3 pts: Descriptive commit message
- 2 pts: `.env` not in repo (security)

---

### 5. Evaluation & Safety Logs (10 points)

Create the following files in your `course‑pack/labs/lab‑6/` folder and commit them along with your lab. These logs demonstrate that you tested your functions, considered safety and connected your work to your capstone.

- **`evaluation_notes.md`** – Record average latency of your function calls and results from 3–5 simple input/output checks. See `examples/evaluation-notes.md` for a sample format.
- **`safety_checklist.md`** – Confirm you removed API keys, avoided personal or private data, handled strange inputs safely and return a fallback when the model produces unsafe content.
- **`ai_use_log.md`** – List any AI tools (ChatGPT, Claude, Cursor, etc.) you used during this lab and briefly describe how they helped you.
- **`capstone_link.md`** – Explain which Lab 6 function you will reuse in your capstone and what improvement you plan next week.

**Grading (10 points):**

- 4 pts: Complete and clear evaluation notes
- 3 pts: Safety checklist fully addressed
- 2 pts: AI use log filled
- 1 pt: Capstone link written

---

## 🚚 Submission Instructions

### Before You Submit

#### Files checklist

- [ ] `src/models/function_models.py` exists
- [ ] `src/functions/tools.py` exists
- [ ] `src/ai/agent.py` exists
- [ ] `tests/test_functions.py` exists
- [ ] `README.md` updated with Week 6 section
- [ ] `.env.example` exists (no real keys!)
- [ ] `.env` is in `.gitignore`
- [ ] `evaluation_notes.md`, `safety_checklist.md`, `ai_use_log.md` and `capstone_link.md` exist in this lab folder

#### Functionality checklist

- [ ] 2–3 functions work
- [ ] LLM calls functions successfully
- [ ] All tests pass (`python -m pytest tests/`)
- [ ] Demo video shows it working
- [ ] No hard‑coded secrets

#### Quality checklist

- [ ] Docstrings on all functions
- [ ] Type hints present
- [ ] Error handling implemented
- [ ] Code follows Python conventions

### How to Submit

1. **Push to GitHub:**
   ```bash
   git push origin main
   ```

2. **Verify on GitHub:**
   - Go to your repo on GitHub.com
   - Check all files are there
   - Verify `.env` is NOT visible

3. **Submit via course system:**
   ```
   Repository URL: https://github.com/username/capstone-project
   Demo Video: [YouTube/Drive link]
   Team: [Member names]
   Project: [Project title]
   Notes: [Any special notes for grader]
   ```

---

## 📊 Grading Rubric

| Component | Points | Criteria |
|-----------|--------|---------|
| **Functions** | 40 | 2–3 working functions with Pydantic, integrated into capstone |
| **Tests & Demo** | 30 | Test suite passes, demo video shows functions working |
| **Code Quality** | 20 | Docstrings, type hints, error handling, no secrets |
| **GitHub** | 10 | Descriptive commit, all files included, pushed properly |
| **Logs & Safety** | 10 | evaluation notes, safety checklist, AI use log, capstone link |
| **Total** | **110** | |

**Deductions:**

- Late (1 day): −10%
- Late (2 days): −20%
- Late (3 days): −30%
- After 3 days: Requires instructor approval
- Code doesn’t run: −20%
- API keys in repo: −10%
- Functions not in capstone: −20%
- No tests: −10%
- No demo video: −10%

---

## ❓ Common Questions

**Q: Can I use examples from lecture?**  
A: Yes, but adapt them to **your** project. Don’t submit generic examples.

**Q: Do I need real database integration?**  
A: Not yet. Mock data is fine for Week 6.

**Q: What if I only have 2 functions?**  
A: That’s fine. Just make sure they’re substantial and working.

**Q: Can I use Claude instead of OpenAI?**  
A: Yes, but adapt the function calling syntax accordingly.

**Q: How long should the demo video be?**  
A: 2–3 minutes. Just show it working.

**Q: Can I submit late?**  
A: Up to 3 days with deductions. After that you need approval.

**Q: What if my teammate isn’t helping?**  
A: Document attempts to contact them. Continue solo if needed; this will be considered in peer reviews.

**Q: Where do I get help?**  
A: See the resources and guides in this repository or contact the instructor.
