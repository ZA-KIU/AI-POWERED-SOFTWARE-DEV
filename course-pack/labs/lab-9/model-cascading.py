"""
Model Cascading Pattern
From Week 10: Production Optimization

Strategy: Try cheap model first → If confidence low, escalate to expensive model
Result: 80% cost savings while maintaining quality

Usage:
    result = cascade_query("Explain quantum physics")
    # Tries Haiku first, escalates if needed
"""

import anthropic
import openai
from dataclasses import dataclass
from typing import Literal

# Configuration
ANTHROPIC_API_KEY = "your-key-here"
OPENAI_API_KEY = "your-key-here"

anthropic_client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
openai_client = openai.OpenAI(api_key=OPENAI_API_KEY)

@dataclass
class CascadeResult:
    """Result from cascaded query"""
    content: str
    model_used: str
    confidence: float
    cost: float
    attempts: int  # How many models tried


def call_haiku(query: str) -> CascadeResult:
    """Try cheapest model first"""
    response = anthropic_client.messages.create(
        model="claude-3-5-haiku-20241022",
        max_tokens=1024,
        messages=[{"role": "user", "content": query}]
    )
    
    # Calculate cost
    input_cost = (response.usage.input_tokens / 1_000_000) * 0.80
    output_cost = (response.usage.output_tokens / 1_000_000) * 4.00
    cost = input_cost + output_cost
    
    # Estimate confidence (you can add actual confidence scoring)
    confidence = estimate_confidence(response.content[0].text, query)
    
    return CascadeResult(
        content=response.content[0].text,
        model_used="haiku",
        confidence=confidence,
        cost=cost,
        attempts=1
    )


def call_mini(query: str) -> CascadeResult:
    """Try mid-tier model"""
    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": query}]
    )
    
    # Calculate cost
    input_cost = (response.usage.prompt_tokens / 1_000_000) * 0.15
    output_cost = (response.usage.completion_tokens / 1_000_000) * 0.60
    cost = input_cost + output_cost
    
    confidence = estimate_confidence(response.choices[0].message.content, query)
    
    return CascadeResult(
        content=response.choices[0].message.content,
        model_used="mini",
        confidence=confidence,
        cost=cost,
        attempts=2
    )


def call_gpt4o(query: str) -> CascadeResult:
    """Use frontier model as last resort"""
    response = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": query}]
    )
    
    # Calculate cost
    input_cost = (response.usage.prompt_tokens / 1_000_000) * 2.50
    output_cost = (response.usage.completion_tokens / 1_000_000) * 10.00
    cost = input_cost + output_cost
    
    confidence = 1.0  # Frontier model assumed high confidence
    
    return CascadeResult(
        content=response.choices[0].message.content,
        model_used="gpt-4o",
        confidence=confidence,
        cost=cost,
        attempts=3
    )


def estimate_confidence(response: str, query: str) -> float:
    """
    Estimate confidence in response quality
    
    Simple heuristics (you can make this smarter):
    - Long responses tend to be more detailed
    - Responses with hedging phrases have lower confidence
    - Short queries with short responses might be confident
    """
    # Check for hedging phrases
    hedging_phrases = [
        "i'm not sure", "might be", "possibly", "unclear",
        "i don't know", "hard to say", "depends"
    ]
    
    response_lower = response.lower()
    has_hedging = any(phrase in response_lower for phrase in hedging_phrases)
    
    # Simple scoring
    if has_hedging:
        return 0.6
    elif len(response) < 100:
        return 0.7
    elif len(response) > 300:
        return 0.9
    else:
        return 0.8


def cascade_query(query: str, thresholds: dict = None) -> CascadeResult:
    """
    Cascade through models until confidence threshold met
    
    Args:
        query: User query
        thresholds: {"haiku": 0.8, "mini": 0.9} - confidence thresholds
    
    Returns:
        CascadeResult with final answer
    """
    if thresholds is None:
        thresholds = {
            "haiku": 0.8,  # If Haiku confidence > 0.8, use it
            "mini": 0.9    # If Mini confidence > 0.9, use it
        }
    
    # Try Haiku first ($0.001 per query avg)
    print("🔹 Trying Haiku...")
    result = call_haiku(query)
    
    if result.confidence >= thresholds["haiku"]:
        print(f"✅ Haiku succeeded! Confidence: {result.confidence:.2f}")
        return result
    
    print(f"⚠️  Haiku confidence low ({result.confidence:.2f}), trying Mini...")
    
    # Try Mini ($0.003 per query avg)
    result = call_mini(query)
    result.cost += 0.001  # Add Haiku cost
    
    if result.confidence >= thresholds["mini"]:
        print(f"✅ Mini succeeded! Confidence: {result.confidence:.2f}")
        return result
    
    print(f"⚠️  Mini confidence low ({result.confidence:.2f}), using GPT-4o...")
    
    # Use GPT-4o as final arbiter ($0.010 per query)
    result = call_gpt4o(query)
    result.cost += 0.004  # Add Haiku + Mini costs
    
    print(f"✅ GPT-4o used. Total cost: ${result.cost:.4f}")
    return result


def batch_cascade(queries: list[str], thresholds: dict = None) -> list[CascadeResult]:
    """
    Process multiple queries with cascading
    
    Returns statistics on model usage
    """
    results = []
    model_counts = {"haiku": 0, "mini": 0, "gpt-4o": 0}
    total_cost = 0
    
    for query in queries:
        result = cascade_query(query, thresholds)
        results.append(result)
        model_counts[result.model_used] += 1
        total_cost += result.cost
    
    # Print statistics
    print("\n📊 Batch Statistics:")
    print(f"Total queries: {len(queries)}")
    print(f"Haiku: {model_counts['haiku']} ({model_counts['haiku']/len(queries)*100:.1f}%)")
    print(f"Mini: {model_counts['mini']} ({model_counts['mini']/len(queries)*100:.1f}%)")
    print(f"GPT-4o: {model_counts['gpt-4o']} ({model_counts['gpt-4o']/len(queries)*100:.1f}%)")
    print(f"Total cost: ${total_cost:.4f}")
    print(f"Avg cost/query: ${total_cost/len(queries):.4f}")
    
    # Calculate savings vs all GPT-4o
    baseline_cost = len(queries) * 0.010
    savings = (baseline_cost - total_cost) / baseline_cost * 100
    print(f"💰 Savings vs all GPT-4o: {savings:.1f}%")
    
    return results


# Example usage
if __name__ == "__main__":
    # Single query example
    print("=== Single Query Example ===")
    result = cascade_query("What is the capital of France?")
    print(f"\nAnswer: {result.content}")
    print(f"Model: {result.model_used}")
    print(f"Cost: ${result.cost:.4f}")
    print(f"Confidence: {result.confidence:.2f}")
    
    print("\n" + "="*50 + "\n")
    
    # Batch example
    print("=== Batch Example ===")
    test_queries = [
        "What is 2+2?",  # Simple - should use Haiku
        "Explain quantum entanglement in detail",  # Complex - should escalate
        "What's the weather like?",  # Ambiguous - might cascade
        "Write a legal contract for employment"  # Complex - should use GPT-4o
    ]
    
    results = batch_cascade(test_queries)


# ============================================================================
# ADAPT THIS FOR YOUR CAPSTONE
# ============================================================================

def capstone_cascade_example(user_query: str, context: str = None):
    """
    Example: Cascading for RAG-powered capstone
    
    Adapt this function for your specific use case
    """
    # Build full prompt with context
    if context:
        full_prompt = f"Context: {context}\n\nQuestion: {user_query}"
    else:
        full_prompt = user_query
    
    # Use cascading
    result = cascade_query(full_prompt)
    
    # Log for tracking
    print(f"Query processed with {result.model_used}")
    print(f"Cost: ${result.cost:.4f}")
    
    return result.content


# ============================================================================
# TUNING TIPS
# ============================================================================

"""
1. Adjust Confidence Thresholds:
   - Lower thresholds = More queries use cheap models (lower cost, possible quality drop)
   - Higher thresholds = More escalations (higher cost, better quality)
   
   Recommended starting points:
   - Haiku: 0.75-0.85
   - Mini: 0.85-0.95

2. Improve Confidence Estimation:
   - Use actual confidence scores if available
   - Train classifier on your data
   - Use embeddings + similarity to known good answers
   
3. Add Query Type Classification:
   - "Simple factual" → Always Haiku
   - "Complex reasoning" → Skip to GPT-4o
   - "Moderate" → Standard cascade

4. Monitor Model Distribution:
   - Target: 70%+ Haiku, 20% Mini, 10% GPT-4o
   - If different, adjust thresholds or classification

5. Measure Quality Impact:
   - Compare cascaded vs all-GPT-4o on test set
   - Acceptable quality drop: <5%
   - If quality drops more, raise thresholds
"""
