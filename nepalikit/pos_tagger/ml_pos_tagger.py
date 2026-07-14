"""
ml_pos_tagger.py

ML-based POS tagger using n-gram statistics and Viterbi decoding.
Context-aware sequence labeling that considers surrounding tokens.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2026
"""

import json
import logging
import math
import re
from pathlib import Path

logger = logging.getLogger(__name__)

START = "<START>"
LOG_MIN = -20.0


class MLPOSTagger:
    """ML-based POS tagger using n-gram statistics and Viterbi decoding.

    Unlike the dictionary tagger which tags each word independently,
    this tagger considers context by using bigram transition probabilities
    and the Viterbi algorithm for optimal sequence labeling.

    Features:
        - Bigram transition model (probability of tag following tag)
        - Emission model (probability of word given tag)
        - Suffix-based emission hints for unknown words
        - Context pattern boosting for common grammatical sequences
        - Viterbi decoding for globally optimal tag sequence
        - Fallback to dictionary-based rules for unknown words

    Attributes:
        tags: list of valid POS tags
        transitions: dict of tag transition probabilities
        emissions: dict of word emission probabilities per tag
        suffix_rules: dict of suffix-to-tag mappings
        context_patterns: list of common tag sequences with boost weights
    """

    def __init__(self, model_path=None):
        """Initialize the ML POS tagger.

        Args:
            model_path: Optional path to a custom JSON model file.
                If None, uses the bundled pos_ngram_model.json.
        """
        self.tags = []
        self.transitions = {}
        self.emissions = {}
        self.suffix_rules = {}
        self.context_patterns = []

        if model_path:
            self._load_model(Path(model_path))
        else:
            self._load_bundled()

    def _load_bundled(self):
        """Load the bundled n-gram model."""
        try:
            data_dir = Path(__file__).parent.parent / "data"
            model_path = data_dir / "pos_ngram_model.json"

            if model_path.exists():
                self._load_model(model_path)
            else:
                logger.warning("Bundled POS model not found, using defaults")
                self._set_defaults()

        except Exception:
            logger.warning("Failed to load bundled POS model")
            self._set_defaults()

    def _load_model(self, path):
        """Load model from a JSON file."""
        if not path.exists():
            raise FileNotFoundError(f"Model file not found: {path}")

        with open(path, encoding="utf-8") as f:
            data = json.load(f)

        self.tags = data.get("tags", [])
        self.transitions = data.get("transitions", {})
        self.emissions = data.get("emissions", {})
        self.suffix_rules = data.get("suffix_rules", {})
        self.context_patterns = data.get("context_patterns", [])

    def _set_defaults(self):
        """Set minimal default values."""
        self.tags = ["N_NN", "V_VM", "PRON", "POSTP", "CONJ", "PART", "ADJ", "ADV", "PUNC"]
        self.transitions = {START: {t: 1.0 / len(self.tags) for t in self.tags}}
        self.emissions = {}
        self.suffix_rules = {}
        self.context_patterns = []

    def _log_prob(self, prob):
        """Convert probability to log probability with floor."""
        if prob <= 0:
            return LOG_MIN
        return max(math.log(prob), LOG_MIN)

    def _get_emission_prob(self, word, tag):
        """Get emission probability P(word|tag)."""
        # Punctuation gets high PUNC probability, low for everything else
        if re.match(r'^[\u0964\u0965,;!?\—\-\.\:\(\)\[\]\s]+$', word):
            return 0.99 if tag == "PUNC" else 0.0001

        tag_emissions = self.emissions.get(tag, {})

        # Exact match
        if word in tag_emissions:
            return tag_emissions[word]

        # Case-insensitive match for Latin
        if word.isascii():
            lower = word.lower()
            if lower in tag_emissions:
                return tag_emissions[lower] * 0.8

        # Suffix-based emission for unknown words
        for suffix in self.suffix_rules.get(tag, []):
            if word.endswith(suffix) and len(word) > len(suffix):
                return 0.01

        # Default emission
        return 0.001

    def _get_transition_prob(self, prev_tag, current_tag):
        """Get transition probability P(tag_i | tag_{i-1})."""
        tag_transitions = self.transitions.get(prev_tag, {})
        if current_tag in tag_transitions:
            return tag_transitions[current_tag]
        # Default uniform transition
        return 1.0 / max(len(self.tags), 1)

    def _apply_context_boost(self, tags_sequence, position):
        """Apply context pattern boost to a tag probability."""
        boost = 1.0
        for pattern_info in self.context_patterns:
            pattern = pattern_info.get("pattern", [])
            weight = pattern_info.get("weight", 1.0)
            pattern_len = len(pattern)

            if position >= pattern_len - 1:
                window = tags_sequence[position - pattern_len + 1 : position + 1]
                if window == pattern:
                    boost *= weight

        return boost

    def _classify_word(self, word):
        """Classify a single word into the most likely tag (standalone)."""
        # Punctuation
        if re.match(r"^[।\,;!?\—\-\.\:\(\)\[\]\s]+$", word):
            return "PUNC"

        # Suffix-based classification
        for tag, suffixes in self.suffix_rules.items():
            for suffix in suffixes:
                if word.endswith(suffix) and len(word) > len(suffix):
                    return tag

        # Check emission probabilities
        best_tag = "N_NN"
        best_score = -float("inf")
        for tag in self.tags:
            if tag == "PUNC":
                continue
            prob = self._get_emission_prob(word, tag)
            score = self._log_prob(prob)
            if score > best_score:
                best_score = score
                best_tag = tag

        return best_tag

    def viterbi(self, words):
        """Run Viterbi algorithm to find optimal tag sequence.

        Args:
            words: List of word tokens.

        Returns:
            List of (word, tag) tuples.
        """
        if not words:
            return []

        n = len(words)
        num_tags = len(self.tags)

        # DP tables
        viterbi_table = [[0.0] * num_tags for _ in range(n)]
        backpointer = [[0] * num_tags for _ in range(n)]

        # Initialization
        for j, tag in enumerate(self.tags):
            trans_prob = self._get_transition_prob(START, tag)
            emit_prob = self._get_emission_prob(words[0], tag)
            viterbi_table[0][j] = self._log_prob(trans_prob) + self._log_prob(emit_prob)

        # Recursion
        for i in range(1, n):
            for j, tag in enumerate(self.tags):
                max_score = -float("inf")
                max_prev = 0

                for k, prev_tag in enumerate(self.tags):
                    trans_prob = self._get_transition_prob(prev_tag, tag)
                    emit_prob = self._get_emission_prob(words[i], tag)
                    score = viterbi_table[i - 1][k] + self._log_prob(trans_prob) + self._log_prob(emit_prob)

                    # Context boost
                    if i >= 2:
                        prev_tags = [self.tags[backpointer[i - 1][k]], prev_tag, tag]
                        for cp in self.context_patterns:
                            pattern = cp.get("pattern", [])
                            weight = cp.get("weight", 1.0)
                            if len(pattern) == 3 and prev_tags == pattern:
                                score += math.log(weight)

                    if score > max_score:
                        max_score = score
                        max_prev = k

                viterbi_table[i][j] = max_score
                backpointer[i][j] = max_prev

        # Termination - find best final tag
        best_final_score = -float("inf")
        best_final_tag = 0
        for j in range(num_tags):
            if viterbi_table[n - 1][j] > best_final_score:
                best_final_score = viterbi_table[n - 1][j]
                best_final_tag = j

        # Backtrace
        tags_indices = [0] * n
        tags_indices[n - 1] = best_final_tag
        for i in range(n - 2, -1, -1):
            tags_indices[i] = backpointer[i + 1][tags_indices[i + 1]]

        return [(words[i], self.tags[tags_indices[i]]) for i in range(n)]

    def tag(self, tokens):
        """Tag a list of tokens using Viterbi decoding.

        Args:
            tokens: List of word strings.

        Returns:
            List of (token, tag) tuples.
        """
        if not tokens:
            return []

        return self.viterbi(tokens)

    def tag_text(self, text):
        """Tag text by splitting on whitespace and running Viterbi.

        Args:
            text: Nepali text string.

        Returns:
            List of (token, tag) tuples.
        """
        if not text:
            return []

        tokens = text.split()
        return self.tag(tokens)


def ml_tag_pos(tokens):
    """Tag POS using the ML tagger.

    Args:
        tokens: List of word strings.

    Returns:
        List of (token, tag) tuples.
    """
    tagger = MLPOSTagger()
    return tagger.tag(tokens)


def ml_tag_text(text):
    """Tag text using the ML tagger.

    Args:
        text: Nepali text string.

    Returns:
        List of (token, tag) tuples.
    """
    tagger = MLPOSTagger()
    return tagger.tag_text(text)
