#!/usr/bin/env python3
"""
Lightweight In-Memory RAG Vector Index for Interactive PDF Audio Tutor
Calculates text similarity and retrieves relevant context for voice Q&A.
"""

from typing import List, Dict, Any

class LightweightRAGEngine:
    def __init__(self, chapters: List[Dict[str, Any]]):
        self.chapters = chapters

    def search_context(self, query: str, top_k: int = 2) -> List[Dict[str, Any]]:
        """Retrieve most relevant text chunks for a query using word-matching similarity"""
        query_words = set(query.lower().split())
        scored_chapters = []

        for ch in self.chapters:
            text_words = set(ch["text"].lower().split())
            overlap = len(query_words.intersection(text_words))
            scored_chapters.append((overlap, ch))

        # Sort by overlap score descending
        scored_chapters.sort(key=lambda x: x[0], reverse=True)
        return [item[1] for item in scored_chapters[:top_k]]
