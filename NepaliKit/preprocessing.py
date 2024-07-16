"""
__init__.py

Preprocessing functions for text processing in  NepaliKit package.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""

import re

def remove_html_tags(text):
    clean_text = re.sub(r'<.*?>', '', text)  # Remove HTML tags
    return clean_text

def remove_special_characters(text):
    # Remove special characters specific to Nepali Unicode
    clean_text = re.sub(r'[^\u0900-\u097F\s]', '', text)  # Unicode range for Devanagari script
    return clean_text

def remove_urls_emails(text):
    clean_text = re.sub(r'\b(?:https?|ftp|mailto):\/\/\S+\b', '', text)  # Remove URLs
    clean_text = re.sub(r'\S*@\S*\s?', '', clean_text)  # Remove emails
    return clean_text

def remove_extra_whitespace(text):
    clean_text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with single space
    return clean_text.strip()  # Strip leading/trailing whitespace

def remove_stopwords(text, stopwords):
    tokens = text.split()  # Split text into tokens
    filtered_tokens = [word for word in tokens if word.lower() not in stopwords]
    return ' '.join(filtered_tokens)

def normalize_text(text):
    # Example: Convert text to lowercase (Nepali text is typically not case-sensitive)
    return text.lower()

def preprocess_text(text, stopwords):
    text = remove_html_tags(text)
    text = remove_special_characters(text)
    text = remove_urls_emails(text)
    text = remove_extra_whitespace(text)
    text = remove_stopwords(text, stopwords)
    text = normalize_text(text)
    return text

if __name__ == "__main__":
    """
    main application logic or script logic
    """
    pass

