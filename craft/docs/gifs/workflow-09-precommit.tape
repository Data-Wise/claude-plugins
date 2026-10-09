# VHS Tape for Pre-commit Check Workflow
# Demonstrates /craft:check --for commit command

Output docs/gifs/workflow-09-precommit.gif

Set Shell "bash"
Set FontSize 14
Set Width 1200
Set Height 600
Set TypingSpeed 50ms
Set Theme "Catppuccin Mocha"

Type "# Pre-commit Check Workflow Demo"
Sleep 1s
Enter
Sleep 500ms

Type "# Scenario: Run checks before committing code"
Sleep 1s
Enter
Sleep 500ms

Type "/craft:check --for commit"
Sleep 500ms
Enter
Sleep 2s

Type ""
Sleep 500ms
Enter
Type "╭─ Pre-Commit Checks ─────────────────────────────────╮"
Sleep 100ms
Enter
Type "│                                                      │"
Sleep 100ms
Enter
Type "│ 🔍 LINTING                                           │"
Sleep 500ms
Enter
Type "│   ✓ ESLint: No issues (42 files)                    │"
Sleep 100ms
Enter
Type "│   ✓ Ruff: No issues (28 files)                      │"
Sleep 100ms
Enter
Type "│                                                      │"
Sleep 500ms
Enter
Type "│ 🎨 FORMATTING                                        │"
Sleep 500ms
Enter
Type "│   ✓ Prettier: All files formatted                   │"
Sleep 100ms
Enter
Type "│   ✓ Black: All files formatted                      │"
Sleep 100ms
Enter
Type "│                                                      │"
Sleep 500ms
Enter
Type "│ 🧪 TESTS                                             │"
Sleep 500ms
Enter
Type "│   ✓ Unit tests: 127/127 passed                      │"
Sleep 100ms
Enter
Type "│   ✓ Coverage: 94% (> 90% required)                  │"
Sleep 100ms
Enter
Type "│                                                      │"
Sleep 500ms
Enter
Type "│ 📝 DOCUMENTATION                                     │"
Sleep 500ms
Enter
Type "│   ✓ No broken links                                 │"
Sleep 100ms
Enter
Type "│   ✓ API docs up to date                             │"
Sleep 100ms
Enter
Type "│                                                      │"
Sleep 500ms
Enter
Type "│ 📊 CHANGED FILES                                     │"
Sleep 500ms
Enter
Type "│   • src/api/routes.js (+45, -12)                    │"
Sleep 100ms
Enter
Type "│   • src/utils/helpers.py (+23, -8)                  │"
Sleep 100ms
Enter
Type "│   • tests/test_api.py (+67, -4)                     │"
Sleep 100ms
Enter
Type "│                                                      │"
Sleep 500ms
Enter
Type "│ 💡 SUGGESTED COMMIT MESSAGE                          │"
Sleep 500ms
Enter
Type "│                                                      │"
Sleep 100ms
Enter
Type "│   feat(api): add user pagination support            │"
Sleep 100ms
Enter
Type "│                                                      │"
Sleep 100ms
Enter
Type "│   - Add limit/offset query parameters               │"
Sleep 100ms
Enter
Type "│   - Update helpers for pagination logic             │"
Sleep 100ms
Enter
Type "│   - Add comprehensive pagination tests              │"
Sleep 100ms
Enter
Type "│                                                      │"
Sleep 100ms
Enter
Type "│ ✅ All checks passed! Safe to commit.                │"
Sleep 100ms
Enter
Type "╰──────────────────────────────────────────────────────╯"
Sleep 2s
Enter
Sleep 1s

Type "# All pre-commit checks passed - ready to commit!"
Sleep 2s
Enter
Sleep 2s
