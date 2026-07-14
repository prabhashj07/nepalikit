"""
TextProcessor.py

Preprocessing functions for text processing in NepaliKit package.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""

import re
from collections import Counter

from nepalikit.preprocessing.urls_emails import urls_emails


class TextProcessor:
    """
    Text preprocessing pipeline for Nepali text.

    Provides methods for HTML tag removal, special character removal,
    whitespace normalization, stopword removal, and text lowercasing.
    """

    def __init__(self, stopwords=None):
        """
        Initialize TextProcessor.

        Args:
            stopwords (list, optional): List of stopwords to remove.
                Defaults to empty list.
        """
        self.stopwords = stopwords or []
        self.urls_emails_processor = urls_emails()

    def remove_html_tags(self, text):
        """Remove HTML tags from text."""
        return re.sub(r"<.*?>", "", text)

    def remove_special_characters(self, text):
        """Remove special characters, keeping only Devanagari and whitespace."""
        return re.sub(r"[^\u0900-\u097F\s]", "", text).replace("।", "")

    def remove_extra_whitespace(self, text):
        """Collapse multiple whitespace to a single space and strip."""
        return re.sub(r"\s+", " ", text).strip()

    def remove_stopwords(self, text):
        """Remove stopwords from text using the configured stopword list."""
        tokens = text.split()
        filtered_tokens = [word for word in tokens if word.lower() not in self.stopwords]
        return " ".join(filtered_tokens)

    def normalize_text(self, text):
        """Convert text to lowercase."""
        return text.lower()

    def preprocess_text(self, text):
        """
        Apply full preprocessing pipeline.

        Steps: HTML tags, URLs/emails, special chars, whitespace,
        stopwords, lowercasing.
        """
        text = self.remove_html_tags(text)
        text = self.urls_emails_processor.remove_urls_emails(text)
        text = self.remove_special_characters(text)
        text = self.remove_extra_whitespace(text)
        text = self.remove_stopwords(text)
        text = self.normalize_text(text)
        return text

    def get_word_frequency(self, tokens):
        """Count frequency of each word in a list of tokens."""
        return Counter(tokens)
