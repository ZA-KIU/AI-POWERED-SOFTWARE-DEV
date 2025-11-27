# Guide: Timeouts and Retry Logic

**Building AI-Powered Applications | Lab 8**

This guide teaches you to implement timeouts and exponential backoff retry logic to handle transient failures gracefully.

---

## Why You Need Timeouts

**Every external call can hang indefinitely.**

Real scenarios:
- API server is overloaded → takes 5 minutes to respond
- Network connection drops mid-request → waits forever
- Database query hits slow table → 10 minute timeout
- LLM generation stalls → never returns

**Without timeouts:** Your agent hangs, user waits forever, resources are wasted.

**With timeouts:** Fail fast, retry, or show error within seconds.

---

## Types of Timeouts

### 1. Connection Timeout

How long to wait for initial connection to establish.

```python
import requests

# Connection timeout: 2 seconds
response = requests.get(
    "https://api.example.com/data",
    timeout=2  # If can't connect in 2s, fail
)
```

**Recommended values:**
- Fast APIs: 2-3 seconds
- Slower APIs: 5 seconds
- Never more than 10 seconds

### 2. Read Timeout

How long to wait for response after connection established.

```python
# Read timeout: 10 seconds
response = requests.get(
    "https://api.example.com/search",
    timeout=(2, 10)  # (connect_timeout, read_timeout)
)
```

**Recommended values:**
- Simple queries: 5-10 seconds
- LLM generation: 20-30 seconds
- Complex processing: 30-60 seconds

### 3. Total Timeout

Maximum time for entire operation (connection + read + processing).

```python
import signal

def timeout_handler(signum, frame):
    raise TimeoutError("Operation took too long")

# Set alarm for 30 seconds total
signal.alarm(30)
try:
    result = complex_operation()
finally:
    signal.alarm(0)  # Cancel alarm
```

---

## Implementing Timeouts in Your Agent

### On LLM API Calls

```python
import openai
from openai import OpenAIError, Timeout

def call_llm_with_timeout(messages, tools, timeout=30):
    """
    Call OpenAI API with timeout.
    
    Args:
        messages: Conversation history
        tools: Available tools
        timeout: Seconds to wait before giving up
    
    Returns:
        Response object or raises exception
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
            tools=tools,
            timeout=timeout  # CRITICAL: Always set timeout
        )
        return response
        
    except Timeout as e:
        # LLM call took too long
        raise TimeoutError(f"LLM API call exceeded {timeout}s timeout")
    
    except OpenAIError as e:
        # Other API errors
        raise Exception(f"LLM API error: {e}")
```

**Integration into agent:**

```python
class SafeAgent:
    def run(self, user_query):
        messages = [...]
        
        for iteration in range(self.max_iterations):
            try:
                # TIMEOUT ON LLM CALL
                response = call_llm_with_timeout(
                    messages,
                    self.tools,
                    timeout=30
                )
                
            except TimeoutError:
                return "I'm having trouble processing your request. Please try again."
            
            # ... rest of ReAct loop ...
```

### On External API Calls

```python
import requests

def call_external_api_with_timeout(url, params, timeout=5):
    """
    Call external API with timeout.
    
    Args:
        url: API endpoint
        params: Query parameters
        timeout: Seconds before giving up (tuple for connect + read)
    
    Returns:
        dict: API response or error
    """
    try:
        response = requests.get(
            url,
            params=params,
            timeout=(2, timeout)  # (connect_timeout, read_timeout)
        )
        
        response.raise_for_status()  # Raise exception for 4xx/5xx
        return response.json()
        
    except requests.Timeout:
        return {
            "error": "API timeout",
            "message": f"Request exceeded {timeout}s timeout"
        }
    
    except requests.ConnectionError:
        return {
            "error": "Connection failed",
            "message": "Could not connect to API"
        }
    
    except requests.RequestException as e:
        return {
            "error": "Request failed",
            "message": str(e)
        }
```

### On Database Queries

```python
import psycopg2
from psycopg2 import extensions

def query_database_with_timeout(query, params, timeout=3):
    """
    Execute database query with timeout.
    
    Args:
        query: SQL query
        params: Query parameters
        timeout: Seconds before canceling query
    
    Returns:
        list: Query results or raises exception
    """
    conn = psycopg2.connect(database="mydb")
    
    try:
        # Set statement timeout
        cursor = conn.cursor()
        cursor.execute(f"SET statement_timeout = {timeout * 1000}")  # milliseconds
        
        # Execute query
        cursor.execute(query, params)
        results = cursor.fetchall()
        
        return results
        
    except psycopg2.errors.QueryCanceled:
        raise TimeoutError(f"Database query exceeded {timeout}s timeout")
    
    finally:
        conn.close()
```

---

## Why You Need Retries

**Many failures are transient (temporary).**

Transient failures:
- Network blip (connection dropped momentarily)
- Server overload (503 Service Unavailable)
- Rate limit hit (429 Too Many Requests)
- Temporary database lock

**Solution:** Wait a bit and try again.

---

## Exponential Backoff

**Don't retry immediately.** That often makes things worse.

**Exponential backoff:** Wait longer between each retry.

```
Attempt 1: Immediate
Attempt 2: Wait 1 second
Attempt 3: Wait 2 seconds
Attempt 4: Wait 4 seconds
Attempt 5: Wait 8 seconds
```

Why this works:
- Gives server time to recover
- Prevents overwhelming already-struggling service
- Standard practice across industry

---

## Implementing Retry with Tenacity

The `tenacity` library makes retry logic easy.

### Basic Retry

```python
from tenacity import retry, stop_after_attempt

@retry(stop=stop_after_attempt(3))
def call_api():
    """Will retry up to 3 times total."""
    response = requests.get("https://api.example.com/data", timeout=5)
    response.raise_for_status()
    return response.json()
```

### Exponential Backoff

```python
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential
)

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=1, max=10)
)
def call_api_with_backoff():
    """
    Retry with exponential backoff:
    - Attempt 1: Immediate
    - Attempt 2: Wait ~1 second
    - Attempt 3: Wait ~2 seconds
    """
    response = requests.get("https://api.example.com/data", timeout=5)
    response.raise_for_status()
    return response.json()
```

**Parameters explained:**
- `multiplier=1`: Base wait time (seconds)
- `min=1`: Minimum wait (won't wait less than this)
- `max=10`: Maximum wait (won't wait more than this)

Formula: `wait = min(max, multiplier * (2 ^ attempt_number))`

### Jittered Backoff (Recommended)

Add randomness to prevent "thundering herd" problem.

```python
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential_jitter
)
import random

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential_jitter(initial=1, max=10)
)
def call_api_with_jitter():
    """
    Retry with jittered exponential backoff.
    
    Adds random 0-50% to wait time to prevent
    many clients retrying simultaneously.
    """
    response = requests.get("https://api.example.com/data", timeout=5)
    response.raise_for_status()
    return response.json()

# Alternative: Manual jitter
@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=1, max=10)
)
def call_api_manual_jitter():
    # Add jitter before making request
    jitter = random.uniform(0, 0.5)
    time.sleep(jitter)
    
    response = requests.get("https://api.example.com/data", timeout=5)
    response.raise_for_status()
    return response.json()
```

### Retry Only Specific Exceptions

**CRITICAL:** Don't retry everything!

```python
from tenacity import (
    retry,
    stop_after_attempt,
    retry_if_exception_type,
    wait_exponential
)
import requests

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=1, max=10),
    retry=retry_if_exception_type((
        requests.Timeout,
        requests.ConnectionError,
        requests.exceptions.HTTPError  # Only for 5xx errors
    ))
)
def call_api_smart_retry():
    """Only retry transient failures."""
    response = requests.get("https://api.example.com/data", timeout=5)
    
    # Raise exception for 4xx (client errors) - don't retry these!
    if 400 <= response.status_code < 500:
        raise ValueError(f"Client error {response.status_code}")
    
    # Raise exception for 5xx (server errors) - DO retry these
    response.raise_for_status()
    
    return response.json()
```

**What to retry:**
- Network errors (timeout, connection failed)
- 5xx server errors (500, 502, 503, 504)
- 429 rate limit (but add backoff)

**What NOT to retry:**
- 4xx client errors (400, 401, 403, 404)
  - These won't succeed on retry - the request is bad
- Authentication errors
- Validation errors

---

## Complete Example: Tool with Timeout and Retry

```python
import requests
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type
)
import logging

logger = logging.getLogger(__name__)

class SafeToolExecutor:
    """Executes tools with timeout and retry."""
    
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=1, max=10),
        retry=retry_if_exception_type((
            requests.Timeout,
            requests.ConnectionError
        ))
    )
    def search_api(self, query: str, max_results: int = 10) -> dict:
        """
        Search external API with timeout and retry.
        
        Will retry up to 3 times with exponential backoff
        on network errors and timeouts.
        """
        logger.info(f"Searching for: {query}")
        
        try:
            response = requests.get(
                "https://api.search.com/v1/search",
                params={
                    "q": query,
                    "limit": max_results
                },
                timeout=(2, 5),  # 2s connect, 5s read
                headers={"Authorization": f"Bearer {self.api_key}"}
            )
            
            # Don't retry client errors (4xx)
            if 400 <= response.status_code < 500:
                logger.error(f"Client error {response.status_code}")
                return {
                    "error": f"Invalid request: {response.status_code}",
                    "results": []
                }
            
            # Do retry server errors (5xx) - tenacity will handle
            response.raise_for_status()
            
            data = response.json()
            logger.info(f"Found {len(data.get('results', []))} results")
            
            return {
                "status": "success",
                "results": data.get("results", []),
                "count": len(data.get("results", []))
            }
            
        except requests.Timeout:
            logger.warning(f"Search API timeout for query: {query}")
            # Tenacity will retry this automatically
            raise
        
        except requests.ConnectionError:
            logger.warning(f"Connection failed to search API")
            # Tenacity will retry this automatically
            raise
        
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return {
                "error": str(e),
                "results": []
            }
```

**Usage in agent:**

```python
def _execute_tool(self, tool_name: str, args: dict) -> dict:
    """Execute tool with automatic timeout and retry."""
    
    tool_executor = SafeToolExecutor()
    
    try:
        if tool_name == "search":
            return tool_executor.search_api(
                query=args["query"],
                max_results=args.get("max_results", 10)
            )
        
        # ... other tools ...
        
    except Exception as e:
        # All retries failed
        logger.error(f"Tool {tool_name} failed after retries: {e}")
        return {
            "error": "Service temporarily unavailable",
            "message": "Please try again in a moment"
        }
```

---

## Retry with Logging

Track retry attempts for debugging:

```python
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    before_log,
    after_log
)
import logging

logger = logging.getLogger(__name__)

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=1, max=10),
    before=before_log(logger, logging.INFO),  # Log before each attempt
    after=after_log(logger, logging.INFO)     # Log after each attempt
)
def call_api_with_logging():
    """Logs each retry attempt."""
    response = requests.get("https://api.example.com/data", timeout=5)
    response.raise_for_status()
    return response.json()

# Logs will show:
# INFO: Starting call 1 of 3
# INFO: Finished call 1 after 5.2s
# INFO: Starting call 2 of 3
# INFO: Finished call 2 after 2.1s
```

### Custom Retry Callback

```python
from tenacity import retry, stop_after_attempt

def log_retry_attempt(retry_state):
    """Called after each failed attempt."""
    attempt_number = retry_state.attempt_number
    outcome = retry_state.outcome
    
    logger.warning(
        f"Retry attempt {attempt_number} failed: {outcome.exception()}"
    )

@retry(
    stop=stop_after_attempt(3),
    after=log_retry_attempt
)
def call_api():
    response = requests.get("https://api.example.com/data", timeout=5)
    response.raise_for_status()
    return response.json()
```

---

## Retry with Rate Limiting

Some APIs have rate limits. Handle 429 specially:

```python
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
    retry_if_result
)
import requests

def is_rate_limited(response):
    """Check if response indicates rate limiting."""
    return response.status_code == 429

@retry(
    stop=stop_after_attempt(5),  # More attempts for rate limits
    wait=wait_exponential(multiplier=2, min=4, max=60),  # Longer waits
    retry=retry_if_exception_type((
        requests.Timeout,
        requests.ConnectionError
    ))
)
def call_rate_limited_api():
    """
    Call API that may rate limit.
    
    Waits longer between retries: 4s → 8s → 16s → 32s → 60s
    """
    response = requests.get("https://api.example.com/data", timeout=5)
    
    if response.status_code == 429:
        # Check Retry-After header
        retry_after = response.headers.get("Retry-After")
        if retry_after:
            wait_seconds = int(retry_after)
            logger.info(f"Rate limited. Waiting {wait_seconds}s")
            time.sleep(wait_seconds)
        
        # Raise to trigger retry
        raise requests.exceptions.HTTPError("Rate limited")
    
    response.raise_for_status()
    return response.json()
```

---

## Integration with Agent

Put it all together in your agent:

```python
import openai
import requests
from tenacity import retry, stop_after_attempt, wait_exponential
import logging

logger = logging.getLogger(__name__)

class ProductionAgent:
    """Agent with timeout and retry on all operations."""
    
    def run(self, user_query: str) -> dict:
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_query}
        ]
        
        for iteration in range(self.max_iterations):
            try:
                # LLM call with timeout
                response = self._call_llm_with_timeout(messages)
                
            except TimeoutError:
                logger.error("LLM timeout")
                return {
                    "success": False,
                    "error": "Processing timeout",
                    "message": "Request took too long. Please try again."
                }
            
            except Exception as e:
                logger.error(f"LLM error: {e}")
                return {
                    "success": False,
                    "error": str(e)
                }
            
            message = response.choices[0].message
            
            if not message.tool_calls:
                return {
                    "success": True,
                    "result": message.content
                }
            
            # Execute tools with retry
            messages.append(message)
            for tool_call in message.tool_calls:
                try:
                    result = self._execute_tool_with_retry(
                        tool_call.function.name,
                        tool_call.function.arguments
                    )
                except Exception as e:
                    # All retries failed
                    result = {"error": str(e)}
                
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": json.dumps(result)
                })
        
        return {
            "success": False,
            "error": "max_iterations_reached"
        }
    
    def _call_llm_with_timeout(self, messages: list, timeout: int = 30):
        """Call LLM with timeout."""
        try:
            return openai.ChatCompletion.create(
                model="gpt-4",
                messages=messages,
                tools=self.tools,
                timeout=timeout
            )
        except openai.Timeout:
            raise TimeoutError(f"LLM call exceeded {timeout}s")
    
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=1, max=10),
        retry=retry_if_exception_type((
            requests.Timeout,
            requests.ConnectionError
        ))
    )
    def _execute_tool_with_retry(self, tool_name: str, args: str) -> dict:
        """Execute tool with automatic retry on transient failures."""
        arguments = json.loads(args)
        
        if tool_name == "search":
            return self._tool_search(arguments)
        
        elif tool_name == "analyze":
            return self._tool_analyze(arguments)
        
        else:
            return {"error": f"Unknown tool: {tool_name}"}
    
    def _tool_search(self, args: dict) -> dict:
        """Search tool with timeout."""
        response = requests.get(
            "https://api.search.com/search",
            params=args,
            timeout=(2, 5)
        )
        response.raise_for_status()
        return response.json()
```

---

## Testing Timeouts and Retries

### Test 1: Verify Timeout Works

```python
import pytest
from unittest.mock import patch, Mock
import time

def test_timeout_enforced():
    """Tool execution should timeout after limit."""
    
    def slow_function():
        time.sleep(10)  # Simulate slow operation
        return "success"
    
    # Should timeout before 10 seconds
    with pytest.raises(TimeoutError):
        # Your timeout wrapper here
        result = execute_with_timeout(slow_function, timeout=2)
```

### Test 2: Verify Retry Happens

```python
def test_retry_on_transient_failure():
    """Should retry on network errors."""
    
    call_count = 0
    
    def flaky_api():
        nonlocal call_count
        call_count += 1
        
        if call_count < 3:
            raise requests.ConnectionError("Network error")
        
        return {"status": "success"}
    
    # Should succeed on 3rd try
    result = call_with_retry(flaky_api)
    
    assert call_count == 3
    assert result["status"] == "success"
```

### Test 3: Verify No Retry on Client Errors

```python
def test_no_retry_on_client_error():
    """Should not retry on 4xx errors."""
    
    call_count = 0
    
    def api_with_client_error():
        nonlocal call_count
        call_count += 1
        
        raise requests.HTTPError("404 Not Found")
    
    # Should fail immediately without retry
    with pytest.raises(requests.HTTPError):
        result = call_with_smart_retry(api_with_client_error)
    
    assert call_count == 1  # Called only once, no retries
```

---

## Common Pitfalls

### ❌ No Timeout

```python
# BAD: Can hang forever
response = requests.get("https://api.example.com/data")
```

```python
# GOOD: Will timeout
response = requests.get(
    "https://api.example.com/data",
    timeout=5
)
```

### ❌ Retry Everything

```python
# BAD: Retries client errors that will never succeed
@retry(stop=stop_after_attempt(3))
def call_api():
    response = requests.get("https://api.example.com/data")
    response.raise_for_status()  # Retries 404, 401, etc.
```

```python
# GOOD: Only retries transient failures
@retry(
    stop=stop_after_attempt(3),
    retry=retry_if_exception_type((
        requests.Timeout,
        requests.ConnectionError
    ))
)
def call_api():
    response = requests.get("https://api.example.com/data", timeout=5)
    
    # Don't raise for 4xx - let it return error
    if 400 <= response.status_code < 500:
        return {"error": f"Client error {response.status_code}"}
    
    response.raise_for_status()  # Only raises for 5xx
```

### ❌ Immediate Retry

```python
# BAD: Retries immediately, hammers server
for i in range(3):
    try:
        return call_api()
    except:
        continue  # Retry immediately
```

```python
# GOOD: Exponential backoff
@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=1, max=10)
)
def call_api():
    # ... implementation ...
```

---

## Summary Checklist

- [ ] Timeouts on ALL external calls (LLM, APIs, database)
- [ ] Timeout values appropriate for operation type
- [ ] Retry with exponential backoff implemented
- [ ] Jitter added to prevent thundering herd
- [ ] Maximum 3-5 retry attempts
- [ ] Only retries transient failures (not 4xx errors)
- [ ] Retry attempts logged
- [ ] All retries failed case handled
- [ ] Timeout and retry tested

**Next Step:** Once timeouts and retries work, proceed to the Circuit Breaker guide to handle repeated failures.
