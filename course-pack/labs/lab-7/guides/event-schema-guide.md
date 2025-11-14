# Event Schema Design Guide

This guide teaches you how to design robust event schemas for AI applications.

## Why Schemas Matter

Without schemas: `TypeError: Cannot read property 'tokens' of undefined`  
With schemas: Clear contracts that prevent bugs and enable debugging.

## Core Principles

1. **Be Specific** - Not "data": "string", but "user_query": {"type": "string", "max_length": 500}
2. **Document Everything** - Type, description, constraints, examples
3. **Plan for Errors** - Schema success AND failure cases
4. **Enable Tracing** - Include request_id, timestamp, component fields

## JSON Schema Basics

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["field1", "field2"],
  "properties": {
    "field1": {"type": "string", "minLength": 1, "maxLength": 500},
    "field2": {"type": "integer", "minimum": 0}
  }
}
```

## Implementation

**Python (Pydantic):**
```python
from pydantic import BaseModel, Field

class UserInputEvent(BaseModel):
    event_type: str = Field("user_input", const=True)
    timestamp: datetime
    request_id: str
    user_query: str = Field(min_length=1, max_length=500)
```

**TypeScript (Zod):**
```typescript
import { z } from 'zod';

const UserInputEvent = z.object({
  event_type: z.literal('user_input'),
  timestamp: z.string().datetime(),
  request_id: z.string(),
  user_query: z.string().min(1).max(500),
});
```

## Common Mistakes

❌ Vague names: "data", "result", "info"  
✅ Specific names: "user_query", "llm_response_text", "token_usage"

❌ No validation: {"query": {"type": "string"}}  
✅ With validation: {"query": {"type": "string", "minLength": 1, "maxLength": 500}}

❌ No examples  
✅ Include realistic examples

## Checklist

- [ ] Every field has type and description
- [ ] Required fields marked
- [ ] Validation constraints added
- [ ] Consistent naming (snake_case recommended)
- [ ] Examples provided
- [ ] Tested with real data

See event-schema-template.md for complete examples.
