# Tokenization

NepaliKit provides two tokenization approaches: rule-based and SentencePiece-based.

## Rule-Based Tokenizer

The `Tokenizer` class splits text using linguistic rules for Nepali. It supports three levels:

- **Word**: Splits on whitespace and punctuation
- **Sentence**: Splits on sentence boundaries (`।`, `॥`, `?`, `!`)
- **Character**: Splits into individual characters

```python
from nepalikit.tokenization import Tokenizer

tokenizer = Tokenizer()

# Word tokenization
tokens = tokenizer.tokenize("म घर जाँदै छु।", level='word')
print(tokens)  # ['म', 'घर', 'जाँदै', 'छु']

# Sentence tokenization
sentences = tokenizer.tokenize("नमस्ते। के छ खबर?", level='sentence')
print(sentences)  # ['नमस्ते।', 'के छ खबर?']

# Character tokenization
chars = tokenizer.tokenize("नेपाल", level='characters')
print(chars)  # ['न', 'े', 'प', 'ा', 'ल']
```

## SentencePiece Tokenizer

The `SentencePieceTokenizer` uses a pre-trained SentencePiece model for subword tokenization, useful for neural NLP models.

```python
from nepalikit.tokenization import SentencePieceTokenizer

tokenizer = SentencePieceTokenizer()
tokens = tokenizer.tokenize("नमस्ते, के छ खबर?")
print(tokens)

# Convert back to text
original = tokenizer.detokenize(tokens)
print(original)
```

## When to Use Which

| Tokenizer | Best For |
|-----------|----------|
| Rule-based | General text processing, rule-based pipelines |
| SentencePiece | Neural models, handling OOV words, subword modeling |
