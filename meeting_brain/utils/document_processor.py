"""
Simple PDF to text converter
"""

import PyPDF2
from pathlib import Path

def read_pdf(path: str) -> str:
    """Extract text from a PDF file"""
    with open(path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text.strip()

def read_pdfs(paths: dict[str, str]) -> dict[str, str]:
    """Extract text from multiple PDF files"""
    results = {}
    for name, path in paths.items():
        results[name] = read_pdf(path)
    return results

def save_text(text: str, path: str) -> None:
    """Save text to a file"""
    Path(path).write_text(text, encoding='utf-8')
