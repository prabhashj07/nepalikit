"""
test/test_ml_pos_tagger.py

Tests for the ML-based POS tagger module (v1.0.6).
Author: Prabhash Kumar Jha
Date: July 2026
"""

from nepalikit.pos_tagger.ml_pos_tagger import MLPOSTagger, ml_tag_pos, ml_tag_text


class TestMLPOSTagger:
    """Tests for the MLPOSPOSTagger class."""

    def setup_method(self):
        """Set up the tagger for each test."""
        self.tagger = MLPOSTagger()

    def test_tag_pronoun(self):
        """PRON tag for first person pronoun."""
        result = self.tagger.tag(["म"])
        assert result == [("म", "PRON")]

    def test_tag_postposition(self):
        """POSTP tag for postposition."""
        result = self.tagger.tag(["मा"])
        assert result == [("मा", "POSTP")]

    def test_tag_conjunction(self):
        """CONJ tag for conjunction."""
        result = self.tagger.tag(["र"])
        assert result == [("र", "CONJ")]

    def test_tag_particle(self):
        """PART tag for particle."""
        result = self.tagger.tag(["पनि"])
        assert result == [("पनि", "PART")]

    def test_tag_interjection(self):
        """INTJ tag for interjection."""
        result = self.tagger.tag(["अरे"])
        assert result == [("अरे", "INTJ")]

    def test_tag_punctuation(self):
        """PUNC tag for punctuation."""
        result = self.tagger.tag(["।"])
        assert result == [("।", "PUNC")]

    def test_tag_verb(self):
        """V_VM tag for verb."""
        result = self.tagger.tag(["छ"])
        assert result == [("छ", "V_VM")]

    def test_tag_proper_noun(self):
        """N_NNP tag for proper noun."""
        result = self.tagger.tag(["नेपाल"])
        assert result == [("नेपाल", "N_NNP")]

    def test_tag_adjective(self):
        """ADJ tag for adjective."""
        result = self.tagger.tag(["राम्रो"])
        assert result == [("राम्रो", "ADJ")]

    def test_tag_adverb(self):
        """ADV tag for adverb."""
        result = self.tagger.tag(["धेरै"])
        assert result == [("धेरै", "ADV")]

    def test_tag_text(self):
        """Tag a full text sentence."""
        result = self.tagger.tag_text("म नेपाली हुँ")
        assert len(result) == 3
        assert result[0] == ("म", "PRON")
        assert result[2] == ("हुँ", "V_VM")

    def test_tag_sentence_with_context(self):
        """Context-aware tagging for a complete sentence."""
        result = self.tagger.tag_text("राम भात खान्छ")
        assert result[0][0] == "राम"
        assert result[2][0] == "खान्छ"
        assert result[2][1] == "V_VM"

    def test_tag_empty_input(self):
        """Empty input returns empty list."""
        assert self.tagger.tag([]) == []
        assert self.tagger.tag_text("") == []

    def test_convenience_ml_tag_pos(self):
        """ml_tag_pos convenience function."""
        result = ml_tag_pos(["म", "छु"])
        assert len(result) == 2
        assert result[0] == ("म", "PRON")

    def test_convenience_ml_tag_text(self):
        """ml_tag_text convenience function."""
        result = ml_tag_text("म नेपाली हुँ")
        assert len(result) == 3

    def test_verb_finite_forms(self):
        """All finite verb forms are tagged as V_VM."""
        verb_forms = ["छ", "छन्", "छु", "छौँ", "हुन्छ", "हुँ", "भयो", "गर्छ"]
        for form in verb_forms:
            result = self.tagger.tag([form])
            assert result[0][1] == "V_VM", f"{form} should be V_VM"

    def test_noun_suffix_haru(self):
        """Words ending in 'हरू' are tagged as N_NN."""
        result = self.tagger.tag(["किताबहरू"])
        assert result[0][1] == "N_NN"

    def test_multiple_sentences(self):
        """Tag multiple sentences."""
        result1 = self.tagger.tag_text("म छु")
        result2 = self.tagger.tag_text("उ छन्")
        assert len(result1) == 2
        assert len(result2) == 2

    def test_mixed_script(self):
        """Tag a sentence mixing Devanagari and punctuation."""
        result = self.tagger.tag_text("नमस्ते , कस्तो छ ?")
        assert len(result) == 5
        assert result[0][0] == "नमस्ते"
        assert result[1][0] == ","

    def test_pos_tags_are_valid(self):
        """All assigned tags are from the valid tag set."""
        text = "म नेपालमा बस्छु र राम्रो काम गर्छु"
        result = self.tagger.tag_text(text)
        valid_tags = {"N_NN", "N_NNP", "V_VM", "ADJ", "ADV", "PRON", "POSTP", "CONJ", "PART", "INTJ", "PUNC"}
        for _, tag in result:
            assert tag in valid_tags, f"Invalid tag: {tag}"
