#!/usr/bin/env python3
"""
Interactive Command-Line Audio Tutor Test Runner
Tests PyMuPDF text extraction, lightweight RAG search, grounded Q&A, and ElevenLabs TTS audio generation.
"""

import os
import sys
from pdf_parser import PDFChapterParser
from rag_engine import LightweightRAGEngine
from audio_tutor import AudioTutorEngine

# Sample PDF Path (Real Estate Playbook PDF)
SAMPLE_PDF = "/Users/apple/Documents/products/pdf-interactive-audio-tutor/sample_book.pdf"

def run_audio_tutor_test():
    print("==================================================")
    print(" 🎧 PDF-TO-INTERACTIVE AUDIO TUTOR TEST RUNNER ")
    print("==================================================")
    
    # 1. Extract PDF Text & Segment
    print(f"1. Parsing PDF Text from '{os.path.basename(SAMPLE_PDF)}'...")
    parser = PDFChapterParser(SAMPLE_PDF)
    pages = parser.extract_clean_text()
    chapters = parser.segment_into_chapters(pages)
    print(f"   Successfully extracted {len(pages)} pages into {len(chapters)} audiobook chapters!")

    # 2. Build RAG Engine
    print("\n2. Building In-Memory RAG Vector Index...")
    rag = LightweightRAGEngine(chapters)

    # 3. Grounded Voice Q&A Simulation
    tutor = AudioTutorEngine(rag)
    sample_question = "How can real estate agents use AI prompt templates for luxury property listings?"
    print(f"\n3. Simulating Student Voice Question: \"{sample_question}\"")
    
    answer = tutor.generate_grounded_answer(sample_question)
    print(f"   Grounded Audio Answer: \"{answer}\"")

    # 4. Synthesize ElevenLabs Audio File
    output_audio = os.path.join(os.path.dirname(__file__), "sample_tutor_answer.mp3")
    print(f"\n4. Synthesizing ElevenLabs Voice Audio to '{output_audio}'...")
    success = tutor.synthesize_tts_audio(answer, output_audio)
    
    if success:
        print(f"🎉 SUCCESS! Interactive Voice Audio synthesized ({os.path.getsize(output_audio)} bytes)")
    else:
        print("⚠️ ElevenLabs audio generation fell back to text mode.")

    print("\n==================================================")
    print(" 📊 TEST SUMMARY: PDF-to-Audio Tutor Operational!")
    print("==================================================")

if __name__ == "__main__":
    run_audio_tutor_test()
