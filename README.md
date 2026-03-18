# Multi-Model Discussion Skill

[![Version](https://img.shields.io/badge/version-0.5.0-blue.svg)](https://github.com/robinzorro/multi-model-discussion/releases/tag/v0.5.0)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A powerful OpenClaw skill for orchestrating discussions among multiple AI models to get diverse perspectives and synthesized insights.

## Features

- **Parallel Execution**: Query multiple AI models simultaneously
- **Smart Synthesis**: 4 synthesis modes (consensus, divergent, comprehensive, voting)
- **Multi-Round Discussion**: Support 1-3 rounds of iterative refinement
- **Quick Presets**: 5 pre-configured presets for common use cases
- **Config Management**: Save and load user preferences
- **Cache Mechanism**: Avoid redundant discussions with smart caching
- **History Cleanup**: Automatic cleanup of old discussions
- **Timeout Control**: Per-model and total timeout management
- **Progress Feedback**: Real-time progress updates

## Supported Models

| Model | Provider | Timeout | Best For |
|-------|----------|---------|----------|
| qwen3.5-plus | bailian | 30s | Coding, reasoning |
| qwen3-max | bailian | 30s | Balanced tasks |
| kimi-k2.5 | bailian | 35s | Long context analysis |
| glm-5 | bailian | 30s | General purpose |
| MiniMax-M2.5 | bailian | 35s | Creative tasks |
| gpt-5.4 | openai-codex | 45s | Best synthesis quality |

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/robinzorro/multi-model-discussion.git

# Copy to OpenClaw skills directory
cp -r multi-model-discussion ~/.openclaw/skills/

# Or use clawhub (if available)
clawhub install multi-model-discussion
```

### Basic Usage

```bash
# List available presets
python3 ~/.openclaw/skills/multi-model-discussion/scripts/enhanced_cli.py --list-presets

# Use a preset for discussion
# (Integrate with your OpenClaw agent workflow)
```

### Using in OpenClaw

Simply mention the skill in your conversation:

```
User: Use multi-model discussion to analyze this strategy
Agent: [Automatically triggers the skill with default config]

User: Discuss with preset=deep mode=divergent
Agent: [Uses deep preset with divergent mode]
```

## Presets

| Preset | Models | Mode | Rounds | Use Case |
|--------|--------|------|--------|----------|
| **quick** | 2 models | consensus | 1 | Fast decisions |
| **deep** | 5 models | comprehensive | 2 | Deep research |
| **code** | 2 models | comprehensive | 1 | Code review |
| **strategy** | 3 models | divergent | 1 | Strategy analysis |
| **creative** | 3 models | comprehensive | 1 | Creative writing |

## Configuration

### Default Configuration

```json
{
  "models": ["bailian/qwen3.5-plus", "bailian/kimi-k2.5", "openai-codex/gpt-5.4"],
  "summarizer": "openai-codex/gpt-5.4",
  "mode": "consensus",
  "rounds": 1,
  "timeout_per_model": 30,
  "total_timeout": 90,
  "cache_enabled": true,
  "cache_ttl_hours": 24
}
```

### Save Custom Configuration

```python
from enhanced_cli import save_config

config = {
    "models": ["bailian/qwen3.5-plus", "openai-codex/gpt-5.4"],
    "mode": "comprehensive",
    "rounds": 2
}
save_config(config)
```

## Synthesis Modes

- **consensus**: Extract common ground and agreed points
- **divergent**: Highlight differences and unique perspectives
- **comprehensive**: Include all perspectives with organization
- **voting**: Rank perspectives by frequency and quality

## File Structure

```
multi-model-discussion/
├── SKILL.md                    # Skill definition and documentation
├── README.md                   # This file
├── INSTALL.md                  # Installation guide
├── USER_GUIDE.md              # Detailed user guide
├── scripts/
│   ├── run_discussion.py      # Main execution script (P0)
│   └── enhanced_cli.py        # Enhanced CLI with P1 features
├── references/
│   └── examples.md            # Usage examples
├── config.json                # User configuration (generated)
└── cache/                     # Discussion cache (generated)
```

## Requirements

- OpenClaw >= 2026.3.2
- Python >= 3.9
- Configured AI models (bailian, openai-codex)

## Documentation

- [User Guide](USER_GUIDE.md) - Detailed usage instructions
- [Installation Guide](INSTALL.md) - Step-by-step installation
- [Examples](references/examples.md) - Usage examples

## Changelog

### v0.5.0 (2026-03-18)
- ✅ P0: Parallel execution, timeout control, multi-round, progress feedback
- ✅ P1: Quick presets, config management, history cleanup, cache mechanism
- 📝 Comprehensive documentation

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Author

**Robin** - [@robinzorro](https://github.com/robinzorro)

## Acknowledgments

- OpenClaw team for the amazing agent framework
- All AI model providers for their APIs
