# NepaliKit

NepaliKit is a Python library for natural language processing tasks in Nepali language.

## Installation

You can install NepaliKit using pip:
```
pip install NepaliKit
```


## Features

Certainly! Here's an expanded section for the features of NepaliKit:

## Features

- **Tokenization**: Tokenize Nepali text using SentencePiece tokenizer.
- **Preprocessing**: Clean and preprocess Nepali text data including removing HTML tags, special characters, and performing other text cleaning tasks.
- **Stopword Management**: Load, add, and remove stopwords from Nepali text.
- **Sentence Operations**: Segment Nepali text into sentences based on punctuation marks.
- **SentencePiece Model Training**: Train custom SentencePiece models for Nepali text data.
- **Utility Functions**: Various utility functions for text processing and manipulation.
- **Integration with PyTorch**: Utilities for integrating with PyTorch for machine learning tasks.

## Usage

### Tokenization Example

```python
from NepaliKit.tokenization import SentencePieceTokenizer

text = "नमस्ते, के छ खबर?"
tokenizer = SentencePieceTokenizer()
tokens = tokenizer.tokenize(text)
print(tokens)
```

## Preprocessing Example

```python
from NepaliKit.preprocessing import remove_html_tags, remove_special_characters

text = "<p>नमस्ते, के छ खबर?</p>"
clean_text = remove_html_tags(text)
clean_text = remove_special_characters(clean_text)
print(clean_text)
```

## Stopword Example 
```python
from NepaliKit.manage_stopwords import load_stopwords, add_stopword, remove_stopword

stopwords = load_stopwords('/path/to/stopword/directory')
add_stopword('नयाँ_स्टापवर्ड')
remove_stopword('कुनै_स्टापवर्ड')
```
## License
This project is licensed under the MIT License.

## Author
- Prabhash Kumar Jha
- Email: prabhashj07@gmail.com
