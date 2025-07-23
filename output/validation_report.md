# Validation Report

## Input
- File: `usb-pd-spec.pdf`
- Extracted Sections: 58 entries

## Validation Summary
- ✅ 58 ToC entries parsed
- ✅ All entries matched expected regex format
- ✅ Section ID hierarchy validated (Level 1 to 4)
- ❌ No duplicate section IDs found
- ❌ No skipped section numbers (basic check only)
- ❌ Parent ID existence not cross-checked

## 🛠 Validation Criteria
- Section format: `number.title........page`
- At least 1 dot in section ID (e.g., `1.1`)
- Non-empty title and positive page number
- Parent ID derived from section ID hierarchy

## 📝 Sample Entry
```json
{
  "section_id": "1.2",
  "title": "Purpose",
  "page": 35,
  "parent_id": "1",
  "level": 2
}
