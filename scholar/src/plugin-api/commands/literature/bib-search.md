---
name: research:bib:search
description: Search BibTeX files for entries
---

# Search BibTeX Files

I'll search your BibTeX files for entries matching your query.

**Usage:** `/research:bib:search <query>` or `/research:bib:search <query> <bib-file>`

**Examples:**
- `/research:bib:search "mediation"`
- `/research:bib:search "MacKinnon" ~/Documents/references/mediation.bib`

## What would you like to search for?

If you provided a query, I'll search now. Otherwise, please provide your search query.

<system>
This command searches BibTeX files for entries matching the user's query.

## Implementation

Use the shell API wrapper from `${CLAUDE_PLUGIN_ROOT}/lib/bibtex-utils.sh`:

```bash
# Source the API wrapper
source "${CLAUDE_PLUGIN_ROOT}/lib/bibtex-utils.sh"

# Extract query and optional file path
QUERY="$1"
BIB_FILE="${2:-}"

if [[ -z "$QUERY" ]]; then
    echo "Error: Search query required"
    exit 1
fi

# Search BibTeX files
if [[ -n "$BIB_FILE" ]]; then
    bib_search "$QUERY" "$BIB_FILE"
else
    bib_search "$QUERY"
fi
```

## Search Locations

If no specific .bib file is provided, searches in:
1. `$HOME/Zotero/bibtex/`
2. `$HOME/Documents/references/`
3. Current working directory

## Output Format

For each match, displays:
1. BibTeX entry type (article, book, inproceedings, etc.)
2. Cite key
3. Title
4. Author(s)
5. Year

## Follow-up Actions

After showing results, offer to:
- View full BibTeX entry
- Copy cite key to clipboard
- Export to new .bib file
- Get full paper metadata from DOI (if available)
- Add notes to Obsidian vault

## Example Interaction

User: `/research:bib:search "MacKinnon"`