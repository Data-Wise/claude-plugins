# VHS Tape for Git Worktree Workflow
# Demonstrates /craft:git:worktree command

Output docs/gifs/workflow-07-git-worktree.gif

Set Shell "bash"
Set FontSize 14
Set Width 1200
Set Height 600
Set TypingSpeed 50ms
Set Theme "Catppuccin Mocha"

Type "# Git Worktree Workflow Demo"
Sleep 1s
Enter
Sleep 500ms

Type "# Scenario: Work on feature while keeping main branch available"
Sleep 1s
Enter
Sleep 500ms

Type "/craft:git:worktree add feature-auth"
Sleep 500ms
Enter
Sleep 2s

Type ""
Sleep 500ms
Enter
Type "╭─ Git Worktree Manager ──────────────────────────────╮"
Sleep 100ms
Enter
Type "│                                                      │"
Sleep 100ms
Enter
Type "│ 🌳 Creating worktree...                             │"
Sleep 500ms
Enter
Type "│                                                      │"
Sleep 100ms
Enter
Type "│   ✓ Branch: feature-auth                            │"
Sleep 100ms
Enter
Type "│   ✓ Location: ../my-project-feature-auth/           │"
Sleep 100ms
Enter
Type "│   ✓ Based on: main                                  │"
Sleep 100ms
Enter
Type "│                                                      │"
Sleep 500ms
Enter
Type "│ 📁 Directory structure:                             │"
Sleep 100ms
Enter
Type "│                                                      │"
Sleep 100ms
Enter
Type "│   my-project/            (main branch)              │"
Sleep 100ms
Enter
Type "│   my-project-feature-auth/  (feature branch)        │"
Sleep 100ms
Enter
Type "│                                                      │"
Sleep 500ms
Enter
Type "│ 🎯 Benefits:                                         │"
Sleep 100ms
Enter
Type "│   • Work on feature without switching branches      │"
Sleep 100ms
Enter
Type "│   • Keep main available for hotfixes                │"
Sleep 100ms
Enter
Type "│   • Run tests in parallel across worktrees          │"
Sleep 100ms
Enter
Type "│   • Compare implementations side-by-side            │"
Sleep 100ms
Enter
Type "│                                                      │"
Sleep 500ms
Enter
Type "│ 💡 Quick commands:                                   │"
Sleep 100ms
Enter
Type "│   • cd ../my-project-feature-auth                   │"
Sleep 100ms
Enter
Type "│   • /craft:git:worktree list                        │"
Sleep 100ms
Enter
Type "│   • /craft:git:worktree remove feature-auth         │"
Sleep 100ms
Enter
Type "│                                                      │"
Sleep 100ms
Enter
Type "│ ✅ Worktree created! Ready to work in parallel.     │"
Sleep 100ms
Enter
Type "╰──────────────────────────────────────────────────────╯"
Sleep 2s
Enter
Sleep 1s

Type "# Work on features in parallel without branch switching!"
Sleep 2s
Enter
Sleep 2s
