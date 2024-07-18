"""
__init__.py

Initialize NepaliKit package.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""

# Import functions from manage_stopwords.py
from .manage_stopwords import load_stopwords 

# Import functions from preprocessing.py
from .preprocessing import (
    remove_html_tags,
    remove_special_characters,
    remove_urls_emails,
    remove_extra_whitespace,
    remove_stopwords,
    normalize_text,
    preprocess_text
)

# Import classes and functions from tokenization/tokenizer.py
from .tokenization.tokenizer import Tokenizer

# Import functions for SentencePiece tokenization
from .tokenization.sentencepiece_tokenizer import SentencePieceTokenizer

# Import functions from utils.py
from .utils import (
    get_word_frequency,
    split_text,
    merge_text,
    count_word,
    count_words_in_paragraph
)

# Import functions from sentence_operations.py
from .sentence_operation import extract_sentences, segment_sentences

__all__ = [
    'remove_html_tags', 'remove_special_characters',
    'remove_urls_emails', 'remove_extra_whitespace',
    'remove_stopwords', 'normalize_text', 'preprocess_text',
    'Tokenizer', 'sentencepiece_tokenize',
    'get_word_frequency', 'split_text', 'merge_text',
    'count_word', 'count_words_in_paragraph',
    'extract_sentences', 'segment_sentences'
]

