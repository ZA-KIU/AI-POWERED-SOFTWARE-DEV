# Function Specification Template

**Team Name:** [Your Team Name]  
**Project:** [Your Project Name]  
**Date:** [Date]

---

## Overview

**Number of Functions:** [2-3 for Lab 5]

**Purpose of Function Calling in Our Project:**

[1-2 sentences explaining why your AI needs function calling. What actions will it take?]

**Example:**
"Our customer service bot needs to check real-time order status, update support tickets, and escalate complex issues to human agents."

---

## Function Calling Flow

Here's how function calling will work in our system:

```
1. User Query → AI receives message
2. AI Decision → Determines if function call needed
3. Function Call → AI generates {"function": "check_order", "arguments": {"order_id": "12345"}}
4. OUR CODE executes → We run check_order("12345") and hit our database
5. Function Result → We send result back to AI as JSON
6. AI Response → AI synthesizes natural language answer with function data
7. User Sees Result → "Your order shipped yesterday and arrives Nov 2nd"
```

**Critical Point:** The LLM does NOT run our functions. It just tells us WHICH function to call and WITH WHAT parameters.

---

## Function 1: [Function Name]

### Basic Information

**Function Name:** `function_name_here`

**Purpose:** [One sentence: what does this function do?]

**When AI Should Call This:**
- [Scenario 1: e.g., "User asks about order status"]
- [Scenario 2: e.g., "User provides an order ID"]
- [Scenario 3: e.g., "User says 'track my order'"]

### Parameters

| Parameter | Type | Required | Validation | Description |
|-----------|------|----------|------------|-------------|
| `param1` | string | Yes | 5-10 alphanumeric chars | Description of what this is |
| `param2` | integer | No | Min: 1, Max: 100 | Description, defaults to 5 |
| `param3` | enum | No | ["option1", "option2"] | Description |

**Example:**
| Parameter | Type | Required | Validation | Description |
|-----------|------|----------|------------|-------------|
| `order_id` | string | Yes | Pattern: ^[A-Z0-9]{5,10}$ | Unique order identifier |
| `include_history` | boolean | No | true/false | Whether to include order history, default: false |

### Return Structure

**On Success:**
```json
{
  "status": "success",
  "data": {
    "field1": "value",
    "field2": 123,
    "field3": ["item1", "item2"]
  }
}
```

**Example:**
```json
{
  "status": "success",
  "data": {
    "order_id": "ABC12345",
    "status": "shipped",
    "estimated_delivery": "2025-11-02",
    "tracking_number": "1Z999AA1",
    "items": ["Widget A", "Gadget B"],
    "total": 149.99
  }
}
```

**On Error:**
```json
{
  "status": "error",
  "error_code": "ORDER_NOT_FOUND",
  "error_message": "No order found with ID ABC12345",
  "details": {}
}
```

### JSON Schema (For the LLM)

```json
{
  "name": "function_name",
  "description": "Clear, specific description of what this function does. Explain when to use it and what it returns.",
  "parameters": {
    "type": "object",
    "properties": {
      "param1": {
        "type": "string",
        "description": "Detailed description of this parameter",
        "pattern": "^[A-Z0-9]{5,10}$"
      },
      "param2": {
        "type": "integer",
        "description": "Detailed description of this parameter",
        "minimum": 1,
        "maximum": 100,
        "default": 5
      }
    },
    "required": ["param1"]
  }
}
```

**Complete Example:**
```json
{
  "name": "check_order_status",
  "description": "Get the current status and details of a customer order by order ID. Returns shipping status, estimated delivery date, tracking number, items, and total cost. Use this when a user asks about their order or wants to track a package.",
  "parameters": {
    "type": "object",
    "properties": {
      "order_id": {
        "type": "string",
        "description": "The unique order identifier (5-10 alphanumeric characters)",
        "pattern": "^[A-Z0-9]{5,10}$"
      },
      "include_history": {
        "type": "boolean",
        "description": "Whether to include full order history (default: false)",
        "default": false
      }
    },
    "required": ["order_id"]
  }
}
```

### Implementation Pseudocode

**What our actual code will do when this function is called:**

```python
def function_name(param1: str, param2: int = 5):
    """
    Step-by-step implementation logic
    """
    # Step 1: Validate input
    if not validate_param1(param1):
        return error_response("INVALID_PARAM1", "...")
    
    # Step 2: Check permissions
    if not user_has_access(current_user, param1):
        return error_response("UNAUTHORIZED", "...")
    
    # Step 3: Query database/API
    result = database.query("SELECT * FROM table WHERE id = ?", param1)
    
    # Step 4: Format response
    return {
        "status": "success",
        "data": {
            "field1": result.field1,
            "field2": result.field2
        }
    }
```

### Example Usage

**User Input:**
```
"What's the status of my order ABC12345?"
```

**AI Generates:**
```json
{
  "function": "check_order_status",
  "arguments": {
    "order_id": "ABC12345",
    "include_history": false
  }
}
```

**Our Code Executes:**
```python
result = check_order_status("ABC12345", include_history=False)
```

**Function Returns:**
```json
{
  "status": "success",
  "data": {
    "order_id": "ABC12345",
    "status": "shipped",
    "estimated_delivery": "2025-11-02",
    "tracking_number": "1Z999AA1"
  }
}
```

**AI Responds to User:**
```
"Your order ABC12345 has shipped! It's on the way and should arrive by 
November 2nd. You can track it with tracking number 1Z999AA1."
```

### Safety Considerations

**Input Validation:**
- [ ] Validate parameter format (regex patterns)
- [ ] Sanitize inputs to prevent injection attacks
- [ ] Check parameter ranges/lengths

**Authorization:**
- [ ] Verify user has permission to access this data
- [ ] Check ownership (user owns this order/document/etc.)
- [ ] Rate limiting per user

**Error Handling:**
- [ ] Never expose internal error details
- [ ] Log all function calls for audit trail
- [ ] Graceful degradation if database/API unavailable

**Specific Safety Rules for This Function:**
1. [e.g., "Always validate order_id matches pattern before querying database"]
2. [e.g., "Only return order info if user_id matches order owner"]
3. [e.g., "Rate limit: 10 calls per minute per user"]

---

## Function 2: [Function Name]

### Basic Information

**Function Name:** `function_name_here`

**Purpose:** [One sentence: what does this function do?]

**When AI Should Call This:**
- [Scenario 1]
- [Scenario 2]
- [Scenario 3]

### Parameters

| Parameter | Type | Required | Validation | Description |
|-----------|------|----------|------------|-------------|
| `param1` | type | Yes/No | validation rules | description |

### Return Structure

**On Success:**
```json
{
  "status": "success",
  "data": {}
}
```

**On Error:**
```json
{
  "status": "error",
  "error_code": "...",
  "error_message": "..."
}
```

### JSON Schema

```json
{
  "name": "function_name",
  "description": "...",
  "parameters": {
    "type": "object",
    "properties": {},
    "required": []
  }
}
```

### Implementation Pseudocode

```python
def function_name(params):
    # Implementation logic
    pass
```

### Example Usage

**User Input:** "..."

**AI Generates:** {...}

**Our Code Executes:** ...

**Function Returns:** {...}

**AI Responds:** "..."

### Safety Considerations

- [ ] Input validation
- [ ] Authorization checks
- [ ] Error handling
- [ ] Rate limiting

---

## Function 3: [Function Name]

[Repeat same structure as Function 2]

---

## Function Calling Implementation Plan

### Week 6: Basic Implementation
- [ ] Set up OpenAI function calling with one simple function
- [ ] Test the complete loop (query → function call → result → response)
- [ ] Handle basic errors

### Week 7: Full Implementation
- [ ] Implement all 2-3 functions
- [ ] Add proper error handling for each
- [ ] Implement authorization/validation

### Week 8: Polish & Testing
- [ ] Test edge cases (invalid inputs, missing data, etc.)
- [ ] Optimize performance (caching, batching)
- [ ] Add logging and monitoring

---

## Error Code Reference

Document all error codes your functions might return:

| Error Code | HTTP Status | Meaning | User-Facing Message |
|------------|-------------|---------|---------------------|
| ORDER_NOT_FOUND | 404 | Order ID doesn't exist | "We couldn't find an order with that ID" |
| UNAUTHORIZED | 403 | User doesn't own this order | "You don't have permission to view this order" |
| INVALID_ORDER_ID | 400 | Order ID format is wrong | "That doesn't look like a valid order ID" |
| DATABASE_ERROR | 500 | Database connection failed | "We're having technical difficulties. Try again soon." |

---

## Testing Strategy

### Unit Tests

**For each function, test:**
- [ ] Valid inputs → correct output
- [ ] Invalid inputs → proper error messages
- [ ] Missing required parameters → error
- [ ] Authorization failures → unauthorized error
- [ ] Database/API failures → graceful degradation

### Integration Tests

**Test the full loop:**
- [ ] User query → AI generates function call → Our code executes → AI responds
- [ ] Multiple function calls in sequence
- [ ] Error recovery (what if function fails?)

### Example Test Cases

**Function 1: check_order_status**
```python
def test_valid_order():
    result = check_order_status("ABC12345")
    assert result["status"] == "success"
    assert "order_id" in result["data"]

def test_invalid_order_id():
    result = check_order_status("invalid!")
    assert result["status"] == "error"
    assert result["error_code"] == "INVALID_ORDER_ID"

def test_unauthorized_access():
    result = check_order_status("DEF67890", user_id="wrong_user")
    assert result["status"] == "error"
    assert result["error_code"] == "UNAUTHORIZED"
```

---

## Performance Metrics

**Target Performance:**
- Function execution time: [e.g., <200ms per call]
- Total query time (including LLM): [e.g., <2 seconds]
- Success rate: [e.g., >99%]
- Error rate: [e.g., <1%]

**Monitoring:**
- [ ] Log every function call (function name, parameters, result, latency)
- [ ] Track success vs error rates
- [ ] Alert if function latency >500ms
- [ ] Dashboard showing function usage stats

---

## Resources

**API Documentation:**
- OpenAI Function Calling: https://platform.openai.com/docs/guides/function-calling
- Anthropic Tool Use: https://docs.anthropic.com/claude/docs/tool-use

**Libraries:**
- [e.g., OpenAI Python SDK, LangChain, etc.]

**Team Responsibilities:**
- Function 1 implementation: [Name]
- Function 2 implementation: [Name]
- Testing & validation: [Name]

---

## Sign-off

**Team Members:**
- [Name 1] - [Contribution]
- [Name 2] - [Contribution]
- [Name 3] - [Contribution]

**Date Completed:** [Date]

**Reviewed By Instructor:** [ ] Yes  [ ] No  [Date: _____ ]

---

## Appendix: Common Patterns

### Pattern 1: Search Functions
Use when: AI needs to search through data
Example: `search_documents(query, filters, max_results)`

### Pattern 2: CRUD Functions
Use when: AI needs to create, read, update, or delete records
Example: `update_ticket(ticket_id, status, notes)`

### Pattern 3: Calculation Functions
Use when: AI needs to perform calculations
Example: `calculate_shipping(origin, destination, weight)`

### Pattern 4: Validation Functions
Use when: AI needs to check if something is valid
Example: `validate_coupon_code(code, user_id)`

### Pattern 5: Escalation Functions
Use when: AI needs to hand off to humans
Example: `escalate_to_human(ticket_id, reason, priority)`
