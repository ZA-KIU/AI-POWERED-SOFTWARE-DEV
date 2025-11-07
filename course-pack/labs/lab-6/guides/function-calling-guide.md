# Function Calling Deep Dive Guide

**What you'll learn:** How to implement function calling from scratch, connect it to LLMs, and integrate with your capstone project.

---

## 🎯 What is Function Calling?

Function calling (also called "tool use") allows LLMs to execute code in your application. Instead of just generating text, the LLM can:
- Save data to your database
- Call external APIs
- Perform calculations  
- Trigger actions in your system

**The flow:**
```
User: "Set a reminder for 3pm tomorrow"
  ↓
LLM: "I should call set_reminder() with time='15:00' and date='tomorrow'"
  ↓
Your Code: Executes set_reminder(time='15:00', date='2025-11-08')
  ↓
Your Code: Returns {"success": true, "reminder_id": "123"}
  ↓
LLM: "Done! I've set your reminder for 3pm tomorrow (ID: 123)"
```

---

## 📐 Part 1: Designing Functions

### Rule 1: Single Responsibility

Each function should do ONE thing well.

**Bad:**
```python
def do_everything(action, data, options):
    # Too vague! LLM won't know when to use this
    pass
```

**Good:**
```python
def save_quiz_result(user_id: str, score: int, quiz_id: str):
    """Save a quiz result to database."""
    # Clear purpose, clear parameters

def generate_quiz(topic: str, num_questions: int):
    """Generate a quiz on a topic."""
    # Different responsibility = different function
```

### Rule 2: Clear Parameters

LLMs need to understand what each parameter means.

**Bad:**
```python
def process_data(data: dict):
    # What keys should be in the dict? LLM doesn't know!
    pass
```

**Good:**
```python
def process_quiz_data(
    topic: str,  # e.g., "photosynthesis"
    difficulty: Literal["easy", "medium", "hard"],
    num_questions: int  # between 1-20
):
    # LLM knows exactly what to provide
    pass
```

### Rule 3: Descriptive Names

Use `verb_noun` pattern: `get_weather`, `save_user`, `calculate_score`

**Bad:** `data()`, `process()`, `handler()`  
**Good:** `fetch_transcript()`, `save_notes()`, `calculate_grade()`

---

## 🛠️ Part 2: JSON Schemas

Every function needs a JSON schema that tells the LLM:
1. What the function is called
2. What it does
3. What parameters it expects
4. What's required vs optional

### Basic Template

```json
{
  "name": "function_name",
  "description": "Clear description of what this function does. Be specific!",
  "parameters": {
    "type": "object",
    "properties": {
      "param_name": {
        "type": "string",
        "description": "What this parameter represents",
        "enum": ["option1", "option2"]  // Optional: restrict to specific values
      },
      "another_param": {
        "type": "integer",
        "description": "Another parameter",
        "minimum": 1,
        "maximum": 10
      }
    },
    "required": ["param_name"]  // List required parameters
  }
}
```

### Example: Quiz Generation

```json
{
  "name": "generate_quiz",
  "description": "Generate a multiple-choice quiz on a given topic with a specified number of questions",
  "parameters": {
    "type": "object",
    "properties": {
      "topic": {
        "type": "string",
        "description": "The subject area for the quiz (e.g., 'photosynthesis', 'World War II', 'Python programming')"
      },
      "num_questions": {
        "type": "integer",
        "description": "Number of questions to generate",
        "minimum": 1,
        "maximum": 20
      },
      "difficulty": {
        "type": "string",
        "description": "Difficulty level of the questions",
        "enum": ["easy", "medium", "hard"]
      }
    },
    "required": ["topic"]
  }
}
```

**Note:** `num_questions` and `difficulty` are optional (not in required array), so they'll have defaults.

---

## 💻 Part 3: Implementation with Pydantic

### Why Pydantic?

Pydantic provides automatic validation, type checking, and serialization. It ensures your functions return EXACTLY the structure you expect.

**Without Pydantic:**
```python
def generate_quiz(topic, num_questions):
    # Returns a dict... but what shape? What if it's missing keys?
    return {"questions": [...]}  # Hope for the best!
```

**With Pydantic:**
```python
from pydantic import BaseModel

class QuizOutput(BaseModel):
    topic: str
    questions: list[dict]
    difficulty: str

def generate_quiz(topic, num_questions) -> QuizOutput:
    # Returns QuizOutput, GUARANTEED to have topic, questions, difficulty
    # If it doesn't, Pydantic raises ValidationError
    return QuizOutput(topic=topic, questions=[...], difficulty="medium")
```

### Step-by-Step Implementation

**Step 1: Define Output Model**

```python
from pydantic import BaseModel, Field, field_validator
from typing import List, Literal

class QuizQuestion(BaseModel):
    """A single quiz question."""
    question: str = Field(min_length=10, description="The question text")
    options: List[str] = Field(min_length=4, max_length=4, description="Four answer options")
    correct_answer: int = Field(ge=0, le=3, description="Index of correct option (0-3)")
    explanation: str = Field(min_length=20, description="Why this answer is correct")
    
    @field_validator('options')
    @classmethod
    def validate_options(cls, v):
        if len(set(v)) != 4:
            raise ValueError("All options must be unique")
        return v

class QuizResult(BaseModel):
    """Complete quiz result."""
    topic: str = Field(description="Quiz topic")
    difficulty: Literal["easy", "medium", "hard"] = Field(description="Difficulty level")
    questions: List[QuizQuestion] = Field(description="List of questions")
    total_points: int = Field(ge=0, description="Total possible points")
    estimated_time_minutes: int = Field(ge=1, le=60, description="Estimated completion time")
```

**Key Pydantic features used:**
- `Field()` - adds validation rules and descriptions
- `ge`, `le` - greater/less than or equal to
- `min_length`, `max_length` - string/list length constraints
- `Literal` - restrict to specific values
- `@field_validator` - custom validation logic

**Step 2: Implement Function**

```python
def generate_quiz(
    topic: str,
    num_questions: int = 5,
    difficulty: Literal["easy", "medium", "hard"] = "medium"
) -> QuizResult:
    """
    Generate a multiple-choice quiz on the given topic.
    
    Args:
        topic: Subject area (e.g., "photosynthesis")
        num_questions: Number of questions (default 5)
        difficulty: Difficulty level (default "medium")
    
    Returns:
        QuizResult with validated structure
    
    Raises:
        ValueError: If topic is empty or invalid
        Validation Error: If result doesn't match QuizResult schema
    """
    # Validate inputs
    if not topic or not topic.strip():
        raise ValueError("Topic cannot be empty")
    
    if not 1 <= num_questions <= 20:
        raise ValueError("num_questions must be between 1 and 20")
    
    # Generate questions (this would call your quiz generation logic)
    questions = []
    for i in range(num_questions):
        question = QuizQuestion(
            question=f"Question {i+1} about {topic}",
            options=["Option A", "Option B", "Option C", "Option D"],
            correct_answer=0,
            explanation=f"This is why Option A is correct for {topic}"
        )
        questions.append(question)
    
    # Calculate metadata
    points_per_question = 10
    estimated_time = num_questions * 2  # 2 minutes per question
    
    # Return validated result
    return QuizResult(
        topic=topic,
        difficulty=difficulty,
        questions=questions,
        total_points=num_questions * points_per_question,
        estimated_time_minutes=estimated_time
    )
```

**Step 3: Test Independently**

```python
if __name__ == "__main__":
    # Test with valid data
    result = generate_quiz("photosynthesis", 3, "easy")
    print(result.model_dump_json(indent=2))
    
    # Test with invalid data (should raise error)
    try:
        bad_result = QuizResult(
            topic="",  # Empty topic - should fail
            difficulty="impossible",  # Not in Literal - should fail
            questions=[],
            total_points=-5  # Negative - should fail
        )
    except ValidationError as e:
        print("Validation caught error:", e)
```

---

## 🔗 Part 4: Connecting to LLMs

### OpenAI Function Calling

```python
import openai
import json

# Your function schema
functions = [
    {
        "name": "generate_quiz",
        "description": "Generate a quiz on a topic",
        "parameters": {
            "type": "object",
            "properties": {
                "topic": {"type": "string"},
                "num_questions": {"type": "integer"},
                "difficulty": {"type": "string", "enum": ["easy", "medium", "hard"]}
            },
            "required": ["topic"]
        }
    }
]

# Call LLM
response = openai.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful tutor."},
        {"role": "user", "content": "Create a 5-question quiz about photosynthesis"}
    ],
    functions=functions,
    function_call="auto"  # Let LLM decide whether to call function
)

# Check if LLM wants to call function
message = response.choices[0].message

if message.function_call:
    # Extract function name and arguments
    function_name = message.function_call.name
    function_args = json.loads(message.function_call.arguments)
    
    print(f"LLM wants to call: {function_name}")
    print(f"With arguments: {function_args}")
    
    # Execute the function
    if function_name == "generate_quiz":
        result = generate_quiz(**function_args)
        
        # Send result back to LLM for final response
        second_response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful tutor."},
                {"role": "user", "content": "Create a 5-question quiz about photosynthesis"},
                message,  # The original function call message
                {
                    "role": "function",
                    "name": function_name,
                    "content": result.model_dump_json()
                }
            ]
        )
        
        final_answer = second_response.choices[0].message.content
        print(final_answer)
```

### Anthropic Tool Use (Claude)

```python
import anthropic

client = anthropic.Anthropic(api_key="your-key")

# Tool definition (similar to function schema)
tools = [
    {
        "name": "generate_quiz",
        "description": "Generate a quiz on a topic",
        "input_schema": {
            "type": "object",
            "properties": {
                "topic": {"type": "string"},
                "num_questions": {"type": "integer"},
                "difficulty": {"type": "string", "enum": ["easy", "medium", "hard"]}
            },
            "required": ["topic"]
        }
    }
]

# Call Claude
response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    tools=tools,
    messages=[
        {"role": "user", "content": "Create a quiz about photosynthesis"}
    ]
)

# Process tool use
for block in response.content:
    if block.type == "tool_use":
        tool_name = block.name
        tool_input = block.input
        
        # Execute tool
        if tool_name == "generate_quiz":
            result = generate_quiz(**tool_input)
            
            # Continue conversation with tool result
            follow_up = client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=1024,
                tools=tools,
                messages=[
                    {"role": "user", "content": "Create a quiz about photosynthesis"},
                    {"role": "assistant", "content": response.content},
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "tool_result",
                                "tool_use_id": block.id,
                                "content": result.model_dump_json()
                            }
                        ]
                    }
                ]
            )
            
            print(follow_up.content[0].text)
```

---

## 🎓 Part 5: Best Practices

### 1. Always Close the Loop

Never let a function call hang without sending the result back to the LLM.

**Bad:**
```python
if message.function_call:
    result = my_function()
    # STOP HERE - user never gets a response!
```

**Good:**
```python
if message.function_call:
    result = my_function()
    # Send result back to LLM for final natural language response
    final_response = call_llm_with_result(result)
    return final_response
```

### 2. Validate Everything

Don't trust the LLM to always provide perfect inputs.

```python
def my_function(param: str):
    # Validate first
    if not param or len(param) < 3:
        raise ValueError("param must be at least 3 characters")
    
    # Then process
    return do_work(param)
```

### 3. Handle Errors Gracefully

```python
try:
    result = my_function(**args)
except ValueError as e:
    # Send error back to LLM
    error_message = f"Function failed: {str(e)}"
    # LLM can apologize to user or retry with different params
```

### 4. Log Everything

```python
import logging

def my_function(param: str):
    logging.info(f"my_function called with param={param}")
    result = do_work(param)
    logging.info(f"my_function returned: {result}")
    return result
```

### 5. Use Type Hints

```python
# Good
def my_function(param: str) -> MyOutput:
    return MyOutput(...)

# Bad
def my_function(param):  # What type? Who knows!
    return something  # What type? Mystery!
```

---

## 🔧 Common Patterns

### Pattern 1: CRUD Operations

```python
class TodoItem(BaseModel):
    id: str
    title: str
    completed: bool
    created_at: datetime

def create_todo(title: str) -> TodoItem:
    """Create a new todo item."""
    return TodoItem(id=str(uuid4()), title=title, completed=False, created_at=datetime.now())

def get_todos(user_id: str) -> List[TodoItem]:
    """Get all todos for a user."""
    # Query database
    return [...]

def update_todo(todo_id: str, completed: bool) -> TodoItem:
    """Mark a todo as complete/incomplete."""
    # Update database
    return TodoItem(...)

def delete_todo(todo_id: str) -> dict:
    """Delete a todo."""
    # Delete from database
    return {"success": True, "deleted_id": todo_id}
```

### Pattern 2: External API Calls

```python
def get_weather(city: str, units: Literal["celsius", "fahrenheit"] = "celsius") -> WeatherResult:
    """Fetch current weather for a city."""
    # Call external weather API
    response = requests.get(f"https://api.weather.com/{city}")
    data = response.json()
    
    return WeatherResult(
        city=city,
        temperature=data["temp"],
        conditions=data["conditions"],
        units=units
    )
```

### Pattern 3: Calculations

```python
def calculate_grade(scores: List[float], weights: List[float]) -> GradeResult:
    """Calculate weighted average grade."""
    if len(scores) != len(weights):
        raise ValueError("scores and weights must be same length")
    
    if sum(weights) != 1.0:
        raise ValueError("weights must sum to 1.0")
    
    weighted_score = sum(s * w for s, w in zip(scores, weights))
    
    return GradeResult(
        final_score=weighted_score,
        letter_grade=score_to_letter(weighted_score),
        components=[{"score": s, "weight": w} for s, w in zip(scores, weights)]
    )
```

---

## 🐛 Troubleshooting

### Issue: LLM not calling my function

**Possible causes:**
1. Function description too vague
2. Function name doesn't match user intent
3. System prompt doesn't mention the function

**Solution:**
```python
# Add to system prompt
system_prompt = """
You are a helpful assistant. When users ask about [X], use the [function_name] function.

Example:
User: "Show me the weather"
You should: Call get_weather() function

Do NOT just describe what you would do - actually call the function!
"""
```

### Issue: Validation errors from Pydantic

**Example error:**
```
ValidationError: 1 validation error for QuizResult
total_points
  ensure this value is greater than or equal to 0 (type=value_error.number.not_ge; limit_value=0)
```

**Solution:**
Check your function logic - you're probably returning invalid data.

```python
# Debug by printing before returning
result_data = {
    "topic": topic,
    "questions": questions,
    "total_points": -5  # BUG! This is negative
}
print("DEBUG:", result_data)  # Will show the issue
return QuizResult(**result_data)  # Will fail validation
```

### Issue: Function arguments are wrong type

**Example:**
LLM passes `num_questions="five"` (string) instead of `5` (int)

**Solution:**
Add explicit type coercion:

```python
def my_function(num_questions: int):
    # Coerce to int if possible
    try:
        num_questions = int(num_questions)
    except (ValueError, TypeError):
        raise ValueError(f"num_questions must be an integer, got {type(num_questions)}")
    
    # Now safe to use
    return do_work(num_questions)
```

---

## ✅ Checklist

Before moving on, make sure you can:

- [ ] Write a function schema in JSON
- [ ] Create a Pydantic model with validation
- [ ] Implement a function that returns the model
- [ ] Test the function independently (without LLM)
- [ ] Connect function to OpenAI or Anthropic
- [ ] Handle the complete loop (call → execute → result → response)
- [ ] Add error handling for invalid inputs
- [ ] Log function calls for debugging

---

## 📚 Additional Resources

- **OpenAI Function Calling:** https://platform.openai.com/docs/guides/function-calling
- **Anthropic Tool Use:** https://docs.anthropic.com/claude/docs/tool-use
- **Pydantic Documentation:** https://docs.pydantic.dev/
- **JSON Schema Reference:** https://json-schema.org/

**Next:** Read `structured-outputs-guide.md` for advanced Pydantic patterns!
