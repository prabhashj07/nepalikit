"""
POS tagger module for Nepali language.

Provides dictionary-based and ML-based part-of-speech tagging.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""

from nepalikit.pos_tagger.pos_tagger import NepaliPOSTagger, tag_pos
from nepalikit.pos_tagger.ml_pos_tagger import MLPOSTagger, ml_tag_pos, ml_tag_text

__all__ = [
    "NepaliPOSTagger",
    "tag_pos",
    "MLPOSTagger",
    "ml_tag_pos",
    "ml_tag_text",
]
