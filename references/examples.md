# Multi-Model Discussion - Usage Examples

## Quick Start Examples

### Example 1: Simple Strategy Analysis

**Input:**
```
Analyze this trading strategy: "Buy when RSI < 30 and sell when RSI > 70"
```

**Configuration:**
```json
{
  "models": ["qwen3.5-plus", "kimi-k2.5", "gpt5"],
  "mode": "divergent",
  "summarizer": "gpt5"
}
```

**Expected Output Structure:**
```markdown
## Multi-Model Discussion Results

### Individual Perspectives

#### qwen3.5-plus
**Strengths:**
- Clear, rule-based approach
- Easy to implement
- Well-known indicator

**Concerns:**
- May generate false signals in trending markets
- Doesn't account for market context

#### kimi-k2.5
**Strengths:**
- Simple to understand
- Good for range-bound markets

**Concerns:**
- Lagging indicator
- Need to combine with other signals

#### gpt5
**Strengths:**
- Classic mean-reversion strategy
- Risk management is clear

**Concerns:**
- Oversold/overbought can persist
- Requires backtesting

### Synthesis (Divergent Mode)

#### Consensus
- All models agree RSI is a valid indicator
- All acknowledge need for additional filters

#### Divergent Views
- qwen3.5-plus: Emphasizes implementation simplicity
- kimi-k2.5: Focuses on market regime dependency
- gpt5: Stresses risk management importance

#### Recommendation
Combine RSI with trend confirmation (e.g., moving average) and implement proper position sizing.
```

---

### Example 2: Code Review

**Input:**
```python
def calculate_position_size(account_balance, risk_percent, stop_loss_pips, pip_value):
    risk_amount = account_balance * (risk_percent / 100)
    position_size = risk_amount / (stop_loss_pips * pip_value)
    return position_size
```

**Configuration:**
```json
{
  "models": ["qwen3.5-plus", "gpt5"],
  "mode": "comprehensive",
  "summarizer": "gpt5"
}
```

---

## Configuration Guide

### Model Selection by Use Case

| Use Case | Recommended Models | Rationale |
|----------|-------------------|-----------|
| **Code Review** | qwen3.5-plus, gpt5 | Strong coding capabilities |
| **Strategy Analysis** | qwen3.5-plus, kimi-k2.5, gpt5 | Balanced reasoning |
| **Creative Writing** | kimi-k2.5, glm-5, minimax | Diverse creative styles |
| **Research** | All 6 models | Maximum coverage |
| **Quick Decision** | qwen3.5-plus, gpt5 | Fast + thorough |

### Mode Selection Guide

| Goal | Recommended Mode | When to Use |
|------|-----------------|-------------|
| **Validate an idea** | consensus | Ensure approach is sound |
| **Explore options** | divergent | Brainstorm alternatives |
| **Deep research** | comprehensive | Thorough analysis |
| **Make a decision** | voting | Choose between options |

---

## Best Practices

1. **Be specific** in your question
2. **Start with 3 models** for cost-effectiveness
3. **Use gpt5 as summarizer** for best synthesis quality
4. **Save important discussions** for future reference
5. **Iterate** - refine question based on initial results
