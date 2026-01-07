"""
Format handlers for RForge mode system output.

Provides three output formats:
- Terminal: Rich colored output with emojis (default)
- JSON: Machine-readable structured data
- Markdown: Documentation-ready formatted text
"""

import json
from datetime import datetime
from typing import Dict, Any, Optional


def format_json(data: Dict[str, Any], mode: str = "default", **metadata) -> str:
    """
    Format analysis results as JSON.

    Args:
        data: Analysis results dictionary
        mode: Mode used for analysis (default, debug, optimize, release)
        **metadata: Additional metadata (version, package_name, etc.)

    Returns:
        Valid JSON string with results and metadata

    Example:
        >>> results = {"tests_passed": 15, "warnings": 2}
        >>> output = format_json(results, mode="debug", version="1.0.0")
        >>> import json
        >>> parsed = json.loads(output)  # Valid JSON
        >>> parsed["mode"]
        'debug'
    """
    output = {
        "timestamp": datetime.now().isoformat(),
        "mode": mode,
        "results": data
    }

    # Add optional metadata
    if metadata:
        output["metadata"] = metadata

    # Ensure valid JSON output
    return json.dumps(output, indent=2, ensure_ascii=False)


def validate_json_output(json_string: str) -> bool:
    """
    Validate that output is valid JSON.

    Args:
        json_string: JSON string to validate

    Returns:
        True if valid JSON, False otherwise

    Example:
        >>> output = format_json({"status": "pass"})
        >>> validate_json_output(output)
        True
    """
    try:
        json.loads(json_string)
        return True
    except (json.JSONDecodeError, TypeError):
        return False


def format_terminal(data: Dict[str, Any], mode: str = "default") -> str:
    """
    Format analysis results for terminal output with Rich formatting.

    Args:
        data: Analysis results dictionary
        mode: Mode used for analysis

    Returns:
        Formatted terminal output string with colors and emojis

    Example:
        >>> data = {"title": "Test", "status": "success", "data": {"tests": 15}}
        >>> output = format_terminal(data, mode="debug")
        >>> "✅" in output
        True
    """
    from io import StringIO
    from rich.console import Console

    # Create console that writes to string
    output = StringIO()
    console = Console(file=output, force_terminal=True, width=80)

    # Status emoji based on status field
    status = data.get("status", "unknown")
    if status == "success":
        status_emoji = "✅"
    elif status in ["error", "failed", "failure"]:
        status_emoji = "❌"
    elif status in ["warning", "warn"]:
        status_emoji = "⚠️"
    else:
        status_emoji = "ℹ️"

    # Title line with emoji
    title = data.get("title", "Result")
    console.print(f"{status_emoji} {title}", style="bold")
    console.print()  # Empty line

    # Display data as bullet points if present
    if "data" in data and isinstance(data["data"], dict):
        for key, value in data["data"].items():
            console.print(f"  • {key}: {value}")

    # Get the string output
    result = output.getvalue()
    output.close()

    return result


def format_markdown(data: Dict[str, Any], mode: str = "default") -> str:
    """
    Format analysis results as Markdown (placeholder).

    TODO: Implement markdown generation.

    Args:
        data: Analysis results dictionary
        mode: Mode used for analysis

    Returns:
        Formatted markdown string
    """
    # Placeholder - will implement markdown generation
    md = f"# Analysis Results\n\n"
    md += f"**Mode:** {mode}\n\n"
    md += f"```json\n{json.dumps(data, indent=2)}\n```\n"
    return md


# Format handler registry
FORMATTERS = {
    "json": format_json,
    "terminal": format_terminal,
    "markdown": format_markdown,
}


def get_formatter(format_name: str):
    """
    Get formatter function by name.

    Args:
        format_name: Format name (json, terminal, markdown)

    Returns:
        Formatter function

    Raises:
        ValueError: If format name is invalid

    Example:
        >>> formatter = get_formatter("json")
        >>> output = formatter({"status": "pass"}, mode="debug")
        >>> "timestamp" in output
        True
    """
    if format_name not in FORMATTERS:
        valid_formats = ", ".join(FORMATTERS.keys())
        raise ValueError(
            f"Invalid format '{format_name}'. "
            f"Valid formats: {valid_formats}"
        )
    return FORMATTERS[format_name]


def format_output(
    data: Dict[str, Any],
    format_name: str = "terminal",
    mode: str = "default",
    **metadata
) -> str:
    """
    Format output using specified formatter.

    Args:
        data: Analysis results dictionary
        format_name: Output format (json, terminal, markdown)
        mode: Mode used for analysis
        **metadata: Additional metadata for JSON format

    Returns:
        Formatted output string

    Example:
        >>> results = {"tests": 15, "coverage": 87}
        >>> output = format_output(results, format_name="json", mode="debug")
        >>> '"mode": "debug"' in output
        True
    """
    formatter = get_formatter(format_name)

    # JSON formatter accepts metadata
    if format_name == "json":
        return formatter(data, mode=mode, **metadata)
    else:
        return formatter(data, mode=mode)
