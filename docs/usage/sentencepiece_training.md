# Training SentencePiece Models

NepaliKit includes a utility for training custom SentencePiece models on your Nepali text corpus.

## Basic Usage

```python
from nepalikit.tokenization.sentencepiece.train import train_model

# Train a SentencePiece model
train_model(
    input_path="corpus.txt",
    model_prefix="nepali_sp",
    vocab_size=8000,
)
```

This generates `nepali_sp.model` and `nepali_sp.vocab` files that can be loaded by `SentencePieceTokenizer`.

## Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `input_path` | Path to training text corpus | Required |
| `model_prefix` | Output model filename prefix | `NepaliKit_sentencepiece` |
| `vocab_size` | Vocabulary size | 10000 |
| `model_type` | Model type: `unigram` or `bpe` | `bpe` |

See the [API reference](../api/sentencepiece_training.md) and [SentencePiece documentation](https://github.com/google/sentencepiece) for advanced options.
