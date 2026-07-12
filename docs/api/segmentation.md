# Segmentation API

## Overview

Sentence segmentation and text analysis utilities.

## Functions

### `segment_sentences(text)`

Segment text into sentences.

```python
from nepalikit.sentence_operation import segment_sentences

sentences = segment_sentences("नमस्ते। के छ खबर? राम्रो छ।")
print(sentences)  # ["नमस्ते।", "के छ खबर?", "राम्रो छ।"]
```

### `extract_sentences(text)`

Extract sentences from text.

```python
from nepalikit.sentence_operation import extract_sentences

extractor = extract_sentences()
sentences = extractor.extract("नमस्ते। के छ खबर?")
print(sentences)
```

### `load_abbreviations(folder_path)`

Load abbreviations from text files.

```python
from nepalikit.sentence_operation import load_abbreviations

abbreviations = load_abbreviations("/path/to/abbreviations/")
print(abbreviations)
```

## Classes

### `AbbreviationReplacer`

Replace abbreviations in text.

```python
from nepalikit.sentence_operation import AbbreviationReplacer

replacer = AbbreviationReplacer()
text = "उ.मा.वि. मा पढ्छु।"
expanded = replacer.replace_abbreviations(text)
print(expanded)
```

### `SentenceAnalyzer`

Analyze sentence statistics.

```python
from nepalikit.sentence_operation import SentenceAnalyzer

analyzer = SentenceAnalyzer()
stats = analyzer.analyze("नमस्ते। के छ खबर?")
print(stats)
```

## Methods

### `segment_sentences(text)`

Segment text into sentences based on punctuation.

**Parameters:**
- `text` (str): Input text

**Returns:** List of sentences

### `load_abbreviations(folder_path)`

Load abbreviations from text files in folder.

**Parameters:**
- `folder_path` (str): Path to folder with abbreviation files

**Returns:** Dictionary of abbreviations
