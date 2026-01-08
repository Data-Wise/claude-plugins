# VHS Tape for Site Creation Workflow
# Demonstrates /craft:site:create command

Output docs/gifs/workflow-02-site-creation.gif

Set Shell "bash"
Set FontSize 14
Set Width 1200
Set Height 600
Set TypingSpeed 50ms
Set Theme "Catppuccin Mocha"

Type "# Site Creation Workflow Demo"
Sleep 1s
Enter
Sleep 500ms

Type "# Scenario: Starting a new documentation site from scratch"
Sleep 1s
Enter
Sleep 500ms

Type "cd ~/projects/my-new-project"
Sleep 500ms
Enter
Sleep 1s

Type "# Create site with ADHD-friendly preset"
Sleep 500ms
Enter
Type "/craft:site:create --preset adhd-focus --quick"
Sleep 500ms
Enter
Sleep 2s

Type ""
Sleep 500ms
Enter
Type "┌─────────────────────────────────────────────────────────────┐"
Sleep 100ms
Enter
Type "│ ✅ DOCUMENTATION SITE CREATED                               │"
Sleep 100ms
Enter
Type "├─────────────────────────────────────────────────────────────┤"
Sleep 100ms
Enter
Type "│                                                             │"
Sleep 100ms
Enter
Type "│ Preset: adhd-focus                                          │"
Sleep 100ms
Enter
Type "│ Framework: MkDocs Material                                  │"
Sleep 100ms
Enter
Type "│                                                             │"
Sleep 100ms
Enter
Type "│ Created:                                                    │"
Sleep 100ms
Enter
Type "│   • mkdocs.yml (site configuration)                         │"
Sleep 100ms
Enter
Type "│   • docs/ (9 pages)                                         │"
Sleep 100ms
Enter
Type "│   • .github/workflows/docs.yml (deployment)                 │"
Sleep 100ms
Enter
Type "│   • .craft/site-design.yaml (design settings)               │"
Sleep 100ms
Enter
Type "│                                                             │"
Sleep 100ms
Enter
Type "│ Quick commands:                                             │"
Sleep 100ms
Enter
Type "│   Preview:  mkdocs serve                                    │"
Sleep 100ms
Enter
Type "│   Build:    mkdocs build                                    │"
Sleep 100ms
Enter
Type "│   Deploy:   mkdocs gh-deploy                                │"
Sleep 100ms
Enter
Type "│                                                             │"
Sleep 100ms
Enter
Type "│ 🎉 Site ready! Preview at http://127.0.0.1:8000            │"
Sleep 100ms
Enter
Type "└─────────────────────────────────────────────────────────────┘"
Sleep 2s
Enter
Sleep 1s

Type "# All site files created with ADHD-friendly calm green theme!"
Sleep 2s
Enter
Sleep 2s
