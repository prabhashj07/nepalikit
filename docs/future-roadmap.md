# Future Roadmap

This document outlines planned features for NepaliKit releases.

## v1.0.5: Production Readiness

### Lemmatizer
**Priority:** High
**Gap:** Current stemming is suffix-strip only. No dictionary-based lemmatization.

**Implementation:**
- Create `nepalikit.lemmatizer` module
- Dictionary-based lemma lookup + rule fallback
- Optional: wrap `transformers` for neural lemmatizer

### ML-based POS Tagger
**Priority:** High
**Gap:** Current POS is dictionary-only. No trained model.

**Implementation:**
- Create `nepalikit.pos_tagger.ml` module
- Optional `torch`/`transformers` dependency
- Bundle a pre-trained BiLSTM-CRF model
- Fallback to dictionary tagger when torch unavailable

### Named Entity Recognition
**Priority:** High
**Gap:** No NER capability at all.

**Implementation:**
- Create `nepalikit.ner` module
- Optional `torch`/`transformers` dependency
- Bundle pre-trained NER model (PERSON, LOCATION, ORGANIZATION, DATE)
- Lazy-load to keep zero-deps default

## v1.1.0: Advanced NLP

### Word Embeddings
**Priority:** Medium
**Gap:** No word embedding support.

**Implementation:**
- Create `nepalikit.embeddings` module
- Optional `fasttext`/`gensim` dependency
- Lazy-load pre-trained Nepali fastText/Word2Vec
- Support similarity, nearest neighbors, vector ops

### Translation
**Priority:** Medium
**Gap:** No translation support.

**Implementation:**
- Create `nepalikit.translation` module
- Optional `deep-translator` or `transformers` dependency
- Support Nepali↔English

### Synonym Generator
**Priority:** Medium
**Gap:** No synonym support.

**Implementation:**
- Create `nepalikit.synonyms` module
- Use pre-trained embeddings for nearest-neighbor synonyms
- Return ranked suggestions

### Spell Checker Improvements
**Priority:** Medium
**Gap:** Current checker is basic. Could add n-gram frequency model and context-aware corrections.

**Implementation:**
- Add n-gram frequency model
- Add context-aware suggestions
- Add batch spell check for documents

## v2.0.0: Ecosystem

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
| 1.0.5 | Lemmatizer | High | Planned |
| 1.0.5 | ML POS Tagger | High | Planned |
| 1.0.5 | Named Entity Recognition | High | Planned |
| 1.1.0 | Word Embeddings | Medium | Planned |
| 1.1.0 | Translation | Medium | Planned |
| 1.1.0 | Synonym Generator | Medium | Planned |
| 1.1.0 | Spell Checker v2 | Medium | Planned |
| 2.0.0 | Dataset Loaders | Low | Future |
| 2.0.0 | Model Hub | Low | Future |
| 2.0.0 | Benchmark Suite | Low | Future |

## How to Contribute

We welcome contributions for these features!

1. **Lemmatizer**: Build dictionary + rule hybrid
2. **ML POS/NER**: Train models, create lazy-loading wrappers
3. **Embeddings**: Create fastText/Word2Vec loaders
4. **Translation**: Wrap translation APIs/models
5. **Datasets**: Add download helpers for public datasets

**Guidelines:**
- Use lazy imports (`try/except ImportError`)
- Keep core zero-deps
- Document all optional dependencies
- Include examples in docs
- Write tests

---

**Last Updated:** July 2026
