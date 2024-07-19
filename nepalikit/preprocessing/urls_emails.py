"""
__init__.py

Preprocessing functions for text processing in  NepaliKit package.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""

import re

class urls_emails:
    """
    Removes (or replaces) URLs and emails within a document.
    """

    def __init__(self, email_replacement="", url_replacement=""):
        """
        Initialize the parser.
        """
        self.email_replacement = email_replacement
        self.url_replacement = url_replacement

    def __call__(self, text):
        """
        Runs the parser.

        Args:
            text: A string document
        Returns:
            text: The document with links removed or replaced
        """
        text = self.replace_urls_emails(text)
        return text

    def replace_urls_emails(self, text):
        """
        Replaces URLs and emails within the text.

        Args:
            text: A string document
        Returns:
            text: The document with links replaced
        """
        # Replace URLs
        if self.url_replacement:
            text = re.sub(r'\b(?:https?|ftp):\/\/\S+\b', self.url_replacement, text)
        else:
            text = re.sub(r'\b(?:https?|ftp):\/\/\S+\b', '', text)

        # Replace emails
        if self.email_replacement:
            text = re.sub(r'\S+@\S+\b', self.email_replacement, text)
        else:
            text = re.sub(r'\S+@\S+\b', '', text)

        return " ".join(text.split())

    @staticmethod
    def remove_urls_emails(text):
        """
        Removes URLs and emails using regular expressions.
        Args:
            text: A string document
        Returns:
            text: The document with links removed
        """
        clean_text = re.sub(r'\s*\b(?:https?|ftp):\/\/\S+\b\s*', ' ', text)  # Remove URLs
        clean_text = re.sub(r'\s*\S+@\S+\b\s*', ' ', clean_text)  # Remove emails
        return " ".join(clean_text.split())


