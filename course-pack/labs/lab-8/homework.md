# Lab 8 Homework Assignment

**Building AI-Powered Applications | Due: End of Week 10**

This homework focuses on implementing production-ready safety features for your capstone project, including comprehensive failure handling and audit logging.

**Points:** Part of Capstone ongoing development (contributes to Milestone 3 - Safety & Evaluation Audit, Week 11)  
**Due Date:** [Check course calendar for exact deadline]  
**Submission:** Update your capstone GitHub repository

---

## Choose Your Path: Agent vs. Non-Agent Implementation

**CRITICAL DECISION:** Not all applications need an agent. Choose based on your actual requirements.

### Path A: Agent Implementation (ReAct Loop)

**Choose this if your capstone needs:**
- ✅ Multi-step reasoning (user asks question → agent searches → analyzes → generates report)
- ✅ Adaptive behavior (agent decides which tools to use based on context)
- ✅ Unknown number of steps (can't predict how many API calls needed)
- ✅ Dynamic tool selection (agent picks from 3+ possible tools)

**Examples:**
- Research assistant that searches, analyzes, and synthesizes
- Travel planner that checks flights, hotels, weather, and makes recommendations
- Data analyst that explores datasets, runs queries, and generates insights
- Customer support that searches docs, checks account, and resolves issues

**What you'll implement:**
- Full ProductionAgent class with ReAct loop
- All 10 safety features from Week 8
- Tool orchestration and decision-making

---

### Path B: Non-Agent Implementation (Direct Function Calling)

**Choose this if your capstone is:**
- ✅ Predictable workflow (always: extract info → call API → format response)
- ✅ Single function call (or fixed sequence of calls)
- ✅ No adaptation needed (same process for every request)
- ✅ Simple tool selection (always call the same function)

**Examples:**
- Document summarizer (extract text → summarize → return)
- Translation service (detect language → translate → format)
- Image analyzer (upload → analyze → describe)
- Sentiment analyzer (extract text → classify → return score)

**What you'll implement:**
- Production-ready function calling system
- Same safety features but adapted for direct calls
- Simpler orchestration but still production-grade

---

### Decision Matrix

| Question | Yes = Agent | No = Direct Calls |
|----------|-------------|-------------------|
| Does user's request require multiple steps to answer? | Agent | Either |
| Do you need to decide which tool to use at runtime? | Agent | Direct |
| Can the number of API calls vary significantly? | Agent | Direct |
| Does context from one call inform the next? | Agent | Either |
| Do you have 3+ different tools to choose from? | Agent | Either |
| Is the workflow always predictable? | Either | Direct |

**When in doubt:** Start with direct function calling. It's simpler, faster, and cheaper. You can always upgrade to an agent later if needed.

---

### Both Paths Require the Same Safety Features

**Regardless of which path you choose, you MUST implement:**

1. ✅ **Timeouts** - All external calls must have timeouts
2. ✅ **Retry Logic** - Exponential backoff on transient failures
3. ✅ **Authorization** - Check permissions before tool execution
4. ✅ **Input Validation** - Pydantic schemas for all inputs
5. ✅ **Audit Logging** - JSON logs for all operations
6. ✅ **Cost Tracking** - Monitor and limit API costs
7. ✅ **Error Handling** - Graceful degradation, never crash
8. ✅ **Circuit Breakers** - Stop calling broken services (if external APIs)
9. ✅ **Testing** - 7+ unit tests covering failures
10. ✅ **Documentation** - Safety docs and README

**The patterns are the same. The complexity differs.**

---

## What You Need to Do

### Core Deliverables (Required)

**First: Document your choice in your capstone repo's `docs/architecture-decision.md`:**

```markdown
# Architecture Decision: Agent vs. Direct Function Calling

**Decision:** [Agent / Direct Function Calling]

**Rationale:**
[Explain why this choice makes sense for your application]

**Justification:**
- [Reason 1: e.g., "Our workflow is always: extract → analyze → format"]
- [Reason 2: e.g., "We only ever call one function per request"]
- [Reason 3: e.g., "Adding agent would increase costs 5-10x with no benefit"]

**Trade-offs Considered:**
- **Advantages:** [What you gain from this choice]
- **Disadvantages:** [What you're giving up]

**Future Considerations:**
[When might you need to switch? What would trigger that decision?]
```

---

#### PATH A: Production Agent Implementation

**Choose this path if you selected "Agent" above.**

#### 1A. Production Agent Class

Implement a complete agent class with all safety features from Week 8 lecture.

**File Location:** `src/agent/production_agent.py` (or equivalent for your tech stack)

**Required Class Structure:**

```python
class ProductionAgent:
    """
    Production-ready AI agent with comprehensive safety features.
    
    Features:
    - ReAct loop with iteration limits
    - Timeouts on all operations
    - Exponential backoff retry
    - Circuit breakers for external services
    - Authorization enforcement
    - Input validation
    - Audit logging
    - Cost tracking and limits
    """
    
    def __init__(
        self,
        tools: List[Tool],
        max_iterations: int = 5,
        timeout_per_tool: int = 5,
        cost_limit_usd: float = 1.0,
        user_id: str = None
    ):
        """
        Initialize production agent.
        
        Args:
            tools: List of available tools/functions
            max_iterations: Maximum ReAct loop iterations
            timeout_per_tool: Timeout in seconds for tool execution
            cost_limit_usd: Maximum cost per agent run
            user_id: User ID for authorization and logging
        """
        self.tools = tools
        self.max_iterations = max_iterations
        self.timeout_per_tool = timeout_per_tool
        self.cost_limit_usd = cost_limit_usd
        self.user_id = user_id
        
        self.total_cost = 0.0
        self.circuit_breakers = {}
        self.conversation_history = []
        self.audit_logger = self._setup_audit_logger()
    
    def run(self, user_query: str) -> dict:
        """
        Execute agent with full safety features.
        
        Args:
            user_query: The user's input query/request
            
        Returns:
            dict: {
                "success": bool,
                "result": str,
                "cost_usd": float,
                "steps_taken": int,
                "tool_calls": list,
                "errors": list,
                "execution_time_ms": int
            }
        """
        start_time = time.time()
        errors = []
        tool_calls_made = []
        
        try:
            # Initialize conversation
            self.conversation_history = [
                {"role": "system", "content": self._get_system_prompt()},
                {"role": "user", "content": user_query}
            ]
            
            # ReAct loop
            for iteration in range(self.max_iterations):
                # Check cost limit before each iteration
                self._check_cost_limit()
                
                # REASON: Get LLM decision
                response = self._call_llm_with_safety()
                
                # Log LLM call
                self._log_llm_call(iteration, response)
                
                # Check if agent is done (no tool calls)
                if not hasattr(response, 'tool_calls') or not response.tool_calls:
                    result = response.content
                    break
                
                # ACT: Execute each tool call
                self.conversation_history.append(response)
                
                for tool_call in response.tool_calls:
                    tool_result = self._execute_tool_safely(
                        tool_call.function.name,
                        tool_call.function.arguments,
                        tool_call.id
                    )
                    
                    tool_calls_made.append({
                        "name": tool_call.function.name,
                        "args": tool_call.function.arguments,
                        "result": str(tool_result)[:200]
                    })
                    
                    # OBSERVE: Add tool result to conversation
                    self.conversation_history.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": json.dumps(tool_result)
                    })
            
            else:
                # Max iterations reached
                result = "I couldn't complete your request within the time limit. Please try rephrasing or breaking it into smaller tasks."
                errors.append("max_iterations_reached")
            
            execution_time = int((time.time() - start_time) * 1000)
            
            return {
                "success": len(errors) == 0 or errors == ["max_iterations_reached"],
                "result": result,
                "cost_usd": round(self.total_cost, 4),
                "steps_taken": iteration + 1,
                "tool_calls": tool_calls_made,
                "errors": errors,
                "execution_time_ms": execution_time
            }
            
        except Exception as e:
            self.audit_logger.error(f"Agent execution failed: {str(e)}")
            return {
                "success": False,
                "result": "I encountered an error processing your request.",
                "cost_usd": round(self.total_cost, 4),
                "steps_taken": iteration if 'iteration' in locals() else 0,
                "tool_calls": tool_calls_made,
                "errors": [str(e)],
                "execution_time_ms": int((time.time() - start_time) * 1000)
            }
    
    def _execute_tool_safely(
        self,
        tool_name: str,
        tool_args: str,
        tool_call_id: str
    ) -> dict:
        """
        Execute tool with all safety checks.
        
        Implements:
        - Authorization checks
        - Input validation
        - Timeout
        - Retry with exponential backoff
        - Circuit breaker
        - Audit logging
        - Cost tracking
        """
        start_time = time.time()
        
        try:
            # 1. Authorization check
            self._authorize_tool(tool_name)
            
            # 2. Parse and validate arguments
            args = json.loads(tool_args)
            validated_args = self._validate_tool_args(tool_name, args)
            
            # 3. Check circuit breaker
            if not self._check_circuit_breaker(tool_name):
                raise Exception(f"Circuit breaker OPEN for {tool_name}")
            
            # 4. Execute with timeout and retry
            result = self._execute_with_timeout_and_retry(
                tool_name,
                validated_args
            )
            
            # 5. Track cost
            cost = self._calculate_tool_cost(tool_name, validated_args, result)
            self.total_cost += cost
            
            # 6. Log successful execution
            latency_ms = int((time.time() - start_time) * 1000)
            self._log_tool_execution(
                tool_name,
                validated_args,
                result,
                cost,
                latency_ms,
                success=True
            )
            
            # 7. Update circuit breaker (success)
            self._record_circuit_breaker_success(tool_name)
            
            return result
            
        except Exception as e:
            # Log failure
            latency_ms = int((time.time() - start_time) * 1000)
            self._log_tool_execution(
                tool_name,
                tool_args,
                {"error": str(e)},
                0,
                latency_ms,
                success=False
            )
            
            # Update circuit breaker (failure)
            self._record_circuit_breaker_failure(tool_name)
            
            return {"error": str(e)}
    
    def _call_llm_with_safety(self) -> Any:
        """Call LLM with timeout and cost tracking."""
        # Implementation required
        pass
    
    def _authorize_tool(self, tool_name: str):
        """Check if user is authorized to call this tool."""
        # Implementation required
        pass
    
    def _validate_tool_args(self, tool_name: str, args: dict) -> dict:
        """Validate tool arguments against schema."""
        # Implementation required
        pass
    
    def _check_circuit_breaker(self, tool_name: str) -> bool:
        """Check if circuit breaker allows call."""
        # Implementation required
        pass
    
    def _execute_with_timeout_and_retry(
        self,
        tool_name: str,
        args: dict
    ) -> dict:
        """Execute tool with timeout and exponential backoff retry."""
        # Implementation required
        pass
    
    def _calculate_tool_cost(
        self,
        tool_name: str,
        args: dict,
        result: dict
    ) -> float:
        """Calculate cost of tool execution."""
        # Implementation required
        pass
    
    def _check_cost_limit(self):
        """Raise exception if cost limit exceeded."""
        if self.total_cost >= self.cost_limit_usd:
            raise Exception(
                f"Cost limit ${self.cost_limit_usd} exceeded. "
                f"Current cost: ${self.total_cost:.4f}"
            )
    
    def _setup_audit_logger(self) -> logging.Logger:
        """Configure audit logger to file."""
        # Implementation required
        pass
    
    def _log_tool_execution(
        self,
        tool_name: str,
        args: Any,
        result: Any,
        cost: float,
        latency_ms: int,
        success: bool
    ):
        """Log tool execution to audit log."""
        # Implementation required
        pass
    
    def _record_circuit_breaker_success(self, tool_name: str):
        """Record successful call for circuit breaker."""
        # Implementation required
        pass
    
    def _record_circuit_breaker_failure(self, tool_name: str):
        """Record failed call for circuit breaker."""
        # Implementation required
        pass
    
    def _get_system_prompt(self) -> str:
        """Get system prompt for your specific agent."""
        # Implementation required - customize for your use case
        pass
```

**Must Implement:**

✅ **ReAct Loop (Week 8 Slide 5)**
- Reason → Act → Observe loop
- `max_iterations` to prevent infinite loops
- Track conversation history across iterations
- Exit when no tool calls or max iterations reached

✅ **Timeouts (Week 8 Slide 10)**
- Connection timeout: 2-5s for establishing connection
- Read timeout: 10-30s for LLM calls, 5s for tool calls
- Use `timeout` parameter in all `requests` and `openai` calls
- Catch `TimeoutError` and handle gracefully

✅ **Retry Logic (Week 8 Slide 11)**
- Exponential backoff: 1s → 2s → 4s → 8s
- Jittered backoff: Add random 0-0.5s to prevent thundering herd
- Maximum 3 retry attempts
- Only retry on transient errors (5xx, network errors, timeouts)
- DO NOT retry on 4xx client errors

✅ **Circuit Breakers (Week 8 Slide 13)**
- States: CLOSED (working), OPEN (broken), HALF_OPEN (testing)
- Open circuit after 5 consecutive failures
- Stay open for 60 seconds timeout period
- Test with one request in HALF_OPEN state
- Implement per-tool (different services have different reliability)

✅ **Authorization (Week 8 Slide 15)**
- Define permission levels: read, write, admin
- Map tools to required permissions
- Check user role before EVERY tool execution
- Never trust agent to enforce authorization
- Raise `PermissionError` if unauthorized

✅ **Input Validation (Week 8 Slide 16)**
- Use Pydantic models for tool argument schemas
- Validate types, ranges, formats
- Sanitize inputs (remove SQL injection attempts, XSS)
- Provide clear error messages on validation failure

✅ **Audit Logging (Week 8 Slide 17)**
- Log to file: `logs/agent_audit.log`
- JSON format for easy parsing
- Log every LLM call and tool execution
- Include: timestamp, user_id, tool_name, args, result, cost, latency, success
- DO NOT log: passwords, API keys, credit cards, PII

✅ **Cost Tracking (Week 8 Slide 18)**
- Track tokens and API costs
- Accumulate across all steps in agent run
- Check against limit before each LLM call
- Raise exception when limit exceeded
- Log final cost in audit log

✅ **Graceful Degradation (Week 8 Slide 19)**
- Agent NEVER crashes - always returns a response
- On timeout: "Taking longer than expected..."
- On max iterations: "Couldn't complete in time..."
- On error: "Encountered an issue..."
- Include error details in logs (but not in user-facing response)

✅ **Error Handling**
- Try-except on all external calls
- Specific exception handling (not just `except Exception`)
- Log full stack traces
- Return structured error responses

---

#### PATH B: Production Function Calling System

**Choose this path if you selected "Direct Function Calling" above.**

#### 1B. Production Function Calling Class

If your application doesn't need an agent, implement a simpler but still production-ready function calling system.

**File Location:** `src/functions/production_function_caller.py` (or equivalent)

**Required Class Structure:**

```python
class ProductionFunctionCaller:
    """
    Production-ready function calling system without ReAct loop.
    
    For applications with predictable workflows that don't need
    multi-step reasoning or dynamic tool selection.
    
    Features:
    - Single or fixed-sequence function calls
    - Timeouts on all operations
    - Exponential backoff retry
    - Circuit breakers for external services
    - Authorization enforcement
    - Input validation
    - Audit logging
    - Cost tracking and limits
    """
    
    def __init__(
        self,
        functions: List[Function],
        timeout_per_function: int = 5,
        cost_limit_usd: float = 0.50,
        user_id: str = None
    ):
        """
        Initialize production function caller.
        
        Args:
            functions: List of available functions
            timeout_per_function: Timeout in seconds for function execution
            cost_limit_usd: Maximum cost per request
            user_id: User ID for authorization and logging
        """
        self.functions = {f.name: f for f in functions}
        self.timeout_per_function = timeout_per_function
        self.cost_limit_usd = cost_limit_usd
        self.user_id = user_id
        
        self.total_cost = 0.0
        self.circuit_breakers = {}
        self.audit_logger = self._setup_audit_logger()
    
    def execute(
        self,
        user_query: str,
        workflow: List[str] = None
    ) -> dict:
        """
        Execute function(s) with full safety features.
        
        Args:
            user_query: The user's input query/request
            workflow: Optional fixed sequence of function names
                     If None, LLM decides which function to call
            
        Returns:
            dict: {
                "success": bool,
                "result": str,
                "cost_usd": float,
                "functions_called": list,
                "errors": list,
                "execution_time_ms": int
            }
        """
        start_time = time.time()
        errors = []
        functions_called = []
        
        try:
            # Check cost limit
            self._check_cost_limit()
            
            if workflow:
                # Fixed workflow: Call functions in sequence
                result = self._execute_workflow(user_query, workflow)
            else:
                # Dynamic: Let LLM decide which function to call
                result = self._execute_with_llm_selection(user_query)
            
            execution_time = int((time.time() - start_time) * 1000)
            
            return {
                "success": len(errors) == 0,
                "result": result,
                "cost_usd": round(self.total_cost, 4),
                "functions_called": functions_called,
                "errors": errors,
                "execution_time_ms": execution_time
            }
            
        except Exception as e:
            self.audit_logger.error(f"Execution failed: {str(e)}")
            return {
                "success": False,
                "result": "I encountered an error processing your request.",
                "cost_usd": round(self.total_cost, 4),
                "functions_called": functions_called,
                "errors": [str(e)],
                "execution_time_ms": int((time.time() - start_time) * 1000)
            }
    
    def _execute_workflow(
        self,
        user_query: str,
        workflow: List[str]
    ) -> str:
        """
        Execute fixed sequence of functions.
        
        Example workflow:
        1. extract_entities(user_query)
        2. search_database(entities)
        3. format_response(results)
        """
        context = {"user_query": user_query}
        
        for function_name in workflow:
            # Execute each function in sequence
            result = self._execute_function_safely(
                function_name,
                context
            )
            
            # Update context with result
            context[f"{function_name}_result"] = result
        
        # Return final result
        return context.get("final_result") or str(result)
    
    def _execute_with_llm_selection(self, user_query: str) -> str:
        """
        Let LLM decide which function to call (single call).
        
        Unlike agent, this makes ONE function call decision, not loop.
        """
        # Check cost
        self._check_cost_limit()
        
        # Get LLM function call decision
        response = self._call_llm_with_safety(user_query)
        
        # Extract function call
        if hasattr(response, 'tool_calls') and response.tool_calls:
            tool_call = response.tool_calls[0]  # Take first call only
            
            # Execute function
            result = self._execute_function_safely(
                tool_call.function.name,
                json.loads(tool_call.function.arguments)
            )
            
            # Optional: Let LLM format the result
            formatted = self._format_result_with_llm(user_query, result)
            return formatted
        else:
            # No function call needed, return LLM response
            return response.content
    
    def _execute_function_safely(
        self,
        function_name: str,
        args: dict
    ) -> dict:
        """
        Execute function with all safety checks.
        
        Implements:
        - Authorization checks
        - Input validation
        - Timeout
        - Retry with exponential backoff
        - Circuit breaker
        - Audit logging
        - Cost tracking
        """
        start_time = time.time()
        
        try:
            # 1. Authorization check
            self._authorize_function(function_name)
            
            # 2. Validate arguments
            validated_args = self._validate_function_args(function_name, args)
            
            # 3. Check circuit breaker
            if not self._check_circuit_breaker(function_name):
                raise Exception(f"Circuit breaker OPEN for {function_name}")
            
            # 4. Execute with timeout and retry
            result = self._execute_with_timeout_and_retry(
                function_name,
                validated_args
            )
            
            # 5. Track cost
            cost = self._calculate_function_cost(function_name, validated_args, result)
            self.total_cost += cost
            
            # 6. Log successful execution
            latency_ms = int((time.time() - start_time) * 1000)
            self._log_function_execution(
                function_name,
                validated_args,
                result,
                cost,
                latency_ms,
                success=True
            )
            
            # 7. Update circuit breaker (success)
            self._record_circuit_breaker_success(function_name)
            
            return result
            
        except Exception as e:
            # Log failure
            latency_ms = int((time.time() - start_time) * 1000)
            self._log_function_execution(
                function_name,
                args,
                {"error": str(e)},
                0,
                latency_ms,
                success=False
            )
            
            # Update circuit breaker (failure)
            self._record_circuit_breaker_failure(function_name)
            
            return {"error": str(e)}
    
    # Same safety methods as agent (timeout, retry, circuit breaker, etc.)
    def _call_llm_with_safety(self, user_query: str) -> Any:
        """Call LLM with timeout and cost tracking."""
        pass
    
    def _authorize_function(self, function_name: str):
        """Check if user is authorized to call this function."""
        pass
    
    def _validate_function_args(self, function_name: str, args: dict) -> dict:
        """Validate function arguments against schema."""
        pass
    
    def _check_circuit_breaker(self, function_name: str) -> bool:
        """Check if circuit breaker allows call."""
        pass
    
    def _execute_with_timeout_and_retry(
        self,
        function_name: str,
        args: dict
    ) -> dict:
        """Execute function with timeout and exponential backoff retry."""
        pass
    
    def _calculate_function_cost(
        self,
        function_name: str,
        args: dict,
        result: dict
    ) -> float:
        """Calculate cost of function execution."""
        pass
    
    def _check_cost_limit(self):
        """Raise exception if cost limit exceeded."""
        if self.total_cost >= self.cost_limit_usd:
            raise Exception(
                f"Cost limit ${self.cost_limit_usd} exceeded. "
                f"Current cost: ${self.total_cost:.4f}"
            )
    
    def _setup_audit_logger(self) -> logging.Logger:
        """Configure audit logger to file."""
        pass
    
    def _log_function_execution(
        self,
        function_name: str,
        args: Any,
        result: Any,
        cost: float,
        latency_ms: int,
        success: bool
    ):
        """Log function execution to audit log."""
        pass
    
    def _record_circuit_breaker_success(self, function_name: str):
        """Record successful call for circuit breaker."""
        pass
    
    def _record_circuit_breaker_failure(self, function_name: str):
        """Record failed call for circuit breaker."""
        pass
```

**Must Implement (Same as Agent, Adapted):**

✅ **Predictable Execution** (instead of ReAct loop)
- Fixed workflow OR single LLM function call decision
- No iteration limit needed (no loop)
- Track execution sequence
- Exit after function(s) complete

✅ **Timeouts** (Week 8 Slide 10)
- Same as agent: 2-5s connect, 5-30s read
- Apply to both LLM calls and function execution

✅ **Retry Logic** (Week 8 Slide 11)
- Same exponential backoff: 1s → 2s → 4s
- Same jitter: random 0-0.5s
- Maximum 3 attempts
- Only retry transient errors

✅ **Circuit Breakers** (Week 8 Slide 13)
- Same states: CLOSED/OPEN/HALF_OPEN
- Open after 5 consecutive failures
- 60 second timeout
- Per-function tracking

✅ **Authorization** (Week 8 Slide 15)
- Same permission levels: read/write/admin
- Check before EVERY function call
- Never trust LLM to enforce

✅ **Input Validation** (Week 8 Slide 16)
- Same Pydantic schemas
- Validate all function arguments

✅ **Audit Logging** (Week 8 Slide 17)
- Same JSON format
- Log every function execution
- Same fields: timestamp, user_id, function_name, cost, latency

✅ **Cost Tracking** (Week 8 Slide 18)
- Same limits: $0.50 per request default
- Track LLM + function costs
- Stop when exceeded

✅ **Graceful Degradation** (Week 8 Slide 19)
- Never crash
- Return error messages on failure
- Log details for debugging

✅ **Error Handling**
- Same try-except patterns
- Specific exception handling
- Structured error responses

---

### Why Path B is Simpler but Still Production-Grade

**What you save:**
- ❌ No ReAct loop complexity
- ❌ No iteration tracking
- ❌ No "max_iterations" logic
- ❌ No conversation history management
- ❌ Fewer LLM calls (usually 1-2 vs 3-10)

**What you keep:**
- ✅ All safety features (timeouts, retry, circuit breakers)
- ✅ Authorization and validation
- ✅ Audit logging
- ✅ Cost tracking
- ✅ Production-ready error handling

**Result:**
- 50-70% less code
- 5-10x lower costs (fewer LLM calls)
- 2-3x faster response times
- Same reliability and safety
- Easier to test and debug

**When to upgrade to agent:**
- User requests become more complex
- You need adaptive behavior
- Workflow can't be predicted in advance
- You're calling 5+ different functions dynamically

---

## Deliverable 2: Safety Documentation

**Both paths require the same documentation.**

**File Location:** `docs/agent-safety.md`

**Required Sections:**

```markdown
# Agent Safety Documentation

## Overview

Brief description of your agent and its purpose.

## Tool Authorization Matrix

| Tool Name | Permission Level | Justification | Risk Level |
|-----------|------------------|---------------|------------|
| search_documents | read | Queries internal docs, no modifications | Low |
| update_database | write | Modifies data, requires user permission | Medium |
| delete_account | admin | Destructive, requires admin rights | High |
| send_email | write | External communication, potential for spam | Medium |

Permission Levels:
- **read**: Public or user-owned data access
- **write**: Modifies data or sends communications
- **admin**: System-level changes, destructive actions

## Failure Scenarios & Handling

### Scenario 1: LLM API Timeout

**Trigger:** API call exceeds 30-second timeout

**Detection:**
```python
except openai.Timeout as e:
    # Log timeout
    logger.warning(f"LLM API timeout: {e}")
```

**Handling:**
- Retry with exponential backoff (3 attempts)
- If all retries fail, return cached response or error message

**User Impact:**
- First timeout: 30s delay, automatic retry
- Second timeout: 60s total delay, automatic retry
- Third timeout: ~120s total, error message shown

**Fallback:**
- Return last successful response if available
- Suggest user rephrase or simplify query
- Log incident for investigation

**Recovery:**
- Circuit breaker may open if repeated timeouts
- Automatic recovery when service responds

---

### Scenario 2: Infinite Loop (Agent repeats same action)

**Trigger:** Agent calls same tool with same arguments multiple times

**Detection:**
```python
if iteration >= max_iterations:
    logger.warning("Max iterations reached")
    return partial_result
```

**Handling:**
- Stop execution at max_iterations (5)
- Return partial results if available
- Log loop detection for prompt engineering improvements

**User Impact:**
- Agent stops after ~30-60 seconds
- Message: "I couldn't complete the task within time limits"
- Suggest breaking into smaller tasks

**Fallback:**
- No fallback - hard stop required
- Return any partial progress made

**Prevention:**
- Improve system prompts to avoid loops
- Add loop detection (same tool + args called 2+ times)
- Review audit logs to identify loop patterns

---

### Scenario 3: Unauthorized Tool Access Attempt

**Trigger:** User with 'read' permission tries to call 'delete' tool

**Detection:**
```python
if user_role != required_role:
    raise PermissionError(f"Unauthorized: {tool_name}")
```

**Handling:**
- Immediately reject tool call
- Log security incident
- Return error to agent (not user directly)

**User Impact:**
- Transparent to user (agent handles gracefully)
- May result in "I don't have permission to do that" message
- No system access granted

**Fallback:**
- Agent should suggest authorized alternative
- Example: "I can search for that information instead"

**Security:**
- Log includes: user_id, attempted_tool, timestamp
- Alert on repeated unauthorized attempts (potential attack)
- Review logs weekly for security audit

---

### Scenario 4: External API Down (Circuit Breaker Opens)

**Trigger:** 5 consecutive failures to external search API

**Detection:**
```python
if circuit_breaker.state == "OPEN":
    return cached_results or error_response
```

**Handling:**
- Circuit breaker opens, blocks requests for 60s
- After 60s, enters HALF_OPEN, tries one test request
- If success, returns to CLOSED; if failure, re-opens

**User Impact:**
- First 5 failures: Retry delays (exponential backoff)
- After circuit opens: Immediate failure responses
- 60s wait before service is retried

**Fallback:**
- Return cached results if available
- Use alternative data source if configured
- Show: "Search service temporarily unavailable"

**Recovery:**
- Automatic after timeout period
- Manual reset option for admin
- Alert sent to monitoring system

---

### Scenario 5: Cost Limit Exceeded

**Trigger:** Accumulated cost reaches $1.00 limit

**Detection:**
```python
if self.total_cost >= self.cost_limit_usd:
    raise CostLimitError("Budget exceeded")
```

**Handling:**
- Immediately stop agent execution
- Return partial results if useful
- Log cost details for review

**User Impact:**
- Agent stops mid-execution
- Message: "Processing budget exhausted for this request"
- No additional API calls made

**Fallback:**
- Return any partial results generated
- Suggest user simplify query
- For premium users: Higher limits available

**Prevention:**
- Set per-user daily limits
- Alert at 80% of limit
- Review high-cost queries monthly

---

## Cost Controls

### Per-Request Limits
- Single agent run: $1.00 maximum
- Average expected cost: $0.10-0.30
- Alert threshold: $0.80 (80%)

### Per-User Limits
- Free tier: $5.00/day, $50/month
- Premium tier: $50/day, $500/month
- Enterprise: Custom limits

### Global Limits
- $10,000/month across all users
- Alert at $8,000 (80%)
- Hard stop at $10,000

### Cost Breakdown by Component
- LLM calls: ~60-70% of costs
- Tool executions (API calls): ~20-30%
- Data processing: ~5-10%

### What Happens When Limit Reached
1. Agent execution stops immediately
2. Partial results returned if available
3. User notified of limit
4. Incident logged with cost details
5. Admin alerted if global limit

### Cost Optimization Strategies
- Cache common queries (60% cost reduction)
- Use cheaper models for simple tasks (see Week 10 Lab)
- Batch similar requests
- Implement request deduplication

---

## Audit Log Schema

```json
{
  "timestamp": "2025-01-15T14:30:00.000Z",
  "log_type": "tool_execution",
  "user_id": "user_abc123",
  "session_id": "session_xyz789",
  "agent_step": 3,
  "tool_name": "search_documents",
  "tool_args": {
    "query": "AI safety best practices",
    "max_results": 10
  },
  "tool_result_summary": "Found 8 relevant documents",
  "tool_result_truncated": true,
  "cost_usd": 0.0023,
  "latency_ms": 847,
  "success": true,
  "error": null,
  "retry_count": 0,
  "circuit_breaker_state": "CLOSED"
}
```

### Log Retention
- Keep logs for 90 days
- Archive after 90 days for compliance
- Delete after 1 year unless flagged

### Log Analysis
- Daily: Review errors and failures
- Weekly: Analyze cost trends
- Monthly: Security audit of unauthorized attempts

---

## Security Considerations

### Prompt Injection Prevention
- Separate user content from system instructions
- Validate all user inputs before passing to LLM
- Use delimiters to mark user content clearly
- Never execute code from LLM responses without validation

### Input Sanitization
- Strip special characters from queries
- Validate URLs before fetching
- Escape SQL in database queries
- HTML encode outputs

### Sensitive Data Protection
- Never log passwords, API keys, credit cards
- Redact PII from logs (use user IDs not names/emails)
- Encrypt audit logs at rest
- Secure log file permissions (owner read/write only)

### Authorization Enforcement
- Check permissions at function level (not prompt level)
- Use middleware/decorators for consistent enforcement
- Log all authorization failures
- Review failed auth attempts weekly

### Rate Limiting
- 100 requests/hour per user (free tier)
- 1000 requests/hour per user (premium tier)
- Block IPs with >500 failed auths per day

---

## Testing Strategy

### Unit Tests
- Each safety feature has dedicated tests
- Mock external APIs (no real calls in tests)
- Test failure scenarios (not just happy path)
- Target: 80%+ code coverage

### Integration Tests
- End-to-end agent runs
- Real API calls in staging environment
- Test with realistic user queries
- Verify audit logs created

### Load Tests
- 10 concurrent users
- 100 requests/minute
- Monitor: latency, error rate, cost
- Target: <2s p95 latency, <1% error rate

### Security Tests
- Attempt unauthorized tool access
- Inject malicious prompts
- Try SQL injection in tool args
- Verify all blocked and logged

---

## Monitoring & Alerts

### Key Metrics
- Agent success rate (target: >95%)
- Average latency (target: <3s)
- Cost per request (target: <$0.50)
- Error rate (target: <5%)

### Alert Conditions
- Error rate >10% for 5 minutes → Page on-call
- Cost >$1,000 in 1 hour → Immediate alert
- Circuit breaker opened → Notification
- >100 unauthorized attempts/day → Security alert

### Dashboards
- Real-time agent activity
- Cost tracking by user/tool
- Error rates and types
- Circuit breaker states

---

## Known Limitations

1. **Complex multi-step tasks may fail**
   - Mitigation: Set max_iterations=10 for premium users
   - User guidance: Break into smaller requests

2. **External API dependencies**
   - Mitigation: Circuit breakers, fallbacks, caching
   - User impact: Occasional delays or cached results

3. **Cost limits may stop long-running tasks**
   - Mitigation: Increase limits for premium users
   - User guidance: Simplify queries or upgrade plan

4. **Agent may not always pick optimal tool**
   - Mitigation: Improve tool descriptions, add examples
   - Ongoing: Monitor and refine prompts

---

## Incident Response

### If Agent Causes Harm
1. Immediately disable agent (kill switch)
2. Investigate audit logs
3. Identify root cause
4. Notify affected users
5. Implement fix and additional safeguards
6. Document incident and learnings

### If Cost Runaway
1. Hit emergency stop (global cost limit)
2. Review logs for responsible requests
3. Identify bug or abuse
4. Refund users if system error
5. Adjust cost limits if needed

### If Security Breach
1. Disable affected user accounts
2. Review audit logs for unauthorized access
3. Assess data exposure
4. Notify security team and affected users
5. Implement additional authorization checks
6. Report to relevant authorities if required

---

## Compliance

### GDPR
- Users can request data deletion
- Audit logs anonymized after 30 days
- Clear consent for data processing

### SOC 2
- Audit logs retained for 90 days
- Access controls enforced
- Security incidents logged and reviewed

### Industry Best Practices
- OWASP Top 10 mitigations implemented
- Regular security audits
- Penetration testing annually
```

---

## Deliverable 3: Testing Suite

**Both paths require comprehensive testing.**

#### 3A. Agent Testing (If You Chose Path A)

**File Location:** `tests/test_agent_safety.py`

**Minimum Required Tests (7):**

```python
import pytest
import time
from unittest.mock import Mock, patch, MagicMock
from src.agent.production_agent import ProductionAgent

class TestAgentSafety:
    
    @pytest.fixture
    def agent(self):
        """Create agent instance for testing."""
        tools = [
            {
                "type": "function",
                "function": {
                    "name": "search",
                    "description": "Search for information",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "query": {"type": "string"}
                        }
                    }
                }
            }
        ]
        return ProductionAgent(
            tools=tools,
            max_iterations=3,
            timeout_per_tool=2,
            cost_limit_usd=0.50,
            user_id="test_user"
        )
    
    def test_max_iterations_prevents_infinite_loop(self, agent):
        """
        Test that agent stops after max_iterations to prevent infinite loops.
        
        Simulates an LLM that always wants to call tools (never returns
        final answer), which would loop forever without iteration limit.
        """
        # Mock LLM to always return tool calls
        with patch('openai.ChatCompletion.create') as mock_llm:
            mock_response = Mock()
            mock_response.tool_calls = [Mock(
                id="call_1",
                function=Mock(name="search", arguments='{"query":"test"}')
            )]
            mock_response.content = None
            mock_llm.return_value.choices = [Mock(message=mock_response)]
            
            result = agent.run("Keep searching forever")
            
            assert result["success"] == False or "couldn't complete" in result["result"].lower()
            assert result["steps_taken"] <= agent.max_iterations
            assert "max_iterations" in result.get("errors", []) or \
                   "max_iterations" in result["result"]
    
    def test_timeout_on_slow_tool(self, agent):
        """
        Test that slow tool executions are killed after timeout.
        
        Simulates a tool that takes too long (network delay, slow API).
        Should timeout and retry, then eventually return error.
        """
        # Mock slow tool that exceeds timeout
        with patch.object(agent, '_execute_with_timeout_and_retry') as mock_execute:
            import requests
            mock_execute.side_effect = requests.Timeout("Tool took too long")
            
            result = agent._execute_tool_safely(
                "slow_tool",
                '{"arg": "value"}',
                "call_123"
            )
            
            assert "error" in result
            assert "timeout" in str(result["error"]).lower() or \
                   "took too long" in str(result["error"]).lower()
    
    def test_retry_on_transient_failure(self, agent):
        """
        Test that transient network failures trigger retry with backoff.
        
        Simulates a flaky API that fails twice then succeeds.
        Should retry with exponential backoff and eventually succeed.
        """
        # Mock API that fails twice then succeeds
        call_count = 0
        
        def flaky_api(*args, **kwargs):
            nonlocal call_count
            call_count += 1
            if call_count < 3:
                raise ConnectionError("Network error")
            return {"status": "success", "data": "result"}
        
        with patch.object(agent, '_execute_tool') as mock_tool:
            mock_tool.side_effect = flaky_api
            
            # This should retry and eventually succeed
            result = agent._execute_with_timeout_and_retry("api_tool", {})
            
            assert call_count == 3  # Failed twice, succeeded on 3rd
            assert result["status"] == "success"
    
    def test_circuit_breaker_opens_after_failures(self, agent):
        """
        Test that circuit breaker opens after repeated failures.
        
        After 5 consecutive failures, circuit should open and block
        requests immediately without attempting call.
        """
        tool_name = "failing_service"
        
        # Cause 5 consecutive failures
        for i in range(5):
            agent._record_circuit_breaker_failure(tool_name)
        
        # Circuit should now be OPEN
        is_open = not agent._check_circuit_breaker(tool_name)
        
        assert is_open, "Circuit breaker should be OPEN after 5 failures"
        
        # Verify that tool calls are blocked
        result = agent._execute_tool_safely(
            tool_name,
            '{"arg": "value"}',
            "call_456"
        )
        
        assert "error" in result
        assert "circuit" in str(result["error"]).lower() or \
               "breaker" in str(result["error"]).lower()
    
    def test_unauthorized_tool_call_blocked(self, agent):
        """
        Test that users cannot call tools they don't have permission for.
        
        User with 'read' permission should not be able to call
        'delete' or other 'admin' tools.
        """
        # Mock user with read-only permissions
        agent.user_id = "readonly_user"
        
        with patch.object(agent, '_get_user_role') as mock_role:
            mock_role.return_value = "read"
            
            # Attempt to call admin tool
            with pytest.raises(PermissionError):
                agent._authorize_tool("delete_all_data")
            
            # Read tools should work
            try:
                agent._authorize_tool("search_documents")
                authorized = True
            except PermissionError:
                authorized = False
            
            assert authorized, "Read tools should be authorized for read users"
    
    def test_cost_limit_enforced(self, agent):
        """
        Test that agent stops when cost limit is reached.
        
        Agent should track costs and stop execution when limit
        exceeded, preventing runaway expenses.
        """
        # Set low cost limit
        agent.cost_limit_usd = 0.10
        agent.total_cost = 0
        
        # Mock expensive tool calls
        def expensive_tool(*args, **kwargs):
            agent.total_cost += 0.05
            return {"result": "data"}
        
        with patch.object(agent, '_execute_tool') as mock_tool:
            mock_tool.side_effect = expensive_tool
            
            # First call: $0.05 (under limit)
            agent._execute_tool_safely("tool1", '{}', "call_1")
            assert agent.total_cost == 0.05
            
            # Second call: $0.10 (at limit)
            agent._execute_tool_safely("tool2", '{}', "call_2")
            assert agent.total_cost == 0.10
            
            # Third call should fail (would exceed limit)
            with pytest.raises(Exception) as exc_info:
                agent._check_cost_limit()
                agent._execute_tool_safely("tool3", '{}', "call_3")
            
            assert "cost limit" in str(exc_info.value).lower()
            assert agent.total_cost <= agent.cost_limit_usd
    
    def test_audit_log_created(self, agent, tmp_path):
        """
        Test that all agent actions are logged to audit log.
        
        Every tool call, LLM call, and error should appear in
        structured audit logs for security and debugging.
        """
        # Configure agent to log to temp file
        log_file = tmp_path / "audit.log"
        agent.audit_logger = agent._setup_audit_logger(str(log_file))
        
        # Execute agent with mock tools
        with patch('openai.ChatCompletion.create') as mock_llm:
            mock_response = Mock()
            mock_response.tool_calls = None
            mock_response.content = "Final answer"
            mock_llm.return_value.choices = [Mock(message=mock_response)]
            
            agent.run("Test query")
        
        # Verify log file exists and contains entries
        assert log_file.exists(), "Audit log file should be created"
        
        log_content = log_file.read_text()
        assert len(log_content) > 0, "Audit log should contain entries"
        assert "Test query" in log_content or "timestamp" in log_content
        
        # Verify JSON format
        import json
        log_lines = log_content.strip().split('\n')
        for line in log_lines:
            try:
                log_entry = json.loads(line)
                assert "timestamp" in log_entry
                assert "user_id" in log_entry
            except json.JSONDecodeError:
                pytest.fail(f"Log line is not valid JSON: {line}")
    
    def test_input_validation_catches_invalid_args(self, agent):
        """
        Test that invalid tool arguments are caught and rejected.
        
        Should validate types, required fields, ranges, etc.
        using Pydantic schemas before executing tools.
        """
        # Mock tool with schema requiring positive integer
        tool_name = "get_items"
        invalid_args = {"count": -5}  # Negative not allowed
        
        with pytest.raises(ValueError):
            agent._validate_tool_args(tool_name, invalid_args)
        
        # Valid args should pass
        valid_args = {"count": 10}
        validated = agent._validate_tool_args(tool_name, valid_args)
        assert validated["count"] == 10
    
    def test_graceful_degradation_on_all_failures(self, agent):
        """
        Test that agent never crashes - always returns response.
        
        Even when everything fails, agent should return graceful
        error message to user, not raise exceptions.
        """
        # Make everything fail
        with patch('openai.ChatCompletion.create') as mock_llm:
            mock_llm.side_effect = Exception("LLM service down")
            
            # Agent should NOT raise exception
            result = agent.run("Test query")
            
            assert isinstance(result, dict)
            assert "result" in result
            assert result["success"] == False
            assert len(result.get("errors", [])) > 0
            
            # User-facing message should be graceful
            assert "error processing" in result["result"].lower() or \
                   "encountered an issue" in result["result"].lower()
```

**Additional Test Ideas (Optional but Recommended):**

```python
def test_jittered_backoff_prevents_thundering_herd(self, agent):
    """Verify retry delays include jitter."""
    pass

def test_conversation_history_maintained_across_steps(self, agent):
    """Verify agent remembers previous tool results."""
    pass

def test_logs_do_not_contain_sensitive_data(self, agent):
    """Verify passwords/keys are not logged."""
    pass

def test_agent_handles_malformed_tool_responses(self, agent):
    """Test agent doesn't crash on unexpected tool output."""
    pass
```

---

#### 3B. Function Calling Testing (If You Chose Path B)

**File Location:** `tests/test_function_safety.py`

**Minimum Required Tests (7):**

```python
import pytest
import time
from unittest.mock import Mock, patch, MagicMock
from src.functions.production_function_caller import ProductionFunctionCaller

class TestFunctionSafety:
    
    @pytest.fixture
    def function_caller(self):
        """Create function caller instance for testing."""
        functions = [
            {
                "type": "function",
                "function": {
                    "name": "search",
                    "description": "Search for information",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "query": {"type": "string"}
                        }
                    }
                }
            }
        ]
        return ProductionFunctionCaller(
            functions=functions,
            timeout_per_function=2,
            cost_limit_usd=0.50,
            user_id="test_user"
        )
    
    def test_fixed_workflow_executes_in_sequence(self, function_caller):
        """
        Test that fixed workflow executes functions in correct order.
        
        For predictable workflows, functions should execute sequentially
        with output of one feeding into input of next.
        """
        # Define workflow: extract → search → format
        workflow = ["extract_entities", "search_database", "format_response"]
        
        with patch.object(function_caller, '_execute_function_safely') as mock_execute:
            mock_execute.side_effect = [
                {"entities": ["AI", "safety"]},
                {"results": [{"title": "AI Safety Paper"}]},
                {"formatted": "Here are results..."}
            ]
            
            result = function_caller.execute(
                "Find papers on AI safety",
                workflow=workflow
            )
            
            # Verify all functions called in order
            assert mock_execute.call_count == 3
            calls = [call[0][0] for call in mock_execute.call_args_list]
            assert calls == workflow
    
    def test_timeout_on_slow_function(self, function_caller):
        """
        Test that slow function executions are killed after timeout.
        
        Same as agent test - timeouts work the same way.
        """
        with patch.object(function_caller, '_execute_with_timeout_and_retry') as mock_execute:
            import requests
            mock_execute.side_effect = requests.Timeout("Function took too long")
            
            result = function_caller._execute_function_safely(
                "slow_function",
                {"arg": "value"}
            )
            
            assert "error" in result
            assert "timeout" in str(result["error"]).lower()
    
    def test_retry_on_transient_failure(self, function_caller):
        """
        Test that transient failures trigger retry with backoff.
        
        Same pattern as agent - retry logic is identical.
        """
        call_count = 0
        
        def flaky_function(*args, **kwargs):
            nonlocal call_count
            call_count += 1
            if call_count < 3:
                raise ConnectionError("Network error")
            return {"status": "success", "data": "result"}
        
        with patch.object(function_caller, '_execute_function') as mock_func:
            mock_func.side_effect = flaky_function
            
            result = function_caller._execute_with_timeout_and_retry("api_function", {})
            
            assert call_count == 3
            assert result["status"] == "success"
    
    def test_circuit_breaker_opens_after_failures(self, function_caller):
        """
        Test that circuit breaker opens after repeated failures.
        
        Same as agent - circuit breakers work identically.
        """
        function_name = "failing_service"
        
        # Cause 5 consecutive failures
        for i in range(5):
            function_caller._record_circuit_breaker_failure(function_name)
        
        # Circuit should now be OPEN
        is_open = not function_caller._check_circuit_breaker(function_name)
        assert is_open
        
        # Verify calls are blocked
        result = function_caller._execute_function_safely(
            function_name,
            {"arg": "value"}
        )
        
        assert "error" in result
        assert "circuit" in str(result["error"]).lower()
    
    def test_unauthorized_function_call_blocked(self, function_caller):
        """
        Test that users cannot call functions they don't have permission for.
        
        Same authorization logic as agent.
        """
        function_caller.user_id = "readonly_user"
        
        with patch.object(function_caller, '_get_user_role') as mock_role:
            mock_role.return_value = "read"
            
            # Attempt to call admin function
            with pytest.raises(PermissionError):
                function_caller._authorize_function("delete_all_data")
            
            # Read functions should work
            try:
                function_caller._authorize_function("search_documents")
                authorized = True
            except PermissionError:
                authorized = False
            
            assert authorized
    
    def test_cost_limit_enforced(self, function_caller):
        """
        Test that execution stops when cost limit is reached.
        
        Same cost tracking as agent.
        """
        function_caller.cost_limit_usd = 0.10
        function_caller.total_cost = 0
        
        def expensive_function(*args, **kwargs):
            function_caller.total_cost += 0.05
            return {"result": "data"}
        
        with patch.object(function_caller, '_execute_function') as mock_func:
            mock_func.side_effect = expensive_function
            
            # First call: $0.05 (under limit)
            function_caller._execute_function_safely("func1", {})
            assert function_caller.total_cost == 0.05
            
            # Second call: $0.10 (at limit)
            function_caller._execute_function_safely("func2", {})
            assert function_caller.total_cost == 0.10
            
            # Third call should fail
            with pytest.raises(Exception) as exc_info:
                function_caller._check_cost_limit()
                function_caller._execute_function_safely("func3", {})
            
            assert "cost limit" in str(exc_info.value).lower()
    
    def test_audit_log_created(self, function_caller, tmp_path):
        """
        Test that all function calls are logged to audit log.
        
        Same logging structure as agent.
        """
        log_file = tmp_path / "audit.log"
        function_caller.audit_logger = function_caller._setup_audit_logger(str(log_file))
        
        with patch.object(function_caller, '_execute_function') as mock_func:
            mock_func.return_value = {"result": "success"}
            
            function_caller.execute(
                "Test query",
                workflow=["test_function"]
            )
        
        assert log_file.exists()
        log_content = log_file.read_text()
        assert len(log_content) > 0
        
        # Verify JSON format
        import json
        log_lines = log_content.strip().split('\n')
        for line in log_lines:
            log_entry = json.loads(line)
            assert "timestamp" in log_entry
            assert "user_id" in log_entry
    
    def test_single_llm_call_no_loop(self, function_caller):
        """
        Test that non-agent makes ONE function call decision, not loop.
        
        This is the key difference from agent: no ReAct loop.
        """
        with patch.object(function_caller, '_call_llm_with_safety') as mock_llm:
            # Mock LLM returning function call
            mock_response = Mock()
            mock_response.tool_calls = [Mock(
                id="call_1",
                function=Mock(name="search", arguments='{"query":"test"}')
            )]
            mock_llm.return_value = mock_response
            
            with patch.object(function_caller, '_execute_function_safely') as mock_execute:
                mock_execute.return_value = {"results": ["item1", "item2"]}
                
                result = function_caller._execute_with_llm_selection("Test query")
                
                # Verify LLM called only ONCE (not in loop)
                assert mock_llm.call_count == 1 or mock_llm.call_count == 2  # 1 for decision, 1 for formatting
                
                # Verify function executed
                assert mock_execute.call_count == 1
    
    def test_graceful_degradation_on_failures(self, function_caller):
        """
        Test that system never crashes - always returns response.
        
        Same graceful degradation as agent.
        """
        with patch.object(function_caller, '_call_llm_with_safety') as mock_llm:
            mock_llm.side_effect = Exception("LLM service down")
            
            result = function_caller.execute("Test query")
            
            assert isinstance(result, dict)
            assert "result" in result
            assert result["success"] == False
            assert len(result.get("errors", [])) > 0
```

---

## Deliverable 4: Update Project README

**Both paths require README updates.**

## Deliverable 4: Update Project README

**Add to your main `README.md` (adapt based on your path):**

### For Agent Implementation (Path A):

```markdown
## Agent Architecture

### Overview

Our application uses a production-ready ReAct (Reasoning + Acting) agent to [describe your agent's purpose].

### How It Works

The agent follows a simple but powerful loop:

1. **Reason**: Analyze the user's request and decide what to do next
2. **Act**: Execute tools (search APIs, databases, calculations, etc.)
3. **Observe**: Examine tool results and update understanding
4. **Repeat**: Continue until goal achieved or maximum steps reached

### Available Tools

Our agent has access to these tools:

- **`search_documents`**: Search internal knowledge base
  - Permission: read
  - Timeout: 5 seconds
  - Use case: Finding relevant information

- **`analyze_data`**: Process and analyze datasets
  - Permission: read
  - Timeout: 10 seconds
  - Use case: Statistical analysis, data visualization

- **`update_records`**: Modify database records
  - Permission: write
  - Timeout: 3 seconds
  - Use case: Saving user preferences, updating status

- **`generate_report`**: Create formatted PDF reports
  - Permission: write
  - Timeout: 15 seconds
  - Use case: Export analysis results

[...list all your tools...]

### Production Safety Features

Our agent includes comprehensive safety features based on industry best practices:

#### Reliability
- ✅ **Max 5 iterations** - Prevents infinite loops
- ✅ **Timeouts on all operations** - 2-15 seconds depending on tool
- ✅ **Exponential backoff retry** - Automatic recovery from transient failures
- ✅ **Circuit breakers** - Stops calling broken services

#### Security
- ✅ **Authorization enforcement** - Three permission levels (read/write/admin)
- ✅ **Input validation** - Pydantic schemas prevent malformed requests
- ✅ **Audit logging** - Every action logged to `logs/agent_audit.log`
- ✅ **No sensitive data in logs** - Passwords and keys never logged

#### Cost Control
- ✅ **$1 per-request limit** - Prevents runaway costs
- ✅ **Per-user daily limits** - $5/day for free tier
- ✅ **Real-time cost tracking** - Accumulated across all agent steps
- ✅ **Automatic stop** - Execution halts when budget exceeded

### Performance Metrics

Based on our testing:

- **Average latency**: 2.3 seconds per request
- **Success rate**: 94% (first attempt), 98% (with retries)
- **Average cost**: $0.23 per agent run
- **Typical steps**: 2-3 tool calls per request

### Example Usage

```python
from src.agent.production_agent import ProductionAgent

# Initialize agent
agent = ProductionAgent(
    tools=my_tools,
    max_iterations=5,
    cost_limit_usd=1.0,
    user_id="user_123"
)

# Run agent
result = agent.run("Find papers on AI safety published in 2024")

# Handle result
if result["success"]:
    print(result["result"])
    print(f"Cost: ${result['cost_usd']:.4f}")
else:
    print("Agent encountered an error:")
    print(result["errors"])
```

### Monitoring

**Audit Logs**
- Location: `logs/agent_audit.log`
- Format: JSON (one entry per line)
- Retention: 90 days
- Analysis: Daily error review, weekly security audit

**Error Tracking**
- Check logs for `"success": false` entries
- Review circuit breaker openings
- Monitor unauthorized access attempts

**Cost Dashboard** (if implemented)
- Real-time cost per user
- Tool usage breakdown
- Budget alerts at 80%

### Known Limitations

1. **Complex tasks may exceed iteration limit**
   - Workaround: Break request into smaller queries
   - Future: Increase max_iterations for premium users

2. **External API dependencies**
   - Impact: Occasional delays or cached results
   - Mitigation: Circuit breakers, fallbacks

3. **Cost limits may stop long tasks**
   - Workaround: Upgrade to premium tier
   - Future: Dynamic limits based on task complexity

4. **Agent tool selection not always optimal**
   - Mitigation: Ongoing prompt engineering
   - Monitoring: Track tool choices in logs

### Development

**Running Tests**
```bash
pytest tests/test_agent_safety.py -v
```

**Viewing Logs**
```bash
tail -f logs/agent_audit.log | jq .
```

**Cost Analysis**
```bash
python scripts/analyze_costs.py --last-7-days
```

### Security

See [Agent Safety Documentation](docs/agent-safety.md) for complete security details.

**Reporting Security Issues**
Email: security@yourapp.com

### Future Enhancements

- [ ] Semantic caching for common queries (Week 10 Lab)
- [ ] Model selection (cheaper models for simple tasks)
- [ ] Evaluation framework with golden datasets (Week 11)
- [ ] Real-time monitoring dashboard
- [ ] Automatic prompt optimization based on logs
```

---

### For Non-Agent Implementation (Path B):

```markdown
## Function Calling Architecture

### Overview

Our application uses a production-ready function calling system with [predictable workflow / single function calls / describe your approach].

**Why We Chose Direct Function Calling Over an Agent:**

[Copy from your architecture-decision.md - explain your reasoning]

Examples:
- "Our workflow is always: extract entities → search database → format response"
- "Users always request one type of operation, so no multi-step reasoning needed"
- "Costs: Function calling costs $0.05/request vs. agent would cost $0.30-0.50/request"

### How It Works

Our system follows a [fixed workflow / dynamic single-call / hybrid] approach:

**Fixed Workflow:**
1. Extract key information from user query
2. Call primary function (search, analyze, etc.)
3. Format and return results

**OR Dynamic Single Call:**
1. LLM analyzes user query
2. Selects appropriate function to call
3. Executes function once
4. Formats and returns result

### Available Functions

Our system has access to these functions:

- **`search_documents`**: Search internal knowledge base
  - Permission: read
  - Timeout: 5 seconds
  - Use case: Finding relevant information

- **`analyze_data`**: Process and analyze datasets
  - Permission: read
  - Timeout: 10 seconds
  - Use case: Statistical analysis

- **`update_records`**: Modify database records
  - Permission: write
  - Timeout: 3 seconds
  - Use case: Saving user preferences

[...list all your functions...]

### Production Safety Features

Our function calling system includes comprehensive safety features:

#### Reliability
- ✅ **Predictable execution** - Fixed workflow or single function call
- ✅ **Timeouts on all operations** - 2-15 seconds depending on function
- ✅ **Exponential backoff retry** - Automatic recovery from transient failures
- ✅ **Circuit breakers** - Stops calling broken services

#### Security
- ✅ **Authorization enforcement** - Three permission levels (read/write/admin)
- ✅ **Input validation** - Pydantic schemas prevent malformed requests
- ✅ **Audit logging** - Every action logged to `logs/function_audit.log`
- ✅ **No sensitive data in logs** - Passwords and keys never logged

#### Cost Control
- ✅ **$0.50 per-request limit** - Lower than agent due to fewer LLM calls
- ✅ **Per-user daily limits** - $5/day for free tier
- ✅ **Real-time cost tracking** - Monitored across all operations
- ✅ **Automatic stop** - Execution halts when budget exceeded

### Performance Metrics

Based on our testing:

- **Average latency**: 1.1 seconds per request (faster than agent!)
- **Success rate**: 96% (first attempt), 99% (with retries)
- **Average cost**: $0.08 per request (5-10x cheaper than agent)
- **Typical calls**: 1-2 function calls per request

### Comparison: Agent vs. Our Approach

| Metric | Agent (Path A) | Our Approach (Path B) |
|--------|----------------|----------------------|
| Latency | 2-3 seconds | 1-2 seconds |
| Cost | $0.20-0.50 | $0.05-0.15 |
| LLM Calls | 3-10 per request | 1-2 per request |
| Complexity | High (ReAct loop) | Low (fixed workflow) |
| Adaptability | High | Limited |
| Reliability | 94% | 96% |

**Trade-off:** We sacrifice adaptability for speed, cost efficiency, and simplicity. This matches our use case perfectly.

### Example Usage

```python
from src.functions.production_function_caller import ProductionFunctionCaller

# Initialize function caller
caller = ProductionFunctionCaller(
    functions=my_functions,
    timeout_per_function=5,
    cost_limit_usd=0.50,
    user_id="user_123"
)

# Option 1: Fixed workflow
result = caller.execute(
    "Summarize this document",
    workflow=["extract_text", "summarize", "format"]
)

# Option 2: Let LLM choose function
result = caller.execute("Search for AI papers")

# Handle result
if result["success"]:
    print(result["result"])
    print(f"Cost: ${result['cost_usd']:.4f}")
else:
    print("Error:", result["errors"])
```

### Monitoring

**Audit Logs**
- Location: `logs/function_audit.log`
- Format: JSON (one entry per line)
- Retention: 90 days

**Error Tracking**
- Check logs for `"success": false` entries
- Review circuit breaker openings
- Monitor unauthorized access attempts

### Known Limitations

1. **Limited to predefined workflows**
   - Workaround: Add new functions as needed
   - Future: May upgrade to agent if requests become more complex

2. **Cannot handle multi-step reasoning**
   - Workaround: Break into multiple requests
   - Consideration: Current use case doesn't require this

3. **External API dependencies**
   - Impact: Occasional delays or cached results
   - Mitigation: Circuit breakers, fallbacks

### When We Might Upgrade to Agent

We'll consider switching to an agent if:
- User requests require 3+ sequential function calls
- We need adaptive tool selection (can't predict workflow)
- Users start asking complex, multi-step questions
- The benefit of flexibility outweighs 5-10x cost increase

Currently: Our predictable workflow approach is optimal for our use case.

### Development

**Running Tests**
```bash
pytest tests/test_function_safety.py -v
```

**Viewing Logs**
```bash
tail -f logs/function_audit.log | jq .
```

### Security

See [Function Safety Documentation](docs/function-safety.md) for complete security details.

### Future Enhancements

- [ ] Semantic caching for common queries (Week 10 Lab)
- [ ] Parallel function execution (where safe)
- [ ] Evaluation framework (Week 11)
- [ ] Real-time monitoring dashboard
```

---

## Grading Rubric

**Note:** Both Agent (Path A) and Non-Agent (Path B) implementations are graded on the same rubric. Path B may be simpler to implement, but both require production-grade safety features.

### Implementation Quality (40%)

**Outstanding (36-40 points):**
- All required safety features implemented perfectly (10 for agent, 9 for non-agent)
- Code is clean, well-documented, testable
- Architecture decision well-justified with evidence
- No bugs in failure handling
- Production-ready quality

**Good (32-35 points):**
- 8-9 features (agent) or 7-8 features (non-agent) implemented correctly
- Architecture decision reasonable
- Minor bugs or edge cases not handled
- Code quality is good but could be cleaner
- Would work in production with minor fixes

**Acceptable (28-31 points):**
- 6-7 features (agent) or 5-6 features (non-agent) implemented
- Architecture decision needs better justification
- Some bugs in failure scenarios
- Code works but needs refactoring
- Not quite production-ready

**Needs Improvement (<28 points):**
- <6 features implemented
- Architecture decision poorly justified or incorrect for use case
- Major bugs or missing error handling
- Code is messy or hard to understand
- Not suitable for production

---

### Safety & Reliability (30%)

**Outstanding (27-30 points):**
- Handles all failure scenarios gracefully
- Never crashes, always returns response
- Comprehensive logging
- Circuit breakers working perfectly
- Authorization rock-solid

**Good (24-26 points):**
- Handles most failures well
- Occasional edge case issues
- Good logging
- Security features working

**Acceptable (21-23 points):**
- Basic error handling
- Some crashes on edge cases
- Minimal logging
- Security has gaps

**Needs Improvement (<21 points):**
- Poor error handling
- Crashes frequently
- Minimal logging
- Security vulnerabilities

---

### Documentation (20%)

**Outstanding (18-20 points):**
- Comprehensive safety documentation
- All failure scenarios documented with examples
- Clear cost controls
- Complete audit log schema
- Security considerations thorough
- README is professional

**Good (16-17 points):**
- Good documentation
- Most scenarios covered
- Cost controls defined
- README updated

**Acceptable (14-15 points):**
- Basic documentation
- Key scenarios covered
- Some gaps or unclear sections

**Needs Improvement (<14 points):**
- Minimal documentation
- Missing key sections
- Unclear or incomplete

---

### Testing (10%)

**Outstanding (9-10 points):**
- 7+ comprehensive tests
- All tests passing
- Covers failure scenarios
- Good test coverage
- Tests are meaningful

**Good (8 points):**
- 5-6 tests, all passing
- Covers main scenarios
- Some edge cases missing

**Acceptable (7 points):**
- 3-4 tests, mostly passing
- Basic coverage only

**Needs Improvement (<7 points):**
- <3 tests or tests failing
- Doesn't test important scenarios

---

### Bonus Points (up to +15%)

- **Monitoring dashboard** (+5%): Visual dashboard showing agent metrics
- **Load testing results** (+5%): Tested with 10+ concurrent users, documented results
- **Novel safety feature** (+10%): Implemented additional safety pattern specific to your use case
- **Security testing** (+10%): Demonstrated prevention of actual security vulnerability (prompt injection, unauthorized access, etc.)
- **Cost optimization** (+5%): Implemented caching or other Week 10 optimizations

---

## Common Mistakes to Avoid

### ❌ "I'll build an agent because it sounds cooler"
**Reality:** Agents are 5-10x more expensive and complex. Only use if you need adaptive, multi-step reasoning. Most applications don't.

**Fix:** Honestly assess your use case. Can you predict the workflow? If yes, use direct function calling.

### ❌ "I'll use direct function calling but not document why"
**Reality:** Instructor needs to see you made an informed decision, not a lazy one.

**Fix:** Write thorough `architecture-decision.md` with evidence and trade-offs.
Automated tests are required. Manual testing doesn't catch edge cases and isn't repeatable.

### ❌ "Authorization in the prompt is good enough"
NEVER EVER trust the agent to enforce security. Always check permissions in code.

### ❌ "Timeouts are optional for my fast APIs"
All APIs are fast until they're not. Networks fail. Always use timeouts.

### ❌ "I don't need max_iterations, my prompts are good"
Your prompts will fail eventually. LLMs are probabilistic. Always set limits.

### ❌ "Logging everything will slow down my agent"
Logging is asynchronous and fast. Debugging without logs is way slower.

### ❌ "I'll catch Exception and retry everything"
Don't retry client errors (400, 401, 403, 404). Only retry transient failures.

### ❌ "Cost limits are overkill for testing"
One infinite loop in testing = real money lost. Set limits everywhere.

### ❌ "My circuit breaker logic is in the prompt"
Circuit breakers must be in code. LLMs can't reliably implement this pattern.

---

## Submission Checklist

**Before you submit, verify:**

**Architecture Decision:**
- [ ] `docs/architecture-decision.md` exists
- [ ] Decision clearly stated (Agent OR Direct Function Calling)
- [ ] Rationale includes 3+ specific reasons
- [ ] Trade-offs explicitly discussed
- [ ] Decision matches actual implementation

**Code (Path A - Agent):**
- [ ] `src/agent/production_agent.py` exists and is complete
- [ ] All 10 safety features implemented
- [ ] ReAct loop with max_iterations working
- [ ] Code has type hints and docstrings
- [ ] No hardcoded secrets or API keys
- [ ] Agent handles errors gracefully (never crashes)

**Code (Path B - Non-Agent):**
- [ ] `src/functions/production_function_caller.py` exists and is complete
- [ ] All 9 safety features implemented (no ReAct loop needed)
- [ ] Fixed workflow OR dynamic single-call working
- [ ] Code has type hints and docstrings
- [ ] No hardcoded secrets or API keys
- [ ] System handles errors gracefully (never crashes)

**Documentation:**
- [ ] `docs/agent-safety.md` OR `docs/function-safety.md` exists and is comprehensive
- [ ] Tool/function authorization matrix complete
- [ ] 5+ failure scenarios documented with handling strategies
- [ ] Cost controls clearly defined
- [ ] Audit log schema documented
- [ ] Security considerations addressed
- [ ] README updated with architecture section

**Tests (Path A - Agent):**
- [ ] `tests/test_agent_safety.py` exists
- [ ] Minimum 7 tests implemented
- [ ] All tests passing (`pytest -v`)
- [ ] Tests cover: max_iterations, timeout, retry, circuit breaker, auth, cost, audit log
- [ ] Tests cover failure scenarios, not just happy path

**Tests (Path B - Non-Agent):**
- [ ] `tests/test_function_safety.py` exists
- [ ] Minimum 7 tests implemented
- [ ] All tests passing (`pytest -v`)
- [ ] Tests cover: timeout, retry, circuit breaker, auth, cost, audit log, no-loop behavior
- [ ] Tests cover failure scenarios, not just happy path

**Functionality (Path A - Agent):**
- [ ] Agent runs successfully on test queries
- [ ] Max iterations prevents infinite loops (tested)
- [ ] Timeouts work (tested)
- [ ] Retry logic functions (tested)
- [ ] Authorization blocks unauthorized calls (tested)
- [ ] Cost limit stops execution (tested)
- [ ] Audit logs are created (verified)

**Functionality (Path B - Non-Agent):**
- [ ] Function caller runs successfully on test queries
- [ ] Fixed workflow OR dynamic selection works
- [ ] Timeouts work (tested)
- [ ] Retry logic functions (tested)
- [ ] Authorization blocks unauthorized calls (tested)
- [ ] Cost limit stops execution (tested)
- [ ] Audit logs are created (verified)
- [ ] Verified NO infinite loops (no ReAct loop to worry about)

**Git:**
- [ ] All code committed with clear messages
- [ ] `.env` files excluded (in `.gitignore`)
- [ ] Audit logs excluded (in `.gitignore`)
- [ ] No sensitive data in repo

---

## What's Next?

**Week 11: Evaluation & Observability**
- Your audit logs will be analyzed for agent performance
- Evaluation frameworks will measure success rates
- Golden datasets will validate agent quality
- This week's safety features enable Week 11's analysis

**Week 12: Production Engineering**
- Your agent will be deployed with CI/CD
- Monitoring systems will track live agent metrics
- Production secrets management will secure your tools

**Week 15: Final Demo**
- Production-ready agent is a key demo highlight
- "Built agent with 99%+ reliability" is impressive
- Safety features show professional engineering discipline

The patterns you're learning—timeouts, retries, circuit breakers, authorization, audit logging—are fundamental distributed systems patterns used everywhere in production software, not just AI agents.

Good luck building your production agent!
