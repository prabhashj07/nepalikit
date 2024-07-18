"""
__init__.py

Initialize NepaliKit package.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""

from NepaliKit.manage_stopwords import *
from NepaliKit.preprocessing import *
from NepaliKit.tokenization import *
from NepaliKit.utils import *
from NepaliKit.sentence_operation import *

__all__ = [
    'TextProcessor', 'urls_emails',
    'remove_stopwords', 'Tokenizer', 'SentencePieceTokenizer',
    'NepaliTextProcessor'
    'extract_sentences', 'load_abbreviation', 'normalize_text', 'AbbreviationReplacer', 'segment_sentences',
    'sentence_stats', 'load_stopwords', 'remove_stopwords_from_text'
]

