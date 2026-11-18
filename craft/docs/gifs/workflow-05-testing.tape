# VHS Tape for Testing Workflow
# Demonstrates /craft:test:run command

Output docs/gifs/workflow-05-testing.gif

Set Shell "bash"
Set FontSize 14
Set Width 1200
Set Height 600
Set TypingSpeed 50ms
Set Theme "Catppuccin Mocha"

Type "# Testing Workflow Demo"
Sleep 1s
Enter
Sleep 500ms

Type "# Scenario: Run tests with debug mode for detailed output"
Sleep 1s
Enter
Sleep 500ms

Type "/craft:test:run debug"
Sleep 500ms
Enter
Sleep 2s

Type ""
Sleep 500ms
Enter
Type "╭─ Test Runner (Debug Mode) ──────────────────────────╮"
Sleep 100ms
Enter
Type "│                                                      │"
Sleep 100ms
Enter
Type "│ 🔍 Detecting test framework...                      │"
Sleep 500ms
Enter
Type "│   ✓ Found: pytest (Python)                          │"
Sleep 100ms
Enter
Type "│                                                      │"
Sleep 500ms
Enter
Type "│ 🧪 Running tests...                                 │"
Sleep 500ms
Enter
Type "│                                                      │"
Sleep 100ms
Enter
Type "│   tests/test_auth.py::test_login ✓                  │"
Sleep 100ms
Enter
Type "│   tests/test_auth.py::test_logout ✓                 │"
Sleep 100ms
Enter
Type "│   tests/test_api.py::test_create_user ✓             │"
Sleep 100ms
Enter
Type "│   tests/test_api.py::test_get_user ✓                │"
Sleep 100ms
Enter
Type "│   tests/test_models.py::test_user_model ✓           │"
Sleep 100ms
Enter
Type "│   tests/test_models.py::test_validation ✗           │"
Sleep 100ms
Enter
Type "│                                                      │"
Sleep 500ms
Enter
Type "│ ❌ FAILED: tests/test_models.py::test_validation    │"
Sleep 100ms
Enter
Type "│                                                      │"
Sleep 100ms
Enter
Type "│   AssertionError: Expected 'Invalid email'          │"
Sleep 100ms
Enter
Type "│   Got: 'Email format is invalid'                    │"
Sleep 100ms
Enter
Type "│                                                      │"
Sleep 500ms
Enter
Type "│ 📊 Results:                                          │"
Sleep 100ms
Enter
Type "│   • 5 passed                                         │"
Sleep 100ms
Enter
Type "│   • 1 failed                                         │"
Sleep 100ms
Enter
Type "│   • Coverage: 87%                                    │"
Sleep 100ms
Enter
Type "│   • Duration: 2.4s                                   │"
Sleep 100ms
Enter
Type "│                                                      │"
Sleep 500ms
Enter
Type "│ 💡 Suggestions:                                      │"
Sleep 100ms
Enter
Type "│   • Update error message in test_validation         │"
Sleep 100ms
Enter
Type "│   • Add tests for edge cases                        │"
Sleep 100ms
Enter
Type "│   • Increase coverage to > 90%                      │"
Sleep 100ms
Enter
Type "╰──────────────────────────────────────────────────────╯"
Sleep 2s
Enter
Sleep 1s

Type "# Debug mode shows detailed output and suggestions!"
Sleep 2s
Enter
Sleep 2s
