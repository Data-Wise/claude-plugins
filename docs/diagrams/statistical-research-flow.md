# Statistical Research Command Flow

**Auto-generated:** 2025-12-23 21:52:13

## Example Command Execution

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude Code
    participant Plugin as statistical-research
    participant Tools as Research Tools

    User->>Claude: /research:arxiv "mediation"
    Claude->>Plugin: Execute command
    Plugin->>Tools: Search arXiv API
    Tools-->>Plugin: Paper results
    Plugin->>Plugin: Format results
    Plugin-->>Claude: Formatted papers
    Claude-->>User: Display papers with metadata
```
