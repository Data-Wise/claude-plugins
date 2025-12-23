#!/bin/bash
# BibTeX utilities for statistical research plugin
# Search, add, and manage BibTeX entries

# Color output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Search .bib files for entries matching query
# Usage: bib_search "query" [bib_file]
bib_search() {
    local query="$1"
    local bib_file="$2"

    if [[ -z "$query" ]]; then
        echo -e "${RED}Error: Query required${NC}" >&2
        return 1
    fi

    # Find .bib files
    local bib_files=()
    if [[ -n "$bib_file" && -f "$bib_file" ]]; then
        bib_files=("$bib_file")
    else
        # Search in common locations
        local search_dirs=(
            "$HOME/Zotero/bibtex"
            "$HOME/Documents/references"
            "$PWD"
        )

        for dir in "${search_dirs[@]}"; do
            if [[ -d "$dir" ]]; then
                while IFS= read -r -d '' file; do
                    bib_files+=("$file")
                done < <(find "$dir" -name "*.bib" -type f -print0 2>/dev/null)
            fi
        done
    fi

    if [[ ${#bib_files[@]} -eq 0 ]]; then
        echo -e "${RED}Error: No .bib files found${NC}" >&2
        return 1
    fi

    echo -e "${BLUE}Searching ${#bib_files[@]} .bib file(s) for: ${YELLOW}$query${NC}" >&2
    echo

    # Search entries
    for file in "${bib_files[@]}"; do
        local matches=$(grep -i -B1 -A10 "@.*{.*," "$file" | grep -i "$query" -B1 -A10)

        if [[ -n "$matches" ]]; then
            echo -e "${CYAN}File: $file${NC}"
            echo "$matches" | python3 -c "
import sys
import re

content = sys.stdin.read()
# Find BibTeX entries
entries = re.findall(r'@(\w+)\{([^,]+),([^@]+)', content, re.MULTILINE | re.DOTALL)

for entry_type, cite_key, entry_body in entries:
    # Extract title
    title_match = re.search(r'title\s*=\s*[{\"]([^}\"]+)[}\"]', entry_body, re.IGNORECASE)
    title = title_match.group(1) if title_match else 'Unknown'

    # Extract author
    author_match = re.search(r'author\s*=\s*[{\"]([^}\"]+)[}\"]', entry_body, re.IGNORECASE)
    author = author_match.group(1) if author_match else 'Unknown'

    # Extract year
    year_match = re.search(r'year\s*=\s*[{\"]?(\d{4})[}\"]?', entry_body, re.IGNORECASE)
    year = year_match.group(1) if year_match else 'N/A'

    print(f'  @{entry_type}{{{cite_key},')
    print(f'    Title: {title}')
    print(f'    Author: {author}')
    print(f'    Year: {year}')
    print()
"
            echo
        fi
    done
}

# Add BibTeX entry to file
# Usage: bib_add <bib_file> <bibtex_entry>
bib_add() {
    local bib_file="$1"
    local bibtex_entry="$2"

    if [[ -z "$bib_file" || -z "$bibtex_entry" ]]; then
        echo -e "${RED}Error: BibTeX file and entry required${NC}" >&2
        return 1
    fi

    # Create file if it doesn't exist
    if [[ ! -f "$bib_file" ]]; then
        echo -e "${YELLOW}Creating new .bib file: $bib_file${NC}" >&2
        touch "$bib_file"
    fi

    # Extract cite key from entry
    local cite_key=$(echo "$bibtex_entry" | grep -o '@.*{[^,]*' | sed 's/@.*{//')

    # Check if entry already exists
    if grep -q "@.*{$cite_key," "$bib_file"; then
        echo -e "${YELLOW}Warning: Entry '$cite_key' already exists in $bib_file${NC}" >&2
        read -p "Overwrite? (y/N): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            echo -e "${BLUE}Skipped${NC}"
            return 0
        fi

        # Remove existing entry
        python3 -c "
import sys
import re

with open('$bib_file', 'r') as f:
    content = f.read()

# Remove entry
pattern = r'@\w+\{$cite_key,.*?\n\}'
content = re.sub(pattern, '', content, flags=re.MULTILINE | re.DOTALL)

with open('$bib_file', 'w') as f:
    f.write(content)
"
    fi

    # Append entry
    echo "" >> "$bib_file"
    echo "$bibtex_entry" >> "$bib_file"

    echo -e "${GREEN}✓ Added entry '$cite_key' to $bib_file${NC}"
}

# Format BibTeX file (clean up spacing, sort entries)
# Usage: bib_format <bib_file>
bib_format() {
    local bib_file="$1"

    if [[ -z "$bib_file" || ! -f "$bib_file" ]]; then
        echo -e "${RED}Error: Valid .bib file required${NC}" >&2
        return 1
    fi

    echo -e "${BLUE}Formatting $bib_file${NC}" >&2

    # Create backup
    cp "$bib_file" "${bib_file}.backup"

    # Format with Python
    python3 -c "
import sys
import re

with open('$bib_file', 'r') as f:
    content = f.read()

# Extract all entries
entries = re.findall(r'(@\w+\{[^@]+\})', content, re.MULTILINE | re.DOTALL)

# Sort entries by cite key
def get_cite_key(entry):
    match = re.search(r'@\w+\{([^,]+)', entry)
    return match.group(1).lower() if match else ''

sorted_entries = sorted(entries, key=get_cite_key)

# Write formatted file
with open('$bib_file', 'w') as f:
    for entry in sorted_entries:
        # Clean up entry
        entry = entry.strip()
        f.write(entry + '\n\n')

print(f'Formatted {len(sorted_entries)} entries', file=sys.stderr)
"

    echo -e "${GREEN}✓ Formatted (backup saved as ${bib_file}.backup)${NC}"
}

# List all entries in .bib file
# Usage: bib_list [bib_file]
bib_list() {
    local bib_file="$1"

    if [[ -n "$bib_file" && ! -f "$bib_file" ]]; then
        echo -e "${RED}Error: File not found: $bib_file${NC}" >&2
        return 1
    fi

    # Find .bib files if none specified
    local bib_files=()
    if [[ -n "$bib_file" ]]; then
        bib_files=("$bib_file")
    else
        local search_dirs=(
            "$HOME/Zotero/bibtex"
            "$HOME/Documents/references"
            "$PWD"
        )

        for dir in "${search_dirs[@]}"; do
            if [[ -d "$dir" ]]; then
                while IFS= read -r -d '' file; do
                    bib_files+=("$file")
                done < <(find "$dir" -name "*.bib" -type f -print0 2>/dev/null)
            fi
        done
    fi

    if [[ ${#bib_files[@]} -eq 0 ]]; then
        echo -e "${RED}Error: No .bib files found${NC}" >&2
        return 1
    fi

    for file in "${bib_files[@]}"; do
        echo -e "${CYAN}File: $file${NC}"

        grep -o '@.*{[^,]*' "$file" | sed 's/@\(.*\){\(.*\)/  \2 (\1)/'

        echo
    done
}

# Export functions
export -f bib_search
export -f bib_add
export -f bib_format
export -f bib_list
