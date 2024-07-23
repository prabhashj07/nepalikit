import os
import sentencepiece as spm

class SentencePieceTokenizer:
    def __init__(self):
        self.this_dir = os.path.dirname(os.path.abspath(__file__))
        self.model_path = os.path.join(self.this_dir, "sentencepiece", "model", "NepaliKit_sentencepiece.model")
        print(f"Model path: {self.model_path}")
        if not os.path.exists(self.model_path):
            raise FileNotFoundError(f"Model file not found: {self.model_path}")

        print("Model found and path is correct.")

    def tokenize(self, text):
        """
        Tokenizes text using SentencePiece model loaded from file.

        Parameters:
        - text: str, a string to be tokenized.

        Returns:
        - a list of str: tokenized.
        """
        model_path = os.path.join(self.this_dir, "sentencepiece", "model", "NepaliKit_sentencepiece.model")
        try:
            sp = spm.SentencePieceProcessor()
            sp.load(model_path)
        except FileNotFoundError:
            raise FileNotFoundError(f"SentencePiece model file '{model_path}' not found.")
        except Exception as e:
            raise RuntimeError(f"Error loading SentencePiece model: {str(e)}")

        return sp.EncodeAsPieces(text)

    def detokenize(self, tokens):
        """
        Detokenize text using SentencePiece model loaded from file.

        Parameters:
        - a list of str: tokenized string to be converted into original form. 

        Returns:
        - original form: text, string
        """
        model_path = os.path.join(self.this_dir, "sentencepiece", "model", "NepaliKit_sentencepiece.model")
        try:
            sp = spm.SentencePieceProcessor()
            sp.load(model_path)
        except FileNotFoundError:
            raise FileNotFoundError(f"SentencePiece model file '{model_path}' not found.")
        except Exception as e:
            raise RuntimeError(f"Error loading SentencePiece model: {str(e)}")

        return sp.DecodePieces(tokens)

if __name__ == "__main__":
    tokenizer = SentencePieceTokenizer();
