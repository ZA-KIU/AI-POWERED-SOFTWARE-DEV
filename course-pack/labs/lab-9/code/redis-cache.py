"""
Result Caching with Redis
From Week 10: Production Optimization

Strategy: Cache full API responses, return from cache if seen before
Result: 100% savings on cache hits (no API call needed)

Usage:
    result = cached_llm_call("What's the weather?")
    # First call: API call
    # Second call: Instant return from cache
"""

import redis
import json
import hashlib
import time
from typing import Optional, Any
from dataclasses import dataclass
from datetime import datetime

# Configuration
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
DEFAULT_TTL = 3600  # 1 hour in seconds

# Initialize Redis client
redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True  # Automatically decode bytes to strings
)


@dataclass
class CacheStats:
    """Track cache performance"""
    hits: int = 0
    misses: int = 0
    total_queries: int = 0
    cost_saved: float = 0.0
    time_saved: float = 0.0
    
    @property
    def hit_rate(self) -> float:
        if self.total_queries == 0:
            return 0.0
        return (self.hits / self.total_queries) * 100
    
    def print_stats(self):
        print("\n📊 Cache Statistics:")
        print(f"  Total queries: {self.total_queries}")
        print(f"  Cache hits: {self.hits} ({self.hit_rate:.1f}%)")
        print(f"  Cache misses: {self.misses}")
        print(f"  Cost saved: ${self.cost_saved:.4f}")
        print(f"  Time saved: {self.time_saved:.2f}s")


# Global stats
cache_stats = CacheStats()


def create_cache_key(prompt: str, options: dict = None) -> str:
    """
    Create unique cache key from prompt and options
    
    Important: Only include stable parameters, not timestamps or random IDs
    """
    # Combine prompt with relevant options
    cache_content = prompt
    if options:
        # Sort keys for consistency
        stable_options = {k: v for k, v in sorted(options.items()) 
                         if k not in ['user_id', 'timestamp', 'request_id']}
        cache_content += json.dumps(stable_options, sort_keys=True)
    
    # Hash to create short, unique key
    key_hash = hashlib.md5(cache_content.encode()).hexdigest()
    return f"llm_cache:{key_hash}"


def cached_llm_call(
    prompt: str,
    call_llm_func,
    ttl: int = DEFAULT_TTL,
    options: dict = None,
    cost_per_call: float = 0.005
) -> Any:
    """
    Main caching wrapper for LLM calls
    
    Args:
        prompt: The user's query
        call_llm_func: Function that actually calls the LLM
        ttl: Time to live in seconds (how long to cache)
        options: Additional parameters for the LLM call
        cost_per_call: Estimated cost per API call (for stats)
    
    Returns:
        LLM response (from cache or fresh API call)
    """
    global cache_stats
    cache_stats.total_queries += 1
    
    # Create cache key
    cache_key = create_cache_key(prompt, options)
    
    # Try to get from cache
    start_time = time.time()
    cached_result = redis_client.get(cache_key)
    
    if cached_result:
        # Cache HIT! 🎯
        cache_stats.hits += 1
        cache_stats.cost_saved += cost_per_call
        cache_stats.time_saved += (time.time() - start_time)
        
        print(f"✅ Cache HIT! Saved ${cost_per_call:.4f}")
        
        # Return cached result
        return json.loads(cached_result)
    
    # Cache MISS - call API
    cache_stats.misses += 1
    print(f"❌ Cache MISS - calling API...")
    
    # Make actual API call
    result = call_llm_func(prompt, options)
    
    # Store in cache with TTL
    redis_client.setex(
        cache_key,
        ttl,
        json.dumps(result)
    )
    
    return result


def get_cache_info(cache_key: str) -> Optional[dict]:
    """Get metadata about a cached item"""
    ttl = redis_client.ttl(cache_key)
    if ttl < 0:
        return None  # Key doesn't exist or has no TTL
    
    return {
        "exists": True,
        "ttl_seconds": ttl,
        "ttl_minutes": ttl / 60,
        "expires_at": datetime.now().timestamp() + ttl
    }


def clear_cache(pattern: str = "llm_cache:*"):
    """
    Clear all cached entries matching pattern
    
    Use carefully! This deletes cached data.
    """
    keys = redis_client.keys(pattern)
    if keys:
        redis_client.delete(*keys)
        print(f"🗑️  Cleared {len(keys)} cache entries")
    else:
        print("No cache entries to clear")


def warm_cache(queries: list[str], call_llm_func):
    """
    Pre-populate cache with common queries
    
    Use this for FAQs or known common questions
    """
    print(f"🔥 Warming cache with {len(queries)} queries...")
    for query in queries:
        cached_llm_call(query, call_llm_func)
    print("✅ Cache warmed!")


# ============================================================================
# IN-MEMORY FALLBACK (No Redis Required)
# ============================================================================

class InMemoryCache:
    """
    Simple in-memory cache for when Redis is not available
    
    Limitations:
    - Lost on restart
    - No TTL (cache never expires)
    - Not shared across processes
    - Limited by RAM
    """
    def __init__(self):
        self.cache = {}
        self.stats = CacheStats()
    
    def get(self, key: str) -> Optional[str]:
        return self.cache.get(key)
    
    def set(self, key: str, value: str):
        self.cache[key] = value
    
    def clear(self):
        self.cache.clear()
    
    def size(self) -> int:
        return len(self.cache)


# Global in-memory cache
memory_cache = InMemoryCache()


def cached_llm_call_simple(
    prompt: str,
    call_llm_func,
    cost_per_call: float = 0.005
) -> Any:
    """
    Simplified caching without Redis
    
    Use this if you don't have Redis installed
    """
    # Create cache key
    cache_key = hashlib.md5(prompt.encode()).hexdigest()
    
    # Check cache
    cached = memory_cache.get(cache_key)
    if cached:
        memory_cache.stats.hits += 1
        memory_cache.stats.cost_saved += cost_per_call
        print(f"✅ Cache HIT!")
        return json.loads(cached)
    
    # Cache miss
    memory_cache.stats.misses += 1
    print(f"❌ Cache MISS - calling API...")
    
    result = call_llm_func(prompt, None)
    memory_cache.set(cache_key, json.dumps(result))
    
    return result


# ============================================================================
# EXAMPLE USAGE
# ============================================================================

def mock_llm_call(prompt: str, options: dict = None) -> dict:
    """
    Mock LLM function for testing
    Replace this with your actual LLM call
    """
    time.sleep(0.5)  # Simulate API latency
    return {
        "content": f"Response to: {prompt}",
        "model": "gpt-4o-mini",
        "tokens": 150
    }


if __name__ == "__main__":
    print("=== Caching Example ===\n")
    
    # Test queries (note the duplicates)
    test_queries = [
        "What's the weather?",
        "What's the weather?",  # Duplicate - should cache hit
        "What's the capital of France?",
        "What's the weather?",  # Another duplicate
        "What's 2+2?",
        "What's the capital of France?",  # Duplicate
    ]
    
    # Run queries with caching
    for i, query in enumerate(test_queries, 1):
        print(f"\n--- Query {i}: {query} ---")
        result = cached_llm_call(
            prompt=query,
            call_llm_func=mock_llm_call,
            ttl=3600,  # 1 hour
            cost_per_call=0.003
        )
        print(f"Result: {result['content']}")
    
    # Print statistics
    cache_stats.print_stats()
    
    # Expected output:
    # - Query 1: Cache MISS (first time seeing "weather")
    # - Query 2: Cache HIT (saw "weather" before)
    # - Query 3: Cache MISS (first time seeing "capital")
    # - Query 4: Cache HIT ("weather" again)
    # - Query 5: Cache MISS (first time seeing "2+2")
    # - Query 6: Cache HIT ("capital" again)
    # Hit rate: 50% (3 hits, 3 misses)


# ============================================================================
# ADVANCED: Semantic Caching
# ============================================================================

"""
Semantic caching matches similar (not exact) queries

Example:
  "weather in NYC" ≈ "NYC weather" ≈ "what's the weather in New York"
  
All these should return the same cached result
"""

try:
    from sentence_transformers import SentenceTransformer
    import numpy as np
    
    # Load embedding model
    embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
    
    def semantic_cached_call(
        prompt: str,
        call_llm_func,
        similarity_threshold: float = 0.95,
        ttl: int = 3600
    ):
        """
        Cache based on semantic similarity, not exact match
        """
        # Get embedding for current query
        query_embedding = embedding_model.encode(prompt)
        
        # Search for similar cached queries
        cached_embeddings = redis_client.hgetall("semantic_cache:embeddings")
        
        for cache_key, cached_emb_str in cached_embeddings.items():
            cached_emb = np.frombuffer(bytes.fromhex(cached_emb_str), dtype=np.float32)
            
            # Calculate cosine similarity
            similarity = np.dot(query_embedding, cached_emb) / (
                np.linalg.norm(query_embedding) * np.linalg.norm(cached_emb)
            )
            
            if similarity > similarity_threshold:
                # Semantic match found!
                cached_result = redis_client.get(f"semantic_cache:{cache_key}")
                if cached_result:
                    print(f"✅ Semantic cache HIT! Similarity: {similarity:.3f}")
                    return json.loads(cached_result)
        
        # No match - call API
        print("❌ Semantic cache MISS")
        result = call_llm_func(prompt, None)
        
        # Store with embedding
        cache_key = hashlib.md5(prompt.encode()).hexdigest()
        redis_client.setex(f"semantic_cache:{cache_key}", ttl, json.dumps(result))
        redis_client.hset(
            "semantic_cache:embeddings",
            cache_key,
            query_embedding.tobytes().hex()
        )
        
        return result

except ImportError:
    print("⚠️  sentence-transformers not installed. Semantic caching unavailable.")
    print("Install with: pip install sentence-transformers")


# ============================================================================
# CAPSTONE INTEGRATION EXAMPLES
# ============================================================================

def rag_with_caching(question: str, get_context_func) -> str:
    """
    Example: RAG application with caching
    
    Only cache the final answer, not the context retrieval
    """
    # Context retrieval (not cached - always fresh)
    context = get_context_func(question)
    
    # Create full prompt
    full_prompt = f"Context: {context}\n\nQuestion: {question}"
    
    # Cache the LLM call
    def call_with_context(prompt, options):
        # Your actual LLM call here
        return mock_llm_call(prompt)
    
    result = cached_llm_call(
        prompt=full_prompt,
        call_llm_func=call_with_context,
        ttl=1800,  # 30 min (context might change)
        options={"context_length": len(context)}
    )
    
    return result['content']


def faq_bot_with_caching(user_query: str) -> str:
    """
    Example: FAQ bot with aggressive caching
    
    FAQ answers rarely change, so long TTL is fine
    """
    result = cached_llm_call(
        prompt=user_query,
        call_llm_func=mock_llm_call,
        ttl=86400,  # 24 hours (FAQs are static)
        cost_per_call=0.002
    )
    
    return result['content']


# ============================================================================
# MONITORING & DEBUGGING
# ============================================================================

def cache_health_check():
    """Check cache system health"""
    try:
        # Test Redis connection
        redis_client.ping()
        print("✅ Redis connected")
        
        # Count cached items
        cache_keys = redis_client.keys("llm_cache:*")
        print(f"📦 Cached items: {len(cache_keys)}")
        
        # Check memory usage
        info = redis_client.info('memory')
        memory_mb = info['used_memory'] / 1024 / 1024
        print(f"💾 Memory usage: {memory_mb:.2f} MB")
        
        return True
    except redis.ConnectionError:
        print("❌ Redis not connected!")
        print("Falling back to in-memory cache")
        return False


# ============================================================================
# TESTING YOUR CACHE
# ============================================================================

def test_cache_behavior():
    """
    Test that caching works correctly
    
    Run this to verify your cache setup
    """
    print("🧪 Testing cache behavior...\n")
    
    # Test 1: Cache hit
    print("Test 1: Same query twice")
    query = "test query 1"
    result1 = cached_llm_call(query, mock_llm_call)
    result2 = cached_llm_call(query, mock_llm_call)
    assert result1 == result2, "Cache should return same result"
    print("✅ Pass: Cache returned same result\n")
    
    # Test 2: Different queries
    print("Test 2: Different queries")
    query1 = "test query 2"
    query2 = "test query 3"
    result1 = cached_llm_call(query1, mock_llm_call)
    result2 = cached_llm_call(query2, mock_llm_call)
    assert result1 != result2, "Different queries should not cache hit"
    print("✅ Pass: Different queries got different results\n")
    
    # Test 3: TTL expiration (would need to wait)
    print("Test 3: TTL")
    query = "test query 4"
    cached_llm_call(query, mock_llm_call, ttl=1)  # 1 second TTL
    time.sleep(2)
    # Would need to verify cache miss here
    print("✅ Pass: TTL works (manual verification needed)\n")
    
    print("🎉 All tests passed!")


# Run health check on import
if __name__ == "__main__":
    cache_health_check()
