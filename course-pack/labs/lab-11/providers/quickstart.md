Quick Start Guide
1. Install Dependencies (2 min)
bashpip install openai anthropic python-dotenv
2. Setup Files (3 min)
bash# Create providers directory
mkdir -p src/providers

# Create __init__.py (required!)
touch src/providers/__init__.py

# Copy templates to these files:
# - base_provider.py
# - openai_provider.py
# - anthropic_provider.py
# - router.py

# Create test file
# - test_fallback.py
3. Add API Keys (1 min)
Create .env file:
bashOPENAI_API_KEY=your-key-here
ANTHROPIC_API_KEY=your-key-here
4. Test (1 min)
bashpython test_fallback.py
You should see:
Trying gpt-4o-mini (attempt 1)...
✓ Success with gpt-4o-mini

==================================================
Response: [haiku about AI]
Model: gpt-4o-mini
Tokens: 45
Cost: $0.0001
Latency: 856ms
==================================================

Common Issues
Issue: ModuleNotFoundError: No module named 'src'
Solution: Make sure you have __init__.py in the src/providers/ directory.
bashtouch src/__init__.py
touch src/providers/__init__.py
Issue: Invalid API key
Solution: Check your .env file format:
bash# Correct
OPENAI_API_KEY=sk-abc123

# Wrong (no quotes needed)
OPENAI_API_KEY="sk-abc123"
Issue: Rate limit exceeded
Solution: You're on free tier. Wait 60 seconds or upgrade account.
Issue: Provider failed but didn't fallback
Solution: Check error classification in classify_error(). Make sure it returns correct error_type.

Integration with Your Capstone
Option 1: Direct Integration
Replace your existing LLM calls with the router:
python# Before (direct OpenAI call)
response = openai_client.chat.completions.create(...)

# After (with fallbacks)
from src.providers.router import SimpleRouter
router = SimpleRouter(providers=[openai, anthropic])
response = router.generate(prompt)
Option 2: Wrapper Function
Create a helper function in your existing code:
pythondef generate_with_fallback(prompt: str) -> str:
    """Generate with automatic fallbacks"""
    router = SimpleRouter(providers=[openai, anthropic])
    response = router.generate(prompt)
    return response.content

Testing Fallbacks
Test Primary Provider Failure
python# In test_fallback.py, simulate OpenAI failure
openai = OpenAIProvider(
    api_key="invalid-key",  # This will fail
    model="gpt-4o-mini"
)

anthropic = AnthropicProvider(
    api_key=os.getenv("ANTHROPIC_API_KEY"),  # This will work
    model="claude-haiku-3-5-20241022"
)

router = SimpleRouter(providers=[openai, anthropic])
response = router.generate("Write a haiku")

# Should see:
# Trying gpt-4o-mini...
# ✗ Error: api_error
# Trying claude-haiku...
# ✓ Success with claude-haiku

Completion Checklist
By end of lab, you should have:

 All 5 template files created
 API keys added to .env
 Dependencies installed
 test_fallback.py running successfully
 Fallback working (tested by breaking primary provider)
 Basic cost tracking showing in output
 Code committed to Git

Time estimate: 30-45 minutes if you follow templates exactly.

Next Steps
After completing this implementation:

Test in production (deploy and verify fallbacks work)
Record your demo video (see video script template)
Document in README (add "Multi-vendor fallbacks" to features)
Prepare presentation (show the fallback working live)


Remember: The goal is "good enough to demo," not perfection. ✅
Questions? Office hours Friday 2-4pm and Monday 10am-12pm.
