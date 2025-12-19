import time
from typing import List
from .base_provider import LLMProvider, ProviderResponse, ProviderError

class SimpleRouter:
    def __init__(self, providers: List[LLMProvider], max_retries: int = 3):
        self.providers = providers
        self.max_retries = max_retries
    
    def generate(self, prompt: str, max_tokens: int = 500) -> ProviderResponse:
        """Try each provider until one succeeds"""
        
        for provider in self.providers:
            for retry in range(self.max_retries):
                try:
                    print(f"Trying {provider.model} (attempt {retry + 1})...")
                    response = provider.generate(prompt, max_tokens)
                    print(f"✓ Success with {provider.model}")
                    return response
                
                except Exception as e:
                    error = provider.classify_error(e)
                    print(f"✗ Error: {error.error_type}")
                    
                    # Rate limited? Wait and retry same provider
                    if error.error_type == "rate_limit" and retry < self.max_retries - 1:
                        wait_time = 2 ** retry  # 1s, 2s, 4s
                        print(f"  Waiting {wait_time}s...")
                        time.sleep(wait_time)
                        continue
                    
                    # Invalid request? Stop immediately
                    if error.error_type == "invalid_request":
                        raise Exception(f"Invalid: {error.message}")
                    
                    # Try next provider
                    break
        
        raise Exception("All providers failed")
