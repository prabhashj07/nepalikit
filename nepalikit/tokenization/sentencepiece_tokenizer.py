"""
sentencepiece_tokenizer.py

SentencePiece-based tokenizer for Nepali text.
Loads a pre-trained SentencePiece model for tokenization and detokenization.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""

import os
from importlib import resources
import sentencepiece as spm


class SentencePieceTokenizer:
    """
    SentencePiece tokenizer for Nepali text.

    Uses a pre-trained SentencePiece model to tokenize and detokenize
    Nepali text into subword units.
    """

    def __init__(self):
        """Initialize tokenizer by loading the bundled SentencePiece model."""
        pkg = resources.files("nepalikit")
        self.model_path = str(
            pkg.joinpath(
                "tokenization",
                "sentencepiece",
                "model",
                "NepaliKit_sentencepiece.model",
            )
        )
        if not os.path.exists(self.model_path):
            raise FileNotFoundError(f"Model file not found: {self.model_path}")
        self._sp = spm.SentencePieceProcessor()
        self._sp.load(self.model_path)

    def tokenize(self, text):
        """Tokenize text into SentencePiece subword pieces.

        Args:
            text (str): Input text to tokenize.

        Returns:
            list: List of subword token strings.
        """
        return self._sp.EncodeAsPieces(text)

    def detokenize(self, tokens):
        """Detokenize subword pieces back to original text.

        Args:
            tokens (list): List of subword token strings.

        Returns:
            str: Reconstructed text.
        """
        return self._sp.DecodePieces(tokens)
