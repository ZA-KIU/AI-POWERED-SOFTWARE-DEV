# Agent Safety Checklist

## ReAct Loop
- [ ] max_iterations set (recommended: 5)
- [ ] Conversation history maintained across iterations
- [ ] Exit on no tool calls
- [ ] Exit message when max iterations reached
- [ ] Loop counter logged

## Timeouts
- [ ] LLM API calls have timeout (10-30s)
- [ ] External API calls have timeout (2-5s)
- [ ] Database queries have timeout (1-3s)
- [ ] File operations have timeout (5s)
- [ ] Timeout exceptions caught and handled

## Retry Logic
- [ ] Exponential backoff implemented (1s → 2s → 4s)
- [ ] Jitter added to backoff (random 0-0.5s)
- [ ] Maximum 3 retry attempts
- [ ] Only retries transient errors (5xx, network, timeout)
- [ ] Does NOT retry client errors (4xx)
- [ ] Retry count logged

## Circuit Breakers
- [ ] Implemented per-tool (not global)
- [ ] Opens after 5 consecutive failures
- [ ] Stays open for 60 seconds
- [ ] Half-open state for testing recovery
- [ ] Circuit state logged
- [ ] Fails fast when open

## Authorization
- [ ] Permission levels defined (read/write/admin)
- [ ] Tools mapped to required permissions
- [ ] Authorization check BEFORE tool execution
- [ ] Never trusts agent to enforce auth
- [ ] PermissionError raised when unauthorized
- [ ] Failed auth attempts logged

## Input Validation
- [ ] Pydantic schemas for all tool inputs
- [ ] Type validation
- [ ] Range validation
- [ ] Format validation
- [ ] Business rule validation
- [ ] Clear error messages on validation failure
- [ ] Validation errors logged

## Audit Logging
- [ ] Logs to file (not just console)
- [ ] JSON format for parsing
- [ ] Includes: timestamp, user_id, tool, args, result, cost, latency, success
- [ ] Does NOT include: passwords, API keys, credit cards, PII
- [ ] Log rotation configured
- [ ] Logs are readable and useful

## Cost Tracking
- [ ] Tracks LLM API costs
- [ ] Tracks tool execution costs
- [ ] Accumulates across agent run
- [ ] Checks against limit before each LLM call
- [ ] Raises exception when limit exceeded
- [ ] Final cost logged
- [ ] Cost included in agent response

## Graceful Degradation
- [ ] Agent NEVER crashes - always returns response
- [ ] Structured error responses
- [ ] User-friendly error messages
- [ ] Technical details in logs (not user response)
- [ ] Fallback behaviors defined
- [ ] Partial results returned when possible

## Error Handling
- [ ] Try-except on all external calls
- [ ] Specific exception types (not just Exception)
- [ ] Full stack traces logged
- [ ] Error context captured
- [ ] Errors don't leak sensitive data to user

## Testing
- [ ] Max iterations test
- [ ] Timeout test
- [ ] Retry test
- [ ] Circuit breaker test
- [ ] Authorization test
- [ ] Cost limit test
- [ ] Audit log test
- [ ] All tests passing
