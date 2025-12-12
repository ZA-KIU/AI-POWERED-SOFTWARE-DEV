#!/usr/bin/env python3
"""
Golden Set Evaluation Script Template

Usage:
    python evaluation-script-template.py --golden-set tests/golden_set.json --output tests/metrics_baseline.json

This script:
1. Loads your golden set
2. Runs each query through your system
3. Evaluates quality
4. Calculates aggregate metrics
5. Saves results

Adapt this template to your project's specific evaluation needs.
"""

import json
import time
import sys
from pathlib import Path
from typing import Dict, List, Any
import argparse

# TODO: Import your system's query function
# from your_project import query_system


def load_golden_set(filepath: str) -> List[Dict[str, Any]]:
    """Load golden set from JSON file"""
    with open(filepath, 'r') as f:
        data = json.load(f)
    return data['golden_set']


def evaluate_exact_match(response: str, expected: str) -> float:
    """
    Evaluate if response exactly matches expected output
    Returns 1.0 for match, 0.0 for no match
    """
    return 1.0 if response.strip().lower() == expected.strip().lower() else 0.0


def evaluate_keyword_presence(response: str, keywords: List[str], min_score: float = 0.7) -> float:
    """
    Evaluate if response contains required keywords
    Returns score based on % of keywords present
    """
    response_lower = response.lower()
    keywords_found = sum(1 for kw in keywords if kw.lower() in response_lower)
    score = keywords_found / len(keywords)
    return score


def evaluate_criteria_based(response: str, criteria: Dict[str, bool]) -> float:
    """
    Evaluate response against custom criteria
    This is a placeholder - implement your specific criteria checks
    
    Example criteria:
    {
        "covers_key_points": true,
        "includes_examples": true,
        "clear_structure": true
    }
    """
    # TODO: Implement your custom evaluation logic
    # For now, return a placeholder score
    return 0.75


def estimate_cost(query: str, response: str, model: str = "gpt-4") -> float:
    """
    Estimate API cost based on token counts
    
    Rough estimates (adjust for your model):
    - GPT-4: $0.03/1K input tokens, $0.06/1K output tokens
    - GPT-3.5: $0.0015/1K input tokens, $0.002/1K output tokens
    """
    # Rough token estimation: ~4 characters per token
    input_tokens = len(query) / 4
    output_tokens = len(response) / 4
    
    if model == "gpt-4":
        cost = (input_tokens / 1000 * 0.03) + (output_tokens / 1000 * 0.06)
    elif model == "gpt-3.5-turbo":
        cost = (input_tokens / 1000 * 0.0015) + (output_tokens / 1000 * 0.002)
    else:
        cost = 0.0  # Unknown model
    
    return cost


def run_evaluation(golden_set: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Run all test queries and collect results
    """
    results = []
    
    for i, test in enumerate(golden_set, 1):
        test_id = test['id']
        query = test['query']
        
        print(f"\n[{i}/{len(golden_set)}] Running test: {test_id}")
        print(f"Query: {query[:80]}{'...' if len(query) > 80 else ''}")
        
        try:
            # Measure latency
            start_time = time.time()
            
            # TODO: Replace with your actual system call
            # response = query_system(query)
            response = f"PLACEHOLDER RESPONSE for: {query}"
            
            latency = time.time() - start_time
            
            # Evaluate quality based on test case type
            if 'expected' in test:
                # Exact match evaluation
                quality = evaluate_exact_match(response, test['expected'])
            elif 'expected_keywords' in test:
                # Keyword presence evaluation
                quality = evaluate_keyword_presence(
                    response, 
                    test['expected_keywords'],
                    test.get('min_quality_score', 0.7)
                )
            elif 'evaluation_criteria' in test:
                # Criteria-based evaluation
                quality = evaluate_criteria_based(response, test['evaluation_criteria'])
            else:
                # No clear evaluation method, manual review needed
                quality = 0.5  # Placeholder
            
            # Estimate cost
            cost = estimate_cost(query, response)
            
            result = {
                'test_id': test_id,
                'query': query,
                'response': response[:200],  # Truncate for storage
                'quality_score': round(quality, 3),
                'passed': quality >= test.get('min_quality_score', 0.8),
                'latency_ms': round(latency * 1000, 1),
                'cost_usd': round(cost, 4),
                'category': test['category'],
                'difficulty': test['difficulty']
            }
            
            results.append(result)
            
            # Print result
            status = "✅ PASS" if result['passed'] else "❌ FAIL"
            print(f"  {status} | Quality: {quality:.1%} | Latency: {latency:.2f}s | Cost: ${cost:.4f}")
            
        except Exception as e:
            print(f"  ❌ ERROR: {str(e)}")
            results.append({
                'test_id': test_id,
                'query': query,
                'error': str(e),
                'passed': False,
                'category': test['category'],
                'difficulty': test['difficulty']
            })
    
    return results


def calculate_metrics(results: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Calculate aggregate metrics from results
    """
    successful_results = [r for r in results if 'error' not in r]
    
    if not successful_results:
        return {
            'error': 'No successful queries',
            'total_queries': len(results),
            'successful_queries': 0
        }
    
    # Overall metrics
    total_queries = len(results)
    successful_queries = len(successful_results)
    error_rate = (total_queries - successful_queries) / total_queries
    
    # Quality metrics
    passed_queries = sum(1 for r in successful_results if r['passed'])
    accuracy = passed_queries / total_queries if total_queries > 0 else 0
    
    avg_quality = sum(r['quality_score'] for r in successful_results) / len(successful_results)
    
    # Performance metrics
    avg_latency_ms = sum(r['latency_ms'] for r in successful_results) / len(successful_results)
    p50_latency = sorted([r['latency_ms'] for r in successful_results])[len(successful_results) // 2]
    p95_latency = sorted([r['latency_ms'] for r in successful_results])[int(len(successful_results) * 0.95)]
    
    # Cost metrics
    total_cost = sum(r['cost_usd'] for r in successful_results)
    avg_cost = total_cost / len(successful_results)
    
    # By difficulty
    by_difficulty = {}
    for difficulty in ['easy', 'medium', 'hard']:
        difficulty_results = [r for r in successful_results if r['difficulty'] == difficulty]
        if difficulty_results:
            by_difficulty[difficulty] = {
                'count': len(difficulty_results),
                'accuracy': sum(1 for r in difficulty_results if r['passed']) / len(difficulty_results),
                'avg_quality': sum(r['quality_score'] for r in difficulty_results) / len(difficulty_results)
            }
    
    # By category
    by_category = {}
    for result in successful_results:
        category = result['category']
        if category not in by_category:
            by_category[category] = {'count': 0, 'passed': 0}
        by_category[category]['count'] += 1
        if result['passed']:
            by_category[category]['passed'] += 1
    
    for category in by_category:
        by_category[category]['accuracy'] = by_category[category]['passed'] / by_category[category]['count']
    
    return {
        'total_queries': total_queries,
        'successful_queries': successful_queries,
        'error_rate': round(error_rate, 3),
        'accuracy': round(accuracy, 3),
        'avg_quality_score': round(avg_quality, 3),
        'avg_latency_ms': round(avg_latency_ms, 1),
        'p50_latency_ms': round(p50_latency, 1),
        'p95_latency_ms': round(p95_latency, 1),
        'total_cost_usd': round(total_cost, 4),
        'avg_cost_per_query_usd': round(avg_cost, 4),
        'by_difficulty': by_difficulty,
        'by_category': by_category
    }


def check_thresholds(metrics: Dict[str, Any], thresholds: Dict[str, float]) -> bool:
    """
    Check if metrics meet minimum thresholds
    Returns True if all thresholds met, False otherwise
    """
    failures = []
    
    # Check accuracy threshold
    if metrics['accuracy'] < thresholds.get('accuracy', 0.8):
        failures.append(f"Accuracy {metrics['accuracy']:.1%} < {thresholds['accuracy']:.1%}")
    
    # Check latency threshold
    if metrics['avg_latency_ms'] > thresholds.get('max_latency_ms', 3000):
        failures.append(f"Latency {metrics['avg_latency_ms']}ms > {thresholds['max_latency_ms']}ms")
    
    # Check cost threshold
    if metrics['avg_cost_per_query_usd'] > thresholds.get('max_cost_per_query', 0.25):
        failures.append(f"Cost ${metrics['avg_cost_per_query_usd']} > ${thresholds['max_cost_per_query']}")
    
    # Check error rate threshold
    if metrics['error_rate'] > thresholds.get('max_error_rate', 0.05):
        failures.append(f"Error rate {metrics['error_rate']:.1%} > {thresholds['max_error_rate']:.1%}")
    
    if failures:
        print("\n❌ THRESHOLD FAILURES:")
        for failure in failures:
            print(f"  - {failure}")
        return False
    else:
        print("\n✅ All thresholds met!")
        return True


def print_report(metrics: Dict[str, Any]):
    """
    Print a formatted metrics report
    """
    print("\n" + "=" * 60)
    print("EVALUATION REPORT")
    print("=" * 60)
    
    print(f"\nOverall Metrics:")
    print(f"  Total Queries: {metrics['total_queries']}")
    print(f"  Successful: {metrics['successful_queries']}")
    print(f"  Error Rate: {metrics['error_rate']:.1%}")
    print(f"  Accuracy: {metrics['accuracy']:.1%} ({int(metrics['accuracy'] * metrics['total_queries'])}/{metrics['total_queries']} passed)")
    print(f"  Avg Quality Score: {metrics['avg_quality_score']:.3f}")
    
    print(f"\nPerformance:")
    print(f"  Avg Latency: {metrics['avg_latency_ms']:.1f}ms")
    print(f"  P50 Latency: {metrics['p50_latency_ms']:.1f}ms")
    print(f"  P95 Latency: {metrics['p95_latency_ms']:.1f}ms")
    
    print(f"\nCost:")
    print(f"  Total: ${metrics['total_cost_usd']:.4f}")
    print(f"  Per Query: ${metrics['avg_cost_per_query_usd']:.4f}")
    
    if 'by_difficulty' in metrics and metrics['by_difficulty']:
        print(f"\nBy Difficulty:")
        for difficulty, stats in metrics['by_difficulty'].items():
            print(f"  {difficulty.capitalize()}: {stats['accuracy']:.1%} accuracy ({stats['count']} queries)")
    
    if 'by_category' in metrics and metrics['by_category']:
        print(f"\nBy Category:")
        for category, stats in metrics['by_category'].items():
            print(f"  {category}: {stats['accuracy']:.1%} accuracy ({stats['count']} queries)")
    
    print("\n" + "=" * 60)


def main():
    parser = argparse.ArgumentParser(description='Evaluate system on golden set')
    parser.add_argument('--golden-set', required=True, help='Path to golden set JSON file')
    parser.add_argument('--output', required=True, help='Path to save results JSON file')
    parser.add_argument('--check-thresholds', action='store_true', help='Check thresholds and exit with error if failed')
    
    args = parser.parse_args()
    
    # Load golden set
    print(f"Loading golden set from {args.golden_set}")
    golden_set = load_golden_set(args.golden_set)
    print(f"Loaded {len(golden_set)} test cases")
    
    # Run evaluation
    print("\nRunning evaluation...")
    results = run_evaluation(golden_set)
    
    # Calculate metrics
    print("\nCalculating metrics...")
    metrics = calculate_metrics(results)
    
    # Print report
    print_report(metrics)
    
    # Check thresholds (if requested)
    if args.check_thresholds:
        thresholds = {
            'accuracy': 0.80,
            'max_latency_ms': 3000,
            'max_cost_per_query': 0.25,
            'max_error_rate': 0.05
        }
        passed = check_thresholds(metrics, thresholds)
        
        if not passed:
            sys.exit(1)
    
    # Save results
    output = {
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
        'golden_set_path': args.golden_set,
        'metrics': metrics,
        'results': results
    }
    
    with open(args.output, 'w') as f:
        json.dump(output, f, indent=2)
    
    print(f"\nResults saved to {args.output}")


if __name__ == '__main__':
    main()
