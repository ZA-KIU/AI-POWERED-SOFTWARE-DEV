# Evaluation Notes  
**Lab 6: Function Calling & Structured Outputs**

### Function Tested
`lookup_order_status(order_id)`

### Test Summary
| Test | Input | Expected | Got | Time (s) | Pass |
|------|--------|-----------|-----|-----------|------|
| 1 | "ORD-1" | "shipped" | "shipped" | 0.32 | ✅ |
| 2 | "ORD-2" | "delivered" | "delivered" | 0.28 | ✅ |
| 3 | "ORD-999" | "not found" | "not found" | 0.35 | ✅ |

### Observations
- Average response time: 0.31 s  
- No crashes or timeout errors  
- Output matched schema for all tests  
- One warning: “Tracking number” missing on `ORD-999` (expected)  

### Next Step
Add more test cases once real database connection is added.
