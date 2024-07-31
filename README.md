NepaliKit
=========

[![Current Release Version](https://img.shields.io/github/release/prabhashj07/nepalikit.svg?style=flat-square&logo=github)](https://github.com/prabhashj07/nepalikit/releases)
[![pypi Version](https://img.shields.io/pypi/v/nepalikit.svg?style=flat-square&logo=pypi&logoColor=white)](https://pypi.org/project/NepaliKit/)
[![PyPi downloads](https://static.pepy.tech/personalized-badge/NepaliKit?period=total&units=international_system&left_color=grey&right_color=orange&left_text=pip%20downloads)](https://pypi.org/project/NepaliKit/)

NepaliKit is a Python library for natural language processing tasks in the Nepali language.

Installation
------------

You can install NepaliKit using pip:

    pip install nepalikit

Alternatively, you can clone the repository and install it manually:

    git clone https://github.com/prabhashj07/nepalikit.git
    cd nepalikit
    pip install .

Features
--------

NepaliKit provides the following features:

- **Tokenization**: Tokenize Nepali text using the SentencePiece tokenizer.
- **Preprocessing**: Clean and preprocess Nepali text data, including removing HTML tags, special characters, and other cleaning tasks.
- **Stopword Management**: Load and remove stopwords from Nepali text.
- **Sentence Operations**: Segment Nepali text into sentences based on punctuation marks.
- **SentencePiece Model Training**: Train custom SentencePiece models for Nepali text data.
- **Utility Functions**: Various utility functions for text processing and manipulation.
- **Integration with PyTorch**: Utilities for integrating with PyTorch for machine learning tasks.

Usage
-----

### Tokenization Example

#### Rule-based Tokenizer

```python
from nepalikit.tokenization import Tokenizer

text = "नमस्ते, के छ खबर? यो एउटा वाक्य हो।"
tokenizer = Tokenizer()

# Sentence tokenization
sentences = tokenizer.tokenize(text, level='sentence')
print(sentences)

# Word tokenization
words = tokenizer.tokenize(text, level='word')
print(words)

# Character tokenization
characters = tokenizer.tokenize(text, level='characters')
print(characters)
```

#### Sentence Piece Tokenizer

```python
from nepalikit.tokenization import SentencePieceTokenizer

text = "नमस्ते, के छ खबर?"
tokenizer = SentencePieceTokenizer()
tokens = tokenizer.tokenize(text)
print(tokens)

# Detokenization
original_text = tokenizer.detokenize(tokens)
print(original_text)
```

## Preprocessing Example

```python
from nepalikit.preprocessing import TextProcessor

text = "<p>नमस्ते, के छ खबर?</p>"
processor = TextProcessor()
clean_text = processor.remove_html_tags(text)
clean_text = processor.remove_special_characters(clean_text)
print(clean_text)
```
### Stopword Example 

```python
from nepalikit.manage_stopwords import load_stopwords, remove_stopword

stopwords = load_stopwords('/path/to/stopword/directory')
remove_stopword('कुनै_स्टापवर्ड')
```

## TextProcessor Class
----------------------

The `TextProcessor` class provides various methods for text preprocessing:

* `remove_html_tags(text)`: Removes HTML tags from the text.
* `remove_special_characters(text)`: Removes special characters, keeping only Devanagari characters and spaces.
* `remove_extra_whitespace(text)`: Removes extra whitespace from the text.
* `remove_stopwords(text)`: Removes stopwords from the text.
* `normalize_text(text)`: Converts the text to lowercase.
* `preprocess_text(text)`: Applies all preprocessing steps to the text.
* `get_word_frequency(tokens)`: Returns the frequency of words in a list of tokens.

## URLs and Emails Removal
--------------------------

The `urls_emails` class provides methods to remove or replace URLs and email addresses in the text:

* `replace_urls_emails(text)`: Replaces URLs and email addresses with specified replacements.
* `remove_urls_emails(text)`: Removes URLs and email addresses from the text.

## Sentence Operations
----------------------

The `sentence_operation` folder contains various modules for sentence-level operations:

* `extract_sentences.py`: Extracts sentences from text.
* `load_abbreviation.py`: Loads abbreviations for text processing.
* `normalize_text.py`: Normalizes text.
* `segment_sentences.py`: Segments text into sentences.
* `sentence_stats.py`: Provides statistics about sentences.

## Tokenizer Classes
--------------------

### Rule-based Tokenizer

The `Tokenizer` class provides the following methods:

* `sentence_tokenize(text)`: Tokenizes input text into sentences based on '।' character.
* `word_tokenize(sentence, new_punctuation=None)`: Tokenizes input sentence into words, handling specified punctuation.
* `character_tokenize(word)`: Tokenizes input word into characters.
* `tokenize(text, level='word', new_punctuation=None)`: General tokenization method for sentence, word, or character level.
* `sentence_detokenize(sentences)`: Detokenizes a list of sentences back into the original text.
* `word_detokenize(words)`: Detokenizes a list of words back into the original sentence.
* `character_detokenize(characters)`: Detokenizes a list of characters back into the original word.
* `detokenize(tokens, level='word')`: General detokenization method for sentence, word, or character level.

### SentencePiece Tokenizer

The `SentencePieceTokenizer` class provides the following methods:

* `tokenize(text)`: Tokenizes text using the SentencePiece model.
* `detokenize(tokens)`: Detokenizes text using the SentencePiece model.


## NepaliTextProcessor Class
----------------------------

The `NepaliTextProcessor` class in `utils.py` offers additional text processing capabilities:

* `merge_text(tokens)`: Merges a list of tokens into a single string.
* `split_text(text)`: Splits a text string into a list of tokens.
* `count_words(text)`: Counts the number of words in a text string.
* `count_words_in_paragraph(paragraph)`: Counts the total number of words in a paragraph.

License
-----
This project is licensed under the MIT License. 

Author
-----
- Prabhash Kumar Jha
- Email: prabhashj07@gmail.com
