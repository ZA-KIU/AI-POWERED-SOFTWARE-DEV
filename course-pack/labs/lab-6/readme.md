# Lab 6: Implementing Function Calling & Structured Outputs

**Week 6 | Building AI‑Powered Applications**  
This week you move from planning into implementation. You'll connect your AI to real functions and use Pydantic models to ensure structured, validated outputs. By the end of this week your capstone project should be able to take meaningful actions.

**Lab duration:** 2 hours in‑class implementation  
**Due date:** End of Week 6 (Friday 11:59 p.m.)

---

## 🎯 Goals for This Week
By end of this week your capstone should:

- Have 2–3 working functions your AI can call
- Use Pydantic models for all function inputs and outputs
- Support multi‑turn conversations where tool usage is visible
- Handle errors and edge cases safely
- Be pushed to GitHub with visible commit progress

This is a project milestone, not just an exercise.

---

## 📊 Implementation Checklist

### Function Calling Tasks

- **Define 2–3 core functions** your project requires  
  Think about what data or actions your AI needs to interact with.
- **Write working implementations** in your code  
  Start with mock data; integrate real systems later.
- **Create JSON schemas** so the LLM knows how to call your functions.
- **Test the full loop:** user request → function call → result → AI response.

### Structured Output Tasks

- **Identify data structures** your project uses. What JSON shapes are needed?
- **Define Pydantic models** for these structures. Include types, validation rules and descriptions.
- **Use structured outputs** with the LLM (`response_format` via `beta.parse`).
- **Integrate results** into your database or UI. Use mock data for now if needed.

Goal: By next week your AI should take real actions in your capstone.

---

## 🛠 Pre‑Lab Setup (CRITICAL)

1. **API Key Configuration**
   ```bash
   echo "OPENAI_API_KEY=sk‑your‑key" >> .env
   ```
   Fund your account via the provider’s billing page or use your Gemini key.

2. **Install Packages**
   ```bash
   pip install openai pydantic python‑dotenv --break‑system‑packages
   ```

3. **Review Week 4 Design Review**  
   Revisit your PRD: which functions did you plan? What data flows did you define?

4. **Pull Latest Materials**
   ```bash
   cd AI‑POWERED‑SOFTWARE‑DEV
   git pull origin main
   cd course‑pack/labs/lab‑6
   ```

---

## 📋 In‑Class Implementation (2 Hours)

### Part 1: Define Your Functions (30 minutes)

Decide which 2–3 functions your project needs. For each, write down the name, parameters (with types) and purpose.

**Examples**

• Support bot: `lookup_order_status(order_id)`, `calculate_refund(order_id, reason)`, `create_support_ticket(title, description)`  
• Recipe app: `search_recipes(query, dietary_restrictions)`, `get_recipe_details(recipe_id)`, `save_to_favorites(user_id, recipe_id)`  
• Study assistant: `generate_quiz(topic, difficulty, count)`, `track_progress(user_id, topic)`, `search_course_materials(query)`

✅ Functions defined with names, typed parameters and descriptions.

### Part 2: Implement Functions & Pydantic Models (60 minutes)

1. **Define input/output models** using Pydantic.
   ```python
   from pydantic import BaseModel, Field
   from typing import List, Literal

   class OrderStatusRequest(BaseModel):
       order_id: str = Field(description="Order ID (format: ORD‑XXXXX)")

   class OrderStatus(BaseModel):
       order_id: str
       status: Literal["pending", "shipped", "delivered"]
       tracking_number: str | None = None
       items: List[str]
   ```

2. **Write the function implementations** (mock data is OK).  
   ```python
   def lookup_order_status(order_id: str) -> OrderStatus:
       return OrderStatus(
           order_id=order_id,
           status="shipped",
           tracking_number="TRACK12345",
           items=["Product A", "Product B"]
       )
   ```

3. **Wire the function schema** into your LLM client.  
   Define the tools parameter with a JSON schema that matches your Pydantic model.

✅ Pydantic models defined; functions implemented; LLM schema wired.

### Part 3: Integration & Testing (30 minutes)

- **Integrate** your functions into your capstone repository (`src/models/`, `src/functions/`, `src/ai/`).
- **Test multi‑turn conversations**: ensure your AI can call multiple functions in sequence and respond correctly.
- **Handle errors gracefully**: wrap calls in try/except blocks and return clear user‑facing messages.

✅ Integrated into capstone; multi‑turn conversation works; error handling in place; commit pushed to GitHub.

---

## 🧠 Quick Evaluation & Safety Guide

To meet the syllabus requirements you must demonstrate that your functions are reliable and that you considered safety:

- **Measure performance**: Use a simple timer around your function call to record execution time and write the result in `evaluation_notes.md`.
- **Create simple tests**: Make a small table (3–5 cases) showing input, expected output, actual output, time and pass/fail. Include it in `evaluation_notes.md`.
- **Handle errors**: Ensure your code catches exceptions and returns a friendly error message. Note any errors in `evaluation_notes.md`.
- **Complete a safety checklist**: In `safety_checklist.md` confirm you removed API keys from code, avoided private data, handled strange inputs safely and added a fallback for unsafe model responses.
- **Log AI tool usage**: In `ai_use_log.md` list any AI tools you used (e.g., ChatGPT, Claude, Cursor) and a brief description of what they helped you with.
- **Connect to your capstone**: In `capstone_link.md` state which Lab 6 function will be part of your capstone and your next planned improvement.

See the guides for templates and examples:  
`examples/evaluation-notes.md`, `guides/safety-checklist.md`, `guides/ai-use-log.md` and `guides/capstone-project-link.md`.

---

## ✅ Submission Checklist

Include these files in your `course‑pack/labs/lab‑6/` folder when you submit this lab:

- `evaluation_notes.md` – Summarize latency measurements and simple test results.
- `safety_checklist.md` – Confirm you addressed API keys, data privacy and input handling.
- `ai_use_log.md` – Record the AI tools you used and why.
- `capstone_link.md` – Explain which function will carry forward into your capstone and your next step.

Each file can be short. One or two paragraphs is fine. The goal is to show you tested your functions, thought about safety, and know how this work connects to your final project.

---

## 📚 Resources

### In This Repository

- **[Function Calling Guide](./guides/function-calling-guide.md)** – Complete implementation patterns
- **[Pydantic Model Guide](./guides/pydantic-model-guide.md)** – Schema validation
- **[Function Schema Template](./templates/function-schema-template.md)** – JSON schema format
- **[RAG Pipeline Examples](./guides/rag-pipeline-examples.py)** – If using retrieval
- **[Troubleshooting Guide](./guides/troubleshooting-guide.md)** – Common issues solved
- **[Sprint Planning Guide](./guides/sprint-planning-guide.md)** – Next sprint planning
- **[Safety Checklist](./guides/safety-checklist.md)** – Basic safety and privacy checks
- **[AI Use Log](./guides/ai-use-log.md)** – How to log AI-assisted coding
- **[Capstone Project Link](./guides/capstone-project-link.md)** – Template for connecting your function to your capstone
- **[Evaluation Notes Example](./examples/evaluation-notes.md)** – Sample evaluation log

### External Documentation

- **OpenAI Function Calling:** https://platform.openai.com/docs/guides/function-calling
- **Pydantic Docs:** https://docs.pydantic.dev/
- **Structured Outputs:** https://platform.openai.com/docs/guides/structured-outputs

---

## 🔑 Week 6 Key Takeaways

### Function Calling = ACTIONS
This is how your AI interacts with the real world. It gives your AI "hands" to use your database, call APIs and save data.

### Structured Outputs = RELIABILITY
Stop parsing text. Get guaranteed, validated JSON every time. This is essential for robust database and frontend integration.

### Safety = NON‑NEGOTIABLE
You are the gatekeeper. Validate all inputs, check all permissions. Never trust the AI. You are responsible for what your code executes.

### You Are Implementing This NOW
This isn't theory. This is your task for this week's lab. What you planned today, you build tomorrow.

---

## 👀 Looking Ahead

**Week 7:**

- User testing round 1 with your working functions
- Iterate based on real user feedback
- Add more functions as needed
- Sprint retrospective

**Week 8–11:**

- Continue building out functionality
- Optimize performance and costs
- Safety and evaluation audit (Week 11)
- Production‑ready features

Your functions are the foundation for everything else you’ll build.

---

## 🙋 Getting Help

### During Lab (Best Option)

- Raise your hand
- Work with your team
- Ask instructor

### Outside Lab Hours

**Email:** zeshan.ahmad@kiu.edu.ge  
Include: Error message, code snippet, what you tried

**GitHub Issues:** Tag questions with `week-6` label

---

## ✅ Ready to Build?

**Pre‑flight checklist:**

- [ ] API key configured and funded
- [ ] Packages installed (`openai`, `pydantic`)
- [ ] Reviewed Week 4 design review
- [ ] Know what 2–3 functions you need
- [ ] Pulled latest lab materials
- [ ] Capstone repo cloned and ready

Time to make your AI do real work. Let’s code!

---

**Lab 6 Materials | Professor Zeshan Ahmad**  
**Building AI‑Powered Applications | Kutaisi International University**  
**Fall 2025**
