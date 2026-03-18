#!/usr/bin/env python3
"""Multi-Model Discussion - P1 Enhanced with Presets, Config, Cleanup, Cache"""

import json
import time
import hashlib
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional

SKILL_DIR = Path.home() / ".openclaw" / "skills" / "multi-model-discussion"
CONFIG_FILE = SKILL_DIR / "config.json"
CACHE_DIR = SKILL_DIR / "cache"
HISTORY_DIR = Path.home() / ".openclaw" / "workspace" / "memory" / "multi-model-discussions"

PRESETS = {
    "quick": {"models": ["bailian/qwen3.5-plus", "openai-codex/gpt-5.4"], "mode": "consensus", "rounds": 1},
    "deep": {"models": ["bailian/qwen3.5-plus", "bailian/kimi-k2.5", "bailian/glm-5", "openai-codex/gpt-5.4"], "mode": "comprehensive", "rounds": "adaptive", "adaptive_threshold": 0.8},
    "code": {"models": ["bailian/qwen3.5-plus", "openai-codex/gpt-5.4"], "mode": "comprehensive", "rounds": 1},
    "strategy": {"models": ["bailian/qwen3.5-plus", "bailian/kimi-k2.5", "openai-codex/gpt-5.4"], "mode": "divergent", "rounds": 1},
    "creative": {"models": ["bailian/kimi-k2.5", "bailian/glm-5", "bailian/MiniMax-M2.5"], "mode": "comprehensive", "rounds": 1}
}

def load_config():
    if CONFIG_FILE.exists():
        try:
            return json.loads(CONFIG_FILE.read_text())
        except:
            pass
    return {}

def save_config(config):
    SKILL_DIR.mkdir(parents=True, exist_ok=True)
    CONFIG_FILE.write_text(json.dumps(config, indent=2))

def list_presets():
    print("📋 Available Presets:")
    for name, preset in PRESETS.items():
        models = ", ".join([m.split('/')[-1] for m in preset["models"]])
        print(f"  {name:10} - {models} | {preset['mode']} | {preset['rounds']}轮")

def cleanup_history(keep_days=30, keep_count=50, dry_run=False):
    if not HISTORY_DIR.exists():
        print("📂 No history found")
        return
    
    files = list(HISTORY_DIR.glob("*.md"))
    files.sort(key=lambda f: f.stat().st_mtime)
    
    cutoff = time.time() - (keep_days * 86400)
    removed = []
    
    for f in files:
        if f.stat().st_mtime < cutoff:
            removed.append(f)
            if not dry_run:
                f.unlink()
    
    remaining = [f for f in files if f not in removed]
    remaining.sort(key=lambda f: f.stat().st_mtime, reverse=True)
    
    for f in remaining[keep_count:]:
        removed.append(f)
        if not dry_run:
            f.unlink()
    
    action = "Would remove" if dry_run else "Removed"
    print(f"🧹 {action} {len(removed)} files, kept {len(remaining) - len(removed) + len([f for f in remaining if f not in remaining[keep_count:]])}")

def get_cache_key(question, models, mode, rounds):
    """Generate cache key for exact match"""
    content = f"{question}|{','.join(sorted(models))}|{mode}|{rounds}"
    return hashlib.md5(content.encode()).hexdigest()

def get_semantic_cache_key(question):
    """Generate semantic cache key using simplified question"""
    # Remove punctuation, lowercase, extract keywords
    simplified = ''.join(c.lower() for c in question if c.isalnum() or c.isspace())
    # Extract first 10 words as key
    words = simplified.split()[:10]
    return hashlib.md5(' '.join(words).encode()).hexdigest()

def find_semantic_cache(question, ttl_hours=48):
    """Find semantically similar cached discussions"""
    if not CACHE_DIR.exists():
        return None
    
    semantic_key = get_semantic_cache_key(question)
    
    # Check all cache files for semantic similarity
    for cache_file in CACHE_DIR.glob("*.json"):
        try:
            data = json.loads(cache_file.read_text())
            if time.time() - data.get("timestamp", 0) > ttl_hours * 3600:
                continue
            
            # Check if semantic key matches
            if data.get("semantic_key") == semantic_key:
                return data.get("result")
        except:
            continue
    return None

def get_cache(cache_key, ttl_hours=24):
    if not CACHE_DIR.exists():
        return None
    cache_file = CACHE_DIR / f"{cache_key}.json"
    if cache_file.exists():
        try:
            data = json.loads(cache_file.read_text())
            if time.time() - data.get("timestamp", 0) < ttl_hours * 3600:
                return data.get("result")
        except:
            pass
    return None

def save_cache(cache_key, result, question=None):
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache_file = CACHE_DIR / f"{cache_key}.json"
    data = {
        "timestamp": time.time(),
        "result": result,
        "semantic_key": get_semantic_cache_key(question) if question else None
    }
    cache_file.write_text(json.dumps(data))

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--list-presets", action="store_true")
    parser.add_argument("--cleanup", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--keep-days", type=int, default=30)
    parser.add_argument("--keep-count", type=int, default=50)
    args = parser.parse_args()
    
    if args.list_presets:
        list_presets()
    elif args.cleanup:
        cleanup_history(args.keep_days, args.keep_count, args.dry_run)
    else:
        print("Use --list-presets or --cleanup")
