#  USB Power Delivery Spec Analyzer (Python Project)

This project parses the USB Power Delivery (USB-PD) Specification PDF, extracts the **Table of Contents**, chunks the content by sections, and lets you **ask questions** about the document from your terminal.

---

##  Folder Structure

```
TaskHubApi2/
├── parser/
│   ├── usb_pd_parser.py           # Extract ToC from PDF
│   ├── chunk_pdf_by_toc.py        # Chunk PDF into sections
│   ├── qa_from_chunks.py          # Question-answer interface
├── pdfs/
│   └── usb-pd-spec.pdf            # Input PDF
├── output/
│   ├── usb_pd_spec.jsonl          # Extracted ToC
│   └── usb_pd_chunks.jsonl        # Full section content
├── requirements.txt               # Python dependencies
└── README.md                      # Project instructions
```

---

##  Features

- Extracts structured Table of Contents from technical PDFs
- Splits the PDF into logical section "chunks"
- Lets you ask questions like: `Section 1.2` or `What is USB PD?`
- Returns accurate matching content from the original document

---

##  Setup Instructions

### 1. Clone or unzip the project

```bash
cd TaskHubApi2
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

##  How to Use

###  Step 1: Extract Table of Contents

```bash
python parser\usb_pd_parser.py
```

Output: `output/usb_pd_spec.jsonl`

---

###  Step 2: Chunk the PDF by section

```bash
python parser\chunk_pdf_by_toc.py
```

Output: `output/usb_pd_chunks.jsonl`

---

###  Step 3: Start QA Terminal

```bash
python parser\qa_from_chunks.py
```

You’ll see:
```
 Ask a question about the USB PD spec (type 'exit' to quit)
 Your Question:
```

---

## Sample Test Case

```
 Your Question: Section 1.2

 Section: 1.2 Purpose (Score: 1.00)

 Answer:
Compatible with existing spec-compliant USB cables.
Minimizes potential damage from non-compliant cables.
Defines mechanisms to discover, enter and exit Alternate Modes...
```

You can also ask:

``` Your Question: What is the purpose of USB Power Delivery?
```

---

## 📦 Requirements

- Python 3.8+
- Key libraries:
  - `pdfplumber`
  - `difflib`
  - `json`
  - `os`

Install all with:

```bash
pip install -r requirements.txt
```

---






