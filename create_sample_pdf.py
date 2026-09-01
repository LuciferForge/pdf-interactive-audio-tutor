#!/usr/bin/env python3
"""
Create sample 3-page academic PDF for PyMuPDF test running.
"""

import fitz # PyMuPDF

def create_sample_academic_pdf(pdf_path: str):
    doc = fitz.open()
    
    # Page 1: Chapter 1
    page1 = doc.new_page()
    page1.insert_text((50, 50), "Chapter 1: Artificial Intelligence in Modern Real Estate", fontsize=16)
    page1.insert_text((50, 90), "Real estate agents can leverage structured AI prompt frameworks to generate high-converting marketing copy in seconds.", fontsize=11)
    page1.insert_text((50, 130), "Luxury property listings require custom prompt templates that emphasize architectural details, premium finishes, and neighborhood amenities.", fontsize=11)

    # Page 2: Chapter 2
    page2 = doc.new_page()
    page2.insert_text((50, 50), "Chapter 2: Automated Lead Nurturing & Email Drip Campaigns", fontsize=16)
    page2.insert_text((50, 90), "High-converting email drip campaigns target expired listings, FSBO sellers, and past client referral networks automatically.", fontsize=11)

    # Page 3: Chapter 3
    page3 = doc.new_page()
    page3.insert_text((50, 50), "Chapter 3: Negotiation & Objection Handling Playbooks", fontsize=16)
    page3.insert_text((50, 90), "Strategic response scripts address lowball buyer offers, commission disputes, and appraisal shortfalls during deal closing.", fontsize=11)

    doc.save(pdf_path)
    doc.close()
    print(f"Sample academic PDF created at '{pdf_path}'")

if __name__ == "__main__":
    create_sample_academic_pdf("/Users/apple/Documents/products/pdf-interactive-audio-tutor/sample_book.pdf")
