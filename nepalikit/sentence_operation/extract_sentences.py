"""
sentence_operations.py

Functions for sentence operations in Nepali text.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""

import re
from nepalikit.preprocessing.TextProcessor import TextProcessor

def extract_sentences(text: str) -> list:
    """Extract sentences splits a given Nepali text into sentences 
    based on punctuation marks and handles common edge cases like abbreviations."""
    normalized_text = normalize_text(text)
    cleaned_text = preprocess_text(normalized_text)
    sentences = re.split(r'([।?!])', cleaned_text)
    
    # Pair sentences with their punctuation
    sentences = [''.join(i) for i in zip(sentences[0::2], sentences[1::2] + [''])]
    
    # Handle abbreviations
    sentences = [re.sub(r'\s+', ' ', sent) for sent in sentences]
    sentences = [sent for sent in sentences if sent.strip()]
    
    return sentences


