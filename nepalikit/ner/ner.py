"""
ner.py

Named Entity Recognition for Nepali text.

Provides dictionary-based and rule-based NER for identifying
PERSON, LOCATION, ORGANIZATION, and DATE entities.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2026
"""

import json
import logging
import re
from pathlib import Path

logger = logging.getLogger(__name__)


class NepaliNER:
    """Named Entity Recognizer for Nepali text.

    Identifies four entity types:
    - PERSON: Names of people
    - LOCATION: Place names, countries, cities, geographical features
    - ORGANIZATION: Government bodies, companies, institutions
    - DATE: Date expressions and time references

    Features:
        - Dictionary-based entity matching
        - Rule-based patterns for dates and numbers
        - Context-aware entity boundary detection
        - Zero-dependency (pure Python)

    Attributes:
        entities: dict mapping entity type to set of known entities
        date_patterns: list of compiled regex patterns for dates
    """

    def __init__(self, dictionary_path=None):
        """Initialize the NER module.

        Args:
            dictionary_path: Optional path to a custom JSON dictionary.
                If None, uses the bundled ner_dictionary.json.
        """
        self.entities = {"PERSON": set(), "LOCATION": set(), "ORGANIZATION": set()}
        self.date_patterns = []

        if dictionary_path:
            self._load_dictionary(Path(dictionary_path))
        else:
            self._load_bundled()

        self._init_date_patterns()

    def _load_bundled(self):
        """Load the bundled NER dictionary."""
        try:
            data_dir = Path(__file__).parent.parent / "data"
            dict_path = data_dir / "ner_dictionary.json"

            if dict_path.exists():
                self._load_dictionary(dict_path)
            else:
                logger.warning("Bundled NER dictionary not found")

        except Exception:
            logger.warning("Failed to load bundled NER dictionary")

    def _load_dictionary(self, path):
        """Load entity dictionary from a JSON file."""
        if not path.exists():
            raise FileNotFoundError(f"Dictionary file not found: {path}")

        with open(path, encoding="utf-8") as f:
            data = json.load(f)

        for entity_type, words in data.items():
            if entity_type in self.entities:
                self.entities[entity_type] = set(words)

    def _init_date_patterns(self):
        """Initialize regex patterns for date recognition."""
        months = "जनवरी|फेब्रुअरी|मार्च|अप्रिल|मे|जुन|जुलाई|अगस्ट|सेप्टेम्बर|अक्टोबर|नोभेम्बर|डिसेम्बर"
        relative = "आज|भोलि|हिजो|अहिले|त्यसपछि|त्यसअघि|पहिले|पछि"
        time_of_day = "बिहान|दिउँसो|साँझ|राति|बेलुका|साँझै"

        self.date_patterns = [
            re.compile(r"\d{4}[/\-]\d{1,2}[/\-]\d{1,2}"),
            re.compile(r"\d{1,2}[/\-]\d{1,2}[/\-]\d{4}"),
            re.compile(rf"^({months})$"),
            re.compile(rf"^({months})\s*\d{{1,2}}$"),
            re.compile(rf"^\d{{1,2}}\s*({months})$"),
            re.compile(rf"^({relative})$"),
            re.compile(rf"^({time_of_day})$"),
            re.compile(r"\d+\s*(वर्ष|महिना|दिन|घण्टा|मिनेट)"),
            re.compile(r"(सन्|AD|BC)\s*\d{4}"),
            re.compile(r"(वि\.?\s*सं\.?|BS)\s*\d{4}"),
        ]

    def _check_date(self, word):
        """Check if a word matches a date pattern."""
        for pattern in self.date_patterns:
            if pattern.fullmatch(word):
                return True
        return False

    def _check_date_phrase(self, tokens, start, end):
        """Check if a span of tokens forms a date expression."""
        if end > len(tokens):
            return False
        text = " ".join(tokens[start:end])
        for pattern in self.date_patterns:
            if pattern.search(text):
                return True
        return False

    def _get_entity_type(self, token):
        """Get entity type for a token."""
        for entity_type, entity_set in self.entities.items():
            if token in entity_set:
                return entity_type
        return None

    def _check_compound(self, token, next_token):
        """Check if two tokens form a compound entity."""
        compound = f"{token} {next_token}"
        for entity_type, entity_set in self.entities.items():
            if compound in entity_set:
                return entity_type
        return None

    def _resolve_ambiguity(self, token, context_tokens, position):
        """Resolve ambiguity when a token appears in multiple entity types."""
        possible_types = []
        for entity_type, entity_set in self.entities.items():
            if token in entity_set:
                possible_types.append(entity_type)

        if len(possible_types) == 1:
            return possible_types[0]
        elif len(possible_types) > 1:
            # Prefer LOCATION for geographical/country names
            if "LOCATION" in possible_types and "PERSON" in possible_types:
                # Check context: if followed by location-like words, prefer LOCATION
                if position + 1 < len(context_tokens):
                    next_token = context_tokens[position + 1]
                    if next_token in ("मा", "बाट", "को", "तिर", "लाई", "सँग"):
                        return "LOCATION"
                # Country/city names that are also person names: prefer LOCATION
                location_preferring = {"नेपाल", "भारत", "गंगा", "यमुना"}
                if token in location_preferring:
                    return "LOCATION"
                return "PERSON"

            # For other ambiguities, prefer the more specific type
            if "ORGANIZATION" in possible_types:
                return "ORGANIZATION"
            if "LOCATION" in possible_types:
                return "LOCATION"

            return possible_types[0]

        return None

    def recognize(self, tokens):
        """Recognize named entities in a list of tokens.

        Args:
            tokens: List of word tokens.

        Returns:
            List of (token, entity_type) tuples.
            Tokens not identified as entities have entity_type=None.
        """
        if not tokens:
            return []

        results = []
        i = 0

        while i < len(tokens):
            token = tokens[i]

            # Check for date expression (multi-token)
            if i + 1 <= len(tokens):
                date_end = i + 1
                while date_end <= len(tokens) and self._check_date_phrase(tokens, i, date_end):
                    date_end += 1

                if date_end > i + 1:
                    for j in range(i, min(date_end, len(tokens))):
                        results.append((tokens[j], "DATE"))
                    i = date_end
                    continue

            # Check single token date
            if self._check_date(token):
                results.append((token, "DATE"))
                i += 1
                continue

            # Check for compound entity first
            if i + 1 < len(tokens):
                compound_type = self._check_compound(token, tokens[i + 1])
                if compound_type:
                    results.append((token, compound_type))
                    results.append((tokens[i + 1], compound_type))
                    i += 2
                    continue

            # Check for entity in dictionary
            entity_type = self._get_entity_type(token)

            if entity_type:
                # Resolve ambiguity
                resolved = self._resolve_ambiguity(token, tokens, i)
                results.append((token, resolved))
                i += 1
                continue

            # No entity found
            results.append((token, None))
            i += 1

        return results

    def recognize_text(self, text):
        """Recognize named entities in text.

        Args:
            text: Nepali text string.

        Returns:
            List of (token, entity_type) tuples.
        """
        if not text:
            return []

        tokens = text.split()
        return self.recognize(tokens)

    def extract_entities(self, text):
        """Extract entities as a dictionary of entity types to lists of entities.

        Args:
            text: Nepali text string.

        Returns:
            dict mapping entity_type to list of unique entity strings.
        """
        results = self.recognize_text(text)
        entities = {"PERSON": [], "LOCATION": [], "ORGANIZATION": [], "DATE": []}

        for token, entity_type in results:
            if entity_type and token not in entities[entity_type]:
                entities[entity_type].append(token)

        return entities


def recognize_entities(tokens):
    """Recognize named entities in tokens.

    Args:
        tokens: List of word tokens.

    Returns:
        List of (token, entity_type) tuples.
    """
    ner = NepaliNER()
    return ner.recognize(tokens)


def extract_entities(text):
    """Extract entities from text as a dictionary.

    Args:
        text: Nepali text string.

    Returns:
        dict mapping entity_type to list of unique entity strings.
    """
    ner = NepaliNER()
    return ner.extract_entities(text)
