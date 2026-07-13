"""
train.py

Train SentencePiece model for NepaliKit package.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""

import logging
from pathlib import Path

import sentencepiece as spm

logger = logging.getLogger(__name__)


def train_model(
    input_path,
    model_prefix="NepaliKit_sentencepiece",
    vocab_size=10000,
    model_type="bpe",
):
    """Train a SentencePiece model on the given input file.

    Args:
        input_path (str or Path): Path to the training text file.
        model_prefix (str): Output model prefix.
        vocab_size (int): Vocabulary size.
        model_type (str): Model type ('bpe' or 'unigram').

    Raises:
        FileNotFoundError: If input_path does not exist.
    """
    input_path = Path(input_path)
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    spm.SentencePieceTrainer.train(
        input=str(input_path),
        model_prefix=model_prefix,
        vocab_size=vocab_size,
        model_type=model_type,
        num_threads=8,
    )
    logger.info(
        "SentencePiece model trained successfully and saved as %s.model", model_prefix
    )
