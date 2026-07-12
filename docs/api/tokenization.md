# Tokenization API

## Overview

NepaliKit provides two tokenization methods:

1. **Rule-based**: Splits text based on linguistic rules
2. **SentencePiece**: Uses pre-trained SentencePiece model

## Classes

### `Tokenizer`

Rule-based tokenizer for Nepali text.

```python
from nepalikit.tokenization import Tokenizer

tokenizer = Tokenizer()

# Word tokenization
tokens = tokenizer.tokenize("म घर जाँदै छु।", level='word')
print(tokens)

# Sentence tokenization
sentences = tokenizer.tokenize("नमस्ते। के छ खबर?", level='sentence')
print(sentences)

# Character tokenization
chars = tokenizer.tokenize("नेपाल", level='characters')
print(chars)
```

### `SentencePieceTokenizer`

SentencePiece-based tokenizer using pre-trained model.

```python
from nepalikit.tokenization import SentencePieceTokenizer

tokenizer = SentencePieceTokenizer()
tokens = tokenizer.tokenize("नमस्ते, के छ खबर?")
print(tokens)

# Detokenize
original = tokenizer.detokenize(tokens)
print(original)
```

## Methods

### `Tokenizer.tokenize(text, level='word', new_punctuation=None)`

Tokenize input text.

**Parameters:**
- `text` (str): Input text
- `level` (str): 'word', 'sentence', or 'characters'
- `new_punctuation` (list, optional): Additional punctuation marks

**Returns:** List of tokens

### `Tokenizer.detokenize(tokens, level='word')`

Detokenize tokens back to text.

**Parameters:**
- `tokens` (list): List of tokens
- `level` (str): 'word', 'sentence', or 'characters'

**Returns:** Detokenized text

### `SentencePieceTokenizer.tokenize(text)`

Tokenize text using SentencePiece model.

**Parameters:**
- `text` (str): Input text

**Returns:** List of tokens

### `SentencePieceTokenizer.detokenize(tokens)`

Detokenize tokens back to text.

**Parameters:**
- `tokens` (list): List of tokens

**Returns:** Detokenized text
