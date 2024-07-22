"""
sentence_operations.py

Functions for sentence operations in Nepali text.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""

import re
from nepalikit.preprocessing.TextProcessor import TextProcessor

class extract_sentences:
    def __init__(self, text: str):
        self.text = text
        self.processor = TextProcessor()  

    def normalize_text(self) -> str:
        """
        Normalize the text using TextProcessor.
        """
        # Assuming TextProcessor has a method `normalize` for normalization
        normalized_text = self.processor.normalize_text(self.text)
        return normalized_text

    def preprocess_text(self, normalized_text: str) -> str:
        """
        Preprocess the text using TextProcessor.
        """
        cleaned_text = self.processor.preprocess_text(normalized_text)
        return cleaned_text

    def extract_sentences(self) -> list:
        """
        Extract sentences splits a given Nepali text into sentences 
        based on punctuation marks and handles common edge cases like abbreviations.
        """
        normalized_text = self.normalize_text()
        cleaned_text = self.preprocess_text(normalized_text)
        sentences = re.split(r'([।?!])', cleaned_text)
        
        # Pair sentences with their punctuation
        sentences = [''.join(i) for i in zip(sentences[0::2], sentences[1::2] + [''])]
        
        # Handle abbreviations
        sentences = [re.sub(r'\s+', ' ', sent) for sent in sentences]
        sentences = [sent for sent in sentences if sent.strip()]
        
        return sentences
