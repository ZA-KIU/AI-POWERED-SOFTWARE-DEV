# Smoke Test Checklist

**Project:** [Your Project Name]  
**Team:** [Team Name]  
**Test Date:** [Date]  
**Tested By:** [Names]

This checklist validates that critical system functionality works before proceeding to Week 8 agent orchestration. For each test, mark **PASS** or **FAIL** and provide evidence.

---

## Instructions

1. Run each test in order
2. Mark result: **✅ PASS** or **❌ FAIL**
3. Collect evidence (log snippet, screenshot, measurement)
4. For failures: document why and mitigation plan
5. Store all evidence in `docs/evidence/` folder

---

## Core Functionality Tests

### Test 1: End-to-End Request Flow

**What we're testing:** User input → System processing → LLM → Response back to user

**How to test:**
1. Start your application
2. Submit a test query via your interface
3. Observe the complete flow
4. Verify response is correct

**Success criteria:**
- Request completes without errors
- Response is relevant to query
- Can repeat test reliably

**Result:** [ ] ✅ PASS  [ ] ❌ FAIL

**Evidence:**
```
[Paste log snippet or screenshot here]

Example:
Request ID: req_abc123
Input: "What is the capital of France?"
Output: "The capital of France is Paris."
Time: 2.3s
Status: Success
```

**If FAIL, why?**  
[Describe the problem]

**Mitigation plan:**  
[What will you fix? Who? By when?]

---

### Test 2: Error Handling - API Failure

**What we're testing:** System gracefully handles LLM API errors

**How to test:**
1. Temporarily break your API connection (wrong key, disconnect network, etc.)
2. Submit a query
3. Verify error is caught and logged
4. Verify user sees appropriate error message (not a crash)

**Success criteria:**
- System catches the error
- Error is logged with details
- User sees helpful error message
- Application doesn't crash

**Result:** [ ] ✅ PASS  [ ] ❌ FAIL

**Evidence:**
```
[Error log or screenshot]
```

**If FAIL, why?**  
[Describe the problem]

**Mitigation plan:**  
[What will you fix? Who? By when?]

---

### Test 3: Error Handling - Invalid Input

**What we're testing:** System validates and rejects invalid user input

**How to test:**
1. Submit empty query
2. Submit extremely long query (>1000 characters)
3. Submit query with special characters/SQL injection attempts
4. Verify each is handled appropriately

**Success criteria:**
- Invalid inputs are rejected before reaching LLM
- User sees clear validation error messages
- No crashes or unexpected behavior

**Result:** [ ] ✅ PASS  [ ] ❌ FAIL

**Evidence:**
```
[Test results for each invalid input type]
```

**If FAIL, why?**  
[Describe the problem]

**Mitigation plan:**  
[What will you fix? Who? By when?]

---

## Performance Tests

### Test 4: Response Latency - Single Request

**What we're testing:** Acceptable response time for typical request

**How to test:**
1. Submit 5 test queries
2. Measure end-to-end latency for each
3. Calculate p50, p95

**Success criteria:**
- p50 (median) < 5 seconds
- p95 < 10 seconds
- All requests complete

**Result:** [ ] ✅ PASS  [ ] ❌ FAIL

**Evidence:**
| Request | Latency (ms) |
|---------|--------------|
| 1       | [value]      |
| 2       | [value]      |
| 3       | [value]      |
| 4       | [value]      |
| 5       | [value]      |
| **p50** | **[value]**  |
| **p95** | **[value]**  |

**If FAIL, why?**  
[Describe the problem - which component is slow?]

**Mitigation plan:**  
[What will you optimize? Who? By when?]

---

### Test 5: Cost Tracking

**What we're testing:** System tracks token usage and cost

**How to test:**
1. Submit 3 test queries
2. Verify tokens are logged for each
3. Calculate cost per request
4. Verify cost calculations are correct

**Success criteria:**
- Token usage logged for every request
- Input and output tokens separately tracked
- Cost calculated correctly (check against API pricing)
- Can show cost per request

**Result:** [ ] ✅ PASS  [ ] ❌ FAIL

**Evidence:**
| Request | Input Tokens | Output Tokens | Total | Cost (USD) |
|---------|--------------|---------------|-------|------------|
| 1       | [value]      | [value]       | [sum] | [value]    |
| 2       | [value]      | [value]       | [sum] | [value]    |
| 3       | [value]      | [value]       | [sum] | [value]    |
| **Avg** | **[avg]**    | **[avg]**     | **[avg]** | **[avg]** |

**If FAIL, why?**  
[Describe the problem]

**Mitigation plan:**  
[What will you implement? Who? By when?]

---

## Integration Tests

### Test 6: Database Integration (if applicable)

**What we're testing:** Database reads/writes work correctly

**How to test:**
1. Query data from database
2. Verify correct data returned
3. (If applicable) Write data to database
4. Verify data persisted correctly

**Success criteria:**
- Database connection established
- Queries execute successfully
- Data is correct
- No connection leaks

**Result:** [ ] ✅ PASS  [ ] ❌ FAIL  [ ] N/A

**Evidence:**
```
[Query results or screenshots]
```

**If FAIL, why?**  
[Describe the problem]

**Mitigation plan:**  
[What will you fix? Who? By when?]

---

### Test 7: RAG Retrieval (if applicable)

**What we're testing:** Document retrieval works and returns relevant results

**How to test:**
1. Submit query that should trigger retrieval
2. Verify documents are retrieved
3. Check relevance scores
4. Verify retrieved content is used in response

**Success criteria:**
- Retrieval executes successfully
- Returns k documents as specified
- Documents are relevant (score > threshold)
- Retrieved content appears in LLM context

**Result:** [ ] ✅ PASS  [ ] ❌ FAIL  [ ] N/A

**Evidence:**
```
Query: [test query]
Retrieved docs: [number]
Top doc score: [value]
Top doc content: [snippet]
```

**If FAIL, why?**  
[Describe the problem]

**Mitigation plan:**  
[What will you fix? Who? By when?]

---

### Test 8: Function Calling (if applicable)

**What we're testing:** LLM can successfully call defined functions

**How to test:**
1. Submit query that should trigger function call
2. Verify LLM requests function call
3. Verify function executes
4. Verify result is returned to LLM
5. Verify LLM uses result in final response

**Success criteria:**
- Function call is triggered appropriately
- Arguments are correct
- Function executes successfully
- Result is formatted correctly
- LLM incorporates result

**Result:** [ ] ✅ PASS  [ ] ❌ FAIL  [ ] N/A

**Evidence:**
```
Function called: [name]
Arguments: [values]
Result: [output]
Final response: [LLM response using function result]
```

**If FAIL, why?**  
[Describe the problem]

**Mitigation plan:**  
[What will you fix? Who? By when?]

---

## Logging & Observability Tests

### Test 9: Structured Logging

**What we're testing:** Events are logged in structured format (JSON)

**How to test:**
1. Submit test query
2. Examine log output
3. Verify logs are structured (JSON, not print statements)
4. Verify all critical fields present

**Success criteria:**
- Logs are in JSON format
- Each log has timestamp, request_id, event_type
- Logs are searchable/parseable
- No sensitive data in logs (API keys, PII)

**Result:** [ ] ✅ PASS  [ ] ❌ FAIL

**Evidence:**
```json
[Example log entry]
{
  "timestamp": "2025-01-15T10:30:00Z",
  "request_id": "req_abc123",
  "event_type": "llm_response",
  "latency_ms": 2300,
  "tokens_used": 155,
  "cost_usd": 0.0046
}
```

**If FAIL, why?**  
[Describe the problem]

**Mitigation plan:**  
[What will you implement? Who? By when?]

---

### Test 10: Request Tracing

**What we're testing:** Can trace single request through entire system

**How to test:**
1. Submit test query and note request_id
2. Search logs for that request_id
3. Verify you can see all events for that request
4. Verify events show correct flow

**Success criteria:**
- Request ID is generated and logged
- Same request ID appears in all related events
- Can reconstruct request flow from logs
- Events are in correct order

**Result:** [ ] ✅ PASS  [ ] ❌ FAIL

**Evidence:**
```
Request ID: req_abc123

Events found:
1. user_input (10:30:00.000)
2. llm_request (10:30:00.123)
3. llm_response (10:30:02.456)
4. response_sent (10:30:02.500)

All events have same request_id ✓
```

**If FAIL, why?**  
[Describe the problem]

**Mitigation plan:**  
[What will you implement? Who? By when?]

---

## Data Quality Tests

### Test 11: Schema Validation

**What we're testing:** Data matches documented event schemas

**How to test:**
1. Generate sample events (user input, LLM response, error)
2. Validate against your documented JSON schemas
3. Verify validation catches invalid data

**Success criteria:**
- Valid data passes validation
- Invalid data is rejected
- All required fields are enforced
- Type constraints work correctly

**Result:** [ ] ✅ PASS  [ ] ❌ FAIL

**Evidence:**
```
Schema: user_input_event
Valid instance: ✓ Passed validation
Invalid instance (missing field): ✓ Rejected correctly
Invalid instance (wrong type): ✓ Rejected correctly
```

**If FAIL, why?**  
[Describe the problem]

**Mitigation plan:**  
[What will you fix? Who? By when?]

---

### Test 12: Data Consistency

**What we're testing:** Data remains consistent across system components

**How to test:**
1. Submit query and track data through system
2. Verify data doesn't get corrupted or lost
3. Check that token counts, costs match across logs
4. Verify request/response data is preserved accurately

**Success criteria:**
- User query text matches in all logs
- Token counts consistent across events
- Cost calculations use same token counts
- No data corruption or truncation

**Result:** [ ] ✅ PASS  [ ] ❌ FAIL

**Evidence:**
```
[Show data consistency across multiple log events]
```

**If FAIL, why?**  
[Describe the problem]

**Mitigation plan:**  
[What will you fix? Who? By when?]

---

## Security Tests

### Test 13: API Key Protection

**What we're testing:** API keys are not exposed in logs or responses

**How to test:**
1. Search logs for API key strings
2. Check error messages sent to users
3. Verify keys are loaded from environment variables
4. Check that `.env` is in `.gitignore`

**Success criteria:**
- No API keys in logs
- No API keys in error messages to users
- Keys loaded from secure storage (env vars)
- `.env` file not committed to git

**Result:** [ ] ✅ PASS  [ ] ❌ FAIL

**Evidence:**
```
Log search for "sk-": No results ✓
.env in .gitignore: ✓
Keys loaded from environment: ✓
```

**If FAIL, why?**  
[Describe the problem]

**Mitigation plan:**  
[What will you fix? Who? By when?]

---

### Test 14: Input Sanitization

**What we're testing:** User input is sanitized before use

**How to test:**
1. Submit query with HTML tags: `<script>alert('test')</script>`
2. Submit query with SQL-like syntax: `'; DROP TABLE users; --`
3. Submit query with special characters
4. Verify none cause issues

**Success criteria:**
- HTML/script tags are escaped or removed
- SQL syntax doesn't reach database layer
- System handles special characters gracefully
- No injection vulnerabilities

**Result:** [ ] ✅ PASS  [ ] ❌ FAIL

**Evidence:**
```
Test 1 (HTML): [result]
Test 2 (SQL): [result]
Test 3 (Special chars): [result]
```

**If FAIL, why?**  
[Describe the problem]

**Mitigation plan:**  
[What will you fix? Who? By when?]

---

## Summary

### Overall Results

- **Total Tests:** [number]
- **Passed:** [number] ✅
- **Failed:** [number] ❌
- **Not Applicable:** [number] N/A
- **Pass Rate:** [percentage]%

### Critical Failures

[List any failed tests that block Week 8 readiness]

1. [Test name] - [Why critical] - [Fix by when]
2. [Test name] - [Why critical] - [Fix by when]

### Action Items

| Priority | Item | Owner | Deadline | Status |
|----------|------|-------|----------|--------|
| Critical | [Task] | [Name] | [Date] | [ ] |
| Important | [Task] | [Name] | [Date] | [ ] |
| Nice-to-have | [Task] | [Name] | [Date] | [ ] |

### Week 8 Readiness Assessment

**Overall Status:** [ ] GREEN ✅  [ ] YELLOW ⚠️  [ ] RED ❌

**Justification:**
[Explain your readiness assessment based on smoke test results]

---

## Notes

**Issues Encountered:**
[Document any unexpected findings during testing]

**Workarounds Implemented:**
[Note any temporary workarounds for failed tests]

**Questions for Instructor:**
[List questions that came up during testing]

---

## Sign-off

**Completed by:**
- [Name 1]: [Signature/Date]
- [Name 2]: [Signature/Date]
- [Name 3]: [Signature/Date] (if applicable)

**Reviewed by Instructor:** [Signature/Date]

**Ready for Week 8:** [ ] YES  [ ] NO  [ ] CONDITIONAL (specify: _____________)
