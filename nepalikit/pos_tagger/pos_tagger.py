"""
pos_tagger.py

Part-of-Speech tagger for Nepali language.
Uses a dictionary-based approach with rule-based fallback.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""

import json
import re
from importlib import resources


class NepaliPOSTagger:
    """
    Part-of-Speech tagger for Nepali.

    Tags tokens into grammatical categories:
    N_NN (noun), N_NNP (proper noun), V_VM (verb),
    ADJ (adjective), ADV (adverb), POSTP (postposition),
    CONJ (conjunction), PART (particle), PUNC (punctuation).

    Uses a dictionary for known words and suffix rules for unknowns.
    """

    TAGS = {
        'N_NN': 'Noun',
        'N_NNP': 'Proper Noun',
        'V_VM': 'Verb',
        'ADJ': 'Adjective',
        'ADV': 'Adverb',
        'PRON': 'Pronoun',
        'POSTP': 'Postposition',
        'CONJ': 'Conjunction',
        'PART': 'Particle',
        'INTJ': 'Interjection',
        'PUNC': 'Punctuation',
    }

    VERB_SUFFIXES = [
        'छ', 'छन्', 'छौँ', 'छु', 'छैन', 'छैनन्',
        'हुन्छ', 'हुन्न', 'हुन्छन्', 'हुन्नन्',
        'हुन्', 'हुने', 'हुँदै', 'हुँदैन',
        'थियो', 'थिए', 'थिएन', 'थिएनन्',
        'गर्', 'भन्', 'जान्', 'आउन्',
        'लाग्', 'पर्', 'सक्', 'सक्छ',
        'नु', 'ने', 'ना', 'इन्', 'उन्',
        'योग्य', 'सक्ने', 'गर्ने', 'भन्ने',
    ]

    PRONOUNS = {
        'म', 'मैं', 'मलाई', 'मेरो', 'मेरा', 'मैले', 'मसँग',
        'तिमी', 'तिमीलाई', 'तिम्रो', 'तिमीले', 'तिमीसँग',
        'तपाईं', 'तपाईंलाई', 'तपाईंको', 'तपाईंले', 'तपाईंसँग',
        'उ', 'उसले', 'उसको', 'उसलाई', 'उससँग',
        'ऊ', 'ऊले', 'ऊको', 'ऊलाई',
        'हामी', 'हामीलाई', 'हाम्रो', 'हामीले', 'हामीसँग',
        'तिमीहरू', 'तिमीहरूलाई', 'तिमीहरूको',
        'तपाईंहरू', 'तपाईंहरूलाई', 'तपाईंहरूको',
        'उनी', 'उनीहरू', 'उनले', 'उनको', 'उनलाई', 'उनसँग',
        'यो', 'यहाँ', 'त्यो', 'त्यहाँ',
        'कसले', 'कसको', 'कसलाई',
        'जो', 'जसले', 'जसको', 'जसलाई',
        'के', 'कुनै', 'सबै', 'अरू', 'अन्य',
    }

    POSTPOSITIONS = {
        'मा', 'बाट', 'लाई', 'को', 'का', 'की', 'ले',
        'सँग', 'प्रति', 'द्वारा', 'माथि', 'तल',
        'अघि', 'पछि', 'बीच', 'तर्फ', 'नजिक', 'देखि',
        'सहित', 'समेत', 'अनुसार', 'विपरीत', 'गत',
        'मध्ये', 'परि', 'सम्बन्धी',
    }

    CONJUNCTIONS = {
        'र', 'तर', 'किनभने', 'वा', 'अथवा', 'तथा',
        'यदि', 'अर्थात्', 'जस्तै',
    }

    PARTICLES = {
        'पनि', 'नै', 'त', 'चाहिँ', 'कि', 'भने',
        'होइन', 'हैन', 'नि', 'न', 'मात्र',
    }

    def __init__(self):
        pkg = resources.files("nepalikit")
        dict_path = str(pkg.joinpath("data", "pos_dictionary.json"))
        self.dictionary = {}
        try:
            with open(dict_path, "r", encoding="utf-8") as f:
                self.dictionary = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    def tag(self, tokens):
        """
        Tag a list of tokens with POS labels.

        Args:
            tokens (list): List of string tokens.

        Returns:
            list: List of (token, tag) tuples.
        """
        result = []
        for token in tokens:
            tag = self._tag_single(token)
            result.append((token, tag))
        return result

    def tag_text(self, text):
        """
        Tokenize and tag text.

        Args:
            text (str): Input Nepali text.

        Returns:
            list: List of (token, tag) tuples.
        """
        tokens = text.split()
        return self.tag(tokens)

    def _tag_single(self, token):
        """Determine POS tag for a single token."""
        if not token:
            return 'PUNC'

        if re.match(r'^[।,;?!—\-\.\:\(\)\[\]]+$', token):
            return 'PUNC'

        if token in self.dictionary:
            return self.dictionary[token]

        clean = token.strip('।,;?!—-')

        if clean in self.PRONOUNS:
            return 'PRON'
        if clean in self.POSTPOSITIONS:
            return 'POSTP'
        if clean in self.CONJUNCTIONS:
            return 'CONJ'
        if clean in self.PARTICLES:
            return 'PART'

        if self._is_proper_noun(clean):
            return 'N_NNP'

        if self._has_verb_suffix(clean):
            return 'V_VM'

        if self._has_adjective_suffix(clean):
            return 'ADJ'

        if self._has_adverb_suffix(clean):
            return 'ADV'

        return 'N_NN'

    def _is_proper_noun(self, word):
        """Check if word looks like a proper noun (first letter is uppercase Latin)."""
        if not word:
            return False
        if word[0].isupper() and word[0].isalpha():
            return True
        return False

    def _has_verb_suffix(self, word):
        """Check if word ends with a common verb suffix."""
        for suffix in self.VERB_SUFFIXES:
            if word.endswith(suffix) and len(word) > len(suffix):
                return True
        return False

    def _has_adjective_suffix(self, word):
        """Check if word ends with a common adjective suffix."""
        adj_suffixes = ['योग्य', 'मय', 'पूर्ण', 'हीन', 'वान', 'लु', 'दार']
        for suffix in adj_suffixes:
            if word.endswith(suffix) and len(word) > len(suffix):
                return True
        return False

    def _has_adverb_suffix(self, word):
        """Check if word ends with a common adverb suffix."""
        adv_suffixes = ['तर', 'रीति', 'शैली', 'पनि']
        for suffix in adv_suffixes:
            if word.endswith(suffix) and len(word) > len(suffix):
                return True
        return False


def tag_pos(tokens):
    """
    Convenience function to POS-tag tokens.

    Args:
        tokens (list): List of string tokens.

    Returns:
        list: List of (token, tag) tuples.
    """
    return NepaliPOSTagger().tag(tokens)
