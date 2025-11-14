# Event Schemas Documentation

**Project:** [Your Project Name]  
**Team:** [Team Name]  
**Last Updated:** [Date]

This document defines the precise JSON schemas for all events in our system. These schemas serve as contracts between components and ensure data consistency.

---

## Schema Format Guidelines

All schemas follow JSON Schema specification (draft-07). Each schema must include:

- **Event type identifier** - Unique name for this event
- **Field definitions** - Name, type, description for each field
- **Required fields** - Which fields must be present
- **Validation rules** - Constraints on field values (length, range, format)
- **Example instance** - At least one realistic example

---

## 1. User Input Event

**Purpose:** Captures user query or command entering the system

**When triggered:** User submits input via frontend interface

**Schema:**
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "title": "UserInputEvent",
  "description": "Event triggered when user submits a query",
  "required": ["event_type", "timestamp", "request_id", "user_query"],
  "properties": {
    "event_type": {
      "type": "string",
      "const": "user_input",
      "description": "Event type identifier"
    },
    "timestamp": {
      "type": "string",
      "format": "date-time",
      "description": "ISO 8601 timestamp when event occurred"
    },
    "request_id": {
      "type": "string",
      "pattern": "^req_[a-zA-Z0-9]{12}$",
      "description": "Unique identifier for this request (for tracing)"
    },
    "user_query": {
      "type": "string",
      "minLength": 1,
      "maxLength": 500,
      "description": "The actual question or command from user"
    },
    "user_id": {
      "type": "string",
      "description": "Unique identifier for the user (optional if no auth)"
    },
    "session_id": {
      "type": "string",
      "description": "Session identifier for conversation tracking"
    },
    "metadata": {
      "type": "object",
      "description": "Additional context (browser, location, etc.)",
      "properties": {
        "user_agent": {"type": "string"},
        "ip_address": {"type": "string"},
        "referrer": {"type": "string"}
      }
    }
  }
}
```

**Example Instance:**
```json
{
  "event_type": "user_input",
  "timestamp": "2025-01-15T10:30:00Z",
  "request_id": "req_abc123def456",
  "user_query": "What were our Q4 sales numbers?",
  "user_id": "user_789",
  "session_id": "session_xyz123",
  "metadata": {
    "user_agent": "Mozilla/5.0...",
    "ip_address": "192.168.1.100",
    "referrer": "https://app.example.com/dashboard"
  }
}
```

---

## 2. LLM Request Event

**Purpose:** Documents request sent to LLM API

**When triggered:** Backend constructs and sends prompt to LLM

**Schema:**
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "title": "LLMRequestEvent",
  "description": "Event triggered when sending request to LLM API",
  "required": ["event_type", "timestamp", "request_id", "model", "messages"],
  "properties": {
    "event_type": {
      "type": "string",
      "const": "llm_request",
      "description": "Event type identifier"
    },
    "timestamp": {
      "type": "string",
      "format": "date-time"
    },
    "request_id": {
      "type": "string",
      "description": "Same request_id from user input (for tracing)"
    },
    "model": {
      "type": "string",
      "enum": ["gpt-4", "gpt-4-turbo", "claude-3-opus", "claude-3-sonnet"],
      "description": "Specific model being called"
    },
    "messages": {
      "type": "array",
      "description": "Array of messages in OpenAI format",
      "items": {
        "type": "object",
        "properties": {
          "role": {"type": "string", "enum": ["system", "user", "assistant"]},
          "content": {"type": "string"}
        }
      }
    },
    "temperature": {
      "type": "number",
      "minimum": 0,
      "maximum": 2,
      "description": "Sampling temperature"
    },
    "max_tokens": {
      "type": "integer",
      "minimum": 1,
      "description": "Maximum tokens to generate"
    },
    "tools": {
      "type": "array",
      "description": "Function calling tools (if applicable)",
      "items": {"type": "object"}
    }
  }
}
```

**Example Instance:**
```json
{
  "event_type": "llm_request",
  "timestamp": "2025-01-15T10:30:01.234Z",
  "request_id": "req_abc123def456",
  "model": "gpt-4-turbo",
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful assistant that answers questions about company sales data."
    },
    {
      "role": "user",
      "content": "What were our Q4 sales numbers?"
    }
  ],
  "temperature": 0.7,
  "max_tokens": 500
}
```

---

## 3. LLM Response Event

**Purpose:** Captures response received from LLM API

**When triggered:** LLM API returns response to backend

**Schema:**
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "title": "LLMResponseEvent",
  "description": "Event triggered when receiving LLM response",
  "required": ["event_type", "timestamp", "request_id", "response_text", "tokens_used", "latency_ms"],
  "properties": {
    "event_type": {
      "type": "string",
      "const": "llm_response"
    },
    "timestamp": {
      "type": "string",
      "format": "date-time"
    },
    "request_id": {
      "type": "string",
      "description": "Same request_id for tracing"
    },
    "response_text": {
      "type": "string",
      "description": "The generated text from LLM"
    },
    "tokens_used": {
      "type": "object",
      "required": ["input_tokens", "output_tokens", "total_tokens"],
      "properties": {
        "input_tokens": {"type": "integer"},
        "output_tokens": {"type": "integer"},
        "total_tokens": {"type": "integer"}
      }
    },
    "latency_ms": {
      "type": "integer",
      "description": "End-to-end API call latency in milliseconds"
    },
    "model": {
      "type": "string",
      "description": "Model that generated response"
    },
    "finish_reason": {
      "type": "string",
      "enum": ["stop", "length", "content_filter", "function_call"],
      "description": "Why generation stopped"
    },
    "tool_calls": {
      "type": "array",
      "description": "Function calls made by LLM (if applicable)",
      "items": {"type": "object"}
    },
    "cost_usd": {
      "type": "number",
      "description": "Calculated cost in USD"
    }
  }
}
```

**Example Instance:**
```json
{
  "event_type": "llm_response",
  "timestamp": "2025-01-15T10:30:03.567Z",
  "request_id": "req_abc123def456",
  "response_text": "Based on our records, Q4 sales were $2.3M, representing a 15% increase over Q3.",
  "tokens_used": {
    "input_tokens": 127,
    "output_tokens": 28,
    "total_tokens": 155
  },
  "latency_ms": 2333,
  "model": "gpt-4-turbo",
  "finish_reason": "stop",
  "cost_usd": 0.00465
}
```

---

## 4. Error Event

**Purpose:** Captures any error that occurs in the system

**When triggered:** Exception caught anywhere in the request pipeline

**Schema:**
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "title": "ErrorEvent",
  "description": "Event triggered when an error occurs",
  "required": ["event_type", "timestamp", "request_id", "error_type", "error_message"],
  "properties": {
    "event_type": {
      "type": "string",
      "const": "error"
    },
    "timestamp": {
      "type": "string",
      "format": "date-time"
    },
    "request_id": {
      "type": "string",
      "description": "Request ID if available (for tracing)"
    },
    "error_type": {
      "type": "string",
      "enum": ["validation_error", "api_error", "database_error", "timeout", "rate_limit", "internal_error"],
      "description": "Category of error"
    },
    "error_message": {
      "type": "string",
      "description": "Human-readable error description"
    },
    "error_code": {
      "type": "string",
      "description": "Machine-readable error code (e.g., HTTP status)"
    },
    "stack_trace": {
      "type": "string",
      "description": "Full stack trace (for debugging, may be omitted in production logs)"
    },
    "component": {
      "type": "string",
      "description": "Which system component threw the error"
    },
    "user_visible": {
      "type": "boolean",
      "description": "Whether this error should be shown to user"
    },
    "retry_possible": {
      "type": "boolean",
      "description": "Whether retrying might succeed"
    }
  }
}
```

**Example Instance:**
```json
{
  "event_type": "error",
  "timestamp": "2025-01-15T10:30:05.123Z",
  "request_id": "req_abc123def456",
  "error_type": "api_error",
  "error_message": "OpenAI API returned 429: Rate limit exceeded",
  "error_code": "429",
  "component": "llm_service",
  "user_visible": true,
  "retry_possible": true
}
```

---

## 5. Retrieval Event (RAG Systems)

**Purpose:** Documents document retrieval for RAG

**When triggered:** System queries vector database for relevant context

**Schema:**
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "title": "RetrievalEvent",
  "description": "Event triggered when retrieving documents for RAG",
  "required": ["event_type", "timestamp", "request_id", "query", "results"],
  "properties": {
    "event_type": {
      "type": "string",
      "const": "retrieval"
    },
    "timestamp": {
      "type": "string",
      "format": "date-time"
    },
    "request_id": {
      "type": "string"
    },
    "query": {
      "type": "string",
      "description": "The query text used for retrieval"
    },
    "embedding_model": {
      "type": "string",
      "description": "Model used to generate query embedding"
    },
    "top_k": {
      "type": "integer",
      "description": "Number of documents requested"
    },
    "results": {
      "type": "array",
      "description": "Retrieved documents",
      "items": {
        "type": "object",
        "properties": {
          "document_id": {"type": "string"},
          "score": {"type": "number"},
          "content": {"type": "string"},
          "metadata": {"type": "object"}
        }
      }
    },
    "latency_ms": {
      "type": "integer",
      "description": "Retrieval latency"
    }
  }
}
```

**Example Instance:**
```json
{
  "event_type": "retrieval",
  "timestamp": "2025-01-15T10:30:01.500Z",
  "request_id": "req_abc123def456",
  "query": "Q4 sales numbers",
  "embedding_model": "text-embedding-ada-002",
  "top_k": 3,
  "results": [
    {
      "document_id": "doc_sales_q4",
      "score": 0.87,
      "content": "Q4 2024 sales totaled $2.3M...",
      "metadata": {"source": "sales_report.pdf", "page": 12}
    },
    {
      "document_id": "doc_sales_summary",
      "score": 0.82,
      "content": "Annual revenue breakdown shows...",
      "metadata": {"source": "annual_report.pdf", "page": 5}
    }
  ],
  "latency_ms": 245
}
```

---

## 6. Tool Call Event (Function Calling)

**Purpose:** Documents function/tool invocation by LLM

**When triggered:** LLM requests to call a function

**Schema:**
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "title": "ToolCallEvent",
  "description": "Event triggered when LLM calls a function",
  "required": ["event_type", "timestamp", "request_id", "tool_name", "tool_arguments"],
  "properties": {
    "event_type": {
      "type": "string",
      "const": "tool_call"
    },
    "timestamp": {
      "type": "string",
      "format": "date-time"
    },
    "request_id": {
      "type": "string"
    },
    "tool_call_id": {
      "type": "string",
      "description": "Unique ID for this specific tool call"
    },
    "tool_name": {
      "type": "string",
      "description": "Name of function being called"
    },
    "tool_arguments": {
      "type": "object",
      "description": "Arguments passed to function"
    },
    "validation_passed": {
      "type": "boolean",
      "description": "Whether arguments passed validation"
    }
  }
}
```

**Example Instance:**
```json
{
  "event_type": "tool_call",
  "timestamp": "2025-01-15T10:30:03.600Z",
  "request_id": "req_abc123def456",
  "tool_call_id": "call_xyz789",
  "tool_name": "get_sales_data",
  "tool_arguments": {
    "quarter": "Q4",
    "year": 2024
  },
  "validation_passed": true
}
```

---

## 7. Tool Result Event (Function Calling)

**Purpose:** Documents function execution result

**When triggered:** Function completes and returns result to LLM

**Schema:**
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "title": "ToolResultEvent",
  "description": "Event triggered when function returns result",
  "required": ["event_type", "timestamp", "request_id", "tool_call_id", "success"],
  "properties": {
    "event_type": {
      "type": "string",
      "const": "tool_result"
    },
    "timestamp": {
      "type": "string",
      "format": "date-time"
    },
    "request_id": {
      "type": "string"
    },
    "tool_call_id": {
      "type": "string",
      "description": "ID of the tool call this result corresponds to"
    },
    "success": {
      "type": "boolean",
      "description": "Whether function executed successfully"
    },
    "result": {
      "type": ["object", "string", "number", "boolean", "array"],
      "description": "The actual result data"
    },
    "error": {
      "type": "string",
      "description": "Error message if success=false"
    },
    "latency_ms": {
      "type": "integer",
      "description": "Function execution time"
    }
  }
}
```

**Example Instance:**
```json
{
  "event_type": "tool_result",
  "timestamp": "2025-01-15T10:30:04.100Z",
  "request_id": "req_abc123def456",
  "tool_call_id": "call_xyz789",
  "success": true,
  "result": {
    "quarter": "Q4",
    "year": 2024,
    "total_sales": 2300000,
    "currency": "USD"
  },
  "latency_ms": 156
}
```

---

## Schema Validation Implementation

### Python (using Pydantic)

```python
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class UserInputEvent(BaseModel):
    event_type: str = Field("user_input", const=True)
    timestamp: datetime
    request_id: str = Field(pattern=r"^req_[a-zA-Z0-9]{12}$")
    user_query: str = Field(min_length=1, max_length=500)
    user_id: Optional[str] = None
    session_id: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "event_type": "user_input",
                "timestamp": "2025-01-15T10:30:00Z",
                "request_id": "req_abc123def456",
                "user_query": "What were our Q4 sales?",
                "user_id": "user_789",
                "session_id": "session_xyz123"
            }
        }
```

### TypeScript (using Zod)

```typescript
import { z } from 'zod';

const UserInputEventSchema = z.object({
  event_type: z.literal('user_input'),
  timestamp: z.string().datetime(),
  request_id: z.string().regex(/^req_[a-zA-Z0-9]{12}$/),
  user_query: z.string().min(1).max(500),
  user_id: z.string().optional(),
  session_id: z.string().optional(),
});

type UserInputEvent = z.infer<typeof UserInputEventSchema>;
```

---

## Event Flow Diagram

[Include a diagram showing how events flow through your system]

```
User Input → Frontend → Backend → [Retrieval?] → LLM Request → LLM Response → [Tool Call?] → [Tool Result?] → Final Response → Frontend → User
     ↓          ↓          ↓            ↓              ↓              ↓             ↓             ↓               ↓              ↓          ↓
  (logged)  (logged)  (logged)     (logged)       (logged)       (logged)      (logged)      (logged)        (logged)       (logged)  (logged)
```

---

## Testing Your Schemas

### Validation Tests

For each schema, test:
1. **Valid instance passes** - Correct data validates successfully
2. **Missing required field fails** - Validation catches missing fields
3. **Invalid type fails** - Wrong types are rejected
4. **Constraint violations fail** - Length/range limits enforced
5. **Optional fields work** - Can be present or absent

### Example Test (Python/Pytest)

```python
def test_user_input_event_validation():
    # Valid instance should pass
    valid_event = {
        "event_type": "user_input",
        "timestamp": "2025-01-15T10:30:00Z",
        "request_id": "req_abc123def456",
        "user_query": "Test query"
    }
    event = UserInputEvent(**valid_event)
    assert event.event_type == "user_input"
    
    # Missing required field should fail
    invalid_event = valid_event.copy()
    del invalid_event["user_query"]
    with pytest.raises(ValidationError):
        UserInputEvent(**invalid_event)
```

---

## Schema Change Management

When updating schemas:

1. **Version your schemas** - Add version field or use separate files
2. **Backwards compatibility** - Don't remove required fields
3. **Migration plan** - Document how to convert old events to new format
4. **Update documentation** - Keep this file current
5. **Test thoroughly** - Validate against real data

---

## Questions & Next Steps

**Questions to address:**
- [ ] Are all schemas complete?
- [ ] Do schemas match actual data?
- [ ] Are validation rules tested?
- [ ] Is tracing implemented (request_id across events)?
- [ ] Are schemas versioned?

**Next steps for Week 8:**
- Implement agent loop events (agent_step, agent_decision, etc.)
- Add retry/backoff events
- Document error recovery flows
- Test schemas with real agent orchestration patterns
