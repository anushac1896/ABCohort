import pdfplumber
from docx import Document

# -------- Extract text from PDF --------
pdf_path = "/Users/anushachennu/Downloads/summaryofbenifits_sample.pdf"

print("Reading PDF...\n")

with pdfplumber.open(pdf_path) as pdf:
    for i, page in enumerate(pdf.pages, start=1):
        print(f"Page {i}")
        print("-" * 40)
        print(page.extract_text())
        print("\n")

# -------- Extract text from Word --------
doc_path = "/Users/anushachennu/Downloads/health-insurance-claim-form.docx"

print("Reading Word document...\n")

doc = Document(doc_path)

for para in doc.paragraphs:
    if para.text.strip():
        print(para.text)