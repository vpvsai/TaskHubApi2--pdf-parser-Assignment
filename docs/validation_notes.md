# Validation Use Cases – Notes

## Use Cases Handled in `validate_toc.py`
- Section IDs follow numeric format (e.g., `1`, `1.2`, `2.3.4`)
- Section titles are non-empty and appear between dots and page numbers
- Page numbers are positive integers
- Parent-child relationship is inferred from dot structure (`1.2` → parent: `1`)
- Basic level-depth detection (based on number of dots)

## Use Cases Not Yet Handled (Suggestions for Improvement)
- Detect duplicate section IDs
- Detect non-sequential section numbering (e.g., `1`, `1.2`, `1.4` without `1.3`)
- Ensure title content does not contain special characters (validation)
- Validate page numbers against actual page count in the PDF
- Check for missing parent sections
- Validate consistent indentation levels visually (not just numerically)
- Warn on suspicious or malformed ToC lines that don’t match expected pattern
