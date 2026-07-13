"""Tests for AbbreviationReplacer with real abbreviations."""

from nepalikit.sentence_operation import AbbreviationReplacer


class TestAbbreviationReplacer:
    def test_empty(self):
        replacer = AbbreviationReplacer()
        result = replacer.replace_abbreviations("उ.मा.वि. मा पढ्छु।")
        assert result == "उ.मा.वि. मा पढ्छु।"

    def test_with_abbreviations(self):
        abbrevs = {"उ.मा.वि.": "उच्च माध्यमिक विद्यालय"}
        replacer = AbbreviationReplacer(abbrevs)
        result = replacer.replace_abbreviations("उ.मा.वि. मा पढ्छु।")
        assert "उच्च माध्यमिक विद्यालय" in result

    def test_multiple_abbreviations(self):
        abbrevs = {
            "उ.मा.वि.": "उच्च माध्यमिक विद्यालय",
            "प्रा.": "प्राथमिक",
        }
        replacer = AbbreviationReplacer(abbrevs)
        result = replacer.replace_abbreviations("उ.मा.वि. र प्रा. विद्यालय।")
        assert "उच्च माध्यमिक विद्यालय" in result
        assert "प्राथमिक" in result

    def test_case_insensitive(self):
        abbrevs = {"USA": "United States of America"}
        replacer = AbbreviationReplacer(abbrevs)
        result = replacer.replace_abbreviations("म USA मा छु।")
        assert "United States of America" in result

    def test_no_match(self):
        abbrevs = {"उ.मा.वि.": "उच्च माध्यमिक विद्यालय"}
        replacer = AbbreviationReplacer(abbrevs)
        result = replacer.replace_abbreviations("नमस्ते कस्तो छ।")
        assert result == "नमस्ते कस्तो छ।"

    def test_init_with_dict(self):
        abbrevs = {"A": "Alpha", "B": "Beta"}
        replacer = AbbreviationReplacer(abbrevs)
        assert len(replacer.abbreviations) == 2
        assert replacer.pattern is not None

    def test_pattern_generation(self):
        replacer = AbbreviationReplacer({"X": "Y"})
        assert replacer.pattern is not None
        assert "X" in replacer.pattern

    def test_pattern_empty(self):
        replacer = AbbreviationReplacer()
        assert replacer.pattern is None
