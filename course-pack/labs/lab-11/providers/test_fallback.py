import os
from src.providers.openai_provider import OpenAIProvider
from src.providers.anthropic_provider import AnthropicProvider
from src.providers.router import SimpleRouter

def test_fallback():
    # Setup providers
    openai = OpenAIProvider(
        api_key=os.getenv("OPENAI_API_KEY"),
        model="gpt-4o-mini"
    )
    
    anthropic = AnthropicProvider(
        api_key=os.getenv("ANTHROPIC_API_KEY"),
        model="claude-haiku-3-5-20241022"
    )
    
    # Create router (OpenAI first, Anthropic backup)
    router = SimpleRouter(providers=[openai, anthropic])
    
    # Test
    print("Testing fallback chain...\n")
    
    try:
        response = router.generate("Write a haiku about AI")
        
        print(f"\n{'='*50}")
        print(f"Response: {response.content}")
        print(f"Model: {response.model}")
        print(f"Tokens: {response.tokens_used}")
        print(f"Cost: ${response.cost:.4f}")
        print(f"Latency: {response.latency_ms:.0f}ms")
        print(f"{'='*50}")
        
    except Exception as e:
        print(f"\nERROR: {e}")

if __name__ == "__main__":
    test_fallback()
