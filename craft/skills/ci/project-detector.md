---
name: project-detector
description: Smart detection of project types, build tools, and CI requirements for automated workflow generation
version: 1.0.0
category: ci
triggers:
  - detect project
  - project type
  - ci detection
  - what kind of project
  - analyze project
  - ci setup
---

# Project Detector Skill

Intelligent detection of project types, build tools, test frameworks, and CI requirements. Used by `/craft:ci:detect` and related commands.

## Detection Priority

Detection runs in priority order (first match wins for primary type):

| Priority | Type | Marker Files | Stack |
|----------|------|--------------|-------|
| 1 | Claude Plugin | `.claude-plugin/plugin.json` | plugin |
| 2 | MCP Server | `package.json` + `mcp` in name/deps | mcp |
| 3 | Tauri | `src-tauri/tauri.conf.json` | tauri |
| 4 | Swift Package | `Package.swift` | swift |
| 5 | Swift iOS/macOS | `*.xcodeproj` OR `*.xcworkspace` | swift |
| 6 | R Package | `DESCRIPTION` + `NAMESPACE` | r |
| 7 | R Quarto | `_quarto.yml` + `*.qmd` | r |
| 8 | Python UV | `pyproject.toml` + `uv.lock` | python |
| 9 | Python Poetry | `pyproject.toml` + `poetry.lock` | python |
| 10 | Python Pip | `pyproject.toml` OR `setup.py` | python |
| 11 | Node Bun | `package.json` + `bun.lock` | node |
| 12 | Node PNPM | `package.json` + `pnpm-lock.yaml` | node |
| 13 | Node Yarn | `package.json` + `yarn.lock` | node |
| 14 | Node NPM | `package.json` + `package-lock.json` | node |
| 15 | Rust | `Cargo.toml` | rust |
| 16 | Go | `go.mod` | go |
| 17 | Java Maven | `pom.xml` | java |
| 18 | Java Gradle | `build.gradle` OR `build.gradle.kts` | java |
| 19 | Homebrew Tap | `Formula/*.rb` OR `Casks/*.rb` | homebrew |
| 20 | ZSH Plugin | `*.plugin.zsh` OR `functions/*.zsh` | zsh |
| 21 | Emacs Package | `*.el` + `-pkg.el` | elisp |
| 22 | Shell | `*.sh` + no other markers | shell |

## Detection Algorithm

```python
from pathlib import Path
from dataclasses import dataclass
from typing import Optional

@dataclass
class ProjectInfo:
    """Detected project information."""
    type: str              # Primary type (python, node, r, etc.)
    variant: str           # Specific variant (uv, poetry, npm, etc.)
    test_framework: str    # pytest, jest, testthat, etc.
    build_tool: str        # uv, npm, cargo, etc.
    ci_template: str       # Recommended CI template
    python_versions: list  # For Python projects
    node_versions: list    # For Node projects
    has_docs: bool         # Has documentation setup
    has_ci: bool           # Already has CI configured

DETECTORS = [
    # (type, variant, required_files, optional_files)
    # Priority 1-5: Specialized/hybrid projects
    ("plugin", "claude", [".claude-plugin/plugin.json"], []),
    ("mcp", "server", ["package.json"], []),  # Check for mcp in name/deps
    ("tauri", "app", ["src-tauri/tauri.conf.json"], ["src-tauri/Cargo.toml"]),
    ("swift", "package", ["Package.swift"], ["Sources/"]),
    ("swift", "xcode", [], []),  # Special: glob for *.xcodeproj
    # Priority 6-7: R ecosystem
    ("r", "package", ["DESCRIPTION", "NAMESPACE"], ["R/", "tests/"]),
    ("r", "quarto", ["_quarto.yml"], ["*.qmd"]),
    # Priority 8-10: Python ecosystem
    ("python", "uv", ["pyproject.toml", "uv.lock"], ["src/"]),
    ("python", "poetry", ["pyproject.toml", "poetry.lock"], ["src/"]),
    ("python", "pip", ["pyproject.toml"], ["requirements.txt"]),
    ("python", "setuptools", ["setup.py"], ["setup.cfg"]),
    # Priority 11-14: Tooling projects (check BEFORE Node to catch hybrids)
    ("homebrew", "tap", [], []),  # Special: glob for Formula/*.rb
    ("zsh", "plugin", [], []),  # Special: glob for *.plugin.zsh
    ("elisp", "package", [], []),  # Special: glob for *-pkg.el
    # Priority 15-18: Node ecosystem (requires real Node project, not just tooling)
    ("node", "bun", ["package.json", "bun.lock"], []),
    ("node", "pnpm", ["package.json", "pnpm-lock.yaml"], []),
    ("node", "yarn", ["package.json", "yarn.lock"], []),
    ("node", "npm", ["package.json"], ["package-lock.json"]),
    # Priority 19-20: Other compiled languages
    ("rust", "cargo", ["Cargo.toml"], ["Cargo.lock"]),
    ("go", "mod", ["go.mod"], ["go.sum"]),
    ("java", "maven", ["pom.xml"], []),
    ("java", "gradle", ["build.gradle"], ["build.gradle.kts"]),
    # Priority 21: Fallback
    ("shell", "script", [], []),  # Fallback for *.sh
]


def is_real_node_project(path: Path) -> bool:
    """Check if package.json indicates a real Node.js project vs just tooling.

    A real Node.js project has at least one of:
    - 'main' field (library entry point)
    - 'bin' field (CLI commands)
    - 'dependencies' (not just devDependencies)
    - 'type': 'module' with actual source files

    Projects with only devDependencies (ESLint, Prettier, etc.) are
    just using Node tooling, not actual Node.js projects.
    """
    pkg = path / "package.json"
    if not pkg.exists():
        return False

    import json
    try:
        data = json.loads(pkg.read_text())
    except json.JSONDecodeError:
        return False

    # Has entry point = real Node project
    if data.get("main"):
        return True

    # Has CLI commands = real Node project
    if data.get("bin"):
        return True

    # Has real dependencies (not just devDependencies) = real Node project
    if data.get("dependencies") and len(data["dependencies"]) > 0:
        return True

    # Has exports field = real Node project (modern ESM)
    if data.get("exports"):
        return True

    # Only has devDependencies = just tooling, not a Node project
    return False


def detect_project(path: Path) -> Optional[ProjectInfo]:
    """Detect project type from directory contents."""
    for proj_type, variant, required, optional in DETECTORS:
        if all((path / f).exists() for f in required):
            # Special handling for Node.js - skip if only tooling
            if proj_type == "node" and not is_real_node_project(path):
                continue  # Skip Node detection, try next detector

            return ProjectInfo(
                type=proj_type,
                variant=variant,
                test_framework=detect_test_framework(path, proj_type),
                build_tool=variant,
                ci_template=f"{proj_type}-{variant}",
                python_versions=detect_python_versions(path) if proj_type == "python" else [],
                node_versions=detect_node_versions(path) if proj_type == "node" else [],
                has_docs=detect_docs(path),
                has_ci=(path / ".github/workflows").exists(),
            )
    return None
```

## Test Framework Detection

### Python
```python
def detect_python_test_framework(path: Path) -> str:
    """Detect Python test framework."""
    pyproject = path / "pyproject.toml"
    if pyproject.exists():
        content = pyproject.read_text()
        if "pytest" in content:
            return "pytest"
        if "unittest" in content:
            return "unittest"

    # Check for test directories
    if (path / "tests").exists():
        test_files = list((path / "tests").glob("test_*.py"))
        if test_files:
            # Check first file for framework hints
            content = test_files[0].read_text()
            if "import pytest" in content or "@pytest" in content:
                return "pytest"
            if "import unittest" in content:
                return "unittest"

    return "pytest"  # Default for Python
```

### Node.js
```python
def detect_node_test_framework(path: Path) -> str:
    """Detect Node.js test framework."""
    pkg = path / "package.json"
    if pkg.exists():
        import json
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

    return "jest"  # Default for Node
```

### R
```python
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

    return "testthat"  # Default for R
```

### Rust
```python
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
            return "criterion"  # Benchmarking

    # Check for test modules in src/
    if (path / "src/lib.rs").exists():
        content = (path / "src/lib.rs").read_text()
        if "#[cfg(test)]" in content:
            return "cargo-test"

    # Check for tests/ directory
    if (path / "tests").exists():
        return "cargo-test"

    return "cargo-test"  # Built-in Rust testing
```

### Go
```python
def detect_go_test_framework(path: Path) -> str:
    """Detect Go test framework."""
    # Check for test files
    test_files = list(path.glob("*_test.go"))
    if not test_files and (path / "pkg").exists():
        test_files = list((path / "pkg").rglob("*_test.go"))

    if test_files:
        # Check first test file for framework hints
        content = test_files[0].read_text()

        if "github.com/stretchr/testify" in content:
            return "testify"
        if "github.com/onsi/ginkgo" in content:
            return "ginkgo"
        if "github.com/onsi/gomega" in content:
            return "ginkgo"  # Gomega usually paired with Ginkgo
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

    return "go-test"  # Built-in Go testing
```

### Tauri (Rust + Node hybrid)
```python
def detect_tauri_project(path: Path) -> bool:
    """Detect Tauri desktop app project."""
    return (path / "src-tauri/tauri.conf.json").exists()

def detect_tauri_test_framework(path: Path) -> dict:
    """Detect test frameworks for both Rust and Node sides."""
    result = {"rust": "cargo-test", "node": "vitest"}

    # Check Rust side
    cargo = path / "src-tauri/Cargo.toml"
    if cargo.exists():
        content = cargo.read_text()
        if "rstest" in content:
            result["rust"] = "rstest"

    # Check Node side
    pkg = path / "package.json"
    if pkg.exists():
        content = pkg.read_text()
        if "vitest" in content:
            result["node"] = "vitest"
        elif "jest" in content:
            result["node"] = "jest"

    return result
```

### Swift
```python
def detect_swift_project(path: Path) -> Optional[str]:
    """Detect Swift project type."""
    # Swift Package Manager
    if (path / "Package.swift").exists():
        return "swift-package"

    # Xcode project
    xcodeproj = list(path.glob("*.xcodeproj"))
    if xcodeproj:
        return "swift-xcode"

    # Xcode workspace
    xcworkspace = list(path.glob("*.xcworkspace"))
    if xcworkspace:
        return "swift-xcode"

    return None

def detect_swift_test_framework(path: Path) -> str:
    """Detect Swift test framework."""
    # Check for Quick/Nimble (BDD)
    pkg = path / "Package.swift"
    if pkg.exists():
        content = pkg.read_text()
        if "Quick" in content or "Nimble" in content:
            return "quick-nimble"

    # Check for test targets in Package.swift
    if pkg.exists():
        content = pkg.read_text()
        if ".testTarget" in content:
            return "xctest"

    # Default to XCTest
    return "xctest"
```

### MCP Server
```python
def detect_mcp_server(path: Path) -> bool:
    """Detect MCP (Model Context Protocol) server project."""
    pkg = path / "package.json"
    if pkg.exists():
        import json
        data = json.loads(pkg.read_text())

        # Check name contains mcp
        name = data.get("name", "").lower()
        if "mcp" in name:
            return True

        # Check for @modelcontextprotocol dependency
        deps = {**data.get("dependencies", {}), **data.get("devDependencies", {})}
        if "@modelcontextprotocol/sdk" in deps:
            return True
        if any("mcp" in dep.lower() for dep in deps):
            return True

    return False
```

### Homebrew Tap
```python
def detect_homebrew_tap(path: Path) -> bool:
    """Detect Homebrew tap project."""
    # Check for Formula directory
    if (path / "Formula").exists():
        rb_files = list((path / "Formula").glob("*.rb"))
        if rb_files:
            return True

    # Check for Casks directory
    if (path / "Casks").exists():
        rb_files = list((path / "Casks").glob("*.rb"))
        if rb_files:
            return True

    return False
```

### ZSH Plugin
```python
def detect_zsh_plugin(path: Path) -> bool:
    """Detect ZSH plugin project."""
    # Check for .plugin.zsh file
    plugin_files = list(path.glob("*.plugin.zsh"))
    if plugin_files:
        return True

    # Check for functions directory with .zsh files
    if (path / "functions").exists():
        zsh_files = list((path / "functions").glob("*.zsh"))
        if zsh_files:
            return True

    # Check for antidote/antigen/oh-my-zsh markers
    if (path / ".zsh_plugins.txt").exists():
        return True

    return False
```

### Emacs Lisp Package
```python
def detect_elisp_package(path: Path) -> bool:
    """Detect Emacs Lisp package project."""
    # Check for *-pkg.el file (MELPA convention)
    pkg_files = list(path.glob("*-pkg.el"))
    if pkg_files:
        return True

    # Check for Cask file (dependency management)
    if (path / "Cask").exists():
        return True

    # Check for .el files with ;;;### autoload markers
    el_files = list(path.glob("*.el"))
    for el_file in el_files:
        if ";;;###autoload" in el_file.read_text():
            return True

    return False

def detect_elisp_test_framework(path: Path) -> str:
    """Detect Emacs test framework."""
    # Check for ERT tests
    test_files = list(path.glob("test*.el")) + list(path.glob("*-test.el"))
    for test_file in test_files:
        content = test_file.read_text()
        if "ert-deftest" in content:
            return "ert"
        if "buttercup" in content:
            return "buttercup"

    return "ert"  # Default to ERT
```

## CI Template Selection

Based on detection, recommend appropriate CI template:

| Project | Template | Key Features |
|---------|----------|--------------|
| `python-uv` | `python-uv-ci.yml` | uv sync, pytest, coverage |
| `python-poetry` | `python-poetry-ci.yml` | poetry install, pytest |
| `python-pip` | `python-pip-ci.yml` | pip install, pytest |
| `node-npm` | `node-npm-ci.yml` | npm ci, jest/vitest |
| `node-pnpm` | `node-pnpm-ci.yml` | pnpm install, tests |
| `node-bun` | `node-bun-ci.yml` | bun install, bun test |
| `r-package` | `r-package-ci.yml` | R CMD check, testthat |
| `r-quarto` | `r-quarto-ci.yml` | quarto render |
| `rust-cargo` | `rust-cargo-ci.yml` | cargo test, clippy |
| `go-mod` | `go-mod-ci.yml` | go test, go vet |
| `plugin-claude` | `plugin-ci.yml` | Structure validation |
| `tauri-app` | `tauri-ci.yml` | Rust + Node build, tauri-action |
| `swift-package` | `swift-ci.yml` | swift build, swift test |
| `swift-xcode` | `xcode-ci.yml` | xcodebuild, xctest |
| `mcp-server` | `mcp-ci.yml` | Node tests, MCP validation |
| `homebrew-tap` | `homebrew-ci.yml` | Formula syntax check, brew audit |
| `zsh-plugin` | `zsh-ci.yml` | Shellcheck, zsh -n syntax check |
| `elisp-package` | `elisp-ci.yml` | Emacs batch compile, ert tests |

## Version Detection

### Python Versions
```python
def detect_python_versions(path: Path) -> list[str]:
    """Detect Python version requirements."""
    pyproject = path / "pyproject.toml"
    if pyproject.exists():
        content = pyproject.read_text()

        # Check requires-python
        import re
        match = re.search(r'requires-python\s*=\s*["\']([^"\']+)["\']', content)
        if match:
            constraint = match.group(1)
            # Parse constraint to version list
            if ">=" in constraint:
                min_ver = constraint.replace(">=", "").strip()
                return get_versions_from(min_ver)

    # Default: Python 3.10-3.12
    return ["3.10", "3.11", "3.12"]

def get_versions_from(min_version: str) -> list[str]:
    """Get Python versions >= min_version."""
    all_versions = ["3.9", "3.10", "3.11", "3.12", "3.13"]
    try:
        idx = all_versions.index(min_version)
        return all_versions[idx:]
    except ValueError:
        return ["3.10", "3.11", "3.12"]
```

### Node Versions
```python
def detect_node_versions(path: Path) -> list[str]:
    """Detect Node.js version requirements."""
    pkg = path / "package.json"
    if pkg.exists():
        import json
        data = json.loads(pkg.read_text())
        engines = data.get("engines", {})
        node_constraint = engines.get("node", "")

        if ">=" in node_constraint:
            # Parse and return appropriate versions
            pass

    # Default: LTS versions
    return ["18", "20", "22"]
```

## Documentation Detection

```python
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
```

## CI Feature Detection

```python
def detect_ci_features(path: Path) -> dict:
    """Detect what CI features are needed."""
    return {
        "tests": detect_test_framework(path) is not None,
        "coverage": has_coverage_config(path),
        "linting": has_linting_config(path),
        "type_checking": has_type_checking(path),
        "docs_build": detect_docs(path).get("mkdocs") or detect_docs(path).get("sphinx"),
        "docker": (path / "Dockerfile").exists(),
        "matrix": should_use_matrix(path),
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
```

## Output Format

When `/craft:ci:detect` runs, output structured results:

```markdown
## Project Detection Results

**Type:** Python (uv)
**Test Framework:** pytest
**Python Versions:** 3.10, 3.11, 3.12

### Detected Features
| Feature | Status |
|---------|--------|
| Tests | ✅ pytest in tests/ |
| Coverage | ✅ coverage config in pyproject.toml |
| Linting | ✅ ruff configured |
| Type Checking | ✅ mypy configured |
| Documentation | ✅ mkdocs.yml found |
| Docker | ❌ No Dockerfile |
| Existing CI | ❌ No .github/workflows/ |

### Recommended CI Template
`python-uv-ci.yml`

### Suggested Workflow
```yaml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.10', '3.11', '3.12']
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v4
      - run: uv sync
      - run: uv run pytest --cov
```

### Next Steps
1. Run `/craft:ci:generate` to create workflow file
2. Customize matrix if needed
3. Add secrets for coverage upload
```

## CI Templates Reference

For production-ready CI examples, see **CI-TEMPLATES.md** with templates from:

| Template Source | Project Type | Key Features |
|-----------------|--------------|--------------|
| aiterm | Python/uv | Multi-OS, multi-Python, Codecov |
| atlas | Node/npm | Multi-Node, unit/integration/e2e |
| nexus-cli | Python/uv | Quality gates, bandit security |
| scribe | Tauri | Rust + Vitest, cross-platform |

**Exemplary patterns from real projects:**
- Python: `uv sync --all-extras`, `pytest --cov`
- Node: `npm ci`, matrix 18/20/22
- Tauri: Separate frontend/backend jobs, Swatinem cache
- MCP: Simple Node tests, optional Bun support

## Integration

Use with:
- `/craft:ci:detect` - Run detection and show results
- `/craft:ci:generate` - Generate workflow from detection
- `/craft:ci:validate` - Validate existing CI against project
- `/craft:check ci` - Quick CI pre-flight check

**After detection:**
1. Review recommended template in CI-TEMPLATES.md
2. Copy template, adjust matrix/coverage as needed
3. Commit to `.github/workflows/test.yml`
