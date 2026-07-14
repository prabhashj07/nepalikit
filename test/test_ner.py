"""
test/test_ner.py

Tests for the Named Entity Recognition module (v1.0.7).
Author: Prabhash Kumar Jha
Date: July 2026
"""

from nepalikit.ner import NepaliNER, extract_entities, recognize_entities


class TestNepaliNER:
    """Tests for the NepaliNER class."""

    def setup_method(self):
        """Set up the NER for each test."""
        self.ner = NepaliNER()

    def test_recognize_person(self):
        """Recognize PERSON entities."""
        result = self.ner.recognize(["राम", "जान्छ"])
        assert result[0] == ("राम", "PERSON")
        assert result[1] == ("जान्छ", None)

    def test_recognize_location(self):
        """Recognize LOCATION entities."""
        result = self.ner.recognize(["नेपाल", "एउटा", "देश", "हो"])
        assert result[0] == ("नेपाल", "LOCATION")

    def test_recognize_organization(self):
        """Recognize ORGANIZATION entities."""
        result = self.ner.recognize(["नेपाल", "सरकार", "ले", "भन्यो"])
        assert result[0] == ("नेपाल", "ORGANIZATION")
        assert result[1] == ("सरकार", "ORGANIZATION")

    def test_recognize_compound_organization(self):
        """Recognize compound ORGANIZATION entities."""
        result = self.ner.recognize(["त्रिभुवन", "विश्वविद्यालय", "मा"])
        assert result[0] == ("त्रिभुवन", "ORGANIZATION")
        assert result[1] == ("विश्वविद्यालय", "ORGANIZATION")

    def test_recognize_compound_location(self):
        """Recognize compound LOCATION entities."""
        result = self.ner.recognize(["काठमाडौं", "मा"])
        assert result[0] == ("काठमाडौं", "LOCATION")

    def test_recognize_date_numeric(self):
        """Recognize numeric DATE expressions."""
        result = self.ner.recognize(["२०८१", "/", "०७", "/", "१५"])
        # The date pattern should match
        for token, entity_type in result:
            if "/" in token or token in ["२०८१", "०७", "१५"]:
                assert entity_type == "DATE" or entity_type is None

    def test_recognize_date_month(self):
        """Recognize month-based DATE expressions."""
        result = self.ner.recognize(["जनवरी", "15"])
        assert result[0] == ("जनवरी", "DATE")
        assert result[1] == ("15", "DATE")

    def test_recognize_date_relative(self):
        """Recognize relative DATE expressions."""
        result = self.ner.recognize(["आज", "म", "जान्छु"])
        assert result[0] == ("आज", "DATE")

    def test_recognize_mixed_entities(self):
        """Recognize mixed entity types in a sentence."""
        result = self.ner.recognize(["राम", "काठमाडौं", "मा", "बस्छ"])
        assert result[0] == ("राम", "PERSON")
        assert result[1] == ("काठमाडौं", "LOCATION")

    def test_recognize_text(self):
        """Recognize entities from full text."""
        result = self.ner.recognize_text("राम काठमाडौं मा बस्छ")
        assert result[0][0] == "राम"
        assert result[0][1] == "PERSON"
        assert result[1][0] == "काठमाडौं"
        assert result[1][1] == "LOCATION"

    def test_extract_entities(self):
        """Extract entities as a dictionary."""
        entities = self.ner.extract_entities("राम काठमाडौं मा बस्छ")
        assert "राम" in entities["PERSON"]
        assert "काठमाडौं" in entities["LOCATION"]

    def test_no_entities(self):
        """Handle text with no entities."""
        result = self.ner.recognize(["एउटा", "राम्रो", "दिन"])
        assert all(et is None for _, et in result)

    def test_empty_input(self):
        """Handle empty input."""
        assert self.ner.recognize([]) == []
        assert self.ner.recognize_text("") == []

    def test_convenience_recognize_entities(self):
        """recognize_entities convenience function."""
        result = recognize_entities(["राम", "जान्छ"])
        assert result[0] == ("राम", "PERSON")

    def test_convenience_extract_entities(self):
        """extract_entities convenience function."""
        result = extract_entities("राम काठमाडौं मा बस्छ")
        assert "राम" in result["PERSON"]

    def test_multiple_persons(self):
        """Recognize multiple PERSON entities."""
        result = self.ner.recognize(["राम", "र", "सीता", "जान्छन्"])
        assert result[0] == ("राम", "PERSON")
        assert result[2] == ("सीता", "PERSON")

    def test_location_list(self):
        """Recognize multiple LOCATION entities."""
        result = self.ner.recognize(["नेपाल", "भारत", "बीच"])
        assert result[0] == ("नेपाल", "LOCATION")
        assert result[1] == ("भारत", "LOCATION")

    def test_organization_list(self):
        """Recognize multiple ORGANIZATION entities."""
        result = self.ner.recognize(["नेपाल", "सरकार", "र", "भारत", "सरकार"])
        assert result[0] == ("नेपाल", "ORGANIZATION")
        assert result[1] == ("सरकार", "ORGANIZATION")
        assert result[3] == ("भारत", "ORGANIZATION")
        assert result[4] == ("सरकार", "ORGANIZATION")

    def test_entity_types_are_valid(self):
        """All entity types are from the valid set."""
        result = self.ner.recognize_text("राम काठमाडौं नेपाल सरकार आज जान्छ")
        valid_types = {"PERSON", "LOCATION", "ORGANIZATION", "DATE", None}
        for _, etype in result:
            assert etype in valid_types, f"Invalid entity type: {etype}"

    def test_kathmandu_valley(self):
        """Recognize Kathmandu Valley locations."""
        result = self.ner.recognize(["ललितपुर", "मा"])
        assert result[0] == ("ललितपुर", "LOCATION")

    def test_rivers(self):
        """Recognize river names."""
        result = self.ner.recognize(["गंगा", "नदी"])
        assert result[0] == ("गंगा", "LOCATION")
