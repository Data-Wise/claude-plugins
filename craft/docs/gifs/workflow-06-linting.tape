# VHS Tape for Linting Workflow
# Demonstrates /craft:code:lint command

Output docs/gifs/workflow-06-linting.gif

Set Shell "bash"
Set FontSize 14
Set Width 1200
Set Height 600
Set TypingSpeed 50ms
Set Theme "Catppuccin Mocha"

Type "# Linting Workflow Demo"
Sleep 1s
Enter
Sleep 500ms

Type "# Scenario: Run linter with auto-fix in optimize mode"
Sleep 1s
Enter
Sleep 500ms

Type "/craft:code:lint optimize"
Sleep 500ms
Enter
Sleep 2s

Type ""
Sleep 500ms
Enter
Type "╭─ Code Linter (Optimize Mode) ───────────────────────╮"
Sleep 100ms
Enter
Type "│                                                      │"
Sleep 100ms
Enter
Type "│ 🔍 Detecting linters...                             │"
Sleep 500ms
Enter
Type "│   ✓ Found: eslint (JavaScript)                      │"
Sleep 100ms
Enter
Type "│   ✓ Found: ruff (Python)                            │"
Sleep 100ms
Enter
Type "│                                                      │"
Sleep 500ms
Enter
Type "│ 🚀 Running in parallel...                           │"
Sleep 500ms
Enter
Type "│                                                      │"
Sleep 100ms
Enter
Type "│   [eslint] Scanning 42 files...                     │"
Sleep 500ms
Enter
Type "│   [ruff] Scanning 28 files...                       │"
Sleep 500ms
Enter
Type "│                                                      │"
Sleep 500ms
Enter
Type "│ 📋 Issues found:                                     │"
Sleep 100ms
Enter
Type "│                                                      │"
Sleep 100ms
Enter
Type "│   src/api/routes.js:15                               │"
Sleep 100ms
Enter
Type "│   ⚠ Unused variable 'userId'                        │"
Sleep 100ms
Enter
Type "│   ✓ Auto-fixed: Removed unused variable             │"
Sleep 100ms
Enter
Type "│                                                      │"
Sleep 100ms
Enter
Type "│   src/utils/helpers.py:42                            │"
Sleep 100ms
Enter
Type "│   ⚠ Line too long (92 > 88 characters)              │"
Sleep 100ms
Enter
Type "│   ✓ Auto-fixed: Reformatted line                    │"
Sleep 100ms
Enter
Type "│                                                      │"
Sleep 100ms
Enter
Type "│   src/models/user.js:8                               │"
Sleep 100ms
Enter
Type "│   ⚠ Missing semicolon                                │"
Sleep 100ms
Enter
Type "│   ✓ Auto-fixed: Added semicolon                     │"
Sleep 100ms
Enter
Type "│                                                      │"
Sleep 500ms
Enter
Type "│ 📊 Summary:                                          │"
Sleep 100ms
Enter
Type "│   • 8 issues found                                   │"
Sleep 100ms
Enter
Type "│   • 8 auto-fixed                                     │"
Sleep 100ms
Enter
Type "│   • 0 manual fixes needed                            │"
Sleep 100ms
Enter
Type "│   • Duration: 1.2s (parallel)                        │"
Sleep 100ms
Enter
Type "│                                                      │"
Sleep 100ms
Enter
Type "│ ✅ All issues resolved!                              │"
Sleep 100ms
Enter
Type "╰──────────────────────────────────────────────────────╯"
Sleep 2s
Enter
Sleep 1s

Type "# Optimize mode runs linters in parallel with auto-fix!"
Sleep 2s
Enter
Sleep 2s
