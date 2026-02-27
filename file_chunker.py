#processes the pdfs into question chunks with appropriate metadata

import pdfplumber
from docx import Document
from pathlib import Path
import json
import re

#extracts all text as from pdf as single string
def extract_pdf_text(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        pages = [page.extract_text() for page in pdf.pages if page.extract_text()]
        return '\n\n'.join(pages)
    

