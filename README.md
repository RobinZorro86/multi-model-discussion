# Multi-Model Discussion Skill / 多模型讨论技能

[![Version](https://img.shields.io/badge/version-0.8.5-blue.svg)](https://github.com/robinzorro/multi-model-discussion/releases/tag/v0.8.5)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

**English** | [中文](#中文文档)

A powerful OpenClaw skill for orchestrating discussions among multiple AI models to get diverse perspectives and synthesized insights.

一个强大的 OpenClaw 技能，用于协调多个 AI 模型之间的讨论，以获取多样化的观点和综合的洞察。

---

## English Documentation

### Features

- **Parallel Execution**: Query multiple AI models simultaneously
- **Smart Synthesis**: 4 synthesis modes (consensus, divergent, comprehensive, voting)
- **Multi-Round Discussion**: Support 1-3 rounds of iterative refinement
- **Quick Presets**: 5 pre-configured presets for common use cases
- **Config Management**: Save and load user preferences
- **Cache Mechanism**: Avoid redundant discussions with smart caching
- **History Cleanup**: Automatic cleanup of old discussions
- **Timeout Control**: Per-model and total timeout management
- **Progress Feedback**: Real-time progress updates

### Supported Models

| Model | Provider | Timeout | Best For |
|-------|----------|---------|----------|
| qwen3.5-plus | bailian | 25s | Coding, reasoning |
| kimi-k2.5 | bailian | 35s | Long context analysis |
| glm-5 | bailian | 30s | General purpose |
| gpt-5.4 | openai-codex | 20s | Best synthesis quality |

### Quick Start

#### Installation

```bash
# Clone the repository
git clone https://github.com/robinzorro/multi-model-discussion.git

# Copy to OpenClaw skills directory
cp -r multi-model-discussion ~/.openclaw/skills/
```

#### Basic Usage

```bash
# List available presets
python3 ~/.openclaw/skills/multi-model-discussion/scripts/enhanced_cli.py --list-presets

# Output:
# 📋 Available Presets:
#   quick      - qwen3.5-plus, gpt-5.4 | consensus | 1 轮
#   deep       - qwen3.5-plus, kimi-k2.5, glm-5, gpt-5.4 | comprehensive | adaptive
#   code       - qwen3.5-plus, gpt-5.4 | comprehensive | 1
#   strategy   - qwen3.5-plus, kimi-k2.5, gpt-5.4 | divergent | 1
#   creative   - kimi-k2.5, glm-5, MiniMax-M2.5 | comprehensive | 1
```

#### Using in OpenClaw

Simply mention the skill in your conversation:

```
User: Use multi-model discussion to analyze this strategy
Agent: [Automatically triggers the skill with default config]

User: Discuss with preset=deep mode=divergent
Agent: [Uses deep preset with divergent mode]
```

### Presets

| Preset | Models | Mode | Rounds | Use Case |
|--------|--------|------|--------|----------|
| **quick** | 2 models | consensus | 1 | Fast decisions |
| **deep** | 4 models | comprehensive | adaptive | Deep research |
| **code** | 2 models | comprehensive | 1 | Code review |
| **strategy** | 3 models | divergent | 1 | Strategy analysis |
| **creative** | 3 models | comprehensive | 1 | Creative writing |

**Note**: v0.8.5 adds GLM-5 to deep mode only (4 models). Other modes remain unchanged (3 models).

### Configuration

#### Default Configuration

```json
{
  "models": ["bailian/qwen3.5-plus", "bailian/kimi-k2.5", "openai-codex/gpt-5.4"],
  "summarizer": "openai-codex/gpt-5.4",
  "mode": "consensus",
  "rounds": 1,
  "timeout_per_model": {
    "qwen3.5-plus": 25,
    "kimi-k2.5": 35,
    "gpt5": 20
  },
  "total_timeout": 90,
  "cache_enabled": true,
  "cache_ttl_hours": 24
}
```

#### Deep Mode Configuration (v0.8.5)

```json
{
  "models": [
    "bailian/qwen3.5-plus",
    "bailian/kimi-k2.5",
    "bailian/glm-5",
    "openai-codex/gpt-5.4"
  ],
  "timeout_per_model": {
    "qwen3.5-plus": 25,
    "kimi-k2.5": 35,
    "glm-5": 30,
    "gpt5": 20
  },
  "total_timeout": 120
}
```

### Synthesis Modes

- **consensus**: Extract common ground and agreed points
- **divergent**: Highlight differences and unique perspectives
- **comprehensive**: Include all perspectives with organization
- **voting**: Rank perspectives by frequency and quality
- **adaptive**: Auto-select based on question type

---

## 中文文档

### 功能特性

- **并行执行**：同时查询多个 AI 模型
- **智能合成**：4 种合成模式（共识、发散、综合、投票）
- **多轮讨论**：支持 1-3 轮迭代优化
- **快速预设**：5 个预配置的常用场景预设
- **配置管理**：保存和加载用户偏好设置
- **缓存机制**：智能缓存避免重复讨论
- **历史清理**：自动清理旧讨论记录
- **超时控制**：单模型和总超时管理
- **进度反馈**：实时进度更新

### 支持的模型

| 模型 | 提供商 | 超时 | 最佳用途 |
|------|--------|------|----------|
| qwen3.5-plus | bailian | 25s | 编程、推理 |
| kimi-k2.5 | bailian | 35s | 长上下文分析 |
| glm-5 | bailian | 30s | 通用目的 |
| gpt-5.4 | openai-codex | 20s | 最佳合成质量 |

### 快速开始

#### 安装

```bash
# 克隆仓库
git clone https://github.com/robinzorro/multi-model-discussion.git

# 复制到 OpenClaw 技能目录
cp -r multi-model-discussion ~/.openclaw/skills/
```

#### 基本使用

```bash
# 列出可用预设
python3 ~/.openclaw/skills/multi-model-discussion/scripts/enhanced_cli.py --list-presets

# 输出：
# 📋 Available Presets:
#   quick      - qwen3.5-plus, gpt-5.4 | consensus | 1 轮
#   deep       - qwen3.5-plus, kimi-k2.5, glm-5, gpt-5.4 | comprehensive | adaptive
#   code       - qwen3.5-plus, gpt-5.4 | comprehensive | 1
#   strategy   - qwen3.5-plus, kimi-k2.5, gpt-5.4 | divergent | 1
#   creative   - kimi-k2.5, glm-5, MiniMax-M2.5 | comprehensive | 1
```

#### 在 OpenClaw 中使用

在对话中直接提及技能即可：

```
用户：使用多模型讨论分析这个策略
Agent：[自动触发技能并使用默认配置]

用户：使用 preset=deep mode=divergent 讨论
Agent：[使用 deep 预设和发散模式]
```

### 预设配置

| 预设 | 模型数 | 模式 | 轮数 | 用途 |
|------|--------|------|------|------|
| **quick** | 2 模型 | consensus | 1 | 快速决策 |
| **deep** | 4 模型 | comprehensive | adaptive | 深度研究 |
| **code** | 2 模型 | comprehensive | 1 | 代码审查 |
| **strategy** | 3 模型 | divergent | 1 | 策略分析 |
| **creative** | 3 模型 | comprehensive | 1 | 创意写作 |

**注意**：v0.8.5 仅在 deep 模式中添加了 GLM-5（4 模型）。其他模式保持不变（3 模型）。

### 配置说明

#### 默认配置

```json
{
  "models": ["bailian/qwen3.5-plus", "bailian/kimi-k2.5", "openai-codex/gpt-5.4"],
  "summarizer": "openai-codex/gpt-5.4",
  "mode": "consensus",
  "rounds": 1,
  "timeout_per_model": {
    "qwen3.5-plus": 25,
    "kimi-k2.5": 35,
    "gpt5": 20
  },
  "total_timeout": 90,
  "cache_enabled": true,
  "cache_ttl_hours": 24
}
```

#### Deep 模式配置（v0.8.5）

```json
{
  "models": [
    "bailian/qwen3.5-plus",
    "bailian/kimi-k2.5",
    "bailian/glm-5",
    "openai-codex/gpt-5.4"
  ],
  "timeout_per_model": {
    "qwen3.5-plus": 25,
    "kimi-k2.5": 35,
    "glm-5": 30,
    "gpt5": 20
  },
  "total_timeout": 120
}
```

### 合成模式

- **consensus（共识）**：提取共同点和一致意见
- **divergent（发散）**：突出差异和独特观点
- **comprehensive（综合）**：包含所有观点并整理
- **voting（投票）**：按频率和质量排序观点
- **adaptive（自适应）**：根据问题类型自动选择

---

## File Structure / 文件结构

```
multi-model-discussion/
├── SKILL.md                    # Skill definition / 技能定义
├── README.md                   # This file / 本文件
├── INSTALL.md                  # Installation guide / 安装指南
├── USER_GUIDE.md              # Detailed user guide / 详细用户指南
├── OPTIMIZED_CONFIG.md        # Optimized configuration / 优化配置
├── scripts/
│   ├── run_discussion.py      # Main execution script / 主执行脚本
│   └── enhanced_cli.py        # Enhanced CLI / 增强 CLI
├── references/
│   └── examples.md            # Usage examples / 使用示例
├── config.json                # User configuration / 用户配置
└── cache/                     # Discussion cache / 讨论缓存
```

## Requirements / 环境要求

- OpenClaw >= 2026.3.2
- Python >= 3.9
- Configured AI models (bailian, openai-codex) / 配置的 AI 模型

## Documentation / 文档

- [User Guide](USER_GUIDE.md) - Detailed usage instructions / 详细使用说明
- [Installation Guide](INSTALL.md) - Step-by-step installation / 分步安装指南
- [Optimized Config](OPTIMIZED_CONFIG.md) - Performance optimization / 性能优化
- [Examples](references/examples.md) - Usage examples / 使用示例

## Changelog / 更新日志

### v0.8.5 (2026-03-18)
- ✅ Added GLM-5 to deep mode only / 仅在 deep 模式中添加 GLM-5
- ✅ Deep mode: 4 models (others unchanged: 3 models)

### v0.8.0 (2026-03-18)
- ✅ Model simplification: 5→3 models
- ✅ Refined timeout per model
- ✅ Adaptive rounds and mode selection
- ✅ Enhanced caching (48h TTL)
- ✅ Cost reduction: ~42%

### v0.5.0 (2026-03-18)
- ✅ Initial release with P0 and P1 features

## License / 许可

MIT License - see [LICENSE](LICENSE) file for details.

## Author / 作者

**Robin** - [@robinzorro](https://github.com/robinzorro)

## Acknowledgments / 致谢

- OpenClaw team for the amazing agent framework
- All AI model providers for their APIs
