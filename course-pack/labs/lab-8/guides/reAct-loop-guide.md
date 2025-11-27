# Guide: Implementing the ReAct Loop

**Building AI-Powered Applications | Lab 8**

This guide walks you through implementing a production-ready ReAct (Reasoning + Acting) agent loop with proper iteration limits and context management.

---

## What is ReAct?

**ReAct** = **Rea**soning + **Act**ing

The agent repeatedly:
1. **Reasons** about what to do next (calls LLM)
2. **Acts** by executing tools based on reasoning
3. **Observes** the results
4. **Repeats** until goal achieved or max iterations reached

This pattern is used by ChatGPT plugins, LangChain agents, AutoGPT, and production AI systems at major companies.

---

## Why You Need Max Iterations

**Without `max_iterations`, your agent WILL loop forever.**

Real failure scenarios:
- Agent keeps searching for "perfect" answer
- Tool returns ambiguous result, agent tries again forever
- Agent gets stuck in cycle: search → refine query → search → refine...
- One bug = $10,000 API bill in 30 minutes

**Always set `max_iterations`.** Industry standard is 3-10 iterations.

---

## Basic ReAct Loop Implementation

### Step 1: Initialize Conversation History

```python
class SimpleAgent:
    def __init__(self, tools, max_iterations=5):
        """
        Initialize agent with tools and safety limits.
        
        Args:
            tools: List of OpenAI function/tool definitions
            max_iterations: Maximum reasoning-acting cycles (CRITICAL!)
        """
        self.tools = tools
        self.max_iterations = max_iterations
    
    def run(self, user_query: str) -> str:
        """Execute agent on user query."""
        
        # Initialize conversation with system prompt and user query
        messages = [
            {
                "role": "system",
                "content": self._get_system_prompt()
            },
            {
                "role": "user",
                "content": user_query
            }
        ]
        
        # ReAct loop starts here...
```

**Key Points:**
- Conversation history starts with system prompt and user query
- History grows with each tool call and result
- Agent needs history to maintain context

---

### Step 2: Implement ReAct Loop

```python
    def run(self, user_query: str) -> str:
        messages = [
            {"role": "system", "content": self._get_system_prompt()},
            {"role": "user", "content": user_query}
        ]
        
        # CRITICAL: Loop with limit
        for iteration in range(self.max_iterations):
            print(f"Agent iteration {iteration + 1}/{self.max_iterations}")
            
            # === REASON ===
            # Ask LLM what to do next
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=messages,
                tools=self.tools,
                tool_choice="auto"  # Let LLM decide if it needs tools
            )
            
            assistant_message = response.choices[0].message
            
            # === CHECK IF DONE ===
            # No tool calls means agent has final answer
            if not assistant_message.tool_calls:
                final_answer = assistant_message.content
                print(f"Agent finished in {iteration + 1} iterations")
                return final_answer
            
            # === ACT ===
            # Agent wants to use tools
            messages.append(assistant_message)
            
            for tool_call in assistant_message.tool_calls:
                tool_name = tool_call.function.name
                tool_args = tool_call.function.arguments
                
                print(f"  Calling tool: {tool_name}")
                
                # Execute the tool
                tool_result = self._execute_tool(tool_name, tool_args)
                
                # === OBSERVE ===
                # Add tool result to conversation
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": tool_name,
                    "content": json.dumps(tool_result)
                })
            
            # Loop continues: agent will reason about tool results
        
        # === MAX ITERATIONS REACHED ===
        print(f"Agent reached max iterations ({self.max_iterations})")
        return self._handle_max_iterations_reached(messages)
```

**Key Points:**

1. **`for iteration in range(self.max_iterations)`**: CRITICAL safety feature
2. **Check if done**: Exit when no tool calls (agent has final answer)
3. **Append assistant message**: Maintains conversation context
4. **Append tool results**: Agent sees what tools returned
5. **Loop continues**: Agent reasons about results and may call more tools

---

### Step 3: Handle Max Iterations

```python
    def _handle_max_iterations_reached(self, messages: list) -> str:
        """
        Return helpful message when max iterations reached.
        
        This is NOT an error - it's a safety feature working correctly.
        Some queries legitimately need more steps than the limit.
        """
        
        # Try to give user something helpful
        partial_result = self._extract_partial_result(messages)
        
        return (
            "I couldn't complete your request within the time limit. "
            "Here's what I found so far:\n\n"
            f"{partial_result}\n\n"
            "Please try:\n"
            "- Breaking your request into smaller parts\n"
            "- Being more specific about what you need\n"
            "- Asking for one thing at a time"
        )
    
    def _extract_partial_result(self, messages: list) -> str:
        """Extract any useful partial results from conversation."""
        # Get last few assistant messages
        assistant_messages = [
            m["content"] for m in messages 
            if m.get("role") == "assistant" and m.get("content")
        ]
        
        if assistant_messages:
            return assistant_messages[-1]
        else:
            return "I was working on your request but needed more time."
```

**Key Points:**
- Max iterations is **not a bug** - it's safety working correctly
- Provide partial results if available
- Give user actionable suggestions
- Log for analysis (may need to increase limit for some queries)

---

### Step 4: Implement Tool Execution

```python
    def _execute_tool(self, tool_name: str, tool_args: str) -> dict:
        """
        Execute a tool and return results.
        
        Args:
            tool_name: Name of tool to execute
            tool_args: JSON string of arguments
            
        Returns:
            dict: Tool results or error
        """
        try:
            # Parse arguments
            args = json.loads(tool_args)
            
            # Find and execute tool
            if tool_name == "search_documents":
                return self._tool_search_documents(**args)
            
            elif tool_name == "analyze_data":
                return self._tool_analyze_data(**args)
            
            elif tool_name == "calculate":
                return self._tool_calculate(**args)
            
            else:
                return {
                    "error": f"Unknown tool: {tool_name}",
                    "available_tools": [t["function"]["name"] for t in self.tools]
                }
        
        except json.JSONDecodeError as e:
            return {"error": f"Invalid JSON arguments: {e}"}
        
        except Exception as e:
            return {"error": f"Tool execution failed: {e}"}
    
    # Define your actual tool functions
    def _tool_search_documents(self, query: str, max_results: int = 10):
        """Search internal documents."""
        # Your implementation here
        results = perform_search(query, max_results)
        return {
            "status": "success",
            "results": results,
            "count": len(results)
        }
    
    def _tool_analyze_data(self, data_id: str, analysis_type: str):
        """Analyze a dataset."""
        # Your implementation here
        pass
```

**Key Points:**
- Tool functions are just regular Python functions
- Return structured dicts (so they convert cleanly to JSON)
- Handle errors gracefully (don't crash the agent)
- Return helpful error messages

---

## Complete Working Example

Here's a complete, minimal working agent:

```python
import openai
import json

class MinimalReActAgent:
    """Minimal working ReAct agent with max_iterations."""
    
    def __init__(self, tools, max_iterations=5):
        self.tools = tools
        self.max_iterations = max_iterations
        openai.api_key = "your-api-key"  # Or use environment variable
    
    def run(self, user_query: str) -> str:
        """Execute ReAct loop."""
        messages = [
            {
                "role": "system",
                "content": "You are a helpful research assistant. Use available tools to help users."
            },
            {
                "role": "user",
                "content": user_query
            }
        ]
        
        for iteration in range(self.max_iterations):
            # REASON
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=messages,
                tools=self.tools
            )
            
            message = response.choices[0].message
            
            # CHECK IF DONE
            if not message.tool_calls:
                return message.content
            
            # ACT
            messages.append(message)
            for tool_call in message.tool_calls:
                result = self._execute_tool(
                    tool_call.function.name,
                    tool_call.function.arguments
                )
                
                # OBSERVE
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": json.dumps(result)
                })
        
        # MAX ITERATIONS
        return "I couldn't complete your request in the time limit. Please try breaking it into smaller parts."
    
    def _execute_tool(self, name: str, args: str) -> dict:
        """Execute tool (implement your tools here)."""
        try:
            arguments = json.loads(args)
            
            if name == "search":
                return {"results": f"Found results for: {arguments.get('query')}"}
            
            return {"error": f"Unknown tool: {name}"}
            
        except Exception as e:
            return {"error": str(e)}


# Usage
tools = [
    {
        "type": "function",
        "function": {
            "name": "search",
            "description": "Search for information",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query"
                    }
                },
                "required": ["query"]
            }
        }
    }
]

agent = MinimalReActAgent(tools, max_iterations=5)
result = agent.run("Search for information about AI safety")
print(result)
```

---

## Common Patterns & Best Practices

### Pattern 1: Track Iteration Count

```python
def run(self, user_query: str) -> dict:
    """Return structured response with metadata."""
    messages = [...]
    
    for iteration in range(self.max_iterations):
        # ... agent logic ...
        
        if not message.tool_calls:
            return {
                "success": True,
                "result": message.content,
                "iterations_used": iteration + 1,
                "max_iterations": self.max_iterations
            }
    
    return {
        "success": False,
        "result": "Max iterations reached",
        "iterations_used": self.max_iterations,
        "max_iterations": self.max_iterations
    }
```

### Pattern 2: Detect and Prevent Tool Loops

```python
def run(self, user_query: str) -> str:
    messages = [...]
    tool_call_history = []  # Track what tools were called
    
    for iteration in range(self.max_iterations):
        response = openai.ChatCompletion.create(...)
        message = response.choices[0].message
        
        if not message.tool_calls:
            return message.content
        
        # Check for loops
        for tool_call in message.tool_calls:
            call_signature = (
                tool_call.function.name,
                tool_call.function.arguments
            )
            
            # Agent calling same tool with same args?
            if tool_call_history.count(call_signature) >= 2:
                return (
                    "I seem to be repeating myself. "
                    "Let me try a different approach. "
                    "[Or return partial results]"
                )
            
            tool_call_history.append(call_signature)
            
        # Continue with tool execution...
```

### Pattern 3: Adaptive Max Iterations

```python
class AdaptiveAgent:
    """Agent that adjusts max_iterations based on query complexity."""
    
    def run(self, user_query: str, complexity: str = "medium") -> str:
        # Adjust iterations based on task
        iterations_map = {
            "simple": 3,
            "medium": 5,
            "complex": 10
        }
        
        max_iterations = iterations_map.get(complexity, 5)
        
        # ... rest of ReAct loop with max_iterations ...
```

### Pattern 4: Stream Progress Updates

```python
def run(self, user_query: str, progress_callback=None):
    """Agent that reports progress."""
    messages = [...]
    
    for iteration in range(self.max_iterations):
        if progress_callback:
            progress_callback(f"Step {iteration + 1}/{self.max_iterations}")
        
        response = openai.ChatCompletion.create(...)
        
        # ... rest of loop ...
```

---

## Debugging Tips

### Issue 1: Agent Loops Forever

**Symptom:** Agent keeps calling tools without finishing

**Diagnosis:**
```python
# Add logging to see what's happening
for iteration in range(self.max_iterations):
    print(f"\n=== Iteration {iteration + 1} ===")
    response = openai.ChatCompletion.create(...)
    
    print(f"Tool calls: {len(message.tool_calls) if message.tool_calls else 0}")
    if message.tool_calls:
        for tc in message.tool_calls:
            print(f"  - {tc.function.name}({tc.function.arguments})")
```

**Fixes:**
- Check tool descriptions (might be unclear)
- Verify tools return useful results
- Add loop detection (see Pattern 2)
- Review system prompt

### Issue 2: Agent Finishes Too Early

**Symptom:** Agent returns answer without using tools

**Diagnosis:**
- Check if tools are actually needed for the query
- Verify tool descriptions are clear
- Test with more complex query

**Fix:**
```python
# Make system prompt more tool-focused
system_prompt = """
You are a research assistant. When users ask questions:
1. ALWAYS search for current information using available tools
2. Analyze data using available tools
3. Only provide final answer after using tools

Available tools: {', '.join([t['function']['name'] for t in self.tools])}
"""
```

### Issue 3: Conversation History Too Large

**Symptom:** Token limit errors after many iterations

**Fix:**
```python
def _truncate_history(self, messages: list, max_tokens: int = 4000) -> list:
    """Keep conversation history under token limit."""
    # Always keep system prompt and original user query
    essential = messages[:2]
    
    # Keep most recent N messages
    recent = messages[-10:]  # Adjust based on your needs
    
    return essential + recent
```

---

## Testing Your ReAct Loop

### Test 1: Verify Max Iterations Works

```python
def test_max_iterations_enforced():
    """Agent must stop after max_iterations."""
    
    # Mock LLM that always wants to call tools (never finishes)
    def mock_llm_always_wants_tools(*args, **kwargs):
        mock_response = Mock()
        mock_response.choices = [Mock()]
        mock_response.choices[0].message = Mock()
        mock_response.choices[0].message.tool_calls = [
            Mock(
                id="call_123",
                function=Mock(name="search", arguments='{"query":"test"}')
            )
        ]
        return mock_response
    
    with patch('openai.ChatCompletion.create', side_effect=mock_llm_always_wants_tools):
        agent = SimpleAgent(tools=[], max_iterations=3)
        result = agent.run("Test query")
        
        assert "max iterations" in result.lower() or \
               "time limit" in result.lower()
```

### Test 2: Verify Conversation History Maintained

```python
def test_conversation_history_maintained():
    """Agent should maintain context across iterations."""
    
    agent = SimpleAgent(tools=[...], max_iterations=5)
    
    # Track messages array
    messages_history = []
    
    def mock_llm(*args, **kwargs):
        messages_history.append(kwargs['messages'])
        # Return mock response...
    
    with patch('openai.ChatCompletion.create', side_effect=mock_llm):
        agent.run("Test query")
    
    # Verify history grows with each iteration
    assert len(messages_history) > 1
    assert len(messages_history[-1]) > len(messages_history[0])
```

### Test 3: Verify Tool Results Added to History

```python
def test_tool_results_in_history():
    """Tool results should be added to conversation."""
    
    agent = SimpleAgent(tools=[...])
    
    # Mock LLM to call tool once, then finish
    call_count = 0
    def mock_llm(*args, **kwargs):
        nonlocal call_count
        call_count += 1
        
        if call_count == 1:
            # First call: use tool
            return mock_tool_call_response()
        else:
            # Second call: final answer
            return mock_final_answer_response()
    
    with patch('openai.ChatCompletion.create', side_effect=mock_llm):
        result = agent.run("Test query")
    
    assert call_count == 2  # Called LLM twice
    # Verify tool result was added to messages
```

---

## Advanced: Conditional Orchestration

Once you have basic ReAct working, you can add conditional logic:

```python
def run(self, user_query: str) -> str:
    messages = [...]
    
    for iteration in range(self.max_iterations):
        response = openai.ChatCompletion.create(...)
        message = response.choices[0].message
        
        if not message.tool_calls:
            return message.content
        
        messages.append(message)
        
        for tool_call in message.tool_calls:
            result = self._execute_tool(
                tool_call.function.name,
                tool_call.function.arguments
            )
            
            # CONDITIONAL: Change behavior based on result
            if result.get("status") == "error":
                # Try alternative approach
                result = self._try_alternative(tool_call)
            
            elif result.get("confidence") < 0.7:
                # Low confidence - ask for clarification
                result = self._request_clarification(result)
            
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(result)
            })
```

---

## Summary Checklist

Before moving to the next guide, verify:

- [ ] ReAct loop implemented with `max_iterations`
- [ ] Conversation history maintained across iterations
- [ ] Agent exits when no tool calls (final answer reached)
- [ ] Agent exits when max iterations reached
- [ ] Helpful message when max iterations reached
- [ ] Tool execution integrated into loop
- [ ] Tool results added to conversation
- [ ] Basic error handling on tool execution
- [ ] Tested with real query

**Next Step:** Once your ReAct loop works, proceed to the Timeout & Retry guide to add failure handling.
