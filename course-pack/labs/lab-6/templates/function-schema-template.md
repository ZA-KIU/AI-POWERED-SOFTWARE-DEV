# Function Schema Template

**Purpose:** Define functions that your LLM can call to interact with external systems, databases, APIs, or perform computations.

---

## Basic Function Template

```python
from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum

# Step 1: Define Pydantic model for parameters
class [FunctionName]Params(BaseModel):
    """
    Clear description of what this function does and when to use it.
    """
    param1: str = Field(
        description="Detailed description of this parameter",
        min_length=1,  # Validation rules
        max_length=100
    )
    param2: int = Field(
        default=5,
        description="Description with default value",
        ge=1,  # greater than or equal to
        le=20  # less than or equal to
    )
    param3: Optional[str] = Field(
        default=None,
        description="Optional parameter"
    )

# Step 2: Implement the function
def [function_name](params: [FunctionName]Params) -> dict:
    """
    Execute the function logic.
    
    Args:
        params: Validated parameters
        
    Returns:
        Dictionary with results and metadata
    """
    try:
        # Your logic here
        result = perform_action(params.param1, params.param2, params.param3)
        
        return {
            "success": True,
            "result": result,
            "metadata": {
                "timestamp": datetime.now().isoformat(),
                "params_used": params.dict()
            }
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "error_type": type(e).__name__
        }

# Step 3: Define schema for LLM
[FUNCTION_NAME]_SCHEMA = {
    "type": "function",
    "function": {
        "name": "[function_name]",
        "description": "Clear, detailed description that tells the LLM WHEN to use this function. Include examples of user queries that should trigger this function.",
        "parameters": {
            "type": "object",
            "properties": {
                "param1": {
                    "type": "string",
                    "description": "What is this parameter? What format should it be in?"
                },
                "param2": {
                    "type": "integer",
                    "description": "What does this control? What are good values?",
                    "default": 5
                },
                "param3": {
                    "type": "string",
                    "description": "Optional parameter for...",
                    "enum": ["option1", "option2", "option3"]  # If applicable
                }
            },
            "required": ["param1"]  # Only truly required fields
        }
    }
}
```

---

## Example 1: Search Knowledge Base

```python
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class SearchKnowledgeBaseParams(BaseModel):
    """
    Search the product documentation knowledge base for relevant information.
    Use this when the user asks questions about:
    - Product features
    - How-to guides
    - Troubleshooting
    - Company policies
    """
    query: str = Field(
        description="The search query. Be specific and include key terms from the user's question."
    )
    limit: int = Field(
        default=5,
        ge=1,
        le=20,
        description="Maximum number of results to return. Use 3-5 for specific questions, 10-20 for broader queries."
    )
    filter_category: Optional[str] = Field(
        default=None,
        description="Optionally filter by category: 'getting-started', 'api', 'troubleshooting', 'billing'"
    )
    minimum_relevance: float = Field(
        default=0.7,
        ge=0.0,
        le=1.0,
        description="Minimum relevance score threshold (0.0-1.0). Higher = more strict."
    )

def search_knowledge_base(params: SearchKnowledgeBaseParams) -> dict:
    """
    Search vector database for relevant documents.
    """
    try:
        # Generate query embedding
        query_embedding = generate_embedding(params.query)
        
        # Perform vector search
        results = vector_db.search(
            embedding=query_embedding,
            limit=params.limit,
            filter_category=params.filter_category,
            min_score=params.minimum_relevance
        )
        
        return {
            "success": True,
            "results": [
                {
                    "text": result.text,
                    "source": result.metadata['source'],
                    "score": result.score,
                    "category": result.metadata['category']
                }
                for result in results
            ],
            "count": len(results),
            "query": params.query,
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"Search failed: {str(e)}",
            "results": [],
            "count": 0
        }

SEARCH_KNOWLEDGE_BASE_SCHEMA = {
    "type": "function",
    "function": {
        "name": "search_knowledge_base",
        "description": """Search our product documentation knowledge base for information. 
        
        Use this function when the user:
        - Asks "How do I..." questions
        - Wants to know about product features
        - Needs troubleshooting help
        - Asks about company policies or procedures
        
        Examples:
        - "How do I reset my password?"
        - "What are the API rate limits?"
        - "Tell me about the premium features"
        """,
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query extracted from the user's question"
                },
                "limit": {
                    "type": "integer",
                    "description": "Number of results (1-20, default 5)",
                    "default": 5
                },
                "filter_category": {
                    "type": "string",
                    "description": "Filter by category if user mentions specific area",
                    "enum": ["getting-started", "api", "troubleshooting", "billing", null]
                },
                "minimum_relevance": {
                    "type": "number",
                    "description": "Relevance threshold 0.0-1.0 (default 0.7)",
                    "default": 0.7
                }
            },
            "required": ["query"]
        }
    }
}
```

---

## Example 2: Get User Context

```python
from pydantic import BaseModel, Field
from typing import Optional

class GetUserContextParams(BaseModel):
    """
    Retrieve user profile and preferences for personalization.
    """
    user_id: str = Field(
        description="The unique user identifier"
    )
    include_history: bool = Field(
        default=False,
        description="Whether to include conversation history"
    )

def get_user_context(params: GetUserContextParams) -> dict:
    """
    Fetch user data from database.
    """
    try:
        user = database.get_user(params.user_id)
        
        context = {
            "name": user.name,
            "preferences": user.preferences,
            "subscription_level": user.subscription_level,
            "account_status": user.status
        }
        
        if params.include_history:
            context["recent_queries"] = database.get_recent_queries(
                user_id=params.user_id,
                limit=5
            )
        
        return {
            "success": True,
            "user_context": context,
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"Could not fetch user context: {str(e)}"
        }

GET_USER_CONTEXT_SCHEMA = {
    "type": "function",
    "function": {
        "name": "get_user_context",
        "description": """Retrieve user profile and preferences for personalization.
        
        Use this when you need to:
        - Personalize responses based on user preferences
        - Check user's subscription level
        - Reference user's past interactions
        
        DO NOT use this for every query - only when personalization is relevant.
        """,
        "parameters": {
            "type": "object",
            "properties": {
                "user_id": {
                    "type": "string",
                    "description": "The user's unique identifier"
                },
                "include_history": {
                    "type": "boolean",
                    "description": "Include recent conversation history (adds latency)",
                    "default": False
                }
            },
            "required": ["user_id"]
        }
    }
}
```

---

## Best Practices

### 1. Clear Descriptions
**Bad:** "Search for stuff"  
**Good:** "Search the product documentation knowledge base for information about features, policies, and troubleshooting. Use when the user asks 'how do I' questions or needs specific product information."

### 2. Include Examples
Add examples of when to use the function:
```python
"description": """Search knowledge base.

Use when user asks:
- "How do I reset my password?"
- "What are the API limits?"
- "Tell me about premium features"

Don't use for:
- General knowledge questions
- Math calculations
- Current events
"""
```

### 3. Appropriate Defaults
```python
limit: int = Field(default=5)  # Good - reasonable default
limit: int = Field(default=1000)  # Bad - way too many results
```

### 4. Validation Rules
```python
age: int = Field(ge=0, le=150)  # Reasonable age range
email: str = Field(regex=r'^[\w\.-]+@[\w\.-]+\.\w+$')  # Email format
percentage: float = Field(ge=0.0, le=1.0)  # Percentage as decimal
```

### 5. Error Handling
Always return structured responses:
```python
# Good - structured error
return {
    "success": False,
    "error": "Database connection timeout after 5 seconds",
    "error_type": "TimeoutError",
    "retry_recommended": True
}

# Bad - raw exception
raise Exception("something broke")
```

---

## Multiple Functions Example

```python
# Collection of all your functions
TOOLS = [
    SEARCH_KNOWLEDGE_BASE_SCHEMA,
    GET_USER_CONTEXT_SCHEMA,
    # Add more functions here
]

# Use in LLM call
response = client.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    tools=TOOLS,
    tool_choice="auto"  # Let LLM decide which to use
)
```

---

## Testing Your Functions

```python
# Test each function independently
def test_search_knowledge_base():
    params = SearchKnowledgeBaseParams(
        query="how to reset password",
        limit=5
    )
    result = search_knowledge_base(params)
    
    assert result["success"] == True
    assert len(result["results"]) > 0
    assert "text" in result["results"][0]
    assert "score" in result["results"][0]
    
    print("✅ Search function works!")

# Test parameter validation
def test_param_validation():
    try:
        # This should fail
        params = SearchKnowledgeBaseParams(
            query="",  # Empty query
            limit=100  # Over limit
        )
        assert False, "Should have raised validation error"
    except ValidationError:
        print("✅ Validation works!")

if __name__ == "__main__":
    test_search_knowledge_base()
    test_param_validation()
```

---

## Common Patterns

### Pattern 1: Database Query
```python
class QueryDatabase(BaseModel):
    table: str
    filters: dict
    limit: int = 100

def query_database(params: QueryDatabase) -> dict:
    # Sanitize input!
    # Use parameterized queries!
    results = db.query(params.table, params.filters, params.limit)
    return {"results": results}
```

### Pattern 2: External API Call
```python
class CallExternalAPI(BaseModel):
    endpoint: str
    method: str = "GET"
    body: Optional[dict] = None

def call_external_api(params: CallExternalAPI) -> dict:
    response = requests.request(
        method=params.method,
        url=params.endpoint,
        json=params.body,
        timeout=5
    )
    return {"status": response.status_code, "data": response.json()}
```

### Pattern 3: Calculation/Transformation
```python
class CalculateMetric(BaseModel):
    metric_name: str
    start_date: str
    end_date: str

def calculate_metric(params: CalculateMetric) -> dict:
    data = fetch_data(params.start_date, params.end_date)
    value = compute_metric(data, params.metric_name)
    return {"metric": params.metric_name, "value": value}
```

---

## Checklist Before Adding Function

- [ ] Clear, specific function name
- [ ] Comprehensive description with examples
- [ ] Pydantic model for parameters
- [ ] Validation rules on all parameters
- [ ] Appropriate defaults
- [ ] Error handling implemented
- [ ] Returns structured response
- [ ] Schema defined for LLM
- [ ] Unit tests written
- [ ] Documented in README

---

Remember: Functions give your LLM **hands** to interact with the world. Make them reliable, well-documented, and easy to use!
