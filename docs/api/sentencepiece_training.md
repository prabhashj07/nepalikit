# SentencePiece Training API

## Overview

Utilities for training SentencePiece models on Nepali text corpora.

## Functions

### `train_model(input_path, model_prefix="NepaliKit_sentencepiece", vocab_size=10000, model_type="bpe")`

Train a SentencePiece model on the given input file.

```python
from nepalikit.tokenization.sentencepiece.train import train_model

# Train a BPE model
train_model("corpus.txt", model_prefix="my_model", vocab_size=5000)
```

**Parameters:**
- `input_path` (str or Path): Path to the training text file
- `model_prefix` (str): Output model prefix (default: `"NepaliKit_sentencepiece"`)
- `vocab_size` (int): Vocabulary size (default: `10000`)
- `model_type` (str): Model type, `'bpe'` or `'unigram'` (default: `"bpe"`)

**Raises:**
- `FileNotFoundError`: If `input_path` does not exist

**Output:**
Creates `{model_prefix}.model` and `{model_prefix}.vocab` files in the current directory.
