"""
sentence_operations.py

Functions for sentence operations in Nepali text.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""

from nepalikit.sentence_operation.load_abbreviation import load_abbreviations
from nepalikit.sentence_operation.extract_sentences import extract_sentences

def segment_sentences(text: str) -> list:
    """
    Segment sentences takes the output of 'extract_sentences'and refines
    it by joining sentences split due to load_abbreviations, ensuring cohesive 
    and accurate sentence segmentation for further processing and analysis.
    """
    abbreviations = load_abbreviations()
    sentences = extract_sentences(text)
    
    # Join sentences split on abbreviations
    final_sentences = []
    for i, sent in enumerate(sentences):
        if i > 0 and sent.split()[0] in abbreviations:
            final_sentences[-1] += ' ' + sent
        else:
            final_sentences.append(sent)
    
    return final_sentences

