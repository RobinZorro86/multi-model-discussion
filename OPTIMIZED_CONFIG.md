# Multi-Model Discussion - Optimized Configuration

## Deep Mode (Optimized with GLM-5)

```json
{
  "deep_optimized": {
    "models": [
      "bailian/qwen3.5-plus",
      "bailian/kimi-k2.5",
      "bailian/glm-5",
      "openai-codex/gpt-5.4"
    ],
    "summarizer": "openai-codex/gpt-5.4",
    "mode": "adaptive",
    "rounds": "adaptive",
    "adaptive_threshold": 0.8,
    "timeout_per_model": {
      "bailian/qwen3.5-plus": 25,
      "bailian/kimi-k2.5": 35,
      "bailian/glm-5": 30,
      "openai-codex/gpt-5.4": 20
    },
    "total_timeout": 120,
    "progress_updates": true,
    "cache": {
      "enabled": true,
      "semantic": true,
      "partial": true,
      "ttl_hours": 48
    },
    "synthesis": {
      "tiered": true,
      "conflict_detection": true
    }
  }
}
```

## Key Optimizations

### 1. Model Configuration (v0.8.5)
- **Deep Mode**: 4 models (qwen3.5 + kimi + glm-5 + gpt5)
- **Other Modes**: 3 models (qwen3.5 + kimi + gpt5)
- **GLM-5 Added**: General purpose reasoning for deep analysis
- **Timeout**: glm-5 uses 30s timeout

### 2. Refined Timeout
| Model | Timeout | Reason |
|-------|---------|--------|
| qwen3.5-plus | 25s | Fast reasoning |
| kimi-k2.5 | 35s | Long context needs time |
| gpt-5.4 | 20s | Subscription, usually fast |

### 3. Adaptive Rounds
- **Consensus >= 0.8**: Skip round 2
- **Consensus < 0.8**: Proceed to round 2
- **Average rounds**: 1.3 (vs fixed 2)

### 4. Dynamic Mode Selection
| Question Pattern | Selected Mode |
|------------------|---------------|
| "验证/确认/对吗" | consensus |
| "创意/想法/方案" | divergent |
| "分析/研究/为什么" | comprehensive |
| "选择/哪个/推荐" | voting |

### 5. Enhanced Caching
- **Semantic cache**: Similar questions reuse results
- **Partial cache**: Failed models don't trigger full rerun
- **TTL**: 48 hours for facts, 24 hours for trends

### 6. Tiered Synthesis
1. Group synthesis (bailian models)
2. Conflict detection
3. Final synthesis with gpt-5.4

### 7. Semantic Caching
- Extracts first 10 keywords
- Matches similar questions
- Extends TTL to 48 hours

## Cost Comparison

| Configuration | Avg Tokens | Cost |
|--------------|------------|------|
| Original (5 models, 2 rounds) | ~15,000 | ¥0.60 |
| Optimized v0.8.0 (3 models, 1.3 rounds) | ~8,500 | ¥0.35 |
| Optimized v0.8.5 (4 models deep, 1.3 rounds) | ~10,200 | ¥0.42 |
| **Savings vs Original** | **~32%** | **~30%** |

## Usage

```bash
# Use optimized deep preset
python3 scripts/enhanced_cli.py --preset deep_optimized

# Or in conversation:
# "Use multi-model discussion with preset=deep_optimized"
```
