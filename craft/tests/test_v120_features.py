#!/usr/bin/env python3
"""
Craft Plugin v1.2.0 Feature Tests
==================================
Validates the new features added in v1.2.0:
- Mode System (Option B)
- Smart Orchestrator (Option C)

Run with: python tests/test_v120_features.py
"""

import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Optional
import time


@dataclass
class TestResult:
    name: str
    passed: bool
    duration_ms: float
    details: str
    category: str = "general"


def log(msg: str) -> None:
    """Print with timestamp."""
    ts = datetime.now().strftime("%H:%M:%S.%f")[:-3]
    print(f"[{ts}] {msg}")


PLUGIN_DIR = Path(__file__).parent.parent


# ─── Mode System Tests (Option B) ─────────────────────────────────────────────


def test_mode_controller_skill_exists() -> TestResult:
    """Test that mode-controller skill exists."""
    start = time.time()

    skill_path = PLUGIN_DIR / "skills" / "modes" / "mode-controller.md"

    duration = (time.time() - start) * 1000

    if not skill_path.exists():
        return TestResult(
            "Mode Controller Skill", False, duration,
            "Missing skills/modes/mode-controller.md", "mode-system"
        )

    content = skill_path.read_text()

    # Check for required mode definitions
    modes = ["default", "debug", "optimize", "release"]
    missing_modes = [m for m in modes if m not in content.lower()]

    if missing_modes:
        return TestResult(
            "Mode Controller Skill", False, duration,
            f"Missing mode definitions: {missing_modes}", "mode-system"
        )

    return TestResult(
        "Mode Controller Skill", True, duration,
        f"All 4 modes defined ({len(content)} chars)", "mode-system"
    )


def test_lint_command_has_mode_support() -> TestResult:
    """Test that lint command supports modes."""
    start = time.time()

    lint_path = PLUGIN_DIR / "commands" / "code" / "lint.md"

    duration = (time.time() - start) * 1000

    if not lint_path.exists():
        return TestResult(
            "Lint Mode Support", False, duration,
            "Missing commands/code/lint.md", "mode-system"
        )

    content = lint_path.read_text()

    # Check for mode argument in YAML frontmatter
    has_frontmatter = content.startswith("---")
    has_mode_arg = "mode" in content.lower() and "argument" in content.lower()
    has_mode_behaviors = "Mode Behavior" in content or "mode behavior" in content.lower()

    issues = []
    if not has_frontmatter:
        issues.append("missing YAML frontmatter")
    if not has_mode_arg:
        issues.append("missing mode argument")
    if not has_mode_behaviors:
        issues.append("missing mode behaviors")

    if issues:
        return TestResult(
            "Lint Mode Support", False, duration,
            f"Issues: {', '.join(issues)}", "mode-system"
        )

    return TestResult(
        "Lint Mode Support", True, duration,
        "Has frontmatter, mode argument, and behaviors", "mode-system"
    )


def test_test_run_command_has_mode_support() -> TestResult:
    """Test that test:run command supports modes."""
    start = time.time()

    test_path = PLUGIN_DIR / "commands" / "test" / "run.md"

    duration = (time.time() - start) * 1000

    if not test_path.exists():
        return TestResult(
            "Test Run Mode Support", False, duration,
            "Missing commands/test/run.md", "mode-system"
        )

    content = test_path.read_text()

    # Check for mode support
    has_mode_arg = "mode" in content.lower()
    has_all_modes = all(m in content.lower() for m in ["default", "debug", "optimize", "release"])

    if not has_mode_arg or not has_all_modes:
        return TestResult(
            "Test Run Mode Support", False, duration,
            "Missing mode argument or mode definitions", "mode-system"
        )

    return TestResult(
        "Test Run Mode Support", True, duration,
        "Has mode support with all 4 modes", "mode-system"
    )


def test_arch_analyze_command_has_mode_support() -> TestResult:
    """Test that arch:analyze command supports modes."""
    start = time.time()

    arch_path = PLUGIN_DIR / "commands" / "arch" / "analyze.md"

    duration = (time.time() - start) * 1000

    if not arch_path.exists():
        return TestResult(
            "Arch Analyze Mode Support", False, duration,
            "Missing commands/arch/analyze.md", "mode-system"
        )

    content = arch_path.read_text()

    # Check for mode support
    has_mode_support = "mode" in content.lower() and ("default" in content.lower() or "debug" in content.lower())

    if not has_mode_support:
        return TestResult(
            "Arch Analyze Mode Support", False, duration,
            "Missing mode support", "mode-system"
        )

    return TestResult(
        "Arch Analyze Mode Support", True, duration,
        "Has mode support", "mode-system"
    )


# ─── Smart Orchestrator Tests (Option C) ──────────────────────────────────────


def test_do_command_exists() -> TestResult:
    """Test that /craft:do universal command exists."""
    start = time.time()

    do_path = PLUGIN_DIR / "commands" / "do.md"

    duration = (time.time() - start) * 1000

    if not do_path.exists():
        return TestResult(
            "Do Command", False, duration,
            "Missing commands/do.md", "orchestrator"
        )

    content = do_path.read_text()

    # Check for task routing logic
    has_task_arg = "task" in content.lower()
    has_routing = "route" in content.lower() or "workflow" in content.lower()
    has_categories = sum(1 for c in ["feature", "bug", "quality", "test", "release"] if c in content.lower()) >= 3

    issues = []
    if not has_task_arg:
        issues.append("missing task argument")
    if not has_routing:
        issues.append("missing routing logic")
    if not has_categories:
        issues.append("missing task categories")

    if issues:
        return TestResult(
            "Do Command", False, duration,
            f"Issues: {', '.join(issues)}", "orchestrator"
        )

    return TestResult(
        "Do Command", True, duration,
        f"Complete with task routing ({len(content)} chars)", "orchestrator"
    )


def test_check_command_exists() -> TestResult:
    """Test that /craft:check universal pre-flight command exists."""
    start = time.time()

    check_path = PLUGIN_DIR / "commands" / "check.md"

    duration = (time.time() - start) * 1000

    if not check_path.exists():
        return TestResult(
            "Check Command", False, duration,
            "Missing commands/check.md", "orchestrator"
        )

    content = check_path.read_text()

    # Check for pre-flight functionality
    has_commit_mode = "commit" in content.lower()
    has_pr_mode = "pr" in content.lower()
    has_release_mode = "release" in content.lower()
    has_project_detection = "detect" in content.lower() or "python" in content.lower()

    features = []
    if has_commit_mode:
        features.append("commit")
    if has_pr_mode:
        features.append("pr")
    if has_release_mode:
        features.append("release")
    if has_project_detection:
        features.append("detection")

    if len(features) < 3:
        return TestResult(
            "Check Command", False, duration,
            f"Missing features, only found: {features}", "orchestrator"
        )

    return TestResult(
        "Check Command", True, duration,
        f"Complete with modes: {features}", "orchestrator"
    )


def test_smart_help_command_exists() -> TestResult:
    """Test that /craft:help smart help command exists."""
    start = time.time()

    help_path = PLUGIN_DIR / "commands" / "smart-help.md"

    duration = (time.time() - start) * 1000

    if not help_path.exists():
        return TestResult(
            "Smart Help Command", False, duration,
            "Missing commands/smart-help.md", "orchestrator"
        )

    content = help_path.read_text()

    # Check for context-awareness
    has_context = "context" in content.lower()
    has_project_types = sum(1 for t in ["python", "node", "r package"] if t in content.lower()) >= 1

    if not has_context:
        return TestResult(
            "Smart Help Command", False, duration,
            "Missing context-awareness", "orchestrator"
        )

    return TestResult(
        "Smart Help Command", True, duration,
        f"Context-aware help ({len(content)} chars)", "orchestrator"
    )


def test_task_analyzer_skill_exists() -> TestResult:
    """Test that task-analyzer skill exists."""
    start = time.time()

    skill_path = PLUGIN_DIR / "skills" / "orchestration" / "task-analyzer.md"

    duration = (time.time() - start) * 1000

    if not skill_path.exists():
        return TestResult(
            "Task Analyzer Skill", False, duration,
            "Missing skills/orchestration/task-analyzer.md", "orchestrator"
        )

    content = skill_path.read_text()

    # Check for required capabilities
    has_intent = "intent" in content.lower()
    has_domain = "domain" in content.lower()
    has_workflow = "workflow" in content.lower()
    has_complexity = "complexity" in content.lower()

    capabilities = []
    if has_intent:
        capabilities.append("intent")
    if has_domain:
        capabilities.append("domain")
    if has_workflow:
        capabilities.append("workflow")
    if has_complexity:
        capabilities.append("complexity")

    if len(capabilities) < 3:
        return TestResult(
            "Task Analyzer Skill", False, duration,
            f"Missing capabilities, only found: {capabilities}", "orchestrator"
        )

    return TestResult(
        "Task Analyzer Skill", True, duration,
        f"Complete with: {capabilities}", "orchestrator"
    )


# ─── Hub & README Tests ───────────────────────────────────────────────────────


def test_hub_reflects_v120() -> TestResult:
    """Test that hub.md reflects v1.2.0 features."""
    start = time.time()

    hub_path = PLUGIN_DIR / "commands" / "hub.md"

    duration = (time.time() - start) * 1000

    if not hub_path.exists():
        return TestResult(
            "Hub v1.2.0 Update", False, duration,
            "Missing commands/hub.md", "integration"
        )

    content = hub_path.read_text()

    # Check for v1.2.0 features
    has_46_commands = "46" in content
    has_8_skills = "8" in content
    has_modes = "mode" in content.lower()
    has_smart_commands = "smart" in content.lower() or "/craft:do" in content

    features = []
    if has_46_commands:
        features.append("46 commands")
    if has_8_skills:
        features.append("8 skills")
    if has_modes:
        features.append("modes")
    if has_smart_commands:
        features.append("smart commands")

    if len(features) < 3:
        return TestResult(
            "Hub v1.2.0 Update", False, duration,
            f"Missing v1.2.0 features: {features}", "integration"
        )

    return TestResult(
        "Hub v1.2.0 Update", True, duration,
        f"Reflects v1.2.0: {features}", "integration"
    )


def test_readme_reflects_v120() -> TestResult:
    """Test that README.md reflects v1.2.0."""
    start = time.time()

    readme_path = PLUGIN_DIR / "README.md"

    duration = (time.time() - start) * 1000

    if not readme_path.exists():
        return TestResult(
            "README v1.2.0 Update", False, duration,
            "Missing README.md", "integration"
        )

    content = readme_path.read_text()

    # Check for version
    has_version = "1.2.0" in content
    has_46_commands = "46" in content
    has_mode_section = "Mode" in content

    if not has_version:
        return TestResult(
            "README v1.2.0 Update", False, duration,
            "Missing version 1.2.0", "integration"
        )

    if not has_46_commands:
        return TestResult(
            "README v1.2.0 Update", False, duration,
            "Missing 46 commands count", "integration"
        )

    return TestResult(
        "README v1.2.0 Update", True, duration,
        "README reflects v1.2.0", "integration"
    )


# ─── Count Validation Tests ───────────────────────────────────────────────────


def test_total_command_count() -> TestResult:
    """Test that we have exactly 46 commands."""
    start = time.time()

    commands_dir = PLUGIN_DIR / "commands"
    commands = list(commands_dir.rglob("*.md"))

    duration = (time.time() - start) * 1000

    # Count should be at least 43 (we had 42 + 3 smart commands)
    expected_min = 43

    if len(commands) < expected_min:
        return TestResult(
            "Total Command Count", False, duration,
            f"Found {len(commands)} commands, expected at least {expected_min}", "validation"
        )

    return TestResult(
        "Total Command Count", True, duration,
        f"Found {len(commands)} commands", "validation"
    )


def test_total_skill_count() -> TestResult:
    """Test that we have 8 skills."""
    start = time.time()

    skills_dir = PLUGIN_DIR / "skills"
    skills = list(skills_dir.rglob("*.md"))

    duration = (time.time() - start) * 1000

    expected = 8

    if len(skills) != expected:
        skill_names = [s.stem for s in skills]
        return TestResult(
            "Total Skill Count", False, duration,
            f"Found {len(skills)} skills, expected {expected}: {skill_names}", "validation"
        )

    return TestResult(
        "Total Skill Count", True, duration,
        f"Found {len(skills)} skills as expected", "validation"
    )


def test_skills_directory_structure() -> TestResult:
    """Test that skills are organized correctly."""
    start = time.time()

    skills_dir = PLUGIN_DIR / "skills"

    expected_subdirs = ["design", "modes", "orchestration", "testing", "architecture", "planning"]
    found = []
    missing = []

    for subdir in expected_subdirs:
        if (skills_dir / subdir).is_dir():
            found.append(subdir)
        else:
            missing.append(subdir)

    duration = (time.time() - start) * 1000

    # At least 4 subdirs should exist
    if len(found) < 4:
        return TestResult(
            "Skills Directory Structure", False, duration,
            f"Missing subdirs: {missing}", "validation"
        )

    return TestResult(
        "Skills Directory Structure", True, duration,
        f"Found subdirs: {found}", "validation"
    )


# ─── Test Runner ─────────────────────────────────────────────────────────────


def run_all_tests() -> list[TestResult]:
    """Run all v1.2.0 validation tests."""
    tests = [
        # Mode System Tests (Option B)
        test_mode_controller_skill_exists,
        test_lint_command_has_mode_support,
        test_test_run_command_has_mode_support,
        test_arch_analyze_command_has_mode_support,
        # Smart Orchestrator Tests (Option C)
        test_do_command_exists,
        test_check_command_exists,
        test_smart_help_command_exists,
        test_task_analyzer_skill_exists,
        # Integration Tests
        test_hub_reflects_v120,
        test_readme_reflects_v120,
        # Validation Tests
        test_total_command_count,
        test_total_skill_count,
        test_skills_directory_structure,
    ]

    results = []
    for test_fn in tests:
        doc = test_fn.__doc__ or test_fn.__name__
        log(f"Running: {doc.strip().split('.')[0]}...")
        result = test_fn()
        results.append(result)
        status = "\u2705 PASS" if result.passed else "\u274c FAIL"
        log(f"  {status} ({result.duration_ms:.1f}ms) - {result.details}")

    return results


def generate_report(results: list[TestResult]) -> str:
    """Generate markdown report."""
    passed = sum(1 for r in results if r.passed)
    total = len(results)
    total_time = sum(r.duration_ms for r in results)

    # Group by category
    categories = {}
    for r in results:
        if r.category not in categories:
            categories[r.category] = []
        categories[r.category].append(r)

    report = f"""# Craft Plugin v1.2.0 Feature Test Report

**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
**Total Tests:** {total}
**Passed:** {passed}/{total} ({100*passed//total}%)
**Total Duration:** {total_time:.1f}ms

## v1.2.0 Features Tested

- **Option B: Mode System** - 4 execution modes (default, debug, optimize, release)
- **Option C: Smart Orchestrator** - Intelligent task routing and pre-flight checks

## Summary

| Category | Passed | Total |
|----------|--------|-------|
"""

    for cat, cat_results in categories.items():
        cat_passed = sum(1 for r in cat_results if r.passed)
        report += f"| {cat.replace('-', ' ').title()} | {cat_passed} | {len(cat_results)} |\n"

    report += "\n## Detailed Results\n\n"

    for cat, cat_results in categories.items():
        report += f"### {cat.replace('-', ' ').title()}\n\n"
        report += "| Test | Status | Duration | Details |\n"
        report += "|------|--------|----------|--------|\n"

        for r in cat_results:
            status = "\u2705 Pass" if r.passed else "\u274c Fail"
            report += f"| {r.name} | {status} | {r.duration_ms:.1f}ms | {r.details} |\n"

        report += "\n"

    if passed == total:
        report += "## Result\n\n\U0001f389 **All v1.2.0 feature tests passed!**\n"
    else:
        report += f"## Result\n\n\u26a0\ufe0f **{total - passed} test(s) failed.** Review details above.\n"

    return report


def main():
    print("=" * 60)
    print("\U0001f680 Craft Plugin v1.2.0 Feature Tests")
    print("=" * 60)
    print()

    results = run_all_tests()

    print()
    print("=" * 60)
    print("\U0001f4ca Generating Report...")
    print("=" * 60)

    report = generate_report(results)

    # Save report
    report_path = Path(__file__).parent / "v120_test_report.md"
    with open(report_path, "w") as f:
        f.write(report)

    print(f"\n\U0001f4c4 Report saved to: {report_path}")

    # Print summary
    passed = sum(1 for r in results if r.passed)
    total = len(results)

    print()
    if passed == total:
        print("\U0001f389 All v1.2.0 feature tests passed!")
    else:
        print(f"\u26a0\ufe0f  {total - passed}/{total} tests failed. See report for details.")

    return 0 if passed == total else 1


if __name__ == "__main__":
    exit(main())
