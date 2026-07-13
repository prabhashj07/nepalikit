import os


def load_abbreviations(folder_path):
    """
    Load abbreviations from text files in the specified folder.

    Args:
        folder_path (str): Path to the folder containing abbreviation text files.

    Returns:
        dict: A dictionary mapping abbreviations to their expanded forms.
    """
    abbreviations = {}
    if not os.path.isdir(folder_path):
        return abbreviations
    file_path = os.path.join(folder_path, 'abbreviation.txt')
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                if ':' in line:
                    key, value = line.strip().split(':', 1)
                    abbreviations[key.strip()] = value.strip()
    except FileNotFoundError:
        pass
    return abbreviations
