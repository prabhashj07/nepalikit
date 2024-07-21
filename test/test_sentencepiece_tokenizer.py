# test/test_sentencepiece_tokenizer.py

import os
import pytest
from nepalikit.tokenization import SentencePieceTokenizer
from nepalikit.sentence_operation import TextNormalizer
import sentencepiece as spm

@pytest.fixture
def tokenizer():
    return SentencePieceTokenizer()

def test_tokenizer_initialization(tokenizer):
    assert isinstance(tokenizer, SentencePieceTokenizer)

def test_tokenize(tokenizer):
    text = "तपाईंलाई कस्तो छ म ठिक छु"
    tokens = tokenizer.tokenize(text)
    assert isinstance(tokens, list)
    # Example: assert tokens == [1, 2, 3, 4, 5]

def test_detokenize(tokenizer):
    tokens = [1, 2, 3, 4, 5]
    text = tokenizer.detokenize(tokens)
    assert isinstance(text, str)
    # Example: assert text == "तपाईंलाई कस्तो छ म ठिक छु"

def test_tokenize_empty_string(tokenizer):
    tokens = tokenizer.tokenize("")
    assert tokens == []

def test_detokenize_empty_list(tokenizer):
    text = tokenizer.detokenize([])
    assert text == ""

def test_roundtrip(tokenizer):
    text = "तपाईंलाई कस्तो छ म ठिक छु"
    tokens = tokenizer.tokenize(text)
    recovered_text = tokenizer.detokenize(tokens)
    assert recovered_text == text

def test_model_file_not_found():
    non_existent_model = '/nonexistent/path/NepaliKit_sentencepiece.model'
    with pytest.raises(OSError):
        sp = spm.SentencePieceProcessor()
        sp.Load(non_existent_model)

def test_text_normalizer():
    text = "तपाईंलाई कस्तो छ म ठिक छु"
    normalizer = TextNormalizer(text)
    normalized_text = normalizer.normalize()
    assert isinstance(normalized_text, str)
