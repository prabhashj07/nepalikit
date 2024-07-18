"""
load_stopwords.py

Load stopwords from text files in a specified folder.

Author: Prabhash Kumar Jha
Email: prabhashj07@gmail.com
Date: July 2024
"""

import os

def load_stopwords(folder_path):
    """
    Load stopwords from text files in the specified folder.

    Args:
        folder_path (str): Path to the folder containing stopwords text files.

    Returns:
        dict: A dictionary where keys are filenames and values are lists of stopwords.
    """
    stopword_dict = {}
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):  # Ensure only text files are considered
            with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as file:
                stopwords = [line.strip() for line in file.readlines()]
                stopword_dict[filename] = stopwords
    return stopword_dict

def main():
    """
    Example usage of load_stopwords function.
    """
    stopwords_folder = "/home/prabhashj07/NepaliKit/data/stopword"
    stopword_dict = load_stopwords(stopwords_folder)
    print("Stopwords loaded:")
    for filename, stopwords in stopword_dict.items():
        print(f"{filename}: {stopwords}")

if __name__ == "__main__":
    main()

