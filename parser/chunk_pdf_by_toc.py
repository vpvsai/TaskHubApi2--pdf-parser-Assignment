import pdfplumber
import json
import os

def load_toc(toc_file):
    with open(toc_file, 'r', encoding='utf-8') as f:
        return [json.loads(line) for line in f]

def save_chunks(chunks, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        for chunk in chunks:
            f.write(json.dumps(chunk) + '\n')

def extract_section_text(pdf, start_page, end_page):
    pages = pdf.pages[start_page:end_page]
    text = ''
    for page in pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + '\n'
    return text.strip()

def chunk_pdf_by_toc(pdf_path, toc):
    chunks = []
    with pdfplumber.open(pdf_path) as pdf:
        for i, entry in enumerate(toc):
            start = entry['page'] - 1  # 0-indexed
            if i + 1 < len(toc):
                end = toc[i + 1]['page'] - 1
            else:
                end = len(pdf.pages)

            section_text = extract_section_text(pdf, start, end)

            chunk = entry.copy()
            chunk['text'] = section_text
            chunks.append(chunk)

    return chunks

if __name__ == "__main__":
    input_pdf = os.path.join("pdfs", "usb-pd-spec.pdf")
    toc_file = os.path.join("output", "usb_pd_spec.jsonl")
    output_file = os.path.join("output", "usb_pd_chunks.jsonl")

    toc_entries = load_toc(toc_file)
    chunks = chunk_pdf_by_toc(input_pdf, toc_entries)
    save_chunks(chunks, output_file)

    print(f"✅ Done! Chunked {len(chunks)} sections from the PDF.")
    print(f"📄 Output saved to {output_file}")
