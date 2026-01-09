---
name: research:doi
description: Look up paper metadata by DOI
---

# DOI Lookup

I'll retrieve metadata for a paper using its DOI (Digital Object Identifier).

**Usage:** `/research:doi <doi>`

**Examples:**
- `/research:doi 10.1037/met0000310`
- `/research:doi 10.1080/00273171.2017.1354758`

## What DOI would you like to look up?

If you provided a DOI, I'll fetch the metadata now. Otherwise, please provide the DOI.

<system>
This command looks up paper metadata using the Crossref API via the shell wrapper.

## Implementation

Use the shell API wrapper from `${CLAUDE_PLUGIN_ROOT}/lib/crossref-api.sh`:

```bash
# Source the API wrapper
source "${CLAUDE_PLUGIN_ROOT}/lib/crossref-api.sh"

# Extract DOI from args
DOI="$1"

# Validate DOI format
if [[ ! "$DOI" =~ ^10\. ]]; then
    echo "Error: Invalid DOI format. DOI should start with '10.'"
    exit 1
fi

# Look up DOI
crossref_lookup_doi "$DOI"
```

## Output Format

The command will display:
1. Title
2. Authors (full list)
3. Journal/Container
4. Publication year
5. Volume, Issue
6. Pages
7. DOI

## Follow-up Actions

After showing metadata, offer to:
- Get BibTeX citation (`crossref_get_bibtex "$DOI"`)
- Check citation count (`crossref_citation_count "$DOI"`)
- Add to bibliography file
- Search for related papers
- Download PDF (if available via DOI resolver)

## Example Interaction

User: `/research:doi 10.1037/met0000310`