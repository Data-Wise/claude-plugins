# VHS Tape for Release Workflow
# Demonstrates /craft:check --for release command

Output docs/gifs/workflow-03-release.gif

Set Shell "bash"
Set FontSize 14
Set Width 1200
Set Height 600
Set TypingSpeed 50ms
Set Theme "Catppuccin Mocha"

Type "# Release Workflow Demo"
Sleep 1s
Enter
Sleep 500ms

Type "# Scenario: Preparing for v1.0.0 release"
Sleep 1s
Enter
Sleep 500ms

Type "/craft:check --for release"
Sleep 500ms
Enter
Sleep 2s

Type ""
Sleep 500ms
Enter
Type "╭─ Pre-Release Checklist ─────────────────────────────╮"
Sleep 100ms
Enter
Type "│                                                      │"
Sleep 100ms
Enter
Type "│ CODE QUALITY                                         │"
Sleep 100ms
Enter
Type "│   ✓ All tests passing (127/127)                     │"
Sleep 100ms
Enter
Type "│   ✓ No linting errors                               │"
Sleep 100ms
Enter
Type "│   ✓ Type checks passed                              │"
Sleep 100ms
Enter
Type "│   ✓ Code coverage: 94% (> 90% required)             │"
Sleep 100ms
Enter
Type "│                                                      │"
Sleep 100ms
Enter
Type "│ DOCUMENTATION                                        │"
Sleep 100ms
Enter
Type "│   ✓ CHANGELOG.md updated                            │"
Sleep 100ms
Enter
Type "│   ✓ API docs regenerated                            │"
Sleep 100ms
Enter
Type "│   ✓ No broken links                                 │"
Sleep 100ms
Enter
Type "│   ✓ Version bumped: 0.9.0 → 1.0.0                   │"
Sleep 100ms
Enter
Type "│                                                      │"
Sleep 100ms
Enter
Type "│ GIT STATUS                                           │"
Sleep 100ms
Enter
Type "│   ✓ On main branch                                  │"
Sleep 100ms
Enter
Type "│   ✓ Clean working tree                              │"
Sleep 100ms
Enter
Type "│   ✓ Synced with origin                              │"
Sleep 100ms
Enter
Type "│                                                      │"
Sleep 100ms
Enter
Type "│ DEPENDENCIES                                         │"
Sleep 100ms
Enter
Type "│   ✓ No security vulnerabilities                     │"
Sleep 100ms
Enter
Type "│   ✓ All dependencies up to date                     │"
Sleep 100ms
Enter
Type "│                                                      │"
Sleep 100ms
Enter
Type "│ 🎉 Ready for release! Run: gh release create v1.0.0 │"
Sleep 100ms
Enter
Type "╰──────────────────────────────────────────────────────╯"
Sleep 2s
Enter
Sleep 1s

Type "# All checks passed - safe to release!"
Sleep 2s
Enter
Sleep 2s
