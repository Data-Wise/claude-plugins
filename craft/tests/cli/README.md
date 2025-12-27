# CLI Tests for Craft Plugin

Bash-based test suites for validating the craft plugin structure and functionality.

## Test Suites

### Automated Tests (`automated-tests.sh`)

Non-interactive tests that validate plugin structure:

```bash
bash tests/cli/automated-tests.sh
```

**What it tests:**
- Plugin structure (plugin.json, directories)
- Command files exist and are valid
- Skill files exist and are valid
- Agent definitions
- Markdown syntax (code fence balance, frontmatter)

**Options:**
- `VERBOSE=1` - Show individual file checks

### Interactive Tests (`interactive-tests.sh`)

Manual testing with expected vs actual comparison:

```bash
bash tests/cli/interactive-tests.sh
```

**What it tests:**
- Plugin JSON content
- Directory structure
- Command/skill/agent counts
- Command content validation
- Markdown validation

**Keys:**
- `y` = pass
- `n` = fail
- `q` = quit

## Logs

Test logs are saved to `tests/cli/logs/`:
- `interactive-test-YYYYMMDD-HHMMSS.log`

## Running from Project Root

```bash
# From craft plugin directory
cd ~/projects/dev-tools/claude-plugins/craft
bash tests/cli/automated-tests.sh

# Verbose mode
VERBOSE=1 bash tests/cli/automated-tests.sh
```
