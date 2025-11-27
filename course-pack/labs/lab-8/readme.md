# Lab 8: Building Production-Ready Agents

**Week 10 | Building AI-Powered Applications**

Welcome back from midterm! This lab applies Week 8's concepts on agents and orchestration to your capstone projects. You'll build production-ready agents with proper failure handling, safety policies, and cost controls.

**Lab Duration:** 2 hours in-class + homework integration into capstone  
**Prerequisites:** Completed Labs 6-7 (function calling, streaming), understanding of Week 8 lecture content

---

## Learning Objectives

By the end of this lab, you will:

- Implement a ReAct agent loop for your capstone project
- Add timeouts and retry logic with exponential backoff
- Implement authorization checks for tool functions
- Set up comprehensive audit logging for all agent actions
- Add cost tracking and budget limits to prevent runaway expenses
- Build graceful degradation patterns for agent failures

---

## What's Due This Week

### In-Lab Deliverable: Agent Implementation Plan

Document in your capstone repository at `docs/agent-implementation-plan.md`:

1. **Agent Design** - Which part of your capstone benefits from agent behavior?
2. **Tool Inventory** - List of tools your agent will use
3. **Safety Requirements** - Authorization, validation, and limits needed
4. **Failure Scenarios** - What can go wrong and how you'll handle it

**Due:** End of lab session (submit link to your plan document)

### Homework: Implement Production Agent

By end of Week 10, implement a production-ready agent for your capstone:

1. ReAct loop with max iterations
2. Timeouts on all API calls and tool executions
3. Retry logic with exponential backoff
4. Authorization checks on tools
5. Comprehensive audit logging
6. Cost tracking and limits

**Due:** End of Week 10 (see course calendar)  
**Points:** Part of Capstone ongoing development (contributes to Milestone 3 - Safety Audit)

---

## Why This Matters

**Real-world context:** A buggy agent without proper safeguards can:
- Loop infinitely and drain your entire API budget in minutes ($$$)
- Hang forever waiting for slow APIs (terrible UX)
- Execute unauthorized actions (security breach)
- Fail silently without logs (impossible to debug)

This lab teaches you the **production patterns** that separate toy demos from reliable systems. Every production agent at OpenAI, Anthropic, and Google includes these safeguards.

**Key insight from Week 8 lecture:** Agents cost 5-20x more than simple functions. Without proper controls, you're one bug away from a $10,000 surprise bill.

---

## Pre-Lab Preparation (Do Before Class)

**Required (30 minutes):**

1. **Review Week 8 Lecture Materials**
   - Slides 3-11: Agent patterns and orchestration
   - Slides 12-18: Failure handling and safety policies
   - Slide 26: Cost optimization strategies

2. **Identify Agent Opportunity in Your Capstone**
   - Where does your app need multi-step reasoning?
   - What tasks require tool selection and coordination?
   - Which features would benefit from adaptive behavior?

3. **Install Dependencies**
   ```bash
   pip install tenacity pydantic --break-system-packages
   ```

**Recommended (15 minutes):**

- Review your existing function calling code from Lab 6
- List all tools/functions your agent might need to use
- Think about what could go wrong (timeouts, bad inputs, API failures)

---

## In-Class Activities (2 hours)

### Part 1: Agent Design Workshop (30 min)

**Objective:** Define what your agent will do and which tools it needs.

**Tasks:**
1. **Identify Agent Use Case** (10 min)
   - Discuss with team: where does your capstone need an agent?
   - Examples: research assistant, data analyst, customer support, travel planner
   - Document the user goal your agent will achieve

2. **Design Tool Set** (15 min)
   - List all tools your agent needs (functions from Week 6)
   - Define clear tool descriptions (the agent uses these to choose)
   - Specify parameters and return types
   - Use [Agent Design Template](./templates/agent-design-template.md)

3. **Map Agent Flow** (5 min)
   - Sketch the ReAct loop: Reason → Act → Observe → Repeat
   - Identify exit conditions (success or max iterations)
   - Note where failures might occur

**Deliverable:** Completed agent design section in implementation plan

**Instructor checkpoint:** Before moving to Part 2

---

### Part 2: Implement ReAct Loop (40 min)

**Objective:** Build the core agent loop with proper iteration limits.

**Tasks:**

1. **Code Along: Basic ReAct Loop** (20 min)

Instructor will demonstrate, then you'll implement for your capstone:

```python
class SimpleAgent:
    def __init__(self, tools, max_iterations=5):
        self.tools = tools
        self.max_iterations = max_iterations
    
    def run(self, user_query):
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_query}
        ]
        
        for i in range(self.max_iterations):
            # REASON: Ask LLM what to do next
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=messages,
                tools=self.tools
            )
            
            message = response.choices[0].message
            
            # Check if done (no tool calls)
            if not message.tool_calls:
                return message.content
            
            # ACT: Execute tools
            messages.append(message)
            for tool_call in message.tool_calls:
                result = self._execute_tool(
                    tool_call.function.name,
                    tool_call.function.arguments
                )
                
                # OBSERVE: Add result to conversation
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result
                })
        
        # Max iterations reached
        return "I couldn't complete the task in time. Please try again."
```

**Key concepts:**
- **max_iterations**: Prevents infinite loops (critical!)
- **Conversation history**: Agent maintains context across steps
- **Tool execution loop**: Agent can call multiple tools in one turn

2. **Adapt to Your Capstone** (15 min)
   - Replace tools with your actual functions
   - Update system prompt for your use case
   - Test with a real user query
   - Verify it stops at max_iterations

3. **Test Edge Cases** (5 min)
   - What if tool returns error?
   - What if LLM keeps calling same tool?
   - What if max_iterations reached?

**Deliverable:** Working ReAct loop for your capstone

---

### Part 3: Add Failure Handling (35 min)

**Objective:** Implement timeouts, retries, and circuit breakers.

**Tasks:**

1. **Add Timeouts** (10 min)

Every API call and tool execution needs a timeout:

```python
import requests
from tenacity import retry, stop_after_attempt, wait_exponential

def execute_tool_with_timeout(tool_name, args, timeout=5):
    """Execute tool with timeout."""
    try:
        # For API calls
        if tool_name == "web_search":
            response = requests.get(
                f"https://api.example.com/search",
                params=args,
                timeout=timeout
            )
            return response.json()
        
        # For LLM calls
        elif tool_name == "summarize":
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": args["text"]}],
                timeout=timeout
            )
            return response.choices[0].message.content
            
    except requests.Timeout:
        return {"error": "Request timed out"}
    except Exception as e:
        return {"error": str(e)}
```

**Add timeouts to:**
- LLM API calls (10-30 seconds)
- External API calls (2-5 seconds)
- Database queries (1-3 seconds)
- File operations (5 seconds)

2. **Implement Retry Logic** (15 min)

Use exponential backoff with jitter (from Week 8 Slide 11):

```python
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type
)
import random

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=1, max=10),
    retry=retry_if_exception_type((requests.Timeout, requests.ConnectionError))
)
def call_api_with_retry(url, params):
    """Call API with exponential backoff retry."""
    # Add jitter to prevent thundering herd
    jitter = random.uniform(0, 0.5)
    time.sleep(jitter)
    
    response = requests.get(url, params=params, timeout=5)
    response.raise_for_status()
    return response.json()
```

**Configure retry for:**
- Transient failures (network blips, rate limits)
- Exponential backoff: 1s → 2s → 4s
- Jittered backoff to prevent synchronized retries
- Do NOT retry on 4xx client errors (bad request, unauthorized)

3. **Implement Circuit Breaker** (10 min)

Stop calling broken services (Week 8 Slide 13):

```python
class CircuitBreaker:
    def __init__(self, failure_threshold=5, timeout=60):
        self.failure_count = 0
        self.failure_threshold = failure_threshold
        self.timeout = timeout
        self.last_failure_time = None
        self.state = "CLOSED"  # CLOSED, OPEN, HALF_OPEN
    
    def call(self, func, *args, **kwargs):
        # OPEN: Service is broken, fail fast
        if self.state == "OPEN":
            if time.time() - self.last_failure_time > self.timeout:
                self.state = "HALF_OPEN"
            else:
                raise Exception("Circuit breaker is OPEN")
        
        try:
            result = func(*args, **kwargs)
            
            # Success: Reset if we were testing (HALF_OPEN)
            if self.state == "HALF_OPEN":
                self.state = "CLOSED"
                self.failure_count = 0
            
            return result
            
        except Exception as e:
            self.failure_count += 1
            self.last_failure_time = time.time()
            
            # Too many failures: Open circuit
            if self.failure_count >= self.failure_threshold:
                self.state = "OPEN"
            
            raise e
```

**Apply circuit breakers to:**
- External APIs that might go down
- Database connections
- Third-party services

**Deliverable:** Agent with timeouts, retries, and circuit breaker

**Instructor checkpoint:** Verify failure handling works

---

### Part 4: Add Safety & Logging (15 min)

**Objective:** Implement authorization, validation, and audit logs.

**Tasks:**

1. **Add Authorization Checks** (5 min)

```python
def authorize_tool_call(user_id, tool_name):
    """Check if user is allowed to call this tool."""
    
    # Define permissions
    permissions = {
        "read": ["search", "get_info", "summarize"],
        "write": ["update", "delete", "send_email"],
        "admin": ["delete_all", "system_config"]
    }
    
    user_role = get_user_role(user_id)  # Your auth system
    
    # Check if tool requires restricted permission
    for role, allowed_tools in permissions.items():
        if tool_name in allowed_tools:
            if user_role != role and role != "read":
                raise PermissionError(
                    f"User {user_id} not authorized for {tool_name}"
                )
    
    return True
```

2. **Add Input Validation** (5 min)

Use Pydantic for schema validation:

```python
from pydantic import BaseModel, validator

class SearchInput(BaseModel):
    query: str
    max_results: int = 10
    
    @validator('query')
    def query_not_empty(cls, v):
        if not v or len(v.strip()) == 0:
            raise ValueError('Query cannot be empty')
        return v
    
    @validator('max_results')
    def max_results_in_range(cls, v):
        if v < 1 or v > 100:
            raise ValueError('max_results must be between 1 and 100')
        return v

# Use in tool execution
def search_tool(args):
    validated = SearchInput(**args)  # Raises error if invalid
    return perform_search(validated.query, validated.max_results)
```

3. **Implement Audit Logging** (5 min)

Log everything (Week 8 Slide 17):

```python
import logging
import json
from datetime import datetime

# Configure logger
logging.basicConfig(
    filename='agent_audit.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

def log_agent_action(
    user_id,
    agent_step,
    tool_name,
    tool_args,
    tool_result,
    cost_usd,
    latency_ms
):
    """Log every agent action for audit trail."""
    
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "user_id": user_id,
        "agent_step": agent_step,
        "tool_name": tool_name,
        "tool_args": tool_args,
        "tool_result": str(tool_result)[:200],  # Truncate
        "cost_usd": cost_usd,
        "latency_ms": latency_ms,
        "success": "error" not in str(tool_result).lower()
    }
    
    logging.info(json.dumps(log_entry))
```

**What to log:**
- User query and user ID
- Every tool call with arguments
- Tool results (truncated if large)
- Errors and exceptions
- Cost and latency per step
- Final response to user

**What NOT to log:**
- Passwords or API keys
- Credit card numbers
- Personal health information
- Full user data (only IDs)

**Deliverable:** Agent with authorization, validation, and logging

---

## Homework Assignment

### Core Deliverables (Required)

#### 1. Production-Ready Agent Implementation

Implement a complete agent in your capstone with all safety features:

**Required Components:**

```python
class ProductionAgent:
    """
    Production-ready agent with full safety features.
    """
    
    def __init__(
        self,
        tools,
        max_iterations=5,
        timeout_per_tool=5,
        cost_limit_usd=1.0
    ):
        self.tools = tools
        self.max_iterations = max_iterations
        self.timeout_per_tool = timeout_per_tool
        self.cost_limit_usd = cost_limit_usd
        self.total_cost = 0
        self.circuit_breakers = {}  # Per-tool circuit breakers
        self.logger = self._setup_logger()
    
    def run(self, user_id, user_query):
        """
        Execute agent with all safety features.
        
        Returns:
            dict: {
                "success": bool,
                "result": str,
                "cost_usd": float,
                "steps_taken": int,
                "errors": list
            }
        """
        # Implementation with all features from lab
        pass
    
    def _execute_tool_safely(self, user_id, tool_name, args):
        """Execute tool with authorization, timeout, retry, logging."""
        pass
    
    def _check_cost_limit(self):
        """Prevent runaway costs."""
        if self.total_cost >= self.cost_limit_usd:
            raise Exception(f"Cost limit ${self.cost_limit_usd} exceeded")
    
    def _setup_logger(self):
        """Configure audit logging."""
        pass
```

**Must Include:**
- [ ] ReAct loop with `max_iterations` (prevent infinite loops)
- [ ] Timeouts on ALL API calls and tool executions
- [ ] Retry logic with exponential backoff + jitter
- [ ] Circuit breakers for external services
- [ ] Authorization checks before tool execution
- [ ] Input validation with Pydantic schemas
- [ ] Comprehensive audit logging (JSON format)
- [ ] Cost tracking with hard limits
- [ ] Graceful degradation on failures
- [ ] Structured error responses

**Where to put it:** `src/agent/production_agent.py` or similar

---

#### 2. Agent Safety Documentation

Create `docs/agent-safety.md` with:

**Required Sections:**

**Tool Authorization Matrix**

| Tool Name | Required Permission | Justification |
|-----------|---------------------|---------------|
| search_web | read | Public data access |
| send_email | write | Modifies external state |
| delete_user | admin | Destructive action |

**Failure Scenarios & Handling**

Document at least 5 failure scenarios:

1. **Scenario:** API timeout
   - **Detection:** Timeout exception after 5s
   - **Handling:** Retry with exponential backoff (3 attempts)
   - **User Impact:** 10-15s delay, graceful error message
   - **Fallback:** Return cached result if available

2. **Scenario:** Infinite loop (agent keeps calling same tool)
   - **Detection:** max_iterations reached
   - **Handling:** Stop execution, return partial result
   - **User Impact:** "I couldn't complete the task" message
   - **Fallback:** Suggest user refine query

[...document 3 more scenarios...]

**Cost Controls**

- Per-request limit: $X
- Per-user daily limit: $Y
- Global monthly limit: $Z
- Alert thresholds: 80% of limits
- What happens when limit reached: [describe]

**Audit Log Schema**

```json
{
  "timestamp": "2025-01-15T10:30:00Z",
  "user_id": "user_123",
  "session_id": "session_456",
  "agent_step": 3,
  "tool_name": "search_web",
  "tool_args": {"query": "AI safety"},
  "tool_result_summary": "Found 10 results",
  "cost_usd": 0.002,
  "latency_ms": 850,
  "success": true,
  "error": null
}
```

**Security Considerations**

- How you prevent prompt injection
- How you sanitize tool inputs
- How you protect sensitive data in logs
- How you enforce authorization

---

#### 3. Agent Testing Suite

Create `tests/test_agent_safety.py` with unit tests:

```python
import pytest
from src.agent.production_agent import ProductionAgent

def test_max_iterations_prevents_infinite_loop():
    """Agent stops after max_iterations."""
    agent = ProductionAgent(tools=[], max_iterations=3)
    
    # Mock LLM that always wants to call tools
    result = agent.run("user_1", "infinite query")
    
    assert result["steps_taken"] <= 3
    assert "couldn't complete" in result["result"].lower()

def test_timeout_on_slow_tool():
    """Tool execution times out after limit."""
    # Test that slow tools are killed after timeout
    pass

def test_retry_on_transient_failure():
    """Transient failures trigger retry."""
    # Test that network errors retry 3 times
    pass

def test_circuit_breaker_opens_after_failures():
    """Circuit breaker stops calling broken service."""
    # Test that after 5 failures, circuit opens
    pass

def test_unauthorized_tool_call_blocked():
    """Users can't call unauthorized tools."""
    # Test that read-only user can't call delete tool
    pass

def test_cost_limit_enforced():
    """Agent stops when cost limit reached."""
    agent = ProductionAgent(tools=[], cost_limit_usd=0.10)
    
    # Simulate expensive operations
    # Assert agent stops before exceeding limit
    pass

def test_audit_log_created():
    """All agent actions are logged."""
    # Test that log file contains expected entries
    pass
```

**Minimum 7 tests:**
1. Max iterations prevents infinite loop
2. Timeouts work on slow tools
3. Retry logic handles transient failures
4. Circuit breaker opens after repeated failures
5. Authorization blocks unauthorized tools
6. Cost limit stops execution
7. Audit logs are created

**Where to put it:** `tests/test_agent_safety.py`

---

#### 4. Update Project README

Add "Agent Architecture" section to your main README.md:

```markdown
## Agent Architecture

### Overview
Our application uses a production-ready ReAct agent to [describe what your agent does].

### Agent Flow
1. **Reason**: LLM analyzes user query and decides which tool to use
2. **Act**: Agent executes tool with safety checks
3. **Observe**: Agent examines tool result
4. **Repeat**: Continue until goal achieved or max iterations

### Available Tools
- `search_docs`: Search internal documentation
- `analyze_data`: Process and analyze datasets
- `generate_report`: Create formatted reports

### Safety Features
- ✅ Max 5 iterations to prevent infinite loops
- ✅ 5-second timeout on all tool executions
- ✅ Exponential backoff retry on transient failures
- ✅ Circuit breakers on external APIs
- ✅ Authorization checks (read/write/admin roles)
- ✅ Input validation with Pydantic
- ✅ Comprehensive audit logging
- ✅ $1 per-request cost limit

### Monitoring
- Audit logs: `logs/agent_audit.log`
- Error tracking: Check logs for `"success": false`
- Cost dashboard: [link if you built one]

### Known Limitations
- Agent may not complete complex multi-step tasks in 5 iterations
- External API timeouts can cause delays
- Circuit breaker may block requests for 60s after failures
```

---

## Detailed Requirements

### Code Quality Standards

**Agent Implementation:**
- [ ] Type hints on all functions
- [ ] Docstrings with parameter and return descriptions
- [ ] Error handling on every external call
- [ ] No hardcoded values (use config file)
- [ ] Graceful degradation (never crash, always respond)

**Testing:**
- [ ] All tests pass
- [ ] Tests cover failure scenarios (not just happy path)
- [ ] Mock external APIs (don't make real calls in tests)
- [ ] Tests run in under 10 seconds total

**Documentation:**
- [ ] Clear English (no AI jargon without explanation)
- [ ] Concrete examples for each failure scenario
- [ ] Screenshots or logs where helpful
- [ ] Honest about limitations

---

### Grading Rubric

**Implementation Quality (40%)**
- Outstanding (90-100%): All 10 safety features implemented, tested, working perfectly
- Good (80-89%): 8-9 features implemented, minor bugs
- Acceptable (70-79%): 6-7 features implemented, some issues
- Needs Improvement (<70%): <6 features or major bugs

**Safety & Reliability (30%)**
- Outstanding: Handles all failure scenarios gracefully, never crashes, comprehensive logging
- Good: Handles most failures, occasional issues, adequate logging
- Acceptable: Basic error handling, some failures not handled
- Needs Improvement: Poor error handling, crashes on failures

**Documentation (20%)**
- Outstanding: Thorough safety doc, all failure scenarios documented, clear testing strategy
- Good: Good documentation, most scenarios covered
- Acceptable: Basic documentation, some gaps
- Needs Improvement: Minimal or unclear documentation

**Testing (10%)**
- Outstanding: 7+ tests, all passing, covers edge cases
- Good: 5-6 tests, all passing
- Acceptable: 3-4 tests, mostly passing
- Needs Improvement: <3 tests or tests failing

**Bonus Points:**
- Monitoring dashboard for agent actions (+5%)
- Load testing with concurrent users (+5%)
- Novel safety feature specific to your use case (+10%)
- Demonstration of agent preventing actual security issue (+10%)

---

## Common Pitfalls to Avoid

### ❌ "Agents are just fancy functions"
No! Agents reason, adapt, and coordinate tools. If you're not using multi-step reasoning, you don't need an agent.

### ❌ "I'll add safety features later"
Safety must be built in from the start. Retrofitting is painful and error-prone.

### ❌ "My agent won't loop infinitely"
Yes it will. Eventually. Always set max_iterations.

### ❌ "I don't need timeouts for fast APIs"
All APIs are fast until they're not. Networks fail. Services go down. Always timeout.

### ❌ "I'll just catch Exception and retry"
Don't retry 4xx client errors (bad request, unauthorized). Only retry transient 5xx/network errors.

### ❌ "Logging is just for debugging"
Audit logs are for security, compliance, and analytics too. Log everything (except secrets).

### ❌ "Cost limits are overkill for my app"
One bug, one infinite loop = $10,000 bill. Always set limits.

### ❌ "My authorization checks are in the prompt"
NEVER trust the agent. Enforce permissions at the system level, not in prompts.

---

## FAQ

### Q: Do we need an agent for our capstone?

A: If your app needs multi-step reasoning or adaptive behavior, yes. If it's simple input→function→output, no. Agents are for complex tasks where the path isn't predetermined.

### Q: Can we use LangChain or other frameworks?

A: Yes, but you must still implement all safety features. Framework defaults often lack production safeguards. Document which features the framework provides vs. what you added.

### Q: What if our agent legitimately needs >5 iterations?

A: Increase max_iterations with justification. Document why. Consider if the task is too complex and should be broken down.

### Q: How do we test timeout logic without waiting 5 seconds?

A: Mock slow functions to return immediately but simulate timeout behavior. Use `pytest`'s mock features.

### Q: Should we implement ALL the safety features even if our agent is simple?

A: Yes. This lab teaches production patterns. Even simple agents need timeouts, logging, and cost limits. Consider it training for your career.

### Q: What if our agent doesn't use external APIs?

A: It still uses LLM APIs. Those need timeouts, retries, and cost tracking. If you have no tools at all, you don't have an agent.

### Q: Can we use Redis/database for circuit breaker state?

A: Yes, that's more production-ready than in-memory. Document the decision. For this lab, in-memory is acceptable.

### Q: How much should we log?

A: Every agent step, every tool call, every error. Logs are cheap, debugging without them is expensive.

---

## Resources

**In This Lab Folder:**
- [Agent Design Template](./templates/agent-design-template.md)
- [Tool Schema Template](./templates/tool-schema-template.md)
- [Safety Checklist](./templates/safety-checklist.md)
- [ReAct Loop Guide](./guides/react-loop-guide.md)
- [Timeout & Retry Guide](./guides/timeout-retry-guide.md)
- [Authorization Patterns](./guides/authorization-guide.md)
- [Audit Logging Best Practices](./guides/audit-logging-guide.md)
- [Cost Tracking Guide](./guides/cost-tracking-guide.md)

**External Resources:**
- Week 8 Lecture Slides (especially Slides 3-18, 26)
- Tenacity library docs: https://tenacity.readthedocs.io/
- Pydantic validation: https://docs.pydantic.dev/
- OpenAI function calling: https://platform.openai.com/docs/guides/function-calling
- AWS Circuit Breaker pattern: https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/

---

## Checklist: Ready to Submit?

**Agent Implementation:**
- [ ] ReAct loop implemented with max_iterations
- [ ] Timeouts on all external calls
- [ ] Retry logic with exponential backoff + jitter
- [ ] Circuit breakers on flaky services
- [ ] Authorization checks enforced
- [ ] Input validation with Pydantic
- [ ] Audit logging to file/database
- [ ] Cost tracking with hard limits
- [ ] Graceful error handling (never crashes)
- [ ] Code is tested and working

**Documentation:**
- [ ] `docs/agent-safety.md` complete
- [ ] Tool authorization matrix filled out
- [ ] 5+ failure scenarios documented
- [ ] Cost controls specified
- [ ] Audit log schema defined
- [ ] README updated with agent architecture

**Testing:**
- [ ] `tests/test_agent_safety.py` created
- [ ] 7+ tests written
- [ ] All tests passing
- [ ] Tests cover failure scenarios

**Quality Checks:**
- [ ] No API keys in code
- [ ] No secrets in logs
- [ ] Type hints on all functions
- [ ] Docstrings on classes and methods
- [ ] Code is readable and well-organized

---

## What's Next?

**Week 11: Evaluation & Observability**
- You'll use your audit logs to analyze agent performance
- Evaluation frameworks will measure agent success rates
- Observability patterns will help you monitor production agents

**Week 12: Production Engineering**
- Your agent will be deployed with CI/CD
- Monitoring dashboards will track agent metrics
- Production secrets management will secure your tools

**Week 15: Final Demo**
- Your production-ready agent is a major demo feature
- "Built an agent with 99.9% reliability" is impressive
- Safety features demonstrate professional engineering

Remember: The patterns you learn here—timeouts, retries, circuit breakers, authorization, audit logging—apply to ANY distributed system, not just AI agents. These are fundamental software engineering skills.

Good luck building your production agent!
