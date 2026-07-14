# Sentence Operations

Tools for extracting, segmenting, and analyzing sentences in Nepali text.

## Features

- Sentence extraction from text
- Sentence segmentation with punctuation awareness
- Abbreviation-aware sentence splitting
- Sentence analysis (word count, character count, etc.)

## Basic Usage

```python
from nepalikit.sentence_operation import extract_sentences, SentenceAnalyzer

# Extract sentences (note: extract_sentences is a class, not a function)
text = "नमस्ते। के छ खबर? म ठिक छु।"
extractor = extract_sentences(text)
sentences = extractor.extract_sentences()
print(sentences)  # ['नमस्ते के छ खबर म ठिक छु']
```

!!! note
    `extract_sentences` internally normalizes and preprocesses text (lowercasing, special char removal, stopword removal), which strips punctuation. For punctuation-aware splitting, use `Tokenizer.tokenize(text, level='sentence')` instead.

## Analyzing Sentences

```python
from nepalikit.sentence_operation import SentenceAnalyzer

analyzer = SentenceAnalyzer()
stats = analyzer.sentence_stats("नमस्ते। के छ खबर?")
print(stats)
# {'char_count': 17, 'word_count': 4, 'stopword_count': 2, 'punctuation_count': 2}
```
