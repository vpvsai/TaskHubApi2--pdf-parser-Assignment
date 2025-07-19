import pdfplumber
import re
import json
import os

def extract_sections(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        all_text = ""
        for page in pdf.pages:
            all_text += page.extract_text() + "\n"

    # Split into lines
    lines = all_text.split('\n')

    sections = []
    current_section = None

    for line in lines:
        line = line.strip()
        match = re.match(r'^(\d+(?:\.\d+)*)(?:\s+)(.+)', line)
        if match:
            # Start of a new section
            if current_section:
                sections.append(current_section)

            section_id = match.group(1)
            title = match.group(2)
            current_section = {
                "section_id": section_id,
                "title": title,
                "content": ""
            }
        elif current_section:
            # Continuation of current section
            current_section["content"] += line + "\n"

    if current_section:
        sections.append(current_section)

    return sections

def save_sections(sections, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        for s in sections:
            f.write(json.dumps(s) + '\n')

if __name__ == "__main__":
    input_pdf = os.path.join("pdfs", "usb-pd-spec.pdf")
    output_file = os.path.join("output", "usb_pd_chunks.jsonl")

    sections = extract_sections(input_pdf)
    save_sections(sections, output_file)

    print(f"✅ Chunked and saved {len(sections)} sections from the PDF.")
