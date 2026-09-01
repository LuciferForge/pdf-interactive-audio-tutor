#!/usr/bin/env python3
"""
PyMuPDF Text Extractor & Chapter Segmenter
Parses multi-column academic PDFs and structures text into clean chapter chunks.
"""

import fitz  # PyMuPDF
import re
from typing import List, Dict, Any

class PDFChapterParser:
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path

    def extract_clean_text(self) -> List[Dict[str, Any]]:
        """Extract page-by-page clean text from PDF using PyMuPDF"""
        doc = fitz.open(self.pdf_path)
        pages_data = []

        for page_num in range(len(doc)):
            page = doc[page_num]
            raw_text = page.get_text("text")
            
            # Remove header/footer line noise
            lines = raw_text.split('\n')
            clean_lines = [l for l in lines if len(l.strip()) > 3]
            clean_text = ' '.join(clean_lines)

            pages_data.append({
                "page": page_num + 1,
                "text": clean_text
            })

        doc.close()
        return pages_data

    def segment_into_chapters(self, pages_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Segment page data into logical chapters or sections"""
        full_text = " ".join([p["text"] for p in pages_data])
        
        # Split into ~500 word chunks
        words = full_text.split()
        chunk_size = 300
        chapters = []

        for i in range(0, len(words), chunk_size):
            chunk_words = words[i:i + chunk_size]
            chapter_text = " ".join(chunk_words)
            chap_num = (i // chunk_size) + 1
            chapters.append({
                "chapter_id": chap_num,
                "title": f"Section {chap_num}",
                "text": chapter_text
            })

        return chapters
