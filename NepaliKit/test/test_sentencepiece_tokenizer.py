import os
import pytest
from NepaliKit.tokenization.sentencepiece_tokenizer import SentencePieceTokenizer
import sentencepiece as spm

@pytest.fixture
def tokenizer():
    return SentencePieceTokenizer()

def test_tokenizer_initialization(tokenizer):
    assert isinstance(tokenizer, SentencePieceTokenizer)

def test_tokenize(tokenizer):
    text = "Hello, world!"
    tokens = tokenizer.tokenize(text)
    assert isinstance(tokens, list)
    # Update this with the actual expected token IDs
    # Example: assert tokens == [682, 151, 48, 583, 111]

def test_detokenize(tokenizer):
    tokens = [682, 151, 48, 583, 111]
    text = tokenizer.detokenize(tokens)
    assert isinstance(text, str)
    # Update this with the actual expected string
    # Example: assert text == "Hello, world!"

def test_tokenize_empty_string(tokenizer):
    tokens = tokenizer.tokenize("")
    assert tokens == []

def test_detokenize_empty_list(tokenizer):
    text = tokenizer.detokenize([])
    assert text == ""

def test_roundtrip(tokenizer):
    text = "Hello, world!"
    tokens = tokenizer.tokenize(text)
    recovered_text = tokenizer.detokenize(tokens)
    assert recovered_text == text

def test_model_file_not_found():
    non_existent_model = '/nonexistent/path/NepaliKit_sentencepiece.model'
    with pytest.raises(OSError):
        sp = spm.SentencePieceProcessor()
        sp.Load(non_existent_model)

