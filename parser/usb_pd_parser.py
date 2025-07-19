import pdfplumber
import re
import json
import os

def extract_toc(pdf_path):
    toc = []
    doc_title = "USB Power Delivery Specification Rev X"

    with pdfplumber.open(pdf_path) as pdf:
        for page_num in range(0, 20):  # look in first 10 pages
            page = pdf.pages[page_num]
            text = page.extract_text()
            if not text:
                continue


            lines = text.split('\n')
            print(f"\n📄 Page {page_num + 1}")
            for line in lines:
                print(line)
            for line in lines:
                match = re.match(r'^(\d+(?:\.\d+)*?)\s+(.*?)\.{3,}\s+(\d+)$', line.strip())

                if match:
                    print("✅ MATCHED:", line)  # Optional debug

                    section_id = match.group(1)
                    title = match.group(2).strip()

                    if title.startswith(section_id):
                        title = title[len(section_id):].strip(" .-")

                    page_number = int(match.group(3))
                    level = section_id.count('.') + 1
                    parent_id = '.'.join(section_id.split('.')[:-1]) if '.' in section_id else None
                    full_path = f"{section_id} {title}"

                    toc.append({
                        "doc_title": doc_title,
                        "section_id": section_id,
                        "title": title,
                        "page": page_number,
                        "level": level,
                        "parent_id": parent_id,
                        "full_path": full_path,
                        "tags": []
                    })


    return toc

def save_as_jsonl(data, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        for entry in data:
            f.write(json.dumps(entry) + '\n')

if __name__ == "__main__":
    input_pdf = os.path.join("pdfs", "usb-pd-spec.pdf")
    output_file = os.path.join("output", "usb_pd_spec.jsonl")

    toc_entries = extract_toc(input_pdf)
    save_as_jsonl(toc_entries, output_file)
    print(f"✅ Done! Extracted {len(toc_entries)} ToC entries.")

    # Optional: View first few entries
    print("\n🔍 Sample ToC Entries:")
    for entry in toc_entries[:5]:
        print(json.dumps(entry, indent=2))
