# Future Roadmap

This document outlines planned features for NepaliKit releases.

## v1.0.5: Lemmatizer ✅ Completed

### Dictionary-based Lemmatizer
**Status:** Released (July 14, 2026)

Dictionary-based lemma lookup with rule-based fallback. 340+ dictionary entries, morphological rules for common Nepali suffixes.

## v1.0.6: ML POS Tagger ✅ Completed

### ML-based POS Tagger
**Status:** Released (July 14, 2026)

Context-aware POS tagger using n-gram statistics and Viterbi decoding. Bigram transition model, emission probabilities, suffix rules, and context pattern boosting. Zero-dependency pure Python implementation.

## v1.0.7: Named Entity Recognition

### NER Module
**Priority:** High
**Gap:** No NER capability at all.

**Implementation:**
- Create `nepalikit.ner` module
- Optional `torch`/`transformers` dependency
- Bundle pre-trained NER model (PERSON, LOCATION, ORGANIZATION, DATE)
- Lazy-load to keep zero-deps default

## v1.0.8: Word Embeddings

### Word Embeddings
**Priority:** Medium
**Gap:** No word embedding support.

**Implementation:**
- Create `nepalikit.embeddings` module
- Optional `fasttext`/`gensim` dependency
- Lazy-load pre-trained Nepali fastText/Word2Vec
- Support similarity, nearest neighbors, vector ops

## v1.0.9: Translation

### Translation
**Priority:** Medium
**Gap:** No translation support.

**Implementation:**
- Create `nepalikit.translation` module
- Optional `deep-translator` or `transformers` dependency
- Support Nepali to English and English to Nepali

## v1.0.10: Synonym Generator

### Synonym Generator
**Priority:** Medium
**Gap:** No synonym support.

**Implementation:**
- Create `nepalikit.synonyms` module
- Use pre-trained embeddings for nearest-neighbor synonyms
- Return ranked suggestions

## v1.0.11: Spell Checker v2

### Spell Checker Improvements
**Priority:** Medium
**Gap:** Current checker is basic. Could add n-gram frequency model and context-aware corrections.

**Implementation:**
- Add n-gram frequency model
- Add context-aware suggestions
- Add batch spell check for documents

## v1.1.0: Ecosystem

### Dataset Loaders
**Priority:** Low

**Implementation:**
- Create `nepalikit.datasets` module
- Download/cache from Hugging Face Hub
- Support: News, Sentiment, NER, QA, POS datasets

### Model Hub Integration
**Priority:** Low

**Implementation:**
- Create `nepalikit.model_hub` module
- Lazy-load Hugging Face models
- Support: NepNewsBERT, Sentiment, Sentence Similarity

### Benchmark Suite
**Priority:** Low

**Implementation:**
- Create `nepalikit.benchmarks` module
- Evaluate on Nepali NLP tasks
- Standardized evaluation metrics

## Summary

| Version | Feature | Priority | Status |
|---------|---------|----------|--------|
| 1.0.5 | Lemmatizer | High | ✅ Completed |
| 1.0.6 | ML POS Tagger | High | ✅ Completed |
| 1.0.7 | Named Entity Recognition | High | Planned |
| 1.0.8 | Word Embeddings | Medium | Planned |
| 1.0.9 | Translation | Medium | Planned |
| 1.0.10 | Synonym Generator | Medium | Planned |
| 1.0.11 | Spell Checker v2 | Medium | Planned |
| 1.1.0 | Dataset Loaders | Low | Future |
| 1.1.0 | Model Hub | Low | Future |
| 1.1.0 | Benchmark Suite | Low | Future |

## How to Contribute

We welcome contributions for these features!

1. **NER**: Build transformer-based NER with lazy loading
2. **Embeddings**: Create fastText/Word2Vec loaders
3. **Translation**: Wrap translation APIs/models
4. **Datasets**: Add download helpers for public datasets

**Guidelines:**
- Use lazy imports (`try/except ImportError`)
- Keep core zero-deps
- Document all optional dependencies
- Include examples in docs
- Write tests

---

**Last Updated:** July 2026
