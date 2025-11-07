# Week 6 Homework: Function Calling Implementation

**Building AI-Powered Applications | Due: End of Week 6**

Implement function calling and structured outputs into your capstone project. This is a **project milestone** - your AI must be able to take real actions by Friday.

**Points:** 10 (Project Milestone)  
**Due:** Friday, Week 6, 11:59 PM  
**Submission:** GitHub repo URL + demo video link

---

## 🎯 What You're Building

By end of Week 6, your capstone must have:
- ✅ 2-3 working functions the AI can call
- ✅ Pydantic models validating all inputs/outputs
- ✅ Multi-turn conversations with tool usage
- ✅ Error handling for function failures
- ✅ Code committed to GitHub

---

## 📋 Required Deliverables

### 1. Function Implementations (40 points)

**What:** 2-3 functions integrated into your capstone project.

**Requirements:**
- [ ] Functions are specific to YOUR project (not generic examples)
- [ ] Located in your capstone repository (not lab folder)
- [ ] Pydantic models for all inputs and outputs
- [ ] JSON schemas correctly defined for LLM
- [ ] Functions execute without errors (mock data OK for Week 6)
- [ ] AI successfully calls functions in conversations

**Where to put it:**
```
your-capstone-repo/
├── src/
│   ├── models/
│   │   └── function_models.py      # Pydantic models
│   ├── functions/
│   │   └── tools.py                # Function implementations
│   └── ai/
│       └── agent.py                # LLM integration
```

**Example structure:**
```python
# src/models/function_models.py
from pydantic import BaseModel, Field
from typing import Literal

class FunctionInput(BaseModel):
    """Input parameters for your function"""
    param1: str = Field(description="What this parameter does")
    param2: int = Field(ge=0, description="Must be positive")

class FunctionOutput(BaseModel):
    """Response from your function"""
    result: str
    success: bool
    data: dict | None = None
```

```python
# src/functions/tools.py
from ..models.function_models import FunctionInput, FunctionOutput

def your_function(param1: str, param2: int) -> FunctionOutput:
    """
    What this function does.
    
    Args:
        param1: Description
        param2: Description
        
    Returns:
        FunctionOutput with results
    """
    # Your implementation here
    return FunctionOutput(result="success", success=True, data={})
```

**Function ideas by project type:**
- **Customer Support:** `lookup_order`, `calculate_refund`, `create_ticket`
- **Recipe App:** `search_recipes`, `get_recipe`, `save_favorite`
- **Study Assistant:** `search_materials`, `generate_quiz`, `track_progress`
- **Document Q&A:** `search_docs`, `get_document`, `summarize_section`

**Grading (40 points):**
- 15 pts: 2-3 functions implemented and working
- 10 pts: Pydantic models with proper validation
- 10 pts: Integrated into capstone (not standalone files)
- 5 pts: Error handling present

---

### 2. Test Cases & Demo Video (30 points)

**A. Test File (20 points)**

Create `tests/test_functions.py` with:

```python
"""
Test cases for Week 6 function calling.
Run: python -m pytest tests/test_functions.py
"""
from src.functions.tools import your_function
from src.models.function_models import FunctionInput

def test_basic_functionality():
    """Test function works with valid input"""
    result = your_function(param1="test", param2=5)
    assert result.success == True
    assert result.result is not None

def test_validation():
    """Test Pydantic catches invalid input"""
    try:
        invalid = FunctionInput(param1="", param2=-1)  # Should fail
        assert False, "Should have raised validation error"
    except:
        pass  # Expected

def test_end_to_end():
    """Test complete flow with LLM"""
    from src.ai.agent import chat_with_tools
    response = chat_with_tools("User query that triggers your function")
    assert response is not None
    assert len(response) > 0
```

**Requirements:**
- [ ] At least 3 test cases per function
- [ ] Test for Pydantic validation
- [ ] End-to-end test with LLM
- [ ] All tests pass when run

**B. Demo Video (10 points)**

Record 2-3 minute video showing:
1. Your capstone running
2. User asking question
3. AI calling your function
4. AI responding with result
5. Show 2-3 different scenarios

**How to record:**
- Screen recording (Loom, QuickTime, OBS)
- Show terminal/logs proving functions are called
- Brief narration explaining what's happening

**Where to submit:**
- Upload to YouTube (unlisted) or Google Drive (viewable)
- Add link to your README.md

**Grading (30 points):**
- 15 pts: Comprehensive test cases that pass
- 10 pts: Demo video clearly shows functions working
- 5 pts: Tests in capstone repo

---

### 3. Documentation & Code Quality (20 points)

**A. README Update (5 points)**

Add to your capstone README.md:

```markdown
## Week 6: Function Calling Implementation

### Implemented Functions

**1. function_name** - Brief description
- **Input:** What parameters it takes
- **Output:** What it returns
- **Use case:** When the AI calls this

**2. function_name** - Brief description
- **Input:** What parameters it takes
- **Output:** What it returns
- **Use case:** When the AI calls this

### Testing

```bash
# Run all tests
python -m pytest tests/test_functions.py

# Test interactively
python -m src.demo
```

### Demo Video
[Link to your demo video]
```

**B. Code Quality (15 points)**

**Docstrings required:**
```python
def my_function(param: str) -> MyModel:
    """
    Brief description.
    
    Args:
        param: What this parameter is
        
    Returns:
        MyModel: What gets returned
    """
```

**Type hints required:**
```python
# Good ✅
def search(query: str, limit: int = 5) -> SearchResponse:
    pass

# Bad ❌
def search(query, limit=5):
    pass
```

**Error handling required:**
```python
try:
    result = execute_function(name, args)
    return {"success": True, "data": result}
except ValueError as e:
    return {"success": False, "error": str(e)}
except Exception as e:
    return {"success": False, "error": "System error"}
```

**No hardcoded secrets:**
```python
# Good ✅
api_key = os.getenv("OPENAI_API_KEY")

# Bad ❌
api_key = "sk-hardcoded-key"  # NEVER!
```

**Grading (20 points):**
- 5 pts: README updated with function docs
- 5 pts: All functions have docstrings
- 5 pts: Type hints present
- 3 pts: Error handling implemented
- 2 pts: No hardcoded secrets

---

### 4. GitHub Commit (10 points)

**What to commit:**
```bash
git add src/models/function_models.py
git add src/functions/tools.py
git add src/ai/agent.py
git add tests/test_functions.py
git add README.md
git add .env.example  # Example only, not real .env!

git commit -m "feat(week6): implement function calling with 3 core functions

- Add search_knowledge_base function
- Add calculate_results function  
- Add save_user_preference function
- Implement Pydantic models for all I/O
- Add comprehensive test suite
- Update README with documentation

Closes #45, #46, #47"

git push origin main
```

**Requirements:**
- [ ] Descriptive commit message (not just "update")
- [ ] All required files included
- [ ] `.env` is NOT committed (in `.gitignore`)
- [ ] Code is pushed to main branch

**Grading (10 points):**
- 5 pts: All required files committed
- 3 pts: Descriptive commit message
- 2 pts: `.env` not in repo (security)

---

## 📦 Submission Instructions

### Before You Submit

**Files checklist:**
- [ ] `src/models/function_models.py` exists
- [ ] `src/functions/tools.py` exists
- [ ] `src/ai/agent.py` exists
- [ ] `tests/test_functions.py` exists
- [ ] `README.md` updated with Week 6 section
- [ ] `.env.example` exists (no real keys!)
- [ ] `.env` in `.gitignore`

**Functionality checklist:**
- [ ] 2-3 functions work
- [ ] LLM calls functions successfully
- [ ] All tests pass: `python -m pytest tests/`
- [ ] Demo video shows it working
- [ ] No hardcoded secrets

**Quality checklist:**
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
|-----------|--------|----------|
| **Functions** | 40 | 2-3 working functions with Pydantic, integrated into capstone |
| **Tests & Demo** | 30 | Test suite passes, demo video shows functions working |
| **Code Quality** | 20 | Docstrings, type hints, error handling, no secrets |
| **GitHub** | 10 | Descriptive commit, all files included, pushed properly |
| **Total** | **100** | |

**Deductions:**
- Late (1 day): -10%
- Late (2 days): -20%
- Late (3 days): -30%
- After 3 days: Requires instructor approval
- Code doesn't run: -20%
- API keys in repo: -10%
- Functions not in capstone: -20%
- No tests: -10%
- No demo video: -10%

---

## ❓ Common Questions

**Q: Can I use examples from lecture?**  
A: Yes, but adapt to YOUR project. Don't submit generic examples.

**Q: Do I need real database integration?**  
A: Not yet. Mock data is fine for Week 6.

**Q: What if I only have 2 functions?**  
A: That's fine. Just make sure they're substantial and working.

**Q: Can I use Claude instead of OpenAI?**  
A: Yes, but adapt the function calling syntax.

**Q: How long should demo video be?**  
A: 2-3 minutes. Just show it works.

**Q: Can I submit late?**  
A: Up to 3 days with deductions. After that, need approval.

**Q: What if my teammate isn't helping?**  
A: Document attempts to contact. Continue solo if needed. This will be considered in peer reviews.

**Q: Where do I get help?**  
A: See resources below.

---

## 📚 Resources

**In Lab Repository:**
- [Function Calling Guide](./guides/function-calling-guide.md)
- [Pydantic Model Guide](./guides/pydantic-model-guide.md)
- [Function Schema Template](./templates/function-schema-template.md)
- [RAG Pipeline Examples](./guides/rag-pipeline-examples.py)
- [Troubleshooting Guide](./guides/troubleshooting-guide.md)

**External Documentation:**
- OpenAI Function Calling: https://platform.openai.com/docs/guides/function-calling
- Pydantic Docs: https://docs.pydantic.dev/
- Structured Outputs: https://platform.openai.com/docs/guides/structured-outputs

**Getting Help:**
- **Lab hours:** Thursday 2-4pm
- **Office hours:** Monday/Wednesday 2-4pm
- **Discord:** #week-6-function-calling
- **Email:** zeshan.ahmad@kiu.edu.ge (include "[Week 6]" in subject)

---

## 💡 Tips for Success

### Start with Mock Data
Don't worry about real databases yet. Use mock data:

```python
def search_database(query: str) -> SearchResponse:
    # Mock data for Week 6
    mock_results = [{"id": 1, "title": "Result 1"}]
    return SearchResponse(results=mock_results, total=1)
```

### Test Incrementally
1. Test Pydantic models alone
2. Test functions alone
3. Test with LLM
4. Test end-to-end

### Use the Guides
Everything you need is documented:
- Stuck on function calling? → Function Calling Guide
- Pydantic errors? → Pydantic Model Guide
- General errors? → Troubleshooting Guide

### Get Help Early
Don't wait until Friday evening. If stuck for 30+ minutes, ask for help.

### Make It Real
Create functions that solve YOUR project's actual problems, not generic examples.

---

## ✅ Success Looks Like This

**By Friday evening:**
- Your capstone repo has 2-3 working functions
- You can ask your AI to do something, and it calls the right function
- Tests pass
- Demo video shows it working
- Code is on GitHub
- You're ready for Week 7 user testing

**This is a major milestone - your AI can now take actions! 🎉**

---

**Course:** Building AI-Powered Applications (CS-AI-2025)  
**Instructor:** Professor Zeshan Ahmad  
**Institution:** Kutaisi International University
