"""Tests for the Nepali lemmatizer module."""

import pytest

from nepalikit.lemmatizer import NepaliLemmatizer, lemmatize, lemmatize_text


@pytest.fixture
def lemmatizer():
    return NepaliLemmatizer()


class TestNepaliLemmatizer:
    """Tests for NepaliLemmatizer class."""

    def test_lemmatize_noun_case(self, lemmatizer):
        assert lemmatizer.lemmatize("घरले") == "घर"
        assert lemmatizer.lemmatize("घरको") == "घर"
        assert lemmatizer.lemmatize("घरमा") == "घर"
        assert lemmatizer.lemmatize("घरबाट") == "घर"
        assert lemmatizer.lemmatize("घरलाई") == "घर"

    def test_lemmatize_plural(self, lemmatizer):
        assert lemmatizer.lemmatize("किताहरू") == "किता"
        assert lemmatizer.lemmatize("घरहरू") == "घर"
        assert lemmatizer.lemmatize("दिनहरू") == "दिन"

    def test_lemmatize_pronouns(self, lemmatizer):
        assert lemmatizer.lemmatize("मैले") == "म"
        assert lemmatizer.lemmatize("मलाई") == "म"
        assert lemmatizer.lemmatize("तिमीले") == "तिमी"
        assert lemmatizer.lemmatize("उनले") == "उ"
        assert lemmatizer.lemmatize("हामीले") == "हामी"

    def test_lemmatize_verbs(self, lemmatizer):
        assert lemmatizer.lemmatize("गर्छन्") == "गर्नु"
        assert lemmatizer.lemmatize("जान्छ") == "जानु"
        assert lemmatizer.lemmatize("आउँछ") == "आउनु"
        assert lemmatizer.lemmatize("हुन्छ") == "हुनु"
        assert lemmatizer.lemmatize("खान्छ") == "खानु"

    def test_lemmatize_verb_past(self, lemmatizer):
        assert lemmatizer.lemmatize("गरेको") == "गर्नु"
        assert lemmatizer.lemmatize("जानेको") == "जानु"
        assert lemmatizer.lemmatize("भएको") == "हुनु"

    def test_lemmatize_rule_fallback(self, lemmatizer):
        # Words not in dictionary should use rule-based fallback
        result = lemmatizer.lemmatize("राम्रोले")
        assert result == "राम्रो"

    def test_lemmatize_unknown_word(self, lemmatizer):
        # Completely unknown short words should return as-is
        assert lemmatizer.lemmatize("नेपाल") == "नेपाल"

    def test_lemmatize_empty(self, lemmatizer):
        assert lemmatizer.lemmatize("") == ""
        assert lemmatizer.lemmatize(None) is None

    def test_lemmatize_text(self, lemmatizer):
        result = lemmatizer.lemmatize_text("मैले किताहरू पढेको छु")
        assert result == "म किता पढ्नु छु"

    def test_lemmatize_text_empty(self, lemmatizer):
        assert lemmatizer.lemmatize_text("") == ""
        assert lemmatizer.lemmatize_text(None) is None

    def test_lemmatize_words(self, lemmatizer):
        result = lemmatizer.lemmatize_words(["मैले", "किताहरू", "पढेको"])
        assert result == ["म", "किता", "पढ्नु"]

    def test_lemmatize_words_empty(self, lemmatizer):
        assert lemmatizer.lemmatize_words([]) == []


class TestConvenienceFunctions:
    """Tests for module-level convenience functions."""

    def test_lemmatize(self):
        assert lemmatize("घरले") == "घर"
        assert lemmatize("गर्छन्") == "गर्नु"

    def test_lemmatize_text(self):
        result = lemmatize_text("मैले किताहरू पढेको छु")
        assert result == "म किता पढ्नु छु"
