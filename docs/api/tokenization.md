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

### `Tokenizer.sentence_tokenize(text)`

Tokenize text into sentences based on `।` character.

**Parameters:**
- `text` (str): Input text

**Returns:** List of sentence strings

### `Tokenizer.word_tokenize(sentence, new_punctuation=None)`

Tokenize a sentence into words.

**Parameters:**
- `sentence` (str): Input sentence
- `new_punctuation` (list, optional): Additional punctuation marks to split on

**Returns:** List of word strings

### `Tokenizer.character_tokenize(word)`

Tokenize a word into characters.

**Parameters:**
- `word` (str): Input word

**Returns:** List of character strings

### `Tokenizer.tokenize(text, level='word', new_punctuation=None)`

General tokenization method.

**Parameters:**
- `text` (str): Input text
- `level` (str): 'word', 'sentence', or 'character'
- `new_punctuation` (list, optional): Additional punctuation marks

**Returns:** List of tokens

### `Tokenizer.sentence_detokenize(sentences)`

Join sentences back with `।` delimiter.

**Parameters:**
- `sentences` (list): List of sentence strings

**Returns:** Detokenized text

### `Tokenizer.word_detokenize(words)`

Join words with spaces.

**Parameters:**
- `words` (list): List of word strings

**Returns:** Detokenized sentence

### `Tokenizer.character_detokenize(characters)`

Join characters without spaces.

**Parameters:**
- `characters` (list): List of character strings

**Returns:** Detokenized word

### `Tokenizer.detokenize(tokens, level='word')`

General detokenization method.

**Parameters:**
- `tokens` (list): List of tokens
- `level` (str): 'word', 'sentence', or 'character'

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
