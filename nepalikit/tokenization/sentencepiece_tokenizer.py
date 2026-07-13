import os
from importlib import resources
import sentencepiece as spm


class SentencePieceTokenizer:
    def __init__(self):
        pkg = resources.files("nepalikit")
        self.model_path = str(
            pkg.joinpath("tokenization", "sentencepiece", "model", "NepaliKit_sentencepiece.model")
        )
        if not os.path.exists(self.model_path):
            raise FileNotFoundError(f"Model file not found: {self.model_path}")
        self._sp = spm.SentencePieceProcessor()
        self._sp.load(self.model_path)

    def tokenize(self, text):
        """
        Tokenizes text using SentencePiece model loaded from file.

        Parameters:
        - text: str, a string to be tokenized.

        Returns:
        - a list of str: tokenized.
        """
        return self._sp.EncodeAsPieces(text)

    def detokenize(self, tokens):
        """
        Detokenize text using SentencePiece model loaded from file.

        Parameters:
        - a list of str: tokenized string to be converted into original form. 

        Returns:
        - original form: text, string
        """
        return self._sp.DecodePieces(tokens)
