# Segmentation API

## Overview

Sentence segmentation and text analysis utilities.

## Functions

### `segment_sentences(text)`

Segment text into sentences.

```python
from nepalikit.sentence_operation import segment_sentences

sentences = segment_sentences("नमस्ते। के छ खबर? राम्रो छ।")
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

### `extract_sentences`

A class to extract sentences from Nepali text. Includes normalization
and preprocessing via `TextProcessor`.

```python
from nepalikit.sentence_operation import extract_sentences

extractor = extract_sentences("नमस्ते। के छ खबर?")
sentences = extractor.extract_sentences()
print(sentences)
```

### `AbbreviationReplacer`

Replace abbreviations in text with their expanded forms.

```python
from nepalikit.sentence_operation import AbbreviationReplacer

abbrevs = {"उ.मा.वि.": "उच्च माध्यमिक विद्यालय", "प्रा.": "प्राथमिक"}
replacer = AbbreviationReplacer(abbrevs)
text = "उ.मा.वि. मा पढ्छु।"
expanded = replacer.replace_abbreviations(text)
print(expanded)  # "उच्च माध्यमिक विद्यालय मा पढ्छु।"
```

### `TextNormalizer`

Normalize Unicode characters in Nepali text using NFKC normalization.

```python
from nepalikit.sentence_operation import TextNormalizer

normalizer = TextNormalizer("म  नाम")
result = normalizer.normalize()
print(result)
```

### `SentenceAnalyzer`

Compute statistics for a given Nepali sentence.

```python
from nepalikit.sentence_operation import SentenceAnalyzer

analyzer = SentenceAnalyzer()
stats = analyzer.sentence_stats("नमस्ते। के छ खबर?")
print(stats)
# {'char_count': 17, 'word_count': 4, 'stopword_count': 2, 'punctuation_count': 2}
```

## Methods

### `extract_sentences.extract_sentences()`

Extract and return a list of sentences from the text.

**Returns:** List of sentence strings

### `extract_sentences.normalize_text()`

Normalize the text using TextProcessor.

**Returns:** Normalized text string

### `extract_sentences.preprocess_text(normalized_text)`

Preprocess the normalized text using TextProcessor.

**Parameters:**
- `normalized_text` (str): Normalized text to preprocess

**Returns:** Preprocessed text string

### `AbbreviationReplacer.replace_abbreviations(text)`

Replace all abbreviations in text with their expanded forms.

**Parameters:**
- `text` (str): Input text containing abbreviations

**Returns:** Text with abbreviations replaced

### `SentenceAnalyzer.sentence_stats(sentence)`

Compute statistics for a given sentence.

**Parameters:**
- `sentence` (str): The sentence to analyze

**Returns:** dict with keys: `char_count`, `word_count`, `stopword_count`, `punctuation_count`

### `TextNormalizer.normalize()`

Normalize Unicode characters using NFKC form.

**Returns:** Normalized text string

### `segment_sentences(text)`

Segment text into sentences based on punctuation.

**Parameters:**
- `text` (str): Input text

**Returns:** List of sentences

### `load_abbreviations(folder_path)`

Load abbreviations from text files in folder.

**Parameters:**
- `folder_path` (str): Path to folder with abbreviation files

**Returns:** Dictionary mapping abbreviations to expanded forms
