"""
train.py

Train SentencePiece model for NepaliKit package.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""

import os
import sentencepiece as spm

# Define paths and parameters
data_dir = "./data"
input_data = os.path.join(data_dir, "OSCAR Corpus Nepali", "ne.txt")
model_prefix = "NepaliKit_sentencepiece"
vocab_size = 10000
model_type = "bpe"

# Create a smaller subset of the data
subset_data = os.path.join(data_dir, "OSCAR Corpus Nepali", "ne_subset.txt")
num_lines = 100000  

with open(input_data, 'r', encoding='utf-8') as infile, open(subset_data, 'w', encoding='utf-8') as outfile:
    for _ in range(num_lines):
        line = infile.readline()
        if not line:
            break
        outfile.write(line)

# Train SentencePiece model on the subset
spm.SentencePieceTrainer.train(
    input=subset_data,
    model_prefix=model_prefix,
    vocab_size=vocab_size,
    model_type=model_type,
    num_threads=8
)

# Print confirmation
print(f"SentencePiece model trained successfully and saved as {model_prefix}.model")

