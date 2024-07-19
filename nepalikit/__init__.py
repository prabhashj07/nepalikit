"""
__init__.py

Initialize NepaliKit package.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""

from nepalikit.manage_stopwords import *
from nepalikit.preprocessing import *
from nepalikit.tokenization import *
from nepalikit.utils import *
from nepalikit.sentence_operation import *

__all__ = [
    'TextProcessor', 'urls_emails',
    'remove_stopwords', 'Tokenizer', 'SentencePieceTokenizer',
    'NepaliTextProcessor'
    'extract_sentences', 'load_abbreviation', 'normalize_text', 'AbbreviationReplacer', 'segment_sentences',
    'sentence_stats', 'load_stopwords', 'remove_stopwords_from_text'
]

