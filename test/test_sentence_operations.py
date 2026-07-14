"""Tests for extract_sentences, segment_sentences, and SentenceAnalyzer."""

from nepalikit.sentence_operation import (
    SentenceAnalyzer,
    extract_sentences,
    segment_sentences,
)


class TestExtractSentences:
    def test_basic(self):
        ext = extract_sentences("म घर जाँदै छु। तिमी कहाँ जाँदैछौ।")
        result = ext.extract_sentences()
        assert isinstance(result, list)
        assert len(result) >= 1

    def test_single_sentence(self):
        ext = extract_sentences("नमस्ते।")
        result = ext.extract_sentences()
        assert isinstance(result, list)
        assert len(result) >= 1

    def test_normalize_text(self):
        ext = extract_sentences("म  नाम")
        result = ext.normalize_text()
        assert isinstance(result, str)
        assert len(result) > 0

    def test_preprocess_text(self):
        ext = extract_sentences("म नाम राम हो।")
        normalized = ext.normalize_text()
        result = ext.preprocess_text(normalized)
        assert isinstance(result, str)

    def test_empty_text(self):
        ext = extract_sentences("")
        result = ext.extract_sentences()
        assert result == [] or result == [""]


class TestSegmentSentences:
    def test_basic(self):
        result = segment_sentences("म घर जाँदै छु। तिमी कहाँ जाँदैछौ।")
        assert isinstance(result, list)
        assert len(result) >= 1

    def test_single_sentence(self):
        result = segment_sentences("नमस्ते।")
        assert isinstance(result, list)
        assert len(result) >= 1

    def test_empty_text(self):
        result = segment_sentences("")
        assert isinstance(result, list)


class TestSentenceAnalyzer:
    def test_basic_stats(self):
        analyzer = SentenceAnalyzer()
        stats = analyzer.sentence_stats("म घर जाँदै छु।")
        assert "char_count" in stats
        assert "word_count" in stats
        assert "stopword_count" in stats
        assert "punctuation_count" in stats
        assert stats["char_count"] > 0
        assert stats["word_count"] >= 3

    def test_stopword_count(self):
        analyzer = SentenceAnalyzer()
        stats = analyzer.sentence_stats("म घर जाँदै छु।")
        assert stats["stopword_count"] >= 1

    def test_punctuation_count(self):
        analyzer = SentenceAnalyzer()
        stats = analyzer.sentence_stats("म घर जाँदै छु। तिमी!")
        assert stats["punctuation_count"] >= 2

    def test_empty_string(self):
        analyzer = SentenceAnalyzer()
        stats = analyzer.sentence_stats("")
        assert stats["char_count"] == 0
        assert stats["word_count"] == 0
