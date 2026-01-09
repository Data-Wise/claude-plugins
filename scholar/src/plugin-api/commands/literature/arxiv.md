---
name: research:arxiv
description: Search arXiv for papers
---

# Search arXiv

I'll help you search arXiv for relevant papers.

**Usage:** `/research:arxiv <query>` or `/research:arxiv <query> [limit]`

**Examples:**
- `/research:arxiv "bootstrap mediation analysis"`
- `/research:arxiv "causal inference" 20`

## What would you like to search for?

If you provided a query, I'll search arXiv now. Otherwise, please provide your search query.

<system>
This command searches arXiv for papers matching the user's query using the arXiv API wrapper.

## Implementation

Use the shell API wrapper from `${CLAUDE_PLUGIN_ROOT}/lib/arxiv-api.sh`:

```bash
# Source the API wrapper
source "${CLAUDE_PLUGIN_ROOT}/lib/arxiv-api.sh"

# Extract query from args
QUERY="$@"
LIMIT=10

# If last arg is a number, use it as limit
if [[ "$*" =~ [0-9]+$ ]]; then
    LIMIT="${@: -1}"
    QUERY="${@:1:$(($#-1))}"
fi

# Search arXiv
arxiv_search "$QUERY" "$LIMIT"
```

## Output Format

The command will display:
1. Paper title
2. Authors (up to 3, with "..." if more)
3. arXiv ID
4. Publication date
5. Brief abstract (first 200 chars)

## Follow-up Actions

After showing results, offer to:
- Get full details for a specific paper (using arXiv ID)
- Download PDF for a paper
- Add BibTeX entry to bibliography file
- Search for related papers

## Example Interaction

User: `/research:arxiv "bootstrap mediation"`