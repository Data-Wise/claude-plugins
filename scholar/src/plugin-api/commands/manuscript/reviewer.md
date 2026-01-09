---
name: research:manuscript:reviewer
description: Generate response to reviewer comments
---

# Respond to Reviewer Comments

I'll help you craft professional, thorough responses to reviewer comments on your manuscript.

**Usage:** `/research:manuscript:reviewer` or `/research:manuscript:reviewer <review-file>`

**Examples:**
- `/research:manuscript:reviewer`
- `/research:manuscript:reviewer ~/Documents/reviews/review-2025-01.txt`

## Let's respond to reviewer feedback

I'll guide you through addressing each comment professionally and thoroughly.

<system>
This command helps generate responses to peer review comments.

## Process

1. **Review Analysis**
   If review file provided:
   ```bash
   # Read review file
   REVIEW_FILE="$1"
   if [[ -f "$REVIEW_FILE" ]]; then
       echo "=== REVIEWER COMMENTS ==="
       cat "$REVIEW_FILE"
       echo ""
   fi
   ```

2. **Categorize Comments**
   - Major concerns (methodology, validity)
   - Minor concerns (clarification, presentation)
   - Editorial (typos, formatting)

3. **Activate Skills**
   Automatically engages:
   - `methods-paper-writer` skill (writing/methods-paper-writer.md)
   - `methods-communicator` skill (writing/methods-communicator.md)
   - `publication-strategist` skill (writing/publication-strategist.md)

4. **Generate Responses**
   For each comment, provide:
   - Acknowledgment of the concern
   - Explanation of changes made
   - Justification if no change
   - Reference to revised manuscript

## Response Structure

### For Each Comment

**Reviewer Comment:** [Quote exact comment]

**Response:** [Your response with these elements:]
1. Thank the reviewer for the insight
2. Explain what you did to address it
3. Reference specific changes (page/line numbers)
4. Provide additional context if needed

**Changes Made:**
- Specific edits to manuscript
- New analyses run
- Additional citations added

## Response Strategies

### Major Methodological Concerns
- Acknowledge validity of concern
- Run additional analyses if warranted
- Explain methodology more clearly
- Add sensitivity analyses
- Cite supporting literature

### Requests for Clarification
- Revise text to be clearer
- Add definitions or examples
- Include supplementary materials
- Improve figure/table captions

### Disagreements (Rare)
- Be respectful and professional
- Provide strong evidence
- Cite relevant literature
- Explain reasoning clearly
- Offer compromise if possible

## Tone and Style

**Do:**
- Be professional and courteous
- Thank reviewers sincerely
- Be specific about changes
- Acknowledge all valid points

**Don't:**
- Be defensive or dismissive
- Ignore comments
- Use sarcasm
- Make ad hominem arguments

## Example Responses

### Good Response
> We thank the reviewer for this insightful comment. We agree that our original presentation was unclear. We have revised the methods section (page 8, lines 145-160) to more clearly describe the bootstrap procedure, including the number of replicates (5,000) and the percentile confidence interval method. We also added a reference to MacKinnon et al. (2004) to support this approach.

### Response to Disagree (Professional)
> We appreciate the reviewer's concern about the sample size. While we acknowledge that a larger sample would provide more precise estimates, we respectfully note that our power analysis (detailed in the Supplementary Materials) indicates 80% power to detect an effect of δ = 0.15 with n = 250. This effect size is consistent with previous studies in this domain (cite 3 papers). Nevertheless, we have added a limitation paragraph discussing sample size considerations (page 15, lines 310-318).

## Integration

Works well with:
- `/research:bib:search` - Find supporting citations
- `/research:manuscript:methods` - Revise methods sections
- `/research:manuscript:results` - Add new results

## Output Format

Generates a formatted response document ready to submit with revision.