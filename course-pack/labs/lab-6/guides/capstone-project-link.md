# Capstone Link  
**Team Name:** AI Support Hub  
**Project Title:** Smart Customer Assistant  

### Function Reused from Lab 6
`lookup_order_status(order_id)`  
Purpose: Retrieve current shipping details for customers.

### Integration Plan
- Move function to `src/functions/tools.py`
- Connect with real order API in Week 7
- Use in chatbot flow:  
  User: “Where’s my order ORD-1245?”  
  → Function returns status → AI replies with delivery update

### Next Step
Add a new function next week:  
`calculate_refund(order_id, reason)`
