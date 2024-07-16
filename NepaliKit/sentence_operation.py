"""
sentence_operations.py

Functions for sentence operations in Nepali text.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""

import re

def extract_sentences(text):
    """extracts sentences from Nepali text based on punctuation."""
    try:
        sentences = re.split(r'[।?!\—-]', text)  # Split by common punctuation marks
        sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
        return sentences
    except TypeError as e:
        print(f"TypeError occurred: {e}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def segment_sentences(text):
    """Segments Nepali text into sentences using custom rules."""
    try:
        # Implement custom segmentation rules
        sentences = extract_sentences(text)
        return sentences
    except TypeError as e:
        print(f"TypeError occurred during segmentation: {e}")
        return []
    except Exception as e:
        print(f"An error occurred during segmentation: {e}")
        return []

if __name__ == "__main__":
    pass

