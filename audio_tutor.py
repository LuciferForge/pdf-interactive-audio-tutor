#!/usr/bin/env python3
"""
Voice Q&A & Narrative Engine for Interactive PDF Audio Tutor
Integrates ElevenLabs / TTS audio narration with grounded Q&A responses.
"""

import os
import requests
from dotenv import load_dotenv
from typing import Dict, Any

load_dotenv('/Users/apple/Documents/Zero_fks/.env')
ELEVENLABS_KEY = os.getenv("ElevenLabs_API", os.getenv("ELEVENLABS_API_KEY", ""))
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

class AudioTutorEngine:
    def __init__(self, rag_engine):
        self.rag = rag_engine
        self.elevenlabs_key = ELEVENLABS_KEY
        self.gemini_key = GEMINI_KEY

    def generate_grounded_answer(self, question: str) -> str:
        """Retrieve context from PDF RAG index and synthesize 2-sentence voice answer"""
        relevant_chunks = self.rag.search_context(question)
        context_str = "\n\n".join([c["text"] for c in relevant_chunks])

        prompt = f"""
You are an interactive PDF audio tutor. Answer the student's question concisely in 2 clear sentences using strictly the PDF context provided below.

PDF Context:
{context_str[:1500]}

Student Question: "{question}"

Concise Audio Answer:
"""
        if self.gemini_key:
            try:
                url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={self.gemini_key}"
                payload = {"contents": [{"parts": [{"text": prompt}]}]}
                r = requests.post(url, json=payload, timeout=10)
                if r.status_code == 200:
                    return r.json()['candidates'][0]['content']['parts'][0]['text'].strip()
            except Exception:
                pass

        # Fallback explanation
        return f"Based on the text in {relevant_chunks[0]['title']}, {relevant_chunks[0]['text'][:150]}..."

    def synthesize_tts_audio(self, text: str, output_mp3_path: str) -> bool:
        """Synthesize natural voice audio file using ElevenLabs API"""
        url = "https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM" # Rachel voice ID
        headers = {
            "xi-api-key": self.elevenlabs_key,
            "Content-Type": "application/json"
        }
        payload = {
            "text": text[:500],
            "model_id": "eleven_monolingual_v1",
            "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}
        }
        try:
            r = requests.post(url, json=payload, headers=headers, timeout=15)
            if r.status_code == 200:
                with open(output_mp3_path, "wb") as f:
                    f.write(r.content)
                return True
            else:
                print(f"ElevenLabs TTS Status: {r.status_code}")
                return False
        except Exception as e:
            print(f"ElevenLabs TTS Error: {e}")
            return False
