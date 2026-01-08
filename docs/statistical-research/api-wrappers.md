# Statistical Research API Wrappers

Lightweight shell-based API wrappers for research tools. Pure shell implementation with no MCP dependencies.

## Overview

Statistical Research uses shell-based APIs for:
- **arXiv search** - Academic paper discovery
- **Crossref API** - DOI resolution and metadata
- **BibTeX utilities** - Bibliography management

**Benefits:**
- No MCP server overhead
- Fast startup (<100ms)
- Easy to maintain and extend
- Shell-scriptable workflows

## arXiv API

Location: `lib/arxiv-api.sh`

### Functions

**search_arxiv(query, max_results)**
Search arXiv for papers.

```bash
# Usage
source "${CLAUDE_PLUGIN_ROOT}/lib/arxiv-api.sh"
search_arxiv "causal mediation" 10
```

**get_arxiv_pdf(arxiv_id, output_path)**
Download PDF from arXiv.

```bash
get_arxiv_pdf "2301.12345" "paper.pdf"
```

**parse_arxiv_metadata(xml_response)**
Extract metadata from arXiv XML.

### API Endpoints

- Search: `http://export.arxiv.org/api/query`
- PDF: `https://arxiv.org/pdf/{arxiv_id}.pdf`

### Rate Limiting

- Max 3 requests per second
- Automatic backoff on 429 errors
- Respects arXiv API guidelines

## Crossref API

Location: `lib/crossref-api.sh`

### Functions

**lookup_doi(doi)**
Resolve DOI to metadata.

```bash
source "${CLAUDE_PLUGIN_ROOT}/lib/crossref-api.sh"
lookup_doi "10.1080/01621459.2020.1765785"
```

**doi_to_bibtex(doi)**
Convert DOI to BibTeX entry.

```bash
doi_to_bibtex "10.1080/01621459.2020.1765785"
```

**search_crossref(query, filter)**
Search Crossref database.

```bash
search_crossref "mediation analysis" "type:journal-article"
```

### API Endpoints

- Works: `https://api.crossref.org/works/{doi}`
- Search: `https://api.crossref.org/works?query={query}`

### Rate Limiting

- Polite pool: 50 requests/second with mailto
- Public pool: 1 request/second
- Set User-Agent with contact email

## BibTeX Utilities

Location: `lib/bibtex-utils.sh`

### Functions

**search_bibtex(pattern, bibfile)**
Search BibTeX files for entries.

```bash
source "${CLAUDE_PLUGIN_ROOT}/lib/bibtex-utils.sh"
search_bibtex "Pearl" references.bib
```

**add_bibtex_entry(entry_file, target_bib)**
Add entry to bibliography.

```bash
add_bibtex_entry new_entry.bib references.bib
```

**validate_bibtex(bibfile)**
Validate BibTeX syntax.

```bash
validate_bibtex references.bib
```

**format_bibtex(bibfile, style)**
Format BibTeX entries.

```bash
format_bibtex references.bib "apalike"
```

**extract_citations(tex_file)**
Extract citations from LaTeX.

```bash
extract_citations manuscript.tex
```

### Supported Operations

- Entry parsing
- Duplicate detection
- Field extraction
- Citation key generation
- Format validation

## Usage Examples

### Complete Literature Search Workflow

```bash
# 1. Search arXiv
/research:arxiv "causal mediation bootstrap"

# 2. Get DOI from result
doi="10.1080/01621459.2020.1765785"

# 3. Get BibTeX
/research:doi "$doi"

# 4. Add to bibliography
echo "@article{..." > entry.bib
/research:bib:add entry.bib references.bib

# 5. Validate
source "${CLAUDE_PLUGIN_ROOT}/lib/bibtex-utils.sh"
validate_bibtex references.bib
```

### Automated Bibliography Management

```bash
#!/bin/bash
# Update bibliography from DOI list

while read doi; do
    # Get BibTeX
    entry=$(doi_to_bibtex "$doi")

    # Add to main bibliography
    echo "$entry" | add_bibtex_entry - references.bib

    # Rate limit
    sleep 0.5
done < dois.txt
```

## Error Handling

All API wrappers implement robust error handling:

```bash
# Check API availability
if ! curl -s "https://export.arxiv.org/api/query" >/dev/null; then
    echo "arXiv API unavailable"
    exit 1
fi

# Handle rate limits
if [[ $http_code == "429" ]]; then
    sleep "$retry_after"
    retry_request
fi

# Validate responses
if ! echo "$response" | grep -q "<entry>"; then
    echo "No results found"
    return 1
fi
```

## Extending APIs

### Adding New API

1. Create `lib/new-api.sh`
2. Implement core functions
3. Add error handling
4. Document usage
5. Update command to use API

**Template:**
```bash
#!/bin/bash
# new-api.sh - API wrapper for [service]

API_BASE="https://api.example.com"
RATE_LIMIT=3  # requests per second

function api_function() {
    local param="$1"

    # Rate limiting
    sleep $(echo "scale=2; 1/$RATE_LIMIT" | bc)

    # Make request
    local response=$(curl -s "${API_BASE}/endpoint?q=${param}")

    # Error handling
    if [[ $? -ne 0 ]]; then
        echo "API request failed"
        return 1
    fi

    # Parse and return
    echo "$response" | jq '.data'
}
```

## Performance

- **arXiv search:** ~500ms per query
- **DOI lookup:** ~300ms per DOI
- **BibTeX operations:** <50ms (local)
- **Startup overhead:** <100ms

## Dependencies

**Required:**
- `curl` - HTTP requests
- `jq` - JSON parsing
- `grep` - Text search

**Optional:**
- `bibtool` - Advanced BibTeX operations
- `bibclean` - BibTeX validation

## See Also

- **[Commands Reference](commands.md)** - 14 commands
- **[Skills Guide](skills.md)** - 17 skills
- **[Examples](examples.md)** - Usage examples

---

**Last Updated:** 2026-01-09
**Document Version:** v1.1.0
**Status:** ✅ Production ready - Shell-based APIs with no MCP dependencies
