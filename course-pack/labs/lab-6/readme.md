# Lab 6: Implementing Function Calling & Structured Outputs

**Week 6 | Building AI-Powered Applications**

This week you move from planning to **implementation**. You'll integrate function calling to give your AI real capabilities and use Pydantic models to ensure reliable, type-safe outputs. This isn't theory - by the end of this week, your capstone should be able to **take actions**.

**Lab Duration:** 2 hours in-class implementation  
**Due Date:** End of Week 6 - Functions integrated into your capstone

---

## 🎯 Week 6 Goals

**By end of this week, your capstone must:**
- ✅ Have 2-3 working functions the AI can call
- ✅ Use Pydantic models for all structured data
- ✅ Complete multi-turn conversations with tool usage
- ✅ Handle errors and edge cases safely
- ✅ Be pushed to GitHub with visible progress

**This is a project milestone - not just exercises.**

---

## 📊 Week 6 Implementation Checklist

### Function Calling Tasks
- [ ] **Define 2-3 core functions** your project needs
  - What data or actions does your AI need?
- [ ] **Write function implementations**
  - Actual Python/JS code that does the work
- [ ] **Create JSON schemas for LLM**
  - Describe functions so AI knows when/how to use them
- [ ] **Test the complete loop**
  - User query → Function call → Result → Response

### Structured Output Tasks  
- [ ] **Identify data structures you need**
  - What JSON shapes does your project use?
- [ ] **Define Pydantic models**
  - Types, validation rules, descriptions
- [ ] **Update LLM calls to use schemas**
  - Switch to `beta.parse` with `response_format`
- [ ] **Integrate with database/frontend**
  - Use structured output directly in your system

**Goal:** By next week, your AI should be able to TAKE ACTIONS in your system.

---

## 🛠️ Pre-Lab Setup (CRITICAL)

### 1. API Key Configured

**OpenAI** (Recommended):
```bash
# In your capstone repo
echo "OPENAI_API_KEY=sk-your-key-here" >> .env
```
- Fund account with $5+ at https://platform.openai.com/account/billing

**OR Google Gemini** (Free tier):
```bash
echo "GOOGLE_API_KEY=your-key-here" >> .env
```
- Get key at https://aistudio.google.com/apikey
- 1,500 requests/day free

### 2. Install Packages

```bash
cd your-capstone-repo
pip install openai pydantic python-dotenv --break-system-packages
```

### 3. Review Your Week 4 Design Review

Look at your PRD from Week 4:
- What functions did you plan?
- What data structures did you specify?
- What needs to be built this week?

### 4. Pull Latest Lab Materials

```bash
cd AI-POWERED-SOFTWARE-DEV
git pull origin main
cd course-pack/labs/lab-6
```

---

## 📋 In-Class Implementation (2 hours)

### Part 1: Define Your Functions (30 min)

**What You're Building:**
2-3 functions specific to YOUR capstone project.

**Examples by Project Type:**

**If you're building a customer support bot:**
- `lookup_order_status(order_id)` → Order details
- `calculate_refund(order_id, reason)` → Refund amount
- `create_support_ticket(title, description)` → Ticket ID

**If you're building a recipe app:**
- `search_recipes(query, dietary_restrictions)` → Recipe list
- `get_recipe_details(recipe_id)` → Full recipe
- `save_to_favorites(user_id, recipe_id)` → Success/failure

**If you're building a study assistant:**
- `search_course_materials(query)` → Relevant documents
- `generate_quiz(topic, difficulty, count)` → Quiz questions
- `track_progress(user_id, topic)` → Progress stats

**Your Turn:**
1. Open [Function Schema Template](./templates/function-schema-template.md)
2. Define 2-3 functions YOUR project needs
3. Write clear descriptions (the AI reads these!)
4. Specify all parameters with types

**Success Criteria:**
- [ ] 2-3 functions defined
- [ ] Each function has clear description
- [ ] All parameters specified with types
- [ ] Parameters have descriptions
- [ ] You know HOW you'll implement each function

**Resources:**
- [Function Calling Guide](./guides/function-calling-guide.md)
- [Function Schema Template](./templates/function-schema-template.md)

---

### Part 2: Implement Functions & Pydantic Models (60 min)

**Step 1: Create Pydantic Models (20 min)**

For each function, create input/output models:

```python
from pydantic import BaseModel, Field
from typing import List, Literal

# Input model for function parameters
class OrderLookupRequest(BaseModel):
    order_id: str = Field(description="Order ID to look up", pattern="^ORD-[0-9]+$")

# Output model for function response
class OrderStatus(BaseModel):
    order_id: str
    status: Literal["pending", "shipped", "delivered", "cancelled"]
    tracking_number: str | None = None
    estimated_delivery: str | None = None
    items: List[str]
```

**Reference:** [Pydantic Model Guide](./guides/pydantic-model-guide.md)

**Step 2: Implement Python Functions (30 min)**

Write the actual code that executes when AI calls your function:

```python
def lookup_order_status(order_id: str) -> OrderStatus:
    """
    Look up order status in database.
    
    This is the actual implementation - connects to your DB,
    makes API calls, does calculations, etc.
    """
    # TODO: Replace with your real implementation
    # For now, mock data works:
    return OrderStatus(
        order_id=order_id,
        status="shipped",
        tracking_number="TRACK123456",
        estimated_delivery="2025-11-10",
        items=["Product A", "Product B"]
    )
```

**Start with mock data, then integrate real systems.**

**Step 3: Wire Up to LLM (10 min)**

```python
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Define tools for the LLM
tools = [{
    "type": "function",
    "function": {
        "name": "lookup_order_status",
        "description": "Retrieve current status of a customer order",
        "parameters": {
            "type": "object",
            "properties": {
                "order_id": {
                    "type": "string",
                    "description": "The order ID (format: ORD-XXXXX)"
                }
            },
            "required": ["order_id"]
        }
    }
}]

# Make API call with tools
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful customer support assistant."},
        {"role": "user", "content": "What's the status of order ORD-12345?"}
    ],
    tools=tools
)

# Check if AI wants to call a function
if response.choices[0].message.tool_calls:
    tool_call = response.choices[0].message.tool_calls[0]
    
    # Execute the function
    if tool_call.function.name == "lookup_order_status":
        args = json.loads(tool_call.function.arguments)
        result = lookup_order_status(**args)
        
        # Return result to AI for final response
        # (See guides for complete multi-turn example)
```

**Success Criteria:**
- [ ] Pydantic models defined for all functions
- [ ] Python functions implemented (mock data OK for now)
- [ ] Tool schemas match your Pydantic models
- [ ] LLM successfully calls your functions
- [ ] You can test end-to-end

**Resources:**
- [Function Calling Guide](./guides/function-calling-guide.md)
- [RAG Pipeline Examples](./guides/rag-pipeline-examples.py) (if using RAG)
- [Troubleshooting Guide](./guides/troubleshooting-guide.md)

---

### Part 3: Integration & Testing (30 min)

**Step 1: Integrate Into Your Capstone Repo**

Move your code from lab exercises to your actual project:

```
your-capstone/
├── src/
│   ├── models/
│   │   └── function_models.py  # Your Pydantic models
│   ├── functions/
│   │   └── tools.py  # Your function implementations
│   └── ai/
│       └── agent.py  # LLM orchestration
```

**Step 2: Test Multi-Turn Conversations**

Test scenarios where the AI needs to call multiple functions:

```
User: "I want to return order ORD-12345 because it's damaged"
→ AI calls: lookup_order_status(order_id="ORD-12345")
→ AI calls: calculate_refund(order_id="ORD-12345", reason="damaged")
→ AI responds: "I've looked up your order. You're eligible for a $45.99 refund..."
```

**Step 3: Handle Errors Gracefully**

```python
def safe_function_call(function_name: str, arguments: dict):
    """Wrapper to catch errors and return user-friendly messages"""
    try:
        # Execute function
        result = globals()[function_name](**arguments)
        return {"success": True, "data": result.model_dump()}
    except ValueError as e:
        return {"success": False, "error": "Invalid input", "details": str(e)}
    except Exception as e:
        return {"success": False, "error": "System error", "details": "Please try again"}
```

**Success Criteria:**
- [ ] Functions work in your actual capstone repo
- [ ] Multi-turn conversations work
- [ ] Errors are caught and handled
- [ ] Code is pushed to GitHub
- [ ] You can demo it working

**Resources:**
- [Troubleshooting Guide](./guides/troubleshooting-guide.md)
- [Sprint Planning Guide](./guides/sprint-planning-guide.md) (for next steps)

---

## 🏠 Homework: Week 6 Implementation

**Due:** End of Week 6 (Friday 11:59 PM)  
**Points:** 10 (Project milestone grade)  
**Deliverable:** Working function calling in your capstone, pushed to GitHub

See [Homework Assignment](./homework-assignment.md) for complete requirements.

### Quick Summary

**You must submit:**
1. **2-3 working functions** integrated into your capstone
2. **Pydantic models** for all function inputs/outputs  
3. **Test cases** showing functions work
4. **GitHub commit** with visible progress
5. **Short demo video** (2-3 min) showing it working

**Grading:**
- 40% - Functions are implemented and working
- 30% - Pydantic models with proper validation
- 20% - Integration into capstone (not standalone)
- 10% - Error handling and code quality

---

## 🚨 Common Issues & Quick Fixes

### "API key not working"
- Check `.env` file exists in project root
- Verify key format: `OPENAI_API_KEY=sk-...`
- Ensure account has credits: https://platform.openai.com/account/billing
- Restart your Python session after changing `.env`

### "Function never gets called"
- Make function description very specific
- Include example usage in description
- Check schema is valid JSON
- See: [Function Calling Guide](./guides/function-calling-guide.md)

### "Pydantic validation failing"
- Use `| None` for optional fields
- Check field types match your data
- Add `default` values where appropriate
- See: [Pydantic Model Guide](./guides/pydantic-model-guide.md)

### "Can't figure out what functions I need"
- Look at your Week 4 Design Review
- What actions does your AI need to take?
- Start with 2 essential functions, add more later
- See: [Function Schema Template](./templates/function-schema-template.md)

**More help:** [Troubleshooting Guide](./guides/troubleshooting-guide.md)

---

## 📖 Resources

### In This Repository
- **[Function Calling Guide](./guides/function-calling-guide.md)** - Complete implementation patterns
- **[Pydantic Model Guide](./guides/pydantic-model-guide.md)** - Schema validation
- **[Function Schema Template](./templates/function-schema-template.md)** - JSON schema format
- **[RAG Pipeline Examples](./guides/rag-pipeline-examples.py)** - If using retrieval
- **[Troubleshooting Guide](./guides/troubleshooting-guide.md)** - Common issues solved
- **[Sprint Planning Guide](./guides/sprint-planning-guide.md)** - Next sprint planning

### External Documentation
- **OpenAI Function Calling:** https://platform.openai.com/docs/guides/function-calling
- **Pydantic Docs:** https://docs.pydantic.dev/
- **Structured Outputs:** https://platform.openai.com/docs/guides/structured-outputs

---

## 💡 Week 6 Key Takeaways

### Function Calling = ACTIONS
This is how your AI interacts with the real world. It gives your AI "hands" to use your database, call APIs, and save data.

### Structured Outputs = RELIABILITY  
Stop parsing text. Get guaranteed, validated JSON every time. This is essential for robust database and frontend integration.

### Safety = NON-NEGOTIABLE
You are the gatekeeper. Validate all inputs, check all permissions. Never trust the AI. You are responsible for what your code executes.

### You Are Implementing This NOW
This isn't theory. This is your task for Thursday's lab and this week's project milestone. What you planned today, you build tomorrow.

---

## 🔮 Looking Ahead

**Week 7:**
- User testing round 1 with your working functions
- Iterate based on real user feedback
- Add more functions as needed
- Sprint retrospective

**Week 8-11:**
- Continue building out functionality
- Optimize performance and costs
- Safety and evaluation audit (Week 11)
- Production-ready features

**Your functions are the foundation for everything else you'll build.**

---

## 📞 Getting Help

### During Lab (Best Option)
- Raise your hand
- Work with your team
- Ask instructor

### Outside Lab Hours
**Email:** zeshan.ahmad@kiu.edu.ge  
*Include:* Error message, code snippet, what you tried

**GitHub Issues:** Tag questions with `week-6` label

---

## ✅ Ready to Build?

**Pre-flight checklist:**
- [ ] API key configured and funded
- [ ] Packages installed (`openai`, `pydantic`)
- [ ] Reviewed Week 4 Design Review
- [ ] Know what 2-3 functions you need
- [ ] Pulled latest lab materials
- [ ] Capstone repo cloned and ready

**Time to make your AI do real work. Let's code! 🚀**

---

**Lab 6 Materials | Professor Zeshan Ahmad**  
**Building AI-Powered Applications | Kutaisi International University**  
**Fall 2025**
