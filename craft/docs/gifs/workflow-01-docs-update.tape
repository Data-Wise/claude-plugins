# VHS Tape for Documentation Workflow
# Demonstrates /craft:docs:update command

Output docs/gifs/workflow-01-docs-update.gif

Set Shell "bash"
Set FontSize 14
Set Width 1200
Set Height 600
Set TypingSpeed 50ms
Set Theme "Catppuccin Mocha"

Type "# Documentation Workflow Demo"
Sleep 1s
Enter
Sleep 500ms

Type "# Scenario: You just updated some code, need to regenerate docs"
Sleep 1s
Enter
Sleep 500ms

Type "cd ~/projects/my-project"
Sleep 500ms
Enter
Sleep 1s

Type "# Run smart documentation update"
Sleep 500ms
Enter
Type "/craft:docs:update"
Sleep 500ms
Enter
Sleep 2s

Type ""
Sleep 500ms
Enter
Type "╭─ Documentation Update ──────────────────────────╮"
Sleep 100ms
Enter
Type "│ ✓ Detecting changes...                          │"
Sleep 100ms
Enter
Type "│   - Modified: src/api/routes.py                 │"
Sleep 100ms
Enter
Type "│   - Modified: src/cli/main.py                   │"
Sleep 100ms
Enter
Type "│                                                 │"
Sleep 100ms
Enter
Type "│ ✓ Generating documentation...                   │"
Sleep 100ms
Enter
Type "│   - Updated: docs/api/routes.md                 │"
Sleep 100ms
Enter
Type "│   - Updated: docs/cli/commands.md               │"
Sleep 100ms
Enter
Type "│   - Updated: REFCARD.md                         │"
Sleep 100ms
Enter
Type "│                                                 │"
Sleep 100ms
Enter
Type "│ ✓ Validating...                                 │"
Sleep 100ms
Enter
Type "│   - No broken links                             │"
Sleep 100ms
Enter
Type "│   - Navigation structure valid                  │"
Sleep 100ms
Enter
Type "│                                                 │"
Sleep 100ms
Enter
Type "│ 🎉 Documentation updated successfully!          │"
Sleep 100ms
Enter
Type "╰─────────────────────────────────────────────────╯"
Sleep 2s
Enter
Sleep 1s

Type "# All docs updated and validated in one command!"
Sleep 2s
Enter
Sleep 2s
