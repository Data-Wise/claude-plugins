# VHS Tape for Homebrew Distribution Workflow
# Demonstrates /craft:dist:homebrew setup command

Output docs/gifs/workflow-08-homebrew-dist.gif

Set Shell "bash"
Set FontSize 14
Set Width 1200
Set Height 600
Set TypingSpeed 50ms
Set Theme "Catppuccin Mocha"

Type "# Homebrew Distribution Workflow Demo"
Sleep 1s
Enter
Sleep 500ms

Type "# Scenario: Set up automated Homebrew formula releases"
Sleep 1s
Enter
Sleep 500ms

Type "/craft:dist:homebrew setup"
Sleep 500ms
Enter
Sleep 2s

Type ""
Sleep 500ms
Enter
Type "╔═══════════════════════════════════════════════════════════╗"
Sleep 100ms
Enter
Type "║       HOMEBREW AUTOMATION SETUP WIZARD                     ║"
Sleep 100ms
Enter
Type "╠═══════════════════════════════════════════════════════════╣"
Sleep 100ms
Enter
Type "║                                                           ║"
Sleep 500ms
Enter
Type "║  Step 1/5: Project Detection                              ║"
Sleep 100ms
Enter
Type "║  ✓ Detected: Python (pyproject.toml)                      ║"
Sleep 100ms
Enter
Type "║  ✓ Name: my-cli-tool | Version: 1.0.0                    ║"
Sleep 500ms
Enter
Type "║                                                           ║"
Sleep 100ms
Enter
Type "║  Step 2/5: Generating Formula                             ║"
Sleep 500ms
Enter
Type "║  ✓ Created: Formula/my-cli-tool.rb                       ║"
Sleep 100ms
Enter
Type "║  ✓ Language: Python::Virtualenv                          ║"
Sleep 100ms
Enter
Type "║  ✓ Dependencies: python@3.10                             ║"
Sleep 500ms
Enter
Type "║                                                           ║"
Sleep 100ms
Enter
Type "║  Step 3/5: Validating Formula                             ║"
Sleep 500ms
Enter
Type "║  ✓ Running: brew audit --strict Formula/my-cli-tool.rb  ║"
Sleep 100ms
Enter
Type "║  ✓ Validation passed                                     ║"
Sleep 500ms
Enter
Type "║                                                           ║"
Sleep 100ms
Enter
Type "║  Step 4/5: GitHub Actions Workflow                        ║"
Sleep 500ms
Enter
Type "║  ✓ Created: .github/workflows/homebrew-release.yml       ║"
Sleep 100ms
Enter
Type "║  ✓ Triggers: Release published, manual dispatch          ║"
Sleep 100ms
Enter
Type "║  ✓ Configured for: username/homebrew-tap                 ║"
Sleep 500ms
Enter
Type "║                                                           ║"
Sleep 100ms
Enter
Type "║  Step 5/5: GitHub Token Setup                             ║"
Sleep 500ms
Enter
Type "║  ⚠ HOMEBREW_TAP_GITHUB_TOKEN not found                   ║"
Sleep 100ms
Enter
Type "║                                                           ║"
Sleep 100ms
Enter
Type "║  To complete setup:                                       ║"
Sleep 100ms
Enter
Type "║  1. Create fine-grained token at github.com/settings     ║"
Sleep 100ms
Enter
Type "║  2. Grant: Contents (Read/Write) to homebrew-tap repo    ║"
Sleep 100ms
Enter
Type "║  3. Run: gh secret set HOMEBREW_TAP_GITHUB_TOKEN          ║"
Sleep 500ms
Enter
Type "║                                                           ║"
Sleep 100ms
Enter
Type "║  ✅ Setup complete! Formula ready for automated releases  ║"
Sleep 100ms
Enter
Type "╚═══════════════════════════════════════════════════════════╝"
Sleep 2s
Enter
Sleep 1s

Type "# Automated Homebrew releases set up in 5 steps!"
Sleep 2s
Enter
Sleep 2s
