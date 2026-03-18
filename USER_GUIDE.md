# Multi-Model Discussion Skill - 使用指南

**版本**: P1 Enhanced  
**更新日期**: 2026-03-18  
**功能**: 快捷预设、配置保存、历史清理、缓存机制

---

## 一、快捷预设使用

### 查看所有预设
```bash
python3 ~/.openclaw/skills/multi-model-discussion/scripts/enhanced_cli.py --list-presets
```

**输出示例**:
```
📋 Available Presets:
  quick      - qwen3.5-plus, gpt-5.4 | consensus | 1轮
  deep       - qwen3.5-plus, kimi-k2.5, glm-5, MiniMax-M2.5, gpt-5.4 | comprehensive | 2轮
  code       - qwen3.5-plus, gpt-5.4 | comprehensive | 1轮
  strategy   - qwen3.5-plus, kimi-k2.5, gpt-5.4 | divergent | 1轮
  creative   - kimi-k2.5, glm-5, MiniMax-M2.5 | comprehensive | 1轮
```

### 预设说明

| 预设 | 场景 | 模型数 | 特点 |
|------|------|--------|------|
| **quick** | 快速决策 | 2 | 速度快，成本低 |
| **deep** | 深度研究 | 5 | 全面分析，2轮讨论 |
| **code** | 代码审查 | 2 | 编程专家模型 |
| **strategy** | 策略分析 | 3 | 多角度发散思维 |
| **creative** | 创意写作 | 3 | 创意型模型组合 |

### 使用预设进行讨论

在 SKILL.md 的执行流程中，使用 `--preset` 参数：

```python
# 示例：使用 strategy 预设分析交易策略
config = apply_preset("strategy")
# 结果：使用 qwen3.5 + kimi + gpt5，divergent 模式，1轮
```

---

## 二、配置保存/加载

### 保存当前配置
```python
from enhanced_cli import save_config

config = {
    "models": ["bailian/qwen3.5-plus", "openai-codex/gpt-5.4"],
    "mode": "consensus",
    "rounds": 1,
    "timeout_per_model": 30
}
save_config(config)
print("✅ 配置已保存")
```

### 加载已保存的配置
```python
from enhanced_cli import load_config

saved_config = load_config()
if saved_config:
    print(f"📂 已加载配置: {saved_config}")
else:
    print("📂 使用默认配置")
```

### 配置文件位置
```
~/.openclaw/skills/multi-model-discussion/config.json
```

---

## 三、历史清理

### 预览清理（dry-run）
```bash
python3 ~/.openclaw/skills/multi-model-discussion/scripts/enhanced_cli.py \
  --cleanup --dry-run --keep-days=30 --keep-count=50
```

**输出示例**:
```
🧹 Would remove 12 files older than 30 days
🧹 Would remove 8 excess files
🧹 Remaining: 50 files
```

### 执行清理
```bash
python3 ~/.openclaw/skills/multi-model-discussion/scripts/enhanced_cli.py \
  --cleanup --keep-days=30 --keep-count=50
```

**输出示例**:
```
🧹 Removed 12 files older than 30 days
🧹 Removed 8 excess files
🧹 Remaining: 50 files
```

### 清理参数
| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--keep-days` | 30 | 保留 N 天内的文件 |
| `--keep-count` | 50 | 保留 N 个最新文件 |
| `--dry-run` | - | 预览模式，不实际删除 |

---

## 四、缓存机制

### 缓存工作原理
1. 基于问题 + 模型 + 模式 + 轮数生成哈希
2. 检查结果是否在缓存中
3. 如果在且未过期（默认 24h），直接返回
4. 如果不在或已过期，执行讨论并缓存结果

### 使用缓存
```python
from enhanced_cli import get_cache_key, get_cache, save_cache

# 生成缓存键
cache_key = get_cache_key(
    question="分析这个策略",
    models=["bailian/qwen3.5-plus", "openai-codex/gpt-5.4"],
    mode="consensus",
    rounds=1
)

# 检查缓存
cached_result = get_cache(cache_key, ttl_hours=24)
if cached_result:
    print("📂 使用缓存结果")
    return cached_result

# 执行讨论
result = await run_discussion(...)

# 保存到缓存
save_cache(cache_key, result)
print("💾 结果已缓存")
```

### 缓存位置
```
~/.openclaw/skills/multi-model-discussion/cache/
└── {hash}.json
```

### 清除缓存
```bash
rm -rf ~/.openclaw/skills/multi-model-discussion/cache/
```

---

## 五、完整使用示例

### 场景 1: 快速分析（使用预设）
```python
# 1. 加载配置
config = load_config()

# 2. 应用 quick 预设
preset_config = apply_preset("quick")
config.update(preset_config)

# 3. 检查缓存
cache_key = get_cache_key(question, config['models'], config['mode'], config['rounds'])
if cached := get_cache(cache_key):
    return cached

# 4. 执行讨论
results = await run_discussion(question, config)

# 5. 缓存结果
save_cache(cache_key, results)

# 6. 保存配置（如果用户修改了）
save_config(config)
```

### 场景 2: 深度研究（自定义配置）
```python
# 自定义配置
config = {
    "models": ["bailian/qwen3.5-plus", "bailian/kimi-k2.5", "openai-codex/gpt-5.4"],
    "mode": "comprehensive",
    "rounds": 2,
    "timeout_per_model": 45
}

# 执行多轮讨论
for round in range(config['rounds']):
    if round > 0:
        question = build_context_prompt(question, previous_responses)
    responses = await query_parallel(question, config['models'])
```

### 场景 3: 定期维护
```bash
# 添加到 crontab，每周清理一次历史
0 0 * * 0 python3 ~/.openclaw/skills/multi-model-discussion/scripts/enhanced_cli.py --cleanup
```

---

## 六、最佳实践

### 1. 选择合适的预设
- **快速决策** → quick（2 模型，1 轮）
- **深度研究** → deep（5 模型，2 轮）
- **代码审查** → code（编程专家模型）
- **策略分析** → strategy（发散思维）
- **创意写作** → creative（创意型模型）

### 2. 利用缓存
- 相同问题重复使用缓存
- 调整 TTL 适应需求（--cache-ttl=48）

### 3. 定期清理
- 建议每周运行一次 cleanup
- 保留最近 30 天或 50 个讨论

### 4. 保存常用配置
- 修改默认配置后保存
- 下次自动加载

---

## 七、故障排除

### 问题: 预设不存在
**解决**: 使用 `--list-presets` 查看可用预设

### 问题: 缓存不生效
**解决**: 检查缓存目录权限，或手动清除缓存

### 问题: 历史清理失败
**解决**: 检查目录权限，确保有写入权限

---

**版本**: P1 Enhanced  
**最后更新**: 2026-03-18
