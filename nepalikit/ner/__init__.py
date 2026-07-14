"""
Named Entity Recognition module for Nepali language.

Provides dictionary-based and rule-based NER for identifying
PERSON, LOCATION, ORGANIZATION, and DATE entities.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2026
"""

from nepalikit.ner.ner import NepaliNER, extract_entities, recognize_entities

__all__ = [
    "NepaliNER",
    "recognize_entities",
    "extract_entities",
]
