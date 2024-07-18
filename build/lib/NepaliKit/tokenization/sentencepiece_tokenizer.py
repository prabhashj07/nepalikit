import os
import sentencepiece as spm

class SentencePieceTokenizer:
    def __init__(self):
        self.this_dir = os.path.dirname(os.path.abspath(__file__))

    def tokenize(self, text):
        """Tokenizes text using SentencePiece model loaded from file."""
        model_path = os.path.join(self.this_dir, "model", "NepaliKit_sentencepiece.model")
        try:
            sp = spm.SentencePieceProcessor()
            sp.load(model_path)
        except FileNotFoundError:
            raise FileNotFoundError(f"SentencePiece model file '{model_path}' not found.")
        except Exception as e:
            raise RuntimeError(f"Error loading SentencePiece model: {str(e)}")

        return sp.encode_as_pieces(text)

if __name__ == "__main__":
    pass
