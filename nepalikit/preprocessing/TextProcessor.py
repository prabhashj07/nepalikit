"""


Preprocessing functions for text processing in NepaliKit package.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""

import re
from collections import Counter
from nepalikit.preprocessing.urls_emails import *

class TextProcessor:
    def __init__(self, stopwords=None):
        self.stopwords = stopwords or []
        self.urls_emails_processor = urls_emails()

    def remove_html_tags(self, text):
        return re.sub(r'<.*?>', '', text)

    def remove_special_characters(self, text):
        return re.sub(r'[^\u0900-\u097F\s]', '', text).replace('।', '')

    def remove_extra_whitespace(self, text):
        return re.sub(r'\s+', ' ', text).strip()

    def remove_stopwords(self, text):
        tokens = text.split()
        filtered_tokens = [word for word in tokens if word.lower() not in self.stopwords]
        return ' '.join(filtered_tokens)

    def normalize_text(self, text):
        return text.lower()

    def preprocess_text(self, text):
        text = self.remove_html_tags(text)
        text = self.remove_special_characters(text)
        text = self.urls_emails_processor.remove_urls_emails(text)
        text = self.remove_extra_whitespace(text)
        text = self.remove_stopwords(text)
        text = self.normalize_text(text)
        return text

    def get_word_frequency(self, tokens):
        return Counter(tokens)

