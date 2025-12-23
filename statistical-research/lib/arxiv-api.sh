#!/bin/bash
# arXiv API wrapper for statistical research plugin
# Provides search and fetch capabilities for arXiv papers

# Configuration
ARXIV_API_URL="http://export.arxiv.org/api/query"
RESULTS_LIMIT=10

# Color output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Search arXiv papers
# Usage: arxiv_search "query" [limit]
arxiv_search() {
    local query="$1"
    local limit="${2:-$RESULTS_LIMIT}"

    if [[ -z "$query" ]]; then
        echo -e "${RED}Error: Query required${NC}" >&2
        return 1
    fi

    echo -e "${BLUE}Searching arXiv for: ${YELLOW}$query${NC}" >&2

    # URL encode the query
    local encoded_query=$(echo "$query" | sed 's/ /+/g')

    # Build API URL
    local url="${ARXIV_API_URL}?search_query=all:${encoded_query}&start=0&max_results=${limit}&sortBy=relevance&sortOrder=descending"

    # Fetch results
    local response=$(curl -s "$url")

    if [[ $? -ne 0 ]]; then
        echo -e "${RED}Error: Failed to fetch from arXiv API${NC}" >&2
        return 1
    fi

    # Parse XML response
    echo "$response" | python3 -c "
import sys
import xml.etree.ElementTree as ET
from datetime import datetime

xml_data = sys.stdin.read()
try:
    root = ET.fromstring(xml_data)
    # Define namespaces
    ns = {
        'atom': 'http://www.w3.org/2005/Atom',
        'arxiv': 'http://arxiv.org/schemas/atom'
    }

    entries = root.findall('atom:entry', ns)

    if not entries:
        print('No results found', file=sys.stderr)
        sys.exit(0)

    for i, entry in enumerate(entries, 1):
        title = entry.find('atom:title', ns).text.strip().replace('\n', ' ')
        authors = [a.find('atom:name', ns).text for a in entry.findall('atom:author', ns)]
        published = entry.find('atom:published', ns).text[:10]  # YYYY-MM-DD
        arxiv_id = entry.find('atom:id', ns).text.split('/')[-1]
        summary = entry.find('atom:summary', ns).text.strip().replace('\n', ' ')[:200] + '...'

        print(f'{i}. {title}')
        print(f'   Authors: {', '.join(authors[:3])}{'...' if len(authors) > 3 else ''}')
        print(f'   arXiv ID: {arxiv_id}')
        print(f'   Published: {published}')
        print(f'   Summary: {summary}')
        print()

except ET.ParseError as e:
    print(f'Error parsing XML: {e}', file=sys.stderr)
    sys.exit(1)
"
}

# Get paper details by arXiv ID
# Usage: arxiv_get_paper "2301.12345"
arxiv_get_paper() {
    local arxiv_id="$1"

    if [[ -z "$arxiv_id" ]]; then
        echo -e "${RED}Error: arXiv ID required${NC}" >&2
        return 1
    fi

    echo -e "${BLUE}Fetching arXiv paper: ${YELLOW}$arxiv_id${NC}" >&2

    local url="${ARXIV_API_URL}?id_list=${arxiv_id}"
    local response=$(curl -s "$url")

    if [[ $? -ne 0 ]]; then
        echo -e "${RED}Error: Failed to fetch from arXiv API${NC}" >&2
        return 1
    fi

    # Parse and display paper details
    echo "$response" | python3 -c "
import sys
import xml.etree.ElementTree as ET

xml_data = sys.stdin.read()
try:
    root = ET.fromstring(xml_data)
    ns = {
        'atom': 'http://www.w3.org/2005/Atom',
        'arxiv': 'http://arxiv.org/schemas/atom'
    }

    entry = root.find('atom:entry', ns)
    if entry is None:
        print('Paper not found', file=sys.stderr)
        sys.exit(1)

    title = entry.find('atom:title', ns).text.strip().replace('\n', ' ')
    authors = [a.find('atom:name', ns).text for a in entry.findall('atom:author', ns)]
    published = entry.find('atom:published', ns).text[:10]
    updated = entry.find('atom:updated', ns).text[:10]
    summary = entry.find('atom:summary', ns).text.strip()
    pdf_link = entry.find('atom:link[@title=\"pdf\"]', ns).attrib['href']

    # Get categories
    categories = [c.attrib['term'] for c in entry.findall('atom:category', ns)]

    print(f'Title: {title}')
    print(f'Authors: {', '.join(authors)}')
    print(f'Published: {published}')
    print(f'Updated: {updated}')
    print(f'Categories: {', '.join(categories)}')
    print(f'PDF: {pdf_link}')
    print()
    print('Abstract:')
    print(summary)

except ET.ParseError as e:
    print(f'Error parsing XML: {e}', file=sys.stderr)
    sys.exit(1)
"
}

# Download PDF
# Usage: arxiv_download_pdf "2301.12345" [output_dir]
arxiv_download_pdf() {
    local arxiv_id="$1"
    local output_dir="${2:-.}"

    if [[ -z "$arxiv_id" ]]; then
        echo -e "${RED}Error: arXiv ID required${NC}" >&2
        return 1
    fi

    local pdf_url="https://arxiv.org/pdf/${arxiv_id}.pdf"
    local output_file="${output_dir}/${arxiv_id}.pdf"

    echo -e "${BLUE}Downloading PDF: ${YELLOW}$arxiv_id${NC}" >&2

    if curl -L -o "$output_file" "$pdf_url" 2>&1 | grep -q "200"; then
        echo -e "${GREEN}✓ Downloaded: $output_file${NC}" >&2
        echo "$output_file"
    else
        echo -e "${RED}Error: Failed to download PDF${NC}" >&2
        return 1
    fi
}

# Export functions
export -f arxiv_search
export -f arxiv_get_paper
export -f arxiv_download_pdf
