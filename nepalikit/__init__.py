"""
__init__.py

Initialize NepaliKit package.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("nepalikit")
except PackageNotFoundError:
    __version__ = "0.0.0"

from nepalikit.lemmatizer import NepaliLemmatizer, lemmatize, lemmatize_text
from nepalikit.manage_stopwords import (
    add_stopwords,
    get_stopwords,
    is_stopword,
    load_stopwords,
    remove_custom_stopwords,
    remove_stopwords_from_text,
)
from nepalikit.ner import NepaliNER, extract_entities, recognize_entities
from nepalikit.normalizer import (
    NepaliNormalizer,
    contains_devanagari,
    contains_latin,
    detect_script,
    is_devanagari,
    mixed_script_ratio,
    normalize,
)
from nepalikit.number_extractor import (
    NepaliNumberExtractor,
    convert_number,
    extract_numbers,
)
from nepalikit.pos_tagger import (
    MLPOSTagger,
    NepaliPOSTagger,
    ml_tag_pos,
    ml_tag_text,
    tag_pos,
)
from nepalikit.preprocessing import TextProcessor, urls_emails
from nepalikit.sentence_operation import (
    AbbreviationReplacer,
    SentenceAnalyzer,
    TextNormalizer,
    extract_sentences,
    load_abbreviations,
    segment_sentences,
)
from nepalikit.spell_checker import (
    NepaliSpellChecker,
    check_spelling,
    suggest_corrections,
)
from nepalikit.stemmer import (
    NepaliStemmer,
    SnowballStemmer,
    snowball_stem,
    stem,
    stem_text,
)
from nepalikit.tokenization import SentencePieceTokenizer, Tokenizer
from nepalikit.transliterate import (
    NepaliTransliterator,
    PreetiConverter,
    devanagari_to_roman,
    preeti_to_unicode,
    roman_to_devanagari,
)
from nepalikit.utils import NepaliTextProcessor

__all__ = [
    "AbbreviationReplacer",
    "MLPOSTagger",
    "NepaliLemmatizer",
    "NepaliNER",
    "NepaliNormalizer",
    "NepaliNumberExtractor",
    "NepaliPOSTagger",
    "NepaliSpellChecker",
    "NepaliStemmer",
    "NepaliTextProcessor",
    "NepaliTransliterator",
    "PreetiConverter",
    "SentenceAnalyzer",
    "SentencePieceTokenizer",
    "SnowballStemmer",
    "TextNormalizer",
    "TextProcessor",
    "Tokenizer",
    "add_stopwords",
    "check_spelling",
    "contains_devanagari",
    "contains_latin",
    "convert_number",
    "devanagari_to_roman",
    "detect_script",
    "extract_entities",
    "extract_numbers",
    "extract_sentences",
    "get_stopwords",
    "is_devanagari",
    "is_stopword",
    "lemmatize",
    "lemmatize_text",
    "load_abbreviations",
    "load_stopwords",
    "ml_tag_pos",
    "ml_tag_text",
    "mixed_script_ratio",
    "normalize",
    "preeti_to_unicode",
    "recognize_entities",
    "remove_custom_stopwords",
    "remove_stopwords_from_text",
    "roman_to_devanagari",
    "segment_sentences",
    "snowball_stem",
    "stem",
    "stem_text",
    "suggest_corrections",
    "tag_pos",
    "urls_emails",
]
