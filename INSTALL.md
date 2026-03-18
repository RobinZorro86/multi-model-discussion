# Installation Guide

**Version**: 0.5.0  
**Last Updated**: 2026-03-18

---

## Prerequisites

Before installing, ensure you have:

- [ ] OpenClaw >= 2026.3.2 installed
- [ ] Git configured with GitHub access
- [ ] Python >= 3.9
- [ ] At least one AI model provider configured (bailian or openai-codex)

---

## Method 1: Direct Clone (Recommended)

### Step 1: Clone Repository

```bash
cd ~/.openclaw/skills
git clone https://github.com/robinzorro/multi-model-discussion.git
```

### Step 2: Verify Installation

```bash
cd multi-model-discussion
ls -la
```

You should see:
```
SKILL.md
README.md
INSTALL.md
USER_GUIDE.md
scripts/
references/
```

### Step 3: Test Basic Functionality

```bash
# Test preset listing
python3 scripts/enhanced_cli.py --list-presets
```

Expected output:
```
📋 Available Presets:
  quick      - qwen3.5-plus, gpt-5.4 | consensus | 1轮
  deep       - qwen3.5-plus, kimi-k2.5, glm-5, MiniMax-M2.5, gpt-5.4 | comprehensive | 2轮
  ...
```

---

## Method 2: Manual Download

### Step 1: Download Release

```bash
cd ~/.openclaw/skills
wget https://github.com/robinzorro/multi-model-discussion/archive/refs/tags/v0.5.0.tar.gz
tar -xzf v0.5.0.tar.gz
mv multi-model-discussion-0.5.0 multi-model-discussion
rm v0.5.0.tar.gz
```

### Step 2: Continue from Step 2 above

---

## Method 3: For Agent Installation

If you're an OpenClaw agent installing this skill:

```python
# Use exec to clone
exec("cd ~/.openclaw/skills && git clone https://github.com/robinzorro/multi-model-discussion.git")

# Verify
exec("ls ~/.openclaw/skills/multi-model-discussion/SKILL.md")

# Test
exec("python3 ~/.openclaw/skills/multi-model-discussion/scripts/enhanced_cli.py --list-presets")
```

---

## Post-Installation Setup

### 1. Create Required Directories

```bash
# The skill will auto-create these, but you can pre-create:
mkdir -p ~/.openclaw/skills/multi-model-discussion/cache
mkdir -p ~/.openclaw/workspace/memory/multi-model-discussions
```

### 2. Configure Default Settings (Optional)

```python
# Create initial config
python3 << 'EOF'
import json
from pathlib import Path

config = {
    "models": ["bailian/qwen3.5-plus", "bailian/kimi-k2.5", "openai-codex/gpt-5.4"],
    "summarizer": "openai-codex/gpt-5.4",
    "mode": "consensus",
    "rounds": 1,
    "cache_enabled": True,
    "cache_ttl_hours": 24
}

config_file = Path.home() / ".openclaw/skills/multi-model-discussion/config.json"
config_file.write_text(json.dumps(config, indent=2))
print("✅ Config created")
EOF
```

### 3. Test Full Workflow

```bash
# Test with a simple question
cd ~/.openclaw/skills/multi-model-discussion

# This will output the execution plan
python3 scripts/run_discussion.py "What is the capital of France?"
```

---

## Verification Checklist

After installation, verify:

- [ ] `SKILL.md` exists and is readable
- [ ] `scripts/run_discussion.py` exists
- [ ] `scripts/enhanced_cli.py` exists
- [ ] `python3 scripts/enhanced_cli.py --list-presets` works
- [ ] `python3 scripts/enhanced_cli.py --cleanup --dry-run` works

---

## Troubleshooting

### Issue: "Command not found: python3"

**Solution**: Use `python` instead, or install Python 3

```bash
# Check Python version
python --version

# Or use python3 explicitly
python3 scripts/enhanced_cli.py --list-presets
```

### Issue: "Permission denied"

**Solution**: Make scripts executable

```bash
chmod +x ~/.openclaw/skills/multi-model-discussion/scripts/*.py
```

### Issue: "Module not found"

**Solution**: Install required packages (if any)

```bash
# This skill uses only standard library, no extra packages needed
```

### Issue: "Git clone failed"

**Solution**: Check GitHub access

```bash
# Test GitHub access
gh auth status

# Or use HTTPS with token
# https://github.com/robinzorro/multi-model-discussion.git
```

---

## Update

To update to a newer version:

```bash
cd ~/.openclaw/skills/multi-model-discussion
git pull origin main

# Or re-clone
cd ~/.openclaw/skills
rm -rf multi-model-discussion
git clone https://github.com/robinzorro/multi-model-discussion.git
```

---

## Uninstall

To remove the skill:

```bash
rm -rf ~/.openclaw/skills/multi-model-discussion
```

This will remove:
- Skill files
- Configuration (config.json)
- Cache (cache/)
- History remains in `~/.openclaw/workspace/memory/multi-model-discussions/`

---

## For Other Agents

If you're installing this skill as an OpenClaw agent:

```markdown
## Quick Install for Agents

1. Clone: `git clone https://github.com/robinzorro/multi-model-discussion.git ~/.openclaw/skills/`
2. Verify: `ls ~/.openclaw/skills/multi-model-discussion/SKILL.md`
3. Test: `python3 ~/.openclaw/skills/multi-model-discussion/scripts/enhanced_cli.py --list-presets`

Done! The skill is ready to use.
```

---

## Support

- **Issues**: https://github.com/robinzorro/multi-model-discussion/issues
- **Documentation**: See README.md and USER_GUIDE.md
- **Examples**: See references/examples.md

---

**Version**: 0.5.0  
**Status**: ✅ Ready for production use
