#!/usr/bin/env python3
"""
Tests for the project-detector skill.

Tests the detection logic for various project types including:
- Python (uv, poetry, pip)
- Node.js (npm, pnpm, yarn)
- R packages and Quarto
- Rust, Go, Java
- Claude plugins
"""

import json
import tempfile
import unittest
from pathlib import Path
from dataclasses import dataclass
from typing import Optional


# ============================================================================
# Implementation (extracted from skill for testing)
# ============================================================================

@dataclass
class ProjectInfo:
    """Detected project information."""
    type: str
    variant: str
    test_framework: str
    build_tool: str
    ci_template: str
    python_versions: list
    node_versions: list
    has_docs: bool
    has_ci: bool


DETECTORS = [
    ("plugin", "claude", [".claude-plugin/plugin.json"], []),
    ("r", "package", ["DESCRIPTION", "NAMESPACE"], ["R/", "tests/"]),
    ("r", "quarto", ["_quarto.yml"], []),
    ("python", "uv", ["pyproject.toml", "uv.lock"], ["src/"]),
    ("python", "poetry", ["pyproject.toml", "poetry.lock"], ["src/"]),
    ("python", "pip", ["pyproject.toml"], ["requirements.txt"]),
    ("python", "setuptools", ["setup.py"], ["setup.cfg"]),
    ("node", "bun", ["package.json", "bun.lock"], []),
    ("node", "pnpm", ["package.json", "pnpm-lock.yaml"], []),
    ("node", "yarn", ["package.json", "yarn.lock"], []),
    ("node", "npm", ["package.json"], ["package-lock.json"]),
    ("rust", "cargo", ["Cargo.toml"], ["Cargo.lock"]),
    ("go", "mod", ["go.mod"], ["go.sum"]),
]


def detect_project(path: Path) -> Optional[ProjectInfo]:
    """Detect project type from directory contents."""
    for proj_type, variant, required, optional in DETECTORS:
        if all((path / f).exists() for f in required):
            return ProjectInfo(
                type=proj_type,
                variant=variant,
                test_framework=detect_test_framework(path, proj_type),
                build_tool=variant,
                ci_template=f"{proj_type}-{variant}",
                python_versions=detect_python_versions(path) if proj_type == "python" else [],
                node_versions=detect_node_versions(path) if proj_type == "node" else [],
                has_docs=any(detect_docs(path).values()),
                has_ci=(path / ".github/workflows").exists(),
            )
    return None


def detect_test_framework(path: Path, proj_type: str) -> str:
    """Detect test framework based on project type."""
    if proj_type == "python":
        return detect_python_test_framework(path)
    elif proj_type == "node":
        return detect_node_test_framework(path)
    elif proj_type == "r":
        return detect_r_test_framework(path)
    elif proj_type == "rust":
        return detect_rust_test_framework(path)
    elif proj_type == "go":
        return detect_go_test_framework(path)
    return "unknown"


def detect_python_test_framework(path: Path) -> str:
    """Detect Python test framework."""
    pyproject = path / "pyproject.toml"
    if pyproject.exists():
        content = pyproject.read_text()
        if "pytest" in content:
            return "pytest"
        if "unittest" in content:
            return "unittest"

    if (path / "tests").exists():
        test_files = list((path / "tests").glob("test_*.py"))
        if test_files:
            content = test_files[0].read_text()
            if "import pytest" in content or "@pytest" in content:
                return "pytest"
            if "import unittest" in content:
                return "unittest"

    return "pytest"


def detect_node_test_framework(path: Path) -> str:
    """Detect Node.js test framework."""
    pkg = path / "package.json"
    if pkg.exists():
        data = json.loads(pkg.read_text())
        deps = {**data.get("devDependencies", {}), **data.get("dependencies", {})}

        if "vitest" in deps:
            return "vitest"
        if "jest" in deps:
            return "jest"
        if "mocha" in deps:
            return "mocha"
        if "ava" in deps:
            return "ava"

    return "jest"


def detect_r_test_framework(path: Path) -> str:
    """Detect R test framework."""
    desc = path / "DESCRIPTION"
    if desc.exists():
        content = desc.read_text()
        if "testthat" in content:
            return "testthat"
        if "tinytest" in content:
            return "tinytest"

    if (path / "tests/testthat").exists():
        return "testthat"

    return "testthat"


def detect_rust_test_framework(path: Path) -> str:
    """Detect Rust test framework."""
    cargo = path / "Cargo.toml"
    if cargo.exists():
        content = cargo.read_text()

        # Check for test frameworks in dev-dependencies
        if "rstest" in content:
            return "rstest"
        if "proptest" in content:
            return "proptest"
        if "quickcheck" in content:
            return "quickcheck"
        if "criterion" in content:
            return "criterion"

    # Check for test modules in src/
    if (path / "src/lib.rs").exists():
        content = (path / "src/lib.rs").read_text()
        if "#[cfg(test)]" in content:
            return "cargo-test"

    # Check for tests/ directory
    if (path / "tests").exists():
        return "cargo-test"

    return "cargo-test"


def detect_go_test_framework(path: Path) -> str:
    """Detect Go test framework."""
    # Check for test files
    test_files = list(path.glob("*_test.go"))
    if not test_files and (path / "pkg").exists():
        test_files = list((path / "pkg").rglob("*_test.go"))

    if test_files:
        content = test_files[0].read_text()

        if "github.com/stretchr/testify" in content:
            return "testify"
        if "github.com/onsi/ginkgo" in content:
            return "ginkgo"
        if "github.com/onsi/gomega" in content:
            return "ginkgo"
        if "gocheck" in content or "gopkg.in/check" in content:
            return "gocheck"
        if "goconvey" in content:
            return "goconvey"

    # Check go.mod for test dependencies
    gomod = path / "go.mod"
    if gomod.exists():
        content = gomod.read_text()
        if "testify" in content:
            return "testify"
        if "ginkgo" in content:
            return "ginkgo"

    return "go-test"


def detect_python_versions(path: Path) -> list:
    """Detect Python version requirements."""
    import re
    pyproject = path / "pyproject.toml"
    if pyproject.exists():
        content = pyproject.read_text()
        match = re.search(r'requires-python\s*=\s*["\']([^"\']+)["\']', content)
        if match:
            constraint = match.group(1)
            if ">=" in constraint:
                min_ver = constraint.replace(">=", "").strip()
                return get_versions_from(min_ver)

    return ["3.10", "3.11", "3.12"]


def get_versions_from(min_version: str) -> list:
    """Get Python versions >= min_version."""
    all_versions = ["3.9", "3.10", "3.11", "3.12", "3.13"]
    try:
        idx = all_versions.index(min_version)
        return all_versions[idx:]
    except ValueError:
        return ["3.10", "3.11", "3.12"]


def detect_node_versions(path: Path) -> list:
    """Detect Node.js version requirements."""
    return ["18", "20", "22"]


def detect_docs(path: Path) -> dict:
    """Detect documentation setup."""
    return {
        "mkdocs": (path / "mkdocs.yml").exists(),
        "sphinx": (path / "docs/conf.py").exists(),
        "docusaurus": (path / "docusaurus.config.js").exists(),
        "vitepress": (path / ".vitepress").exists(),
        "quarto": (path / "_quarto.yml").exists(),
        "readme": (path / "README.md").exists(),
    }


def has_coverage_config(path: Path) -> bool:
    """Check for coverage configuration."""
    pyproject = path / "pyproject.toml"
    if pyproject.exists() and "coverage" in pyproject.read_text():
        return True
    if (path / ".coveragerc").exists():
        return True
    if (path / "codecov.yml").exists():
        return True
    return False


def has_linting_config(path: Path) -> bool:
    """Check for linting configuration."""
    lint_files = [".eslintrc", ".eslintrc.js", ".eslintrc.json",
                  "ruff.toml", ".ruff.toml", ".flake8", ".pylintrc"]
    return any((path / f).exists() for f in lint_files)


def has_type_checking(path: Path) -> bool:
    """Check for type checking configuration."""
    type_files = ["mypy.ini", ".mypy.ini", "pyrightconfig.json", "tsconfig.json"]
    pyproject = path / "pyproject.toml"
    if pyproject.exists() and "[tool.mypy]" in pyproject.read_text():
        return True
    return any((path / f).exists() for f in type_files)


# ============================================================================
# Test Cases
# ============================================================================

class TestProjectDetection(unittest.TestCase):
    """Test project type detection."""

    def setUp(self):
        """Create temp directory for each test."""
        self.temp_dir = tempfile.mkdtemp()
        self.path = Path(self.temp_dir)

    def tearDown(self):
        """Clean up temp directory."""
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    # -------------------------------------------------------------------------
    # Python Project Detection
    # -------------------------------------------------------------------------

    def test_detect_python_uv_project(self):
        """Detect Python project with uv."""
        (self.path / "pyproject.toml").write_text('[project]\nname = "test"')
        (self.path / "uv.lock").write_text("# uv lockfile")

        result = detect_project(self.path)

        self.assertIsNotNone(result)
        self.assertEqual(result.type, "python")
        self.assertEqual(result.variant, "uv")
        self.assertEqual(result.ci_template, "python-uv")

    def test_detect_python_poetry_project(self):
        """Detect Python project with Poetry."""
        (self.path / "pyproject.toml").write_text('[tool.poetry]\nname = "test"')
        (self.path / "poetry.lock").write_text("# poetry lockfile")

        result = detect_project(self.path)

        self.assertIsNotNone(result)
        self.assertEqual(result.type, "python")
        self.assertEqual(result.variant, "poetry")

    def test_detect_python_pip_project(self):
        """Detect Python project with pip (pyproject.toml only)."""
        (self.path / "pyproject.toml").write_text('[project]\nname = "test"')

        result = detect_project(self.path)

        self.assertIsNotNone(result)
        self.assertEqual(result.type, "python")
        self.assertEqual(result.variant, "pip")

    def test_detect_python_setuptools_project(self):
        """Detect Python project with setup.py."""
        (self.path / "setup.py").write_text('from setuptools import setup\nsetup()')

        result = detect_project(self.path)

        self.assertIsNotNone(result)
        self.assertEqual(result.type, "python")
        self.assertEqual(result.variant, "setuptools")

    def test_uv_takes_priority_over_pip(self):
        """UV should be detected over plain pip when uv.lock exists."""
        (self.path / "pyproject.toml").write_text('[project]\nname = "test"')
        (self.path / "uv.lock").write_text("# lockfile")

        result = detect_project(self.path)

        self.assertEqual(result.variant, "uv")

    # -------------------------------------------------------------------------
    # Node.js Project Detection
    # -------------------------------------------------------------------------

    def test_detect_node_npm_project(self):
        """Detect Node.js project with npm."""
        (self.path / "package.json").write_text('{"name": "test"}')

        result = detect_project(self.path)

        self.assertIsNotNone(result)
        self.assertEqual(result.type, "node")
        self.assertEqual(result.variant, "npm")

    def test_detect_node_pnpm_project(self):
        """Detect Node.js project with pnpm."""
        (self.path / "package.json").write_text('{"name": "test"}')
        (self.path / "pnpm-lock.yaml").write_text("# pnpm lockfile")

        result = detect_project(self.path)

        self.assertIsNotNone(result)
        self.assertEqual(result.type, "node")
        self.assertEqual(result.variant, "pnpm")

    def test_detect_node_yarn_project(self):
        """Detect Node.js project with yarn."""
        (self.path / "package.json").write_text('{"name": "test"}')
        (self.path / "yarn.lock").write_text("# yarn lockfile")

        result = detect_project(self.path)

        self.assertIsNotNone(result)
        self.assertEqual(result.type, "node")
        self.assertEqual(result.variant, "yarn")

    # -------------------------------------------------------------------------
    # R Project Detection
    # -------------------------------------------------------------------------

    def test_detect_r_package(self):
        """Detect R package project."""
        (self.path / "DESCRIPTION").write_text("Package: test\nTitle: Test")
        (self.path / "NAMESPACE").write_text("export(test)")

        result = detect_project(self.path)

        self.assertIsNotNone(result)
        self.assertEqual(result.type, "r")
        self.assertEqual(result.variant, "package")

    def test_detect_r_quarto(self):
        """Detect R Quarto project."""
        (self.path / "_quarto.yml").write_text("project:\n  type: book")

        result = detect_project(self.path)

        self.assertIsNotNone(result)
        self.assertEqual(result.type, "r")
        self.assertEqual(result.variant, "quarto")

    # -------------------------------------------------------------------------
    # Other Project Types
    # -------------------------------------------------------------------------

    def test_detect_rust_project(self):
        """Detect Rust project."""
        (self.path / "Cargo.toml").write_text('[package]\nname = "test"')

        result = detect_project(self.path)

        self.assertIsNotNone(result)
        self.assertEqual(result.type, "rust")
        self.assertEqual(result.variant, "cargo")

    def test_detect_go_project(self):
        """Detect Go project."""
        (self.path / "go.mod").write_text("module test")

        result = detect_project(self.path)

        self.assertIsNotNone(result)
        self.assertEqual(result.type, "go")
        self.assertEqual(result.variant, "mod")

    def test_detect_claude_plugin(self):
        """Detect Claude plugin project."""
        (self.path / ".claude-plugin").mkdir()
        (self.path / ".claude-plugin/plugin.json").write_text('{"name": "test"}')

        result = detect_project(self.path)

        self.assertIsNotNone(result)
        self.assertEqual(result.type, "plugin")
        self.assertEqual(result.variant, "claude")

    def test_detect_empty_directory(self):
        """Empty directory returns None."""
        result = detect_project(self.path)
        self.assertIsNone(result)

    # -------------------------------------------------------------------------
    # Priority Tests
    # -------------------------------------------------------------------------

    def test_claude_plugin_highest_priority(self):
        """Claude plugin should be detected first even with other markers."""
        (self.path / ".claude-plugin").mkdir()
        (self.path / ".claude-plugin/plugin.json").write_text('{"name": "test"}')
        (self.path / "pyproject.toml").write_text('[project]\nname = "test"')
        (self.path / "package.json").write_text('{"name": "test"}')

        result = detect_project(self.path)

        self.assertEqual(result.type, "plugin")


class TestTestFrameworkDetection(unittest.TestCase):
    """Test test framework detection."""

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.path = Path(self.temp_dir)

    def tearDown(self):
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_detect_pytest_from_pyproject(self):
        """Detect pytest from pyproject.toml."""
        (self.path / "pyproject.toml").write_text('[project.optional-dependencies]\ndev = ["pytest"]')

        result = detect_python_test_framework(self.path)

        self.assertEqual(result, "pytest")

    def test_detect_pytest_from_test_file(self):
        """Detect pytest from test file imports."""
        (self.path / "pyproject.toml").write_text('[project]\nname = "test"')
        (self.path / "tests").mkdir()
        (self.path / "tests/test_main.py").write_text("import pytest\n\ndef test_something(): pass")

        result = detect_python_test_framework(self.path)

        self.assertEqual(result, "pytest")

    def test_detect_unittest_from_test_file(self):
        """Detect unittest from test file imports."""
        (self.path / "pyproject.toml").write_text('[project]\nname = "test"')
        (self.path / "tests").mkdir()
        (self.path / "tests/test_main.py").write_text("import unittest\n\nclass TestMain(unittest.TestCase): pass")

        result = detect_python_test_framework(self.path)

        self.assertEqual(result, "unittest")

    def test_detect_jest_from_package_json(self):
        """Detect Jest from package.json."""
        (self.path / "package.json").write_text('{"devDependencies": {"jest": "^29.0.0"}}')

        result = detect_node_test_framework(self.path)

        self.assertEqual(result, "jest")

    def test_detect_vitest_from_package_json(self):
        """Detect Vitest from package.json."""
        (self.path / "package.json").write_text('{"devDependencies": {"vitest": "^1.0.0"}}')

        result = detect_node_test_framework(self.path)

        self.assertEqual(result, "vitest")

    def test_detect_testthat_from_description(self):
        """Detect testthat from DESCRIPTION."""
        (self.path / "DESCRIPTION").write_text("Package: test\nSuggests: testthat")

        result = detect_r_test_framework(self.path)

        self.assertEqual(result, "testthat")

    def test_detect_testthat_from_directory(self):
        """Detect testthat from tests/testthat directory."""
        (self.path / "tests/testthat").mkdir(parents=True)

        result = detect_r_test_framework(self.path)

        self.assertEqual(result, "testthat")

    def test_detect_mocha_from_package_json(self):
        """Detect Mocha from package.json."""
        (self.path / "package.json").write_text('{"devDependencies": {"mocha": "^10.0.0"}}')

        result = detect_node_test_framework(self.path)

        self.assertEqual(result, "mocha")

    def test_detect_ava_from_package_json(self):
        """Detect AVA from package.json."""
        (self.path / "package.json").write_text('{"devDependencies": {"ava": "^5.0.0"}}')

        result = detect_node_test_framework(self.path)

        self.assertEqual(result, "ava")

    def test_detect_cargo_test_default(self):
        """Detect cargo-test as default for Rust."""
        (self.path / "Cargo.toml").write_text('[package]\nname = "myproject"')

        result = detect_rust_test_framework(self.path)

        self.assertEqual(result, "cargo-test")

    def test_detect_rstest_from_cargo(self):
        """Detect rstest from Cargo.toml."""
        (self.path / "Cargo.toml").write_text('[dev-dependencies]\nrstest = "0.18"')

        result = detect_rust_test_framework(self.path)

        self.assertEqual(result, "rstest")

    def test_detect_proptest_from_cargo(self):
        """Detect proptest from Cargo.toml."""
        (self.path / "Cargo.toml").write_text('[dev-dependencies]\nproptest = "1.0"')

        result = detect_rust_test_framework(self.path)

        self.assertEqual(result, "proptest")

    def test_detect_cargo_test_from_test_module(self):
        """Detect cargo-test from #[cfg(test)] in lib.rs."""
        (self.path / "Cargo.toml").write_text('[package]\nname = "myproject"')
        (self.path / "src").mkdir()
        (self.path / "src/lib.rs").write_text('pub fn add(a: i32, b: i32) -> i32 { a + b }\n\n#[cfg(test)]\nmod tests {}')

        result = detect_rust_test_framework(self.path)

        self.assertEqual(result, "cargo-test")

    def test_detect_cargo_test_from_tests_dir(self):
        """Detect cargo-test from tests/ directory."""
        (self.path / "Cargo.toml").write_text('[package]\nname = "myproject"')
        (self.path / "tests").mkdir()

        result = detect_rust_test_framework(self.path)

        self.assertEqual(result, "cargo-test")

    def test_detect_go_test_default(self):
        """Detect go-test as default for Go."""
        (self.path / "go.mod").write_text('module myproject\n\ngo 1.21')

        result = detect_go_test_framework(self.path)

        self.assertEqual(result, "go-test")

    def test_detect_testify_from_test_file(self):
        """Detect testify from test file imports."""
        (self.path / "go.mod").write_text('module myproject\n\ngo 1.21')
        (self.path / "main_test.go").write_text('package main\n\nimport "github.com/stretchr/testify/assert"')

        result = detect_go_test_framework(self.path)

        self.assertEqual(result, "testify")

    def test_detect_ginkgo_from_test_file(self):
        """Detect Ginkgo from test file imports."""
        (self.path / "go.mod").write_text('module myproject\n\ngo 1.21')
        (self.path / "main_test.go").write_text('package main\n\nimport "github.com/onsi/ginkgo/v2"')

        result = detect_go_test_framework(self.path)

        self.assertEqual(result, "ginkgo")

    def test_detect_testify_from_gomod(self):
        """Detect testify from go.mod dependencies."""
        (self.path / "go.mod").write_text('module myproject\n\ngo 1.21\n\nrequire github.com/stretchr/testify v1.8.0')

        result = detect_go_test_framework(self.path)

        self.assertEqual(result, "testify")


class TestPythonVersionDetection(unittest.TestCase):
    """Test Python version detection."""

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.path = Path(self.temp_dir)

    def tearDown(self):
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_detect_requires_python_310(self):
        """Detect requires-python >= 3.10."""
        (self.path / "pyproject.toml").write_text('requires-python = ">=3.10"')

        result = detect_python_versions(self.path)

        self.assertEqual(result, ["3.10", "3.11", "3.12", "3.13"])

    def test_detect_requires_python_311(self):
        """Detect requires-python >= 3.11."""
        (self.path / "pyproject.toml").write_text('requires-python = ">=3.11"')

        result = detect_python_versions(self.path)

        self.assertEqual(result, ["3.11", "3.12", "3.13"])

    def test_default_versions_when_no_constraint(self):
        """Default to 3.10-3.12 when no constraint."""
        (self.path / "pyproject.toml").write_text('[project]\nname = "test"')

        result = detect_python_versions(self.path)

        self.assertEqual(result, ["3.10", "3.11", "3.12"])

    def test_get_versions_from_valid(self):
        """get_versions_from returns correct versions."""
        self.assertEqual(get_versions_from("3.10"), ["3.10", "3.11", "3.12", "3.13"])
        self.assertEqual(get_versions_from("3.12"), ["3.12", "3.13"])

    def test_get_versions_from_invalid(self):
        """get_versions_from handles invalid version."""
        result = get_versions_from("3.99")
        self.assertEqual(result, ["3.10", "3.11", "3.12"])


class TestDocumentationDetection(unittest.TestCase):
    """Test documentation setup detection."""

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.path = Path(self.temp_dir)

    def tearDown(self):
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_detect_mkdocs(self):
        """Detect MkDocs documentation."""
        (self.path / "mkdocs.yml").write_text("site_name: Test")

        result = detect_docs(self.path)

        self.assertTrue(result["mkdocs"])
        self.assertFalse(result["sphinx"])

    def test_detect_sphinx(self):
        """Detect Sphinx documentation."""
        (self.path / "docs").mkdir()
        (self.path / "docs/conf.py").write_text("# Sphinx config")

        result = detect_docs(self.path)

        self.assertTrue(result["sphinx"])
        self.assertFalse(result["mkdocs"])

    def test_detect_readme(self):
        """Detect README.md."""
        (self.path / "README.md").write_text("# Project")

        result = detect_docs(self.path)

        self.assertTrue(result["readme"])


class TestCIFeatureDetection(unittest.TestCase):
    """Test CI feature detection."""

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.path = Path(self.temp_dir)

    def tearDown(self):
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_detect_coverage_in_pyproject(self):
        """Detect coverage config in pyproject.toml."""
        (self.path / "pyproject.toml").write_text('[tool.coverage.run]\nsource = ["src"]')

        result = has_coverage_config(self.path)

        self.assertTrue(result)

    def test_detect_coveragerc(self):
        """Detect .coveragerc file."""
        (self.path / ".coveragerc").write_text("[run]\nsource = src")

        result = has_coverage_config(self.path)

        self.assertTrue(result)

    def test_detect_codecov_yml(self):
        """Detect codecov.yml file."""
        (self.path / "codecov.yml").write_text("coverage:\n  status: true")

        result = has_coverage_config(self.path)

        self.assertTrue(result)

    def test_detect_ruff_config(self):
        """Detect ruff linting configuration."""
        (self.path / "ruff.toml").write_text('[lint]\nselect = ["E", "W"]')

        result = has_linting_config(self.path)

        self.assertTrue(result)

    def test_detect_eslint_config(self):
        """Detect ESLint configuration."""
        (self.path / ".eslintrc.json").write_text('{"extends": "standard"}')

        result = has_linting_config(self.path)

        self.assertTrue(result)

    def test_detect_mypy_in_pyproject(self):
        """Detect mypy config in pyproject.toml."""
        (self.path / "pyproject.toml").write_text('[tool.mypy]\nstrict = true')

        result = has_type_checking(self.path)

        self.assertTrue(result)

    def test_detect_tsconfig(self):
        """Detect TypeScript configuration."""
        (self.path / "tsconfig.json").write_text('{"compilerOptions": {}}')

        result = has_type_checking(self.path)

        self.assertTrue(result)

    def test_detect_existing_ci(self):
        """Detect existing CI workflows."""
        (self.path / ".github/workflows").mkdir(parents=True)
        (self.path / ".github/workflows/ci.yml").write_text("name: CI")
        (self.path / "pyproject.toml").write_text('[project]\nname = "test"')

        result = detect_project(self.path)

        self.assertTrue(result.has_ci)


class TestIntegration(unittest.TestCase):
    """Integration tests for complete detection flow."""

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.path = Path(self.temp_dir)

    def tearDown(self):
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_full_python_uv_project(self):
        """Test complete Python/uv project detection."""
        # Create full project structure
        (self.path / "pyproject.toml").write_text('''
[project]
name = "test"
requires-python = ">=3.10"

[project.optional-dependencies]
dev = ["pytest", "pytest-cov", "ruff", "mypy"]

[tool.coverage.run]
source = ["src"]

[tool.mypy]
strict = true
''')
        (self.path / "uv.lock").write_text("# lockfile")
        (self.path / "src/test").mkdir(parents=True)
        (self.path / "tests").mkdir()
        (self.path / "tests/test_main.py").write_text("import pytest\ndef test_main(): pass")
        (self.path / "mkdocs.yml").write_text("site_name: Test")
        (self.path / "README.md").write_text("# Test Project")

        result = detect_project(self.path)

        self.assertEqual(result.type, "python")
        self.assertEqual(result.variant, "uv")
        self.assertEqual(result.test_framework, "pytest")
        self.assertEqual(result.ci_template, "python-uv")
        self.assertIn("3.10", result.python_versions)
        self.assertTrue(result.has_docs)
        self.assertFalse(result.has_ci)

        # Check additional features
        self.assertTrue(has_coverage_config(self.path))
        self.assertTrue(has_type_checking(self.path))

    def test_full_node_project(self):
        """Test complete Node.js project detection."""
        (self.path / "package.json").write_text(json.dumps({
            "name": "test",
            "version": "1.0.0",
            "devDependencies": {
                "vitest": "^1.0.0",
                "eslint": "^8.0.0"
            },
            "engines": {
                "node": ">=18"
            }
        }))
        (self.path / "pnpm-lock.yaml").write_text("# lockfile")
        (self.path / ".eslintrc.json").write_text('{}')
        (self.path / "tsconfig.json").write_text('{}')

        result = detect_project(self.path)

        self.assertEqual(result.type, "node")
        self.assertEqual(result.variant, "pnpm")
        self.assertEqual(result.test_framework, "vitest")
        self.assertTrue(has_linting_config(self.path))
        self.assertTrue(has_type_checking(self.path))


# ============================================================================
# New Detection Functions (to be added to implementation)
# ============================================================================

def detect_tauri_project(path: Path) -> bool:
    """Detect Tauri desktop app project."""
    return (path / "src-tauri/tauri.conf.json").exists()


def detect_swift_project(path: Path) -> Optional[str]:
    """Detect Swift project type."""
    if (path / "Package.swift").exists():
        return "swift-package"
    xcodeproj = list(path.glob("*.xcodeproj"))
    if xcodeproj:
        return "swift-xcode"
    xcworkspace = list(path.glob("*.xcworkspace"))
    if xcworkspace:
        return "swift-xcode"
    return None


def detect_mcp_server(path: Path) -> bool:
    """Detect MCP server project."""
    pkg = path / "package.json"
    if pkg.exists():
        data = json.loads(pkg.read_text())
        name = data.get("name", "").lower()
        if "mcp" in name:
            return True
        deps = {**data.get("dependencies", {}), **data.get("devDependencies", {})}
        if "@modelcontextprotocol/sdk" in deps:
            return True
        if any("mcp" in dep.lower() for dep in deps):
            return True
    return False


def detect_homebrew_tap(path: Path) -> bool:
    """Detect Homebrew tap project."""
    if (path / "Formula").exists():
        rb_files = list((path / "Formula").glob("*.rb"))
        if rb_files:
            return True
    if (path / "Casks").exists():
        rb_files = list((path / "Casks").glob("*.rb"))
        if rb_files:
            return True
    return False


def detect_zsh_plugin(path: Path) -> bool:
    """Detect ZSH plugin project."""
    plugin_files = list(path.glob("*.plugin.zsh"))
    if plugin_files:
        return True
    if (path / "functions").exists():
        zsh_files = list((path / "functions").glob("*.zsh"))
        if zsh_files:
            return True
    if (path / ".zsh_plugins.txt").exists():
        return True
    return False


def detect_elisp_package(path: Path) -> bool:
    """Detect Emacs Lisp package project."""
    pkg_files = list(path.glob("*-pkg.el"))
    if pkg_files:
        return True
    if (path / "Cask").exists():
        return True
    el_files = list(path.glob("*.el"))
    for el_file in el_files:
        if ";;;###autoload" in el_file.read_text():
            return True
    return False


# ============================================================================
# New Test Classes
# ============================================================================

class TestTauriDetection(unittest.TestCase):
    """Test Tauri project detection."""

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.path = Path(self.temp_dir)

    def tearDown(self):
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_detect_tauri_project(self):
        """Detect Tauri project from src-tauri/tauri.conf.json."""
        (self.path / "src-tauri").mkdir()
        (self.path / "src-tauri/tauri.conf.json").write_text('{"build": {}}')

        result = detect_tauri_project(self.path)

        self.assertTrue(result)

    def test_not_tauri_without_config(self):
        """Not a Tauri project without tauri.conf.json."""
        result = detect_tauri_project(self.path)

        self.assertFalse(result)


class TestSwiftDetection(unittest.TestCase):
    """Test Swift project detection."""

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.path = Path(self.temp_dir)

    def tearDown(self):
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_detect_swift_package(self):
        """Detect Swift Package Manager project."""
        (self.path / "Package.swift").write_text('// swift-tools-version:5.9')

        result = detect_swift_project(self.path)

        self.assertEqual(result, "swift-package")

    def test_detect_xcode_project(self):
        """Detect Xcode project."""
        (self.path / "MyApp.xcodeproj").mkdir()

        result = detect_swift_project(self.path)

        self.assertEqual(result, "swift-xcode")

    def test_detect_xcode_workspace(self):
        """Detect Xcode workspace."""
        (self.path / "MyApp.xcworkspace").mkdir()

        result = detect_swift_project(self.path)

        self.assertEqual(result, "swift-xcode")

    def test_not_swift_empty_dir(self):
        """Empty directory is not a Swift project."""
        result = detect_swift_project(self.path)

        self.assertIsNone(result)


class TestMCPServerDetection(unittest.TestCase):
    """Test MCP server detection."""

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.path = Path(self.temp_dir)

    def tearDown(self):
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_detect_mcp_by_name(self):
        """Detect MCP server by name containing 'mcp'."""
        (self.path / "package.json").write_text('{"name": "my-mcp-server"}')

        result = detect_mcp_server(self.path)

        self.assertTrue(result)

    def test_detect_mcp_by_sdk_dependency(self):
        """Detect MCP server by @modelcontextprotocol/sdk dependency."""
        (self.path / "package.json").write_text(json.dumps({
            "name": "my-server",
            "dependencies": {"@modelcontextprotocol/sdk": "^1.0.0"}
        }))

        result = detect_mcp_server(self.path)

        self.assertTrue(result)

    def test_not_mcp_regular_node(self):
        """Regular Node.js project is not MCP server."""
        (self.path / "package.json").write_text('{"name": "my-app"}')

        result = detect_mcp_server(self.path)

        self.assertFalse(result)


class TestHomebrewTapDetection(unittest.TestCase):
    """Test Homebrew tap detection."""

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.path = Path(self.temp_dir)

    def tearDown(self):
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_detect_formula_directory(self):
        """Detect Homebrew tap with Formula directory."""
        (self.path / "Formula").mkdir()
        (self.path / "Formula/myapp.rb").write_text('class Myapp < Formula')

        result = detect_homebrew_tap(self.path)

        self.assertTrue(result)

    def test_detect_casks_directory(self):
        """Detect Homebrew tap with Casks directory."""
        (self.path / "Casks").mkdir()
        (self.path / "Casks/myapp.rb").write_text('cask "myapp" do')

        result = detect_homebrew_tap(self.path)

        self.assertTrue(result)

    def test_not_homebrew_empty_dir(self):
        """Empty directory is not a Homebrew tap."""
        result = detect_homebrew_tap(self.path)

        self.assertFalse(result)


class TestZSHPluginDetection(unittest.TestCase):
    """Test ZSH plugin detection."""

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.path = Path(self.temp_dir)

    def tearDown(self):
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_detect_plugin_zsh_file(self):
        """Detect ZSH plugin by .plugin.zsh file."""
        (self.path / "myplugin.plugin.zsh").write_text('# ZSH plugin')

        result = detect_zsh_plugin(self.path)

        self.assertTrue(result)

    def test_detect_functions_directory(self):
        """Detect ZSH plugin by functions directory."""
        (self.path / "functions").mkdir()
        (self.path / "functions/myfunction.zsh").write_text('myfunction() {}')

        result = detect_zsh_plugin(self.path)

        self.assertTrue(result)

    def test_detect_zsh_plugins_txt(self):
        """Detect ZSH plugin by .zsh_plugins.txt."""
        (self.path / ".zsh_plugins.txt").write_text('zsh-users/zsh-autosuggestions')

        result = detect_zsh_plugin(self.path)

        self.assertTrue(result)

    def test_not_zsh_empty_dir(self):
        """Empty directory is not a ZSH plugin."""
        result = detect_zsh_plugin(self.path)

        self.assertFalse(result)


class TestElispPackageDetection(unittest.TestCase):
    """Test Emacs Lisp package detection."""

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.path = Path(self.temp_dir)

    def tearDown(self):
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_detect_pkg_el_file(self):
        """Detect Elisp package by *-pkg.el file."""
        (self.path / "mypackage-pkg.el").write_text('(define-package "mypackage" "1.0")')

        result = detect_elisp_package(self.path)

        self.assertTrue(result)

    def test_detect_cask_file(self):
        """Detect Elisp package by Cask file."""
        (self.path / "Cask").write_text('(source melpa)')

        result = detect_elisp_package(self.path)

        self.assertTrue(result)

    def test_detect_autoload_marker(self):
        """Detect Elisp package by ;;;###autoload marker."""
        (self.path / "mypackage.el").write_text(';;;###autoload\n(defun my-func () nil)')

        result = detect_elisp_package(self.path)

        self.assertTrue(result)

    def test_not_elisp_empty_dir(self):
        """Empty directory is not an Elisp package."""
        result = detect_elisp_package(self.path)

        self.assertFalse(result)


class TestBunDetection(unittest.TestCase):
    """Test Bun package manager detection."""

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.path = Path(self.temp_dir)

    def tearDown(self):
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_detect_bun_project(self):
        """Detect Bun project by bun.lock file."""
        (self.path / "package.json").write_text('{"name": "test"}')
        (self.path / "bun.lock").write_text('# bun lockfile')

        result = detect_project(self.path)

        self.assertEqual(result.type, "node")
        self.assertEqual(result.variant, "bun")


if __name__ == "__main__":
    # Run tests with verbose output
    unittest.main(verbosity=2)
