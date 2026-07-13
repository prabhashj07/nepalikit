"""
__init__.py

Initialize NepaliKit package.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""

from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("nepalikit")
except PackageNotFoundError:
    __version__ = "0.0.0"

from nepalikit.manage_stopwords import (
    load_stopwords, remove_stopwords_from_text,
    get_stopwords, is_stopword, add_stopwords, remove_custom_stopwords,
)
from nepalikit.preprocessing import *
from nepalikit.tokenization import *
from nepalikit.utils import *
from nepalikit.sentence_operation import *

from nepalikit.stemmer import NepaliStemmer, stem, stem_text
from nepalikit.normalizer import NepaliNormalizer, normalize, detect_script
from nepalikit.number_extractor import NepaliNumberExtractor, extract_numbers, convert_number
from nepalikit.pos_tagger import NepaliPOSTagger, tag_pos
from nepalikit.spell_checker import NepaliSpellChecker, check_spelling, suggest_corrections
from nepalikit.transliterate import NepaliTransliterator, roman_to_devanagari, devanagari_to_roman

__all__ = [
    # Existing
    'TextProcessor', 'urls_emails',
    'remove_stopwords_from_text', 'Tokenizer', 'SentencePieceTokenizer',
    'NepaliTextProcessor',
    'extract_sentences', 'load_abbreviations', 'TextNormalizer', 'AbbreviationReplacer', 'segment_sentences',
    'SentenceAnalyzer', 'load_stopwords',

    # Stopwords (enhanced)
    'get_stopwords', 'is_stopword', 'add_stopwords', 'remove_custom_stopwords',

    # New: Stemmer
    'NepaliStemmer', 'stem', 'stem_text',

    # New: Normalizer
    'NepaliNormalizer', 'normalize', 'detect_script',

    # New: Number Extractor
    'NepaliNumberExtractor', 'extract_numbers', 'convert_number',

    # New: POS Tagger
    'NepaliPOSTagger', 'tag_pos',

    # New: Spell Checker
    'NepaliSpellChecker', 'check_spelling', 'suggest_corrections',

    # New: Transliteration
    'NepaliTransliterator', 'roman_to_devanagari', 'devanagari_to_roman',
]
