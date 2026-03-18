#!/usr/bin/env python3
"""
Multi-Model Discussion System - P0 Fixed Version
Implements parallel execution, timeout control, multi-round discussion, and progress feedback
"""

import json
import asyncio
import argparse
import time
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
import re

# Default configuration
DEFAULT_CONFIG = {
    "models": ["bailian/qwen3.5-plus", "bailian/kimi-k2.5", "openai-codex/gpt-5.4"],
    "summarizer": "openai-codex/gpt-5.4",
    "mode": "consensus",
    "rounds": 1,
    "timeout_per_model": 30,
    "total_timeout": 90,
    "progress_updates": True,
    "min_successful_models": 2,
    "output_format": "markdown"
}

# Model aliases for convenience
MODEL_ALIASES = {
    "qwen3.5-plus": "bailian/qwen3.5-plus",
    "qwen3-max": "bailian/qwen3-max-2026-01-23",
    "kimi-k2.5": "bailian/kimi-k2.5",
    "glm-5": "bailian/glm-5",
    "minimax": "bailian/MiniMax-M2.5",
    "gpt5": "openai-codex/gpt-5.4",
    "gpt-5.4": "openai-codex/gpt-5.4"
}

# Model-specific timeouts (seconds)
MODEL_TIMEOUTS = {
    "bailian/qwen3.5-plus": 30,
    "bailian/qwen3-max-2026-01-23": 30,
    "bailian/kimi-k2.5": 35,
    "bailian/glm-5": 30,
    "bailian/MiniMax-M2.5": 35,
    "openai-codex/gpt-5.4": 45
}

def resolve_model(model: str) -> str:
    """Resolve model alias to full identifier"""
    return MODEL_ALIASES.get(model, model)

def get_model_timeout(model: str) -> int:
    """Get timeout for specific model"""
    return MODEL_TIMEOUTS.get(model, 30)

def safe_filename(question: str, timestamp: str) -> str:
    """Generate safe filename from question"""
    # Remove special characters, keep alphanumeric and spaces
    safe = re.sub(r'[^\w\s-]', '_', question[:50])
    # Replace spaces with underscores
    safe = re.sub(r'\s+', '_', safe)
    return f"discussion-{timestamp}-{safe}.md"

def main():
    parser = argparse.ArgumentParser(description='Multi-Model Discussion System - P0 Fixed')
    parser.add_argument('question', help='The question to discuss')
    parser.add_argument('--models', default=','.join(DEFAULT_CONFIG['models']),
                       help='Comma-separated list of models')
    parser.add_argument('--summarizer', default=DEFAULT_CONFIG['summarizer'],
                       help='Model to use for synthesis')
    parser.add_argument('--mode', default=DEFAULT_CONFIG['mode'],
                       choices=['consensus', 'divergent', 'comprehensive', 'voting'],
                       help='Synthesis mode')
    parser.add_argument('--rounds', type=int, default=1,
                       help='Number of discussion rounds (1-3)')
    parser.add_argument('--timeout', type=int, default=30,
                       help='Timeout per model in seconds')
    parser.add_argument('--total-timeout', type=int, default=90,
                       help='Total timeout in seconds')
    parser.add_argument('--min-models', type=int, default=2,
                       help='Minimum successful models required')
    parser.add_argument('--output', choices=['markdown', 'json'], default='markdown',
                       help='Output format')
    parser.add_argument('--no-progress', action='store_true',
                       help='Disable progress updates')
    
    args = parser.parse_args()
    
    # Resolve model names
    models = [resolve_model(m.strip()) for m in args.models.split(',')]
    summarizer = resolve_model(args.summarizer)
    
    # Build configuration
    config = {
        "models": models,
        "summarizer": summarizer,
        "mode": args.mode,
        "rounds": args.rounds,
        "timeout_per_model": args.timeout,
        "total_timeout": args.total_timeout,
        "min_successful_models": args.min_models,
        "progress_updates": not args.no_progress,
        "output_format": args.output
    }
    
    # Output configuration for agent to use
    output = {
        "status": "ready",
        "version": "2.0-p0-fixed",
        "config": config,
        "question": args.question,
        "features": {
            "parallel_execution": True,
            "timeout_control": True,
            "multi_round": args.rounds > 1,
            "progress_updates": not args.no_progress,
            "error_handling": "retry_and_skip",
            "min_models_check": True
        },
        "instructions": "Use sessions_spawn with timeout for each model. Implement progress updates. Handle timeouts and failures. Support multi-round discussion.",
        "execution_plan": [
            "1. Validate configuration and estimate cost",
            "2. Send initial progress update",
            "3. For each round:",
            "   a. Spawn subagents for all models in parallel with timeout",
            "   b. Collect responses with progress updates",
            "   c. Handle timeouts and failures",
            "4. Check minimum successful models",
            "5. Synthesize results using summarizer",
            "6. Generate output and save history"
        ]
    }
    
    print(json.dumps(output, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
