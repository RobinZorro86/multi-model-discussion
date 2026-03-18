---
name: multi-model-discussion
description: Multi-model discussion system that sends the same question to multiple AI models in parallel, collects their responses, and generates a synthesized summary. Use when the user wants to get diverse perspectives on a complex problem, compare different models' reasoning approaches, or leverage collective intelligence for better decision-making. Triggers on phrases like "multi-model discussion", "let multiple models discuss", "get opinions from different models", "compare model perspectives", "ensemble analysis".
---

# Multi-Model Discussion System

A skill for orchestrating discussions among multiple AI models to get diverse perspectives and synthesized insights.

## Overview

This skill enables parallel querying of multiple AI models with the same question, then synthesizes their responses into a comprehensive analysis highlighting agreements, disagreements, and unique insights.

## When to Use

- Complex problem analysis requiring diverse perspectives
- Strategy evaluation and validation
- Code review with multiple expert opinions
- Content creation with creative diversity
- Decision-making with comprehensive consideration
- Research and investigation tasks

## Supported Models

All models are pre-configured in the system:

| Model | Provider | Strengths | Timeout |
|-------|----------|-----------|---------|
| qwen3.5-plus | bailian | Strong reasoning, coding | 30s |
| qwen3-max | bailian | Balanced performance | 30s |
| kimi-k2.5 | bailian | Long context, analysis | 35s |
| glm-5 | bailian | General purpose | 30s |
| MiniMax-M2.5 | bailian | Creative tasks | 35s |
| gpt-5.4 | openai-codex | Best reasoning, synthesis | 45s |

## Configuration

Default configuration:
```json
{
  "models": ["qwen3.5-plus", "kimi-k2.5", "gpt5"],
  "summarizer": "gpt5",
  "mode": "consensus",
  "rounds": 1,
  "timeout_per_model": 30,
  "total_timeout": 90,
  "progress_updates": true
}
```

### Parameters

- `models`: Array of model identifiers to participate
- `summarizer`: Model used for final synthesis
- `mode`: Synthesis mode (consensus/divergent/comprehensive/voting)
- `rounds`: Number of discussion rounds (1-3)
- `timeout_per_model`: Timeout per model in seconds
- `total_timeout`: Total timeout for all models
- `progress_updates`: Whether to show progress updates

### Synthesis Modes

- **consensus**: Extract common ground and agreed points
- **divergent**: Highlight differences and unique perspectives
- **comprehensive**: Include all perspectives with organization
- **voting**: Rank perspectives by frequency/quality

## Usage

### Step 1: Parse Request
Extract the question and configuration from user input.

### Step 2: Validate Configuration
- Check all specified models are available
- Validate timeout settings
- Calculate estimated cost

### Step 3: Send Progress Update
```
🔄 Starting multi-model discussion...
Question: {question}
Models: {model_list}
Estimated time: {estimated_time}s
```

### Step 4: Parallel Model Queries
For each model in parallel (using sessions_spawn):

```python
# For each model, spawn a subagent with timeout
tasks = []
for model in config['models']:
    task = sessions_spawn(
        task=question,
        model=model,
        mode="run",
        runTimeoutSeconds=config['timeout_per_model']
    )
    tasks.append((model, task))
```

**Progress Update After Each Model:**
```
✅ Model 1/3: qwen3.5-plus completed (2.3s)
⏳ Model 2/3: kimi-k2.5 running...
⏳ Model 3/3: gpt5 pending...
```

### Step 5: Handle Timeouts and Failures
- If a model times out: Mark as failed, continue with others
- If minimum models (2) succeed: Proceed to synthesis
- If fewer than 2 succeed: Report failure

### Step 6: Multi-Round Discussion (if rounds > 1)
For each additional round:
1. Build context from previous round responses
2. Send contextualized question to all models
3. Collect new responses

### Step 7: Synthesize Results
Use the summarizer model with appropriate synthesis prompt.

### Step 8: Generate Output
Format results in structured markdown.

### Step 9: Save History
Save discussion to `~/.openclaw/workspace/memory/multi-model-discussions/`

## Output Format

```markdown
# Multi-Model Discussion Results

**Discussion Time**: {timestamp}
**Original Question**: {question}
**Execution Time**: {duration}s

## Configuration

| Parameter | Value |
|-----------|-------|
| Models | {list} |
| Summarizer | {summarizer} |
| Mode | {mode} |
| Rounds | {rounds} |

## Progress Log

- ✅ 13:15:01 - qwen3.5-plus completed (2.3s)
- ✅ 13:15:03 - kimi-k2.5 completed (3.1s)
- ✅ 13:15:08 - gpt5 completed (8.2s)
- ✅ 13:15:12 - Synthesis completed (3.5s)

## Individual Perspectives

### Model 1
{response}

### Model 2
{response}

### Model 3
{response}

## Synthesis ({mode} Mode)

{synthesis}

## Statistics

- Total Time: {duration}s
- Successful Models: {success}/{total}
- Failed Models: {failed}/{total}
- Total Tokens: ~{tokens}

---
*Saved to: {filepath}*
```

## Error Handling

### Model Timeout
```
⚠️ kimi-k2.5 timed out after 35s, skipping...
✅ Continuing with 2/3 models
```

### Model Failure
```
⚠️ glm-5 failed (API error), skipping...
✅ Continuing with available models
```

### Minimum Models Not Met
```
❌ Discussion failed: Only 1/3 models responded (minimum 2 required)
Available response: {single_response}
```

### Synthesis Failure
```
⚠️ Synthesis failed, returning individual responses:

## Raw Responses
{formatted_responses}
```

## Best Practices

1. **Model Selection**: Use 3-4 models for cost-effectiveness, 5-6 for thoroughness
2. **Summarizer Choice**: gpt5 recommended for best synthesis quality
3. **Timeout Settings**: 
   - Standard models: 30s
   - Complex reasoning (gpt5): 45s
   - Total: 90s max
4. **Mode Selection**:
   - Use `consensus` for validation tasks
   - Use `divergent` for creative exploration
   - Use `comprehensive` for research tasks
   - Use `voting` for decision-making
5. **Multi-Round**: Enable for complex topics needing refinement
6. **Cost Awareness**: Each discussion costs ~12k tokens

## Cost Estimation

Formula:
```
Input tokens: 500 × n_models
Output tokens: 1000 × n_models  
Synthesis: 2000 + 1000
Total: ~500 + 1000×n + 3000 tokens

Example (3 models):
- Input: 500 × 3 = 1,500
- Output: 1,000 × 3 = 3,000
- Synthesis: 3,000
- Total: ~7,500 tokens (~¥0.30)
```

## Scripts

### run_discussion.py
Main execution script providing:
- Configuration parsing
- Synthesis prompt generation
- Output formatting
- History saving

Usage:
```bash
python scripts/run_discussion.py "Your question here" \
  --models=qwen3.5-plus,kimi-k2.5,gpt5 \
  --mode=consensus \
  --rounds=1
```

## History

Discussions are saved to:
`~/.openclaw/workspace/memory/multi-model-discussions/`

Format: `discussion-{timestamp}-{safe-question}.md`

## Troubleshooting

### Issue: Models timeout frequently
**Solution**: Increase timeout_per_model to 45s for complex questions

### Issue: Synthesis quality poor
**Solution**: Use gpt5 as summarizer, or try comprehensive mode

### Issue: Cost too high
**Solution**: Reduce to 3 models, or use cheaper models

### Issue: Results inconsistent
**Solution**: Enable multi-round discussion (rounds=2)
