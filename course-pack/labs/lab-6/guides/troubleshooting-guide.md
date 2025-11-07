# Lab 6 Troubleshooting Guide

**Quick solutions to common issues**

---

## 🔧 Function Calling Issues

### Issue 1: LLM Not Calling My Function

**Symptoms:**
- LLM responds with text instead of calling function
- Function is defined but never executed

**Common Causes:**
1. Function description too vague
2. System prompt doesn't mention when to use functions
3. Function name doesn't match user intent

**Solutions:**

```python
# ❌ Bad - vague description
{
  "name": "do_thing",
  "description": "Does something"
}

# ✅ Good - specific description
{
  "name": "generate_quiz",
  "description": "Generate a multiple-choice quiz on a specific topic. Use this when user asks to create, make, or generate a quiz or test. Returns structured quiz data with questions, options, and correct answers."
}
```

**System Prompt Fix:**
```python
system_prompt = """
You are a tutor assistant. When users ask you to create a quiz, you MUST use the generate_quiz function.

DO: Call generate_quiz() when user says "make me a quiz" or similar
DON'T: Just say "I'll create a quiz" without actually calling the function

Available functions: {function_list}
"""
```

---

### Issue 2: Function Arguments Wrong Type

**Symptoms:**
- `TypeError: expected int, got str`
- LLM passes `"5"` instead of `5`

**Solution:**
Add type coercion in your function:

```python
def my_function(num_questions: int):
    # Coerce to correct type
    try:
        num_questions = int(num_questions)
    except (ValueError, TypeError):
        raise ValueError(f"num_questions must be integer, got {type(num_questions)}")
    
    # Now safe to use
    return process(num_questions)
```

---

### Issue 3: Function Call Loop Not Closing

**Symptoms:**
- Function executes but user gets no response
- Conversation hangs after function call

**Solution:**
Always send function result back to LLM:

```python
# ❌ Bad - stops after function call
if message.function_call:
    result = my_function()
    print(result)  # User never sees this!

# ✅ Good - closes the loop
if message.function_call:
    result = my_function()
    
    # Send result back to LLM for final response
    final_response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            original_messages,
            message,  # The function call
            {"role": "function", "name": "my_function", "content": str(result)}
        ]
    )
    
    return final_response.choices[0].message.content
```

---

## 🔍 Pydantic Validation Errors

### Issue 4: ValidationError - Field Required

**Error Message:**
```
ValidationError: 1 validation error for QuizResult
topic
  field required (type=value_error.missing)
```

**Solution:**
Ensure all required fields are provided:

```python
# ❌ Bad - missing required field
return QuizResult(
    questions=[...]  # Forgot 'topic'!
)

# ✅ Good - all required fields
return QuizResult(
    topic=topic,
    questions=[...],
    difficulty="medium"
)
```

---

### Issue 5: ValidationError - Value Not Valid

**Error Message:**
```
ValidationError: 1 validation error for QuizResult
total_points
  ensure this value is greater than or equal to 0
```

**Solution:**
Check your Field constraints:

```python
class QuizResult(BaseModel):
    total_points: int = Field(ge=0)  # Must be >= 0

# If you're getting this error, you're passing negative number
# Debug by printing before creating model:
print(f"DEBUG: total_points = {total_points}")  # Shows -5
```

---

### Issue 6: ValidationError - Type Error

**Error Message:**
```
ValidationError: 1 validation error for QuizResult
difficulty
  value is not a valid enumeration member; permitted: 'easy', 'medium', 'hard'
```

**Solution:**
Use Literal types and validate inputs:

```python
from typing import Literal

class QuizResult(BaseModel):
    difficulty: Literal["easy", "medium", "hard"]

def my_function(difficulty: str):
    # Validate before creating model
    valid_difficulties = ["easy", "medium", "hard"]
    if difficulty not in valid_difficulties:
        difficulty = "medium"  # Default fallback
    
    return QuizResult(difficulty=difficulty, ...)
```

---

## 🌐 Lovable Integration Issues

### Issue 7: CORS Error

**Error Message:**
```
Access to fetch at 'http://localhost:8000/api/...' from origin 'https://your-app.lovable.app' 
has been blocked by CORS policy
```

**Solution:**
Add CORS middleware to your backend:

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-app.lovable.app", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

### Issue 8: API Key Not Working in Lovable

**Symptoms:**
- API calls work locally
- Fail in Lovable with "401 Unauthorized"

**Solution:**
Use Lovable environment variables:

1. Go to Lovable project settings
2. Add environment variable: `OPENAI_API_KEY=your-key`
3. Access in code:
```javascript
const apiKey = import.meta.env.VITE_OPENAI_API_KEY;
```

**Never hardcode API keys in Lovable projects!**

---

### Issue 9: Lovable UI Not Calling Backend

**Symptoms:**
- Frontend makes API call
- Nothing happens on backend

**Solution:**
Check your endpoint URL:

```javascript
// ❌ Bad - localhost won't work in deployed Lovable
const response = await fetch('http://localhost:8000/api/generate-quiz')

// ✅ Good - use environment variable
const API_BASE = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'
const response = await fetch(`${API_BASE}/api/generate-quiz`)
```

---

## 🔗 RAG + Function Integration Issues

### Issue 10: RAG Context Lost After Function Call

**Symptoms:**
- LLM forgets RAG context when calling function
- Response doesn't use retrieved documents

**Solution:**
Keep RAG context in conversation history:

```python
# Build messages with RAG context
messages = [
    {"role": "system", "content": "You are a tutor with access to documents and functions."},
    {"role": "user", "content": user_query},
]

# Add RAG context
if rag_results:
    rag_context = "\n".join([doc.content for doc in rag_results])
    messages.append({
        "role": "system",
        "content": f"Relevant documents:\n{rag_context}"
    })

# Call LLM with functions
response = client.chat.completions.create(
    model="gpt-4",
    messages=messages,
    functions=functions
)

# If function called, keep RAG context in follow-up
if response.choices[0].message.function_call:
    result = execute_function(...)
    
    # Include all previous messages (including RAG context)
    messages.append(response.choices[0].message)
    messages.append({"role": "function", "name": func_name, "content": str(result)})
    
    final_response = client.chat.completions.create(
        model="gpt-4",
        messages=messages  # RAG context still here!
    )
```

---

### Issue 11: LLM Calling Function Instead of RAG

**Symptoms:**
- LLM always calls functions
- Never uses RAG retrieval even when it should

**Solution:**
Make system prompt explicit about when to use what:

```python
system_prompt = """
You are a tutor. You have two capabilities:

1. RETRIEVAL: Search documents to answer factual questions
   - Use when: User asks "what is...", "explain...", "tell me about..."
   - Process: Retrieve documents first, then answer

2. FUNCTIONS: Take actions or generate content
   - Use when: User asks to "create", "generate", "save", "calculate"
   - Process: Call appropriate function

**Decision flow:**
- If question needs factual info → Retrieve from documents first
- If question needs action → Call function
- If both → Retrieve first, then use function with retrieved context

Available functions: {functions}
"""
```

---

## 📊 Performance Issues

### Issue 12: Slow Response Times

**Symptoms:**
- Function calls take 10+ seconds
- Users complain about latency

**Solutions:**

1. **Reduce RAG retrieval**:
```python
# ❌ Bad - retrieving 10 chunks
rag_results = vector_db.search(query, top_k=10)

# ✅ Good - retrieve 3 chunks
rag_results = vector_db.search(query, top_k=3)
```

2. **Cache function results**:
```python
from functools import lru_cache

@lru_cache(maxsize=100)
def expensive_function(topic: str):
    # Results cached for same topic
    return compute_expensive_thing(topic)
```

3. **Use faster models**:
```python
# ❌ Slow - GPT-4 for every call
model = "gpt-4"

# ✅ Faster - Use GPT-3.5 for function calling, GPT-4 for final response
model_for_function = "gpt-3.5-turbo"
model_for_response = "gpt-4"
```

---

### Issue 13: High API Costs

**Symptoms:**
- Running out of API credits quickly
- Each interaction costs > $0.10

**Solutions:**

1. **Minimize token usage**:
```python
# ❌ Bad - sending full document content
context = document.full_text  # 10,000 tokens!

# ✅ Good - send only relevant chunks
context = "\n".join(doc.content[:500] for doc in rag_results[:3])  # ~1,500 tokens
```

2. **Cache LLM responses**:
```python
import hashlib

def get_cached_response(user_query, functions):
    # Create cache key from query + functions
    cache_key = hashlib.md5(f"{user_query}{functions}".encode()).hexdigest()
    
    # Check cache first
    if cache_key in cache:
        return cache[cache_key]
    
    # Call LLM if not cached
    response = call_llm(user_query, functions)
    cache[cache_key] = response
    
    return response
```

3. **Batch operations**:
```python
# ❌ Bad - 5 separate API calls
for topic in topics:
    quiz = generate_quiz(topic)

# ✅ Good - 1 API call
topics_string = ", ".join(topics)
all_quizzes = generate_quizzes_batch(topics_string)
```

---

## 🐛 General Debugging Tips

### Debug Technique 1: Print Everything

```python
def my_function(param: str):
    print(f"🔍 DEBUG: my_function called with param={param}")
    print(f"🔍 DEBUG: param type = {type(param)}")
    
    result = do_work(param)
    
    print(f"🔍 DEBUG: result = {result}")
    print(f"🔍 DEBUG: result type = {type(result)}")
    
    return result
```

### Debug Technique 2: Log LLM Interactions

```python
import logging

logging.basicConfig(level=logging.DEBUG)

# Log before calling LLM
logging.debug(f"Calling LLM with messages: {messages}")
logging.debug(f"Functions: {functions}")

response = client.chat.completions.create(...)

# Log LLM response
logging.debug(f"LLM response: {response}")
```

### Debug Technique 3: Test Functions Independently

```python
# Test without LLM first
if __name__ == "__main__":
    print("Testing generate_quiz...")
    result = generate_quiz("photosynthesis", 5, "easy")
    print("✅ Success:", result)
    
    print("\nTesting with invalid data...")
    try:
        bad_result = generate_quiz("", -5, "impossible")
    except Exception as e:
        print("✅ Error caught:", e)
```

---

## 💡 Quick Fixes Checklist

When something breaks, try these in order:

- [ ] Check the error message carefully (read it word by word)
- [ ] Print all variables involved in the error
- [ ] Test the failing function independently (without LLM)
- [ ] Check if API keys are valid
- [ ] Verify network connectivity (can you reach the API?)
- [ ] Check if you're using the correct model name
- [ ] Verify your function schemas match your implementations
- [ ] Check Pydantic model constraints
- [ ] Look for typos in variable/function names
- [ ] Check if you're closing the function call loop

---

## 🆘 Still Stuck?

If none of these solutions work:

2. **Office Hours:**
   - Bring your laptop
   - Have the error reproducible
   - Show what debugging you've done

3. **Email Instructor:**
   - Include GitHub repo link
   - Describe the issue step-by-step
   - Mention what troubleshooting you've attempted

---

**Remember:** Every bug is a learning opportunity. Document what fixed it so you (and others) don't hit it again!
