"""Tests for the Tokenizer class."""

import pytest
from nepalikit.tokenization import Tokenizer


@pytest.fixture
def tokenizer():
    return Tokenizer()


class TestSentenceTokenize:
    def test_basic(self, tokenizer):
        result = tokenizer.sentence_tokenize("म घर जाँदै छु। तिमी कहाँ जाँदैछौ।")
        sentences = [s for s in result if s.strip()]
        assert len(sentences) == 2
        assert "घर" in sentences[0]

    def test_single_sentence(self, tokenizer):
        result = tokenizer.sentence_tokenize("नमस्ते।")
        sentences = [s for s in result if s.strip()]
        assert len(sentences) == 1
        assert "नमस्ते" in sentences[0]

    def test_strips_english_punctuation(self, tokenizer):
        result = tokenizer.sentence_tokenize("Hello, world! Bye.")
        assert "Hello" in result[0] if result else False

    def test_empty_string(self, tokenizer):
        result = tokenizer.sentence_tokenize("")
        assert result == []

    def test_no_devanagari_danda(self, tokenizer):
        result = tokenizer.sentence_tokenize("नमस्ते कस्तो छ")
        assert result == ["नमस्ते कस्तो छ"]


class TestWordTokenize:
    def test_basic(self, tokenizer):
        result = tokenizer.word_tokenize("म घर जाँदै छु")
        assert result == ["म", "घर", "जाँदै", "छु"]

    def test_with_punctuation(self, tokenizer):
        result = tokenizer.word_tokenize("म घर, जाँदै छु।")
        assert "घर" in result
        assert "जाँदै" in result

    def test_custom_punctuation(self, tokenizer):
        result = tokenizer.word_tokenize("word1;word2", new_punctuation=[";"])
        assert result == ["word1", "word2"]

    def test_empty_string(self, tokenizer):
        result = tokenizer.word_tokenize("")
        assert result == []

    def test_single_word(self, tokenizer):
        result = tokenizer.word_tokenize("नमस्ते")
        assert result == ["नमस्ते"]


class TestCharacterTokenize:
    def test_basic(self, tokenizer):
        result = tokenizer.character_tokenize("मन")
        assert result == ["म", "न"]

    def test_empty_string(self, tokenizer):
        result = tokenizer.character_tokenize("")
        assert result == []

    def test_english(self, tokenizer):
        result = tokenizer.character_tokenize("abc")
        assert result == ["a", "b", "c"]


class TestTokenize:
    def test_word_level(self, tokenizer):
        result = tokenizer.tokenize("म घर जाँदै छु", level="word")
        assert result == ["म", "घर", "जाँदै", "छु"]

    def test_sentence_level(self, tokenizer):
        result = tokenizer.tokenize("म घर जाँदै छु। तिमी कहाँ जाँदैछौ।", level="sentence")
        assert len(result) >= 2

    def test_character_level(self, tokenizer):
        result = tokenizer.tokenize("मन", level="character")
        assert result == ["म", "न"]

    def test_characters_alias(self, tokenizer):
        result = tokenizer.tokenize("मन", level="characters")
        assert result == ["म", "न"]

    def test_invalid_level(self, tokenizer):
        with pytest.raises(ValueError, match="Unsupported tokenization level"):
            tokenizer.tokenize("text", level="invalid")


class TestDetokenize:
    def test_sentence_detokenize(self, tokenizer):
        result = tokenizer.sentence_detokenize(["म घर", "जाँदै छु"])
        assert result == "म घर।जाँदै छु"

    def test_word_detokenize(self, tokenizer):
        result = tokenizer.word_detokenize(["म", "घर"])
        assert result == "म घर"

    def test_character_detokenize(self, tokenizer):
        result = tokenizer.character_detokenize(["म", "न"])
        assert result == "मन"

    def test_detokenize_word_level(self, tokenizer):
        result = tokenizer.detokenize(["म", "घर"], level="word")
        assert result == "म घर"

    def test_detokenize_sentence_level(self, tokenizer):
        result = tokenizer.detokenize(["म घर", "छु"], level="sentence")
        assert result == "म घर।छु"

    def test_detokenize_character_level(self, tokenizer):
        result = tokenizer.detokenize(["म", "न"], level="character")
        assert result == "मन"

    def test_detokenize_invalid_level(self, tokenizer):
        with pytest.raises(ValueError, match="Unsupported detokenization level"):
            tokenizer.detokenize(["a"], level="invalid")


class TestStr:
    def test_str(self, tokenizer):
        assert str(tokenizer) == "Tokenizer for Nepali language"
