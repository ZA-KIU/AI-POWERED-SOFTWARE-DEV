# Safety and Privacy Checklist  
**Lab 6: Function Calling & Structured Outputs**

| Check | Status |
|-------|---------|
| Removed all API keys from code | ✅ |
| No private or personal data used | ✅ |
| Function handles bad inputs safely | ✅ |
| Function returns friendly error messages | ✅ |
| User consent not required (no user data collected) | ✅ |

### Example Safety Handling
If a user enters “delete everything” or an invalid order ID, the code returns:  
`{"success": false, "error": "Invalid input. Please try again."}`

### Plan to Improve
Add keyword filter for unsafe phrases in Week 7.
