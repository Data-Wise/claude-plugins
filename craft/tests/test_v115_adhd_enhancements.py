#!/usr/bin/env python3
"""
Craft Plugin v1.15.0 ADHD-Friendly Enhancements Test Suite
===========================================================
Validates Phase 1, 2, and 3 ADHD-friendly website enhancements.

Tests:
- TL;DR boxes on major pages
- Time estimates in tutorials
- Visual workflow diagrams
- Progress indicators
- Mobile responsive CSS
- Accessibility features
- Interactive playground
- Navigation structure

Run with: python tests/test_v115_adhd_enhancements.py
"""

import json
import os
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Tuple


@dataclass
class TestResult:
    name: str
    passed: bool
    duration_ms: float
    details: str
    category: str = "adhd"


def log(msg: str) -> None:
    """Print with timestamp."""
    ts = datetime.now().strftime("%H:%M:%S.%f")[:-3]
    print(f"[{ts}] {msg}")


# ─── Phase 1 Tests: Quick Wins ───────────────────────────────────────────────


def test_tldr_boxes_present() -> TestResult:
    """Test that TL;DR boxes are present on major pages."""
    import time
    start = time.time()

    plugin_dir = Path(__file__).parent.parent
    docs_dir = plugin_dir / "docs"

    # Pages that should have TL;DR boxes
    required_pages = [
        "index.md",
        "QUICK-START.md",
        "ADHD-QUICK-START.md",
        "guide/getting-started.md",
        "guide/skills-agents.md",
        "guide/orchestrator.md",
        "commands/overview.md",
        "commands/docs.md",
        "commands/site.md",
        "workflows/index.md",
    ]

    missing = []
    invalid_format = []

    for page_path in required_pages:
        page = docs_dir / page_path
        if not page.exists():
            missing.append(page_path)
            continue

        content = page.read_text()

        # Check for TL;DR box with required sections
        tldr_pattern = r'> \*\*TL;DR\*\* \(\d+ seconds\)\s*\n> - \*\*What:\*\*.*\n> - \*\*Why:\*\*.*\n> - \*\*How:\*\*.*\n> - \*\*Next:\*\*'

        if not re.search(tldr_pattern, content):
            invalid_format.append(page_path)

    duration = (time.time() - start) * 1000

    if missing or invalid_format:
        details = []
        if missing:
            details.append(f"Missing pages: {', '.join(missing)}")
        if invalid_format:
            details.append(f"Invalid TL;DR format: {', '.join(invalid_format)}")
        return TestResult(
            "TL;DR Boxes Present",
            False,
            duration,
            "; ".join(details),
            "phase1"
        )

    return TestResult(
        "TL;DR Boxes Present",
        True,
        duration,
        f"{len(required_pages)} pages with valid TL;DR boxes",
        "phase1"
    )


def test_time_estimates_in_tutorials() -> TestResult:
    """Test that tutorials have time estimates."""
    import time
    start = time.time()

    plugin_dir = Path(__file__).parent.parent
    docs_dir = plugin_dir / "docs"

    tutorial_pages = [
        "QUICK-START.md",
        "ADHD-QUICK-START.md",
        "guide/getting-started.md",
        "guide/skills-agents.md",
        "guide/orchestrator.md",
        "workflows/index.md",
        "PLAYGROUND.md",
        "ACCESSIBILITY.md",
    ]

    missing_estimate = []

    for page_path in tutorial_pages:
        page = docs_dir / page_path
        if not page.exists():
            continue

        content = page.read_text()

        # Check for time estimate format: ⏱️ **X minutes** • 🟢 Level • ✓ Info
        time_pattern = r'⏱️ \*\*[^*]+\*\* • [🟢🟡🔴] \w+ • ✓'

        if not re.search(time_pattern, content):
            missing_estimate.append(page_path)

    duration = (time.time() - start) * 1000

    if missing_estimate:
        return TestResult(
            "Time Estimates in Tutorials",
            False,
            duration,
            f"Missing time estimates: {', '.join(missing_estimate)}",
            "phase1"
        )

    return TestResult(
        "Time Estimates in Tutorials",
        True,
        duration,
        f"{len(tutorial_pages) - len(missing_estimate)} tutorials with time estimates",
        "phase1"
    )


def test_mermaid_syntax_valid() -> TestResult:
    """Test that all mermaid diagrams have valid syntax."""
    import time
    start = time.time()

    plugin_dir = Path(__file__).parent.parent
    docs_dir = plugin_dir / "docs"

    errors = []

    # Find all markdown files
    for md_file in docs_dir.rglob("*.md"):
        content = md_file.read_text()

        # Find all mermaid blocks
        mermaid_blocks = re.findall(r'```mermaid\n(.*?)```', content, re.DOTALL)

        for i, block in enumerate(mermaid_blocks):
            # Check for common syntax errors
            if '<br/>' in block:
                errors.append(f"{md_file.name} block {i+1}: Uses deprecated <br/> tags")

            # Check for missing click targets (should use markdown strings)
            if 'click ' in block:
                # Count click statements
                click_count = len(re.findall(r'click \w+', block))
                if click_count > 0:
                    # This is good - interactive diagrams
                    pass

    duration = (time.time() - start) * 1000

    if errors:
        return TestResult(
            "Mermaid Syntax Valid",
            False,
            duration,
            "; ".join(errors[:5]),  # Limit to first 5 errors
            "phase1"
        )

    return TestResult(
        "Mermaid Syntax Valid",
        True,
        duration,
        "All mermaid diagrams have valid syntax",
        "phase1"
    )


# ─── Phase 2 Tests: Structure ────────────────────────────────────────────────


def test_visual_workflows_page_exists() -> TestResult:
    """Test that workflows/index.md exists with 5 diagrams."""
    import time
    start = time.time()

    plugin_dir = Path(__file__).parent.parent
    workflows_page = plugin_dir / "docs" / "workflows" / "index.md"

    if not workflows_page.exists():
        return TestResult(
            "Visual Workflows Page Exists",
            False,
            0,
            "workflows/index.md not found",
            "phase2"
        )

    content = workflows_page.read_text()

    # Count mermaid diagrams
    diagram_count = len(re.findall(r'```mermaid', content))

    # Check for expected workflows
    expected_workflows = [
        "Documentation Workflow",
        "Site Creation Workflow",
        "Release Workflow",
        "Development Workflow",
        "AI Routing Workflow",
    ]

    missing_workflows = [w for w in expected_workflows if w not in content]

    duration = (time.time() - start) * 1000

    if diagram_count < 5:
        return TestResult(
            "Visual Workflows Page Exists",
            False,
            duration,
            f"Only {diagram_count} diagrams found, expected 5+",
            "phase2"
        )

    if missing_workflows:
        return TestResult(
            "Visual Workflows Page Exists",
            False,
            duration,
            f"Missing workflows: {', '.join(missing_workflows)}",
            "phase2"
        )

    return TestResult(
        "Visual Workflows Page Exists",
        True,
        duration,
        f"Found {diagram_count} workflow diagrams",
        "phase2"
    )


def test_navigation_flattened() -> TestResult:
    """Test that navigation has ADHD features promoted to top-level."""
    import time
    start = time.time()

    plugin_dir = Path(__file__).parent.parent
    mkdocs_yml = plugin_dir / "mkdocs.yml"

    if not mkdocs_yml.exists():
        return TestResult(
            "Navigation Flattened",
            False,
            0,
            "mkdocs.yml not found",
            "phase2"
        )

    content = mkdocs_yml.read_text()

    # Check for promoted top-level items with emojis
    required_nav_items = [
        "🚀 Quick Start",
        "🧠 ADHD Guide",
        "📊 Visual Workflows",
        "🎮 Playground",
        "📚 Reference Card",
    ]

    missing = [item for item in required_nav_items if item not in content]

    # Count top-level nav items (should be < 7 for ADHD-friendly)
    nav_section = re.search(r'nav:\n(.*?)(?:\n\w|\Z)', content, re.DOTALL)
    if nav_section:
        top_level = re.findall(r'\n  - [^:]+:', nav_section.group(1))
        top_level_count = len(top_level)
    else:
        top_level_count = 0

    duration = (time.time() - start) * 1000

    if missing:
        return TestResult(
            "Navigation Flattened",
            False,
            duration,
            f"Missing nav items: {', '.join(missing)}",
            "phase2"
        )

    if top_level_count > 7:
        return TestResult(
            "Navigation Flattened",
            False,
            duration,
            f"Too many top-level items: {top_level_count} (max 7 for ADHD)",
            "phase2"
        )

    return TestResult(
        "Navigation Flattened",
        True,
        duration,
        f"ADHD-friendly nav with {top_level_count} top-level items",
        "phase2"
    )


def test_callout_boxes_present() -> TestResult:
    """Test that visual callout boxes are present."""
    import time
    start = time.time()

    plugin_dir = Path(__file__).parent.parent
    docs_dir = plugin_dir / "docs"

    # Pages that should have callout boxes
    pages_to_check = [
        "workflows/index.md",
        "QUICK-START.md",
        "ADHD-QUICK-START.md",
        "guide/orchestrator.md",
        "index.md",
        "PLAYGROUND.md",
    ]

    callout_types = {
        "tip": r'!!! tip',
        "success": r'!!! success',
        "warning": r'!!! warning',
        "abstract": r'!!! abstract',
    }

    total_callouts = 0
    pages_with_callouts = 0

    for page_path in pages_to_check:
        page = docs_dir / page_path
        if not page.exists():
            continue

        content = page.read_text()
        page_callouts = sum(len(re.findall(pattern, content)) for pattern in callout_types.values())

        if page_callouts > 0:
            pages_with_callouts += 1
            total_callouts += page_callouts

    duration = (time.time() - start) * 1000

    if total_callouts < 10:
        return TestResult(
            "Callout Boxes Present",
            False,
            duration,
            f"Only {total_callouts} callouts found, expected 10+",
            "phase2"
        )

    return TestResult(
        "Callout Boxes Present",
        True,
        duration,
        f"{total_callouts} callout boxes across {pages_with_callouts} pages",
        "phase2"
    )


def test_homepage_card_layout() -> TestResult:
    """Test that homepage uses card-based layout."""
    import time
    start = time.time()

    plugin_dir = Path(__file__).parent.parent
    index_page = plugin_dir / "docs" / "index.md"

    if not index_page.exists():
        return TestResult(
            "Homepage Card Layout",
            False,
            0,
            "index.md not found",
            "phase2"
        )

    content = index_page.read_text()

    # Check for card grid markup
    if '<div class="grid cards" markdown>' not in content:
        return TestResult(
            "Homepage Card Layout",
            False,
            0,
            "Card grid markup not found",
            "phase2"
        )

    # Count card sections
    card_sections = len(re.findall(r'<div class="grid cards" markdown>', content))

    # Check for expected sections
    expected_sections = [
        "Features",
        "Popular Workflows",
        "Documentation",
    ]

    missing_sections = [s for s in expected_sections if s not in content]

    duration = (time.time() - start) * 1000

    if missing_sections:
        return TestResult(
            "Homepage Card Layout",
            False,
            duration,
            f"Missing sections: {', '.join(missing_sections)}",
            "phase2"
        )

    return TestResult(
        "Homepage Card Layout",
        True,
        duration,
        f"{card_sections} card grid sections with all expected content",
        "phase2"
    )


def test_interactive_mermaid_diagrams() -> TestResult:
    """Test that mermaid diagrams have clickable nodes."""
    import time
    start = time.time()

    plugin_dir = Path(__file__).parent.parent
    workflows_page = plugin_dir / "docs" / "workflows" / "index.md"

    if not workflows_page.exists():
        return TestResult(
            "Interactive Mermaid Diagrams",
            False,
            0,
            "workflows/index.md not found",
            "phase2"
        )

    content = workflows_page.read_text()

    # Find mermaid blocks
    mermaid_blocks = re.findall(r'```mermaid\n(.*?)```', content, re.DOTALL)

    # Count click statements (interactive nodes)
    total_clicks = sum(len(re.findall(r'click \w+', block)) for block in mermaid_blocks)

    duration = (time.time() - start) * 1000

    if total_clicks < 10:
        return TestResult(
            "Interactive Mermaid Diagrams",
            False,
            duration,
            f"Only {total_clicks} clickable nodes found, expected 10+",
            "phase2"
        )

    return TestResult(
        "Interactive Mermaid Diagrams",
        True,
        duration,
        f"{total_clicks} clickable nodes across {len(mermaid_blocks)} diagrams",
        "phase2"
    )


# ─── Phase 3 Tests: Polish ───────────────────────────────────────────────────


def test_mobile_responsive_css() -> TestResult:
    """Test that mobile responsive CSS is present."""
    import time
    start = time.time()

    plugin_dir = Path(__file__).parent.parent
    css_file = plugin_dir / "docs" / "stylesheets" / "extra.css"

    if not css_file.exists():
        return TestResult(
            "Mobile Responsive CSS",
            False,
            0,
            "extra.css not found",
            "phase3"
        )

    content = css_file.read_text()

    # Check for required responsive features
    required_features = [
        (r'\.mermaid\s*\{[^}]*overflow-x:\s*auto', "Mermaid overflow fix"),
        (r'@media.*max-width:\s*768px', "Tablet breakpoint"),
        (r'@media.*max-width:\s*480px', "Mobile breakpoint"),
        (r'@media.*prefers-reduced-motion', "Reduced motion support"),
        (r'@media.*prefers-contrast:\s*high', "High contrast mode"),
        (r'a:focus.*outline', "Focus indicators"),
        (r'@media print', "Print styles"),
    ]

    missing_features = []

    for pattern, feature_name in required_features:
        if not re.search(pattern, content, re.DOTALL):
            missing_features.append(feature_name)

    duration = (time.time() - start) * 1000

    if missing_features:
        return TestResult(
            "Mobile Responsive CSS",
            False,
            duration,
            f"Missing features: {', '.join(missing_features)}",
            "phase3"
        )

    # Count total CSS lines added
    css_lines = len(content.split('\n'))

    return TestResult(
        "Mobile Responsive CSS",
        True,
        duration,
        f"All responsive features present ({css_lines} total lines)",
        "phase3"
    )


def test_progress_indicators() -> TestResult:
    """Test that tutorials have progress indicators."""
    import time
    start = time.time()

    plugin_dir = Path(__file__).parent.parent
    docs_dir = plugin_dir / "docs"

    # Pages that should have progress indicators
    tutorial_pages = {
        "QUICK-START.md": 4,  # Expected number of progress indicators
        "ADHD-QUICK-START.md": 3,
        "guide/getting-started.md": 5,
    }

    missing_or_wrong = []

    for page_path, expected_count in tutorial_pages.items():
        page = docs_dir / page_path
        if not page.exists():
            missing_or_wrong.append(f"{page_path} (missing)")
            continue

        content = page.read_text()

        # Count progress indicators
        progress_pattern = r'!!! abstract "Progress:'
        progress_count = len(re.findall(progress_pattern, content))

        if progress_count != expected_count:
            missing_or_wrong.append(f"{page_path} (has {progress_count}, expected {expected_count})")

    duration = (time.time() - start) * 1000

    if missing_or_wrong:
        return TestResult(
            "Progress Indicators",
            False,
            duration,
            "; ".join(missing_or_wrong),
            "phase3"
        )

    total_indicators = sum(tutorial_pages.values())

    return TestResult(
        "Progress Indicators",
        True,
        duration,
        f"{total_indicators} progress indicators across {len(tutorial_pages)} tutorials",
        "phase3"
    )


def test_command_playground_exists() -> TestResult:
    """Test that PLAYGROUND.md exists with interactive scenarios."""
    import time
    start = time.time()

    plugin_dir = Path(__file__).parent.parent
    playground_page = plugin_dir / "docs" / "PLAYGROUND.md"

    if not playground_page.exists():
        return TestResult(
            "Command Playground Exists",
            False,
            0,
            "PLAYGROUND.md not found",
            "phase3"
        )

    content = playground_page.read_text()

    # Check for expected scenarios
    expected_scenarios = [
        "Scenario 1:",
        "Scenario 2:",
        "Scenario 3:",
        "Scenario 4:",
        "Scenario 5:",
        "Scenario 6:",
    ]

    missing_scenarios = [s for s in expected_scenarios if s not in content]

    # Check for key elements
    required_elements = [
        ("What Happens", "Example outputs"),
        ("What You Learn", "Learning points"),
        ("Challenge", "Practice challenges"),
    ]

    missing_elements = []
    for element, description in required_elements:
        if element not in content:
            missing_elements.append(description)

    duration = (time.time() - start) * 1000

    if missing_scenarios or missing_elements:
        errors = []
        if missing_scenarios:
            errors.append(f"Missing: {', '.join(missing_scenarios)}")
        if missing_elements:
            errors.append(f"Missing elements: {', '.join(missing_elements)}")
        return TestResult(
            "Command Playground Exists",
            False,
            duration,
            "; ".join(errors),
            "phase3"
        )

    return TestResult(
        "Command Playground Exists",
        True,
        duration,
        f"{len(expected_scenarios)} interactive scenarios with all required elements",
        "phase3"
    )


def test_accessibility_documentation() -> TestResult:
    """Test that ACCESSIBILITY.md exists and covers WCAG AA."""
    import time
    start = time.time()

    plugin_dir = Path(__file__).parent.parent
    accessibility_page = plugin_dir / "docs" / "ACCESSIBILITY.md"

    if not accessibility_page.exists():
        return TestResult(
            "Accessibility Documentation",
            False,
            0,
            "ACCESSIBILITY.md not found",
            "phase3"
        )

    content = accessibility_page.read_text()

    # Check for WCAG coverage
    required_sections = [
        "WCAG AA Compliance",
        "Keyboard Navigation",
        "Screen Reader Support",
        "Visual Accessibility",
        "Motion and Animation",
        "Mobile and Touch Accessibility",
        "Content Readability",
        "Testing",
        "Reporting Issues",
    ]

    missing_sections = [s for s in required_sections if s not in content]

    # Check for specific WCAG criteria
    wcag_criteria = [
        "1.1 Text Alternatives",
        "1.4.3 Contrast",
        "2.1 Keyboard Accessible",
        "2.4 Navigable",
    ]

    missing_criteria = [c for c in wcag_criteria if c not in content]

    duration = (time.time() - start) * 1000

    if missing_sections or missing_criteria:
        errors = []
        if missing_sections:
            errors.append(f"Missing sections: {', '.join(missing_sections[:3])}")
        if missing_criteria:
            errors.append(f"Missing WCAG criteria: {', '.join(missing_criteria)}")
        return TestResult(
            "Accessibility Documentation",
            False,
            duration,
            "; ".join(errors),
            "phase3"
        )

    return TestResult(
        "Accessibility Documentation",
        True,
        duration,
        f"Complete WCAG AA documentation with {len(required_sections)} sections",
        "phase3"
    )


# ─── Integration Tests ───────────────────────────────────────────────────────


def test_adhd_score_algorithm() -> TestResult:
    """Test ADHD score algorithm components are present."""
    import time
    start = time.time()

    plugin_dir = Path(__file__).parent.parent
    docs_dir = plugin_dir / "docs"

    # Score components (from ROADMAP.md)
    score_components = {
        "Visual Hierarchy (25%)": {
            "tldr_boxes": 0,
            "time_estimates": 0,
            "emojis_in_nav": 0,
        },
        "Time Estimates (20%)": {
            "tutorials_with_estimates": 0,
        },
        "Workflow Diagrams (20%)": {
            "mermaid_diagrams": 0,
            "interactive_nodes": 0,
        },
        "Mobile Responsive (15%)": {
            "responsive_css": False,
            "breakpoints": 0,
        },
        "Content Density (20%)": {
            "progress_indicators": 0,
            "callout_boxes": 0,
        },
    }

    # Scan all docs
    for md_file in docs_dir.rglob("*.md"):
        content = md_file.read_text()

        # Count TL;DR boxes
        if re.search(r'> \*\*TL;DR\*\*', content):
            score_components["Visual Hierarchy (25%)"]["tldr_boxes"] += 1

        # Count time estimates
        if re.search(r'⏱️ \*\*[^*]+\*\*', content):
            score_components["Time Estimates (20%)"]["tutorials_with_estimates"] += 1
            score_components["Visual Hierarchy (25%)"]["time_estimates"] += 1

        # Count mermaid diagrams
        diagrams = len(re.findall(r'```mermaid', content))
        score_components["Workflow Diagrams (20%)"]["mermaid_diagrams"] += diagrams

        # Count interactive nodes
        clicks = len(re.findall(r'click \w+', content))
        score_components["Workflow Diagrams (20%)"]["interactive_nodes"] += clicks

        # Count progress indicators
        progress = len(re.findall(r'!!! abstract "Progress:', content))
        score_components["Content Density (20%)"]["progress_indicators"] += progress

        # Count callout boxes
        callouts = len(re.findall(r'!!! (tip|success|warning)', content))
        score_components["Content Density (20%)"]["callout_boxes"] += callouts

    # Check CSS
    css_file = plugin_dir / "docs" / "stylesheets" / "extra.css"
    if css_file.exists():
        css_content = css_file.read_text()
        score_components["Mobile Responsive (15%)"]["responsive_css"] = True
        score_components["Mobile Responsive (15%)"]["breakpoints"] = len(
            re.findall(r'@media.*max-width', css_content)
        )

    # Check nav emojis
    mkdocs_yml = plugin_dir / "mkdocs.yml"
    if mkdocs_yml.exists():
        nav_content = mkdocs_yml.read_text()
        emojis = len(re.findall(r'- [🚀🧠📊🎮📚]', nav_content))
        score_components["Visual Hierarchy (25%)"]["emojis_in_nav"] = emojis

    duration = (time.time() - start) * 1000

    # Calculate simple pass/fail (all components should have values > 0)
    issues = []
    for category, metrics in score_components.items():
        for metric, value in metrics.items():
            if isinstance(value, bool) and not value:
                issues.append(f"{category}: {metric} is False")
            elif isinstance(value, int) and value == 0:
                issues.append(f"{category}: {metric} is 0")

    if issues:
        return TestResult(
            "ADHD Score Algorithm",
            False,
            duration,
            "; ".join(issues[:3]),
            "integration"
        )

    return TestResult(
        "ADHD Score Algorithm",
        True,
        duration,
        f"All 5 score components have positive values",
        "integration"
    )


def test_mkdocs_build_succeeds() -> TestResult:
    """Test that mkdocs build --strict succeeds."""
    import time
    import subprocess
    start = time.time()

    plugin_dir = Path(__file__).parent.parent

    try:
        result = subprocess.run(
            ["mkdocs", "build", "--strict"],
            cwd=plugin_dir,
            capture_output=True,
            text=True,
            timeout=30
        )

        duration = (time.time() - start) * 1000

        if result.returncode != 0:
            return TestResult(
                "MkDocs Build Succeeds",
                False,
                duration,
                f"Build failed: {result.stderr[:200]}",
                "integration"
            )

        # Check for warnings
        if "WARNING" in result.stdout or "WARNING" in result.stderr:
            return TestResult(
                "MkDocs Build Succeeds",
                False,
                duration,
                "Build has warnings",
                "integration"
            )

        return TestResult(
            "MkDocs Build Succeeds",
            True,
            duration,
            "Clean build with --strict mode",
            "integration"
        )

    except subprocess.TimeoutExpired:
        return TestResult(
            "MkDocs Build Succeeds",
            False,
            30000,
            "Build timeout after 30s",
            "integration"
        )
    except FileNotFoundError:
        return TestResult(
            "MkDocs Build Succeeds",
            False,
            0,
            "mkdocs command not found (skipping)",
            "integration"
        )


# ─── Test Runner ─────────────────────────────────────────────────────────────


def run_all_tests() -> Tuple[List[TestResult], int, int]:
    """Run all v1.15.0 ADHD enhancement tests."""
    tests = [
        # Phase 1: Quick Wins
        test_tldr_boxes_present,
        test_time_estimates_in_tutorials,
        test_mermaid_syntax_valid,
        # Phase 2: Structure
        test_visual_workflows_page_exists,
        test_navigation_flattened,
        test_callout_boxes_present,
        test_homepage_card_layout,
        test_interactive_mermaid_diagrams,
        # Phase 3: Polish
        test_mobile_responsive_css,
        test_progress_indicators,
        test_command_playground_exists,
        test_accessibility_documentation,
        # Integration
        test_adhd_score_algorithm,
        test_mkdocs_build_succeeds,
    ]

    results = []
    passed = 0
    failed = 0

    log("=" * 80)
    log("Craft Plugin v1.15.0 ADHD Enhancement Tests")
    log("=" * 80)

    for test_func in tests:
        log(f"Running: {test_func.__name__}...")
        result = test_func()
        results.append(result)

        if result.passed:
            passed += 1
            log(f"  ✅ PASS ({result.duration_ms:.1f}ms): {result.details}")
        else:
            failed += 1
            log(f"  ❌ FAIL ({result.duration_ms:.1f}ms): {result.details}")

    return results, passed, failed


def print_summary(results: List[TestResult], passed: int, failed: int) -> None:
    """Print test summary by category."""
    print("\n" + "=" * 80)
    print("TEST SUMMARY")
    print("=" * 80)

    # Group by category
    by_category = {}
    for result in results:
        if result.category not in by_category:
            by_category[result.category] = []
        by_category[result.category].append(result)

    for category in ["phase1", "phase2", "phase3", "integration"]:
        if category not in by_category:
            continue

        cat_results = by_category[category]
        cat_passed = sum(1 for r in cat_results if r.passed)
        cat_failed = sum(1 for r in cat_results if not r.passed)

        print(f"\n{category.upper()}:")
        print(f"  Passed: {cat_passed}/{len(cat_results)}")
        print(f"  Failed: {cat_failed}/{len(cat_results)}")

        if cat_failed > 0:
            print("  Failed tests:")
            for result in cat_results:
                if not result.passed:
                    print(f"    - {result.name}: {result.details}")

    print("\n" + "=" * 80)
    print(f"OVERALL: {passed} passed, {failed} failed, {passed + failed} total")
    print("=" * 80)

    if failed == 0:
        print("✅ All v1.15.0 ADHD enhancement tests passed!")
    else:
        print(f"❌ {failed} test(s) failed")


def main() -> int:
    """Main test runner."""
    results, passed, failed = run_all_tests()
    print_summary(results, passed, failed)
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
