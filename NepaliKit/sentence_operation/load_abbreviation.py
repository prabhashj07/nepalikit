import os

# Use a relative path from the script location
script_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(script_dir, '..', '..', 'data')
abbreviation_file = os.path.join(data_dir, 'abbreviation.txt')

def load_abbreviations(folder_path):
    """
    Load abbreviations from text files in the specified folder.
    
    Args:
        folder_path (str): Path to the folder containing abbreviation text files.
    
    Returns:
        dict: A dictionary mapping abbreviations to their expanded forms.
    """
    abbreviations = {}
    try:
        file_path = os.path.join(folder_path, 'abbreviation.txt')
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                if ':' in line:
                    key, value = line.strip().split(':')
                    abbreviations[key.strip()] = value.strip()
        return abbreviations

    except FileNotFoundError:
        print(f"Error: Abbreviation file not found in '{folder_path}'.")
        return {}
    
    except Exception as e:
        print(f"Error loading abbreviations: {e}")
        return {}

"""
# Call the function
abbreviations = load_abbreviations(abbreviation_file)

# Check if any abbreviations were loaded
if not abbreviations:
    print("No abbreviations were loaded. Check the file path and file content.")
"""
