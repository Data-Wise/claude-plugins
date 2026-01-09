#!/bin/bash
# Crossref API wrapper for statistical research plugin
# Provides DOI lookup and metadata retrieval

# Configuration
CROSSREF_API_URL="https://api.crossref.org/works"
USER_AGENT="StatisticalResearchPlugin/1.0 (mailto:your-email@example.com)"

# Color output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Lookup DOI
# Usage: crossref_lookup_doi "10.1037/met0000310"
crossref_lookup_doi() {
    local doi="$1"

    if [[ -z "$doi" ]]; then
        echo -e "${RED}Error: DOI required${NC}" >&2
        return 1
    fi

    echo -e "${BLUE}Looking up DOI: ${YELLOW}$doi${NC}" >&2

    local url="${CROSSREF_API_URL}/${doi}"
    local response=$(curl -s -H "User-Agent: $USER_AGENT" "$url")

    if [[ $? -ne 0 ]]; then
        echo -e "${RED}Error: Failed to fetch from Crossref API${NC}" >&2
        return 1
    fi

    # Check for error
    if echo "$response" | jq -e '.status == "error"' > /dev/null 2>&1; then
        echo -e "${RED}Error: DOI not found${NC}" >&2
        return 1
    fi

    # Parse and display paper details
    echo "$response" | python3 -c "
import sys
import json

data = json.load(sys.stdin)
message = data.get('message', {})

# Extract metadata
title = message.get('title', ['Unknown'])[0]
authors = message.get('author', [])
author_names = [f\"{a.get('given', '')} {a.get('family', '')}\" for a in authors]
published = message.get('published', {}).get('date-parts', [[None]])[0]
container = message.get('container-title', ['Unknown'])[0]
volume = message.get('volume', 'N/A')
issue = message.get('issue', 'N/A')
pages = message.get('page', 'N/A')
doi = message.get('DOI', 'Unknown')

# Format published date
pub_year = published[0] if published and len(published) > 0 else 'Unknown'
pub_date = f\"{published[0]}-{published[1]:02d}\" if published and len(published) > 1 else str(pub_year)

print(f'Title: {title}')
print(f'Authors: {', '.join(author_names)}')
print(f'Journal: {container}')
print(f'Year: {pub_year}')
print(f'Volume: {volume}, Issue: {issue}')
print(f'Pages: {pages}')
print(f'DOI: {doi}')
"
}

# Get BibTeX citation
# Usage: crossref_get_bibtex "10.1037/met0000310"
crossref_get_bibtex() {
    local doi="$1"

    if [[ -z "$doi" ]]; then
        echo -e "${RED}Error: DOI required${NC}" >&2
        return 1
    fi

    echo -e "${BLUE}Fetching BibTeX for DOI: ${YELLOW}$doi${NC}" >&2

    local url="${CROSSREF_API_URL}/${doi}/transform/application/x-bibtex"
    local bibtex=$(curl -s -H "User-Agent: $USER_AGENT" "$url")

    if [[ $? -ne 0 ]]; then
        echo -e "${RED}Error: Failed to fetch BibTeX${NC}" >&2
        return 1
    fi

    echo "$bibtex"
}

# Search Crossref by query
# Usage: crossref_search "mediation analysis" [limit]
crossref_search() {
    local query="$1"
    local limit="${2:-10}"

    if [[ -z "$query" ]]; then
        echo -e "${RED}Error: Query required${NC}" >&2
        return 1
    fi

    echo -e "${BLUE}Searching Crossref for: ${YELLOW}$query${NC}" >&2

    # URL encode query
    local encoded_query=$(echo "$query" | sed 's/ /%20/g')
    local url="${CROSSREF_API_URL}?query=${encoded_query}&rows=${limit}"

    local response=$(curl -s -H "User-Agent: $USER_AGENT" "$url")

    if [[ $? -ne 0 ]]; then
        echo -e "${RED}Error: Failed to search Crossref${NC}" >&2
        return 1
    fi

    # Parse and display results
    echo "$response" | python3 -c "
import sys
import json

data = json.load(sys.stdin)
items = data.get('message', {}).get('items', [])

if not items:
    print('No results found', file=sys.stderr)
    sys.exit(0)

for i, item in enumerate(items, 1):
    title = item.get('title', ['Unknown'])[0]
    authors = item.get('author', [])
    author_names = [f\"{a.get('given', '')} {a.get('family', '')}\" for a in authors[:3]]
    more_authors = '...' if len(authors) > 3 else ''

    published = item.get('published', {}).get('date-parts', [[None]])[0]
    pub_year = published[0] if published and len(published) > 0 else 'Unknown'

    container = item.get('container-title', ['Unknown'])[0]
    doi = item.get('DOI', 'Unknown')

    print(f'{i}. {title}')
    print(f'   Authors: {', '.join(author_names)}{more_authors}')
    print(f'   Journal: {container}')
    print(f'   Year: {pub_year}')
    print(f'   DOI: {doi}')
    print()
"
}

# Get citation count (using Crossref metadata)
# Usage: crossref_citation_count "10.1037/met0000310"
crossref_citation_count() {
    local doi="$1"

    if [[ -z "$doi" ]]; then
        echo -e "${RED}Error: DOI required${NC}" >&2
        return 1
    fi

    echo -e "${BLUE}Fetching citation count for: ${YELLOW}$doi${NC}" >&2

    local url="${CROSSREF_API_URL}/${doi}"
    local response=$(curl -s -H "User-Agent: $USER_AGENT" "$url")

    if [[ $? -ne 0 ]]; then
        echo -e "${RED}Error: Failed to fetch citation data${NC}" >&2
        return 1
    fi

    echo "$response" | python3 -c "
import sys
import json

data = json.load(sys.stdin)
message = data.get('message', {})

title = message.get('title', ['Unknown'])[0]
cited_by = message.get('is-referenced-by-count', 0)

print(f'Title: {title}')
print(f'Cited by: {cited_by} works')
"
}

# Export functions
export -f crossref_lookup_doi
export -f crossref_get_bibtex
export -f crossref_search
export -f crossref_citation_count
