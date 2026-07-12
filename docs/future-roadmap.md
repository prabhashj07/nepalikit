# Future Roadmap

This document outlines features planned for future releases of NepaliKit.

## Phase 2.3: Ecosystem & Infrastructure

### Dataset Loaders
**Status:** Planned
**Priority:** Low
**Challenge:** No library currently provides packaged dataset loaders. Community-curated dataset lists exist but require download helpers.

**Implementation Path:**
- Create `nepalikit.datasets` module
- Download and cache datasets from GitHub/Hugging Face
- Support for: News, Sentiment, NER, QA datasets

### Model Hub Integration
**Status:** Planned
**Priority:** Low
**Challenge:** No library provides packaged model hub integration. Pre-trained models exist on Hugging Face but require lazy-loading wrappers.

**Implementation Path:**
- Create `nepalikit.model_hub` module
- Lazy-load Hugging Face models
- Support for: NepNewsBERT, Sentiment Analysis, Sentence Similarity

### Benchmark Integration
**Status:** Planned
**Priority:** Low
**Challenge:** No library provides packaged benchmark integration. NLUE benchmark exists but requires evaluation utilities.

**Implementation Path:**
- Create `nepalikit.benchmarks` module
- Evaluate models on NLUE tasks
- Support for: Classification, NLI, QA, NER

## Phase 3: Advanced AI

### Named Entity Recognition (NER)
**Status:** Future
**Priority:** Medium
**Challenge:** Requires pre-trained models. No library packages NER models; they exist as separate research artifacts.

**Current Landscape:**
- Research models exist but are not packaged as Python libraries

**Implementation Path:**
- Add optional `torch`/`transformers` dependency
- Create `nepalikit.ner` module
- Load pre-trained NER models lazily
- Support for: PERSON, LOCATION, ORGANIZATION, DATE

### Word Embeddings
**Status:** Future
**Priority:** Low
**Challenge:** Requires pre-trained model files (fastText/Word2Vec). No library packages these.

**Current Landscape:**
- Academic models exist but not packaged

**Implementation Path:**
- Add optional `fasttext`/`gensim` dependency
- Create `nepalikit.embeddings` module
- Load pre-trained embeddings lazily
- Support for: Similarity, Nearest Neighbors, Vector Operations

## Summary

| Phase | Feature | Status | Priority |
|-------|---------|--------|----------|
| 2.3 | Dataset Loaders | Planned | Low |
| 2.3 | Model Hub Integration | Planned | Low |
| 2.3 | Benchmark Integration | Planned | Low |
| 3 | NER | Future | Medium |
| 3 | Word Embeddings | Future | Low |

## How to Contribute

We welcome contributions for these features! Here's how you can help:

1. **Dataset Loaders**: Add download helpers for public datasets
2. **Model Hub**: Create wrappers for Hugging Face models
3. **NER**: Integrate NER models with lazy loading
4. **Embeddings**: Add fastText/Word2Vec loaders

**Guidelines:**
- Use lazy imports (`try/except ImportError`)
- Document all dependencies
- Include examples in README
- Write comprehensive tests

---

**Last Updated:** January 2026
