"""
__init__.py

Initialize tokenization module for NepaliKit package.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""

from .tokenizer import Tokenizer
# from .sentencepiece_tokenizer import SentencePieceTokenizer
from nepalikit.tokenization.sentencepiece_tokenizer import SentencePieceTokenizer

__all__ = [
    'Tokenizer',
    'SentencePieceTokenizer'
]

