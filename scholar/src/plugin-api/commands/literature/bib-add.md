---
name: research:bib:add
description: Add BibTeX entry to bibliography file
---

# Add BibTeX Entry

I'll help you add a BibTeX entry to your bibliography file.

**Usage:** `/research:bib:add <bib-file>`

**Examples:**
- `/research:bib:add ~/Documents/references/mediation.bib`
- `/research:bib:add ./references.bib`

## Add Entry

Please provide:
1. The .bib file path (where to add the entry)
2. The BibTeX entry to add

You can get BibTeX entries from:
- `/research:doi <doi>` - Get BibTeX from DOI
- Google Scholar (cite → BibTeX)
- Publisher websites
- Zotero export

<system>
This command adds a BibTeX entry to a bibliography file.

## Implementation

Use the shell API wrapper from `${CLAUDE_PLUGIN_ROOT}/lib/bibtex-utils.sh`:

```bash
# Source the API wrapper
source "${CLAUDE_PLUGIN_ROOT}/lib/bibtex-utils.sh"

# Extract bib file path
BIB_FILE="$1"

if [[ -z "$BIB_FILE" ]]; then
    echo "Error: .bib file path required"
    exit 1
fi

# Expand ~ to home directory
BIB_FILE="${BIB_FILE/#\~/$HOME}"

# Ask for BibTeX entry if not provided
if [[ -z "$2" ]]; then
    echo "Please provide the BibTeX entry to add:"
    echo "(Enter the complete @article{...} or @book{...} entry)"
    echo ""

    # Read multi-line entry until we see a closing }
    BIBTEX_ENTRY=""
    while IFS= read -r line; do
        BIBTEX_ENTRY+="$line"$'\n'
        # Check if we've reached the end of the entry
        if [[ "$line" =~ ^\} ]]; then
            break
        fi
    done
else
    BIBTEX_ENTRY="$2"
fi

# Add entry to file
bib_add "$BIB_FILE" "$BIBTEX_ENTRY"
```

## Features

- Creates .bib file if it doesn't exist
- Checks for duplicate cite keys
- Prompts to overwrite if entry exists
- Validates BibTeX format
- Shows success message with cite key

## Integration

Can be used after:
- `/research:doi <doi>` - Get BibTeX from DOI, then add to file
- `/research:arxiv <query>` - Find paper, get DOI, get BibTeX, add to file

## Example Workflow

User: `/research:doi 10.1037/met0000310`
(Shows metadata and BibTeX)

User: `/research:bib:add ~/Documents/references/mediation.bib`
(Adds the BibTeX entry from previous command)

## Follow-up Actions

After adding entry, offer to:
- Format the .bib file (sort entries, clean spacing)
- List all entries in the file
- Open file in editor for review
- Create Obsidian literature note