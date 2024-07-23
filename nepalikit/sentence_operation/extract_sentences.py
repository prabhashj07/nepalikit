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
    """
    A class to extract sentences from Nepali text, which includes normalization,
    processing and handling of common edge cases like abbreviations.

    Attributes:
    ----------
    text: str, the text to be processed and from which sentences will be extracteed : TextProcessor
    An instance of TextProcessor to handle text normalization and preprocessing.

    Methods:
    -------
    normalize_text() -> str:
    - Normalize the text using the TextProcessor.

    preprocess_text(normalized_text: str) -> str:
    - Preprocess the normalized text using the TextProcessor.

    extract_sentences -> list:
    - Extract and returns a list of sentences from the text.
    """
    def __init__(self, text: str):
        """
        Initializes the extract_sentences class with the provided text and initializes a TextProcessor instance.

        Parameters:
        text: str, The text to be processed and from which sentences will be extracted.
        """
        self.text = text
        self.processor = TextProcessor() 

    def normalize_text(self) -> str:
        """
        Normalize the text using TextProcessor.

        Returns:
        str: The normalized text.
        """
        # Assuming TextProcessor has a method `normalize` for normalization
        normalized_text = self.processor.normalize_text(self.text)
        return normalized_text

    def preprocess_text(self, normalized_text: str) -> str:
        """
        Preprocess the text using TextProcessor.

        Parameters:
        normalize_text: str
        - The normalized text to be preprocessed. 

        Returns:
        str: The preprocessed text.
        """
        cleaned_text = self.processor.preprocess_text(normalized_text)
        return cleaned_text

    def extract_sentences(self) -> list:
        """
        Extract sentences splits a given Nepali text into sentences 
        based on punctuation marks and handles common edge cases like abbreviations.

        Returns:
        list: A list of extracted sentences.
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
