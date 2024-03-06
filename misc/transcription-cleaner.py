# The purpose of this script is multiple. 
# 1) Replace commands for punctuation and line control with their appropriate replacements, i.e., [ comma ] => , [ new paragraph ] => \n\n 
# 2) Remove all-capitalized words and replace with the first letter capitalized
# 3) Convert 'Numeral one' to 1 and so on 
# 4) capitalize headers, though this functionality is only relevant for a few transcriptions
# 5) Save the output as a .txt file labeled sequentially 

import re

def capitalize_headers(input_text):
    headers = ['DESCRIPTION ', '2D STUDY', 'DOPPLER ', 'SUMMARY']
    for header in headers:
        input_text = input_text.replace(header, header.capitalize())
    return input_text

def clean_text(input_text):
    # Remove square brackets and their surrounding whitespace
    input_text = re.sub(r'\s*\[\s*|\s*\]\s*', ' ', input_text)

    # Capitalize section headers
    input_text = capitalize_headers(input_text)

    # # Numerical list formatting
    replacements = {
        ' period': '.',
        ' comma': ',',
        ' colon': ':',
        ' colon ': ':',
        ' dash': '-',
        ' open parenthesis': '(',
        'close parenthesis': ')',
        'quote': '"',
        'close quote': '"',
        'end quote': '"',
        ' new line ': '\n',
        ' new paragraph ': '\n\n'
    }
    for key, value in replacements.items():
        input_text = input_text.replace(key, value)

    # Replace "Numeral" phrases with actual numerals
    numerals = {
        'Numeral one': '1',
        'Numeral two': '2',
        'Numeral three': '3',
        'Numeral four': '4',
        'Numeral five': '5',
        'Numeral six': '6',
        'Numeral seven': '7',
        'Numeral eight': '8',
        'Numeral nine': '9',
        'Numeral ten': '10',
        'Numeral 10': '10',
        'Numeral 11': '11',
    }
    for key, value in numerals.items():
        input_text = input_text.replace(key, value)

    # Trim unnecessary whitespace
    # Split the text into lines, trim each line, then join them back together
    lines = input_text.split('\n')
    trimmed_lines = [line.strip() for line in lines]
    input_text = '\n'.join(trimmed_lines)
    print(input_text)
    return input_text

def save_output(output_text, file_prefix="cleaned-transcription"):
    """
    Save the output text to a file with sequential naming.
    Args:
    output_text (str): The text to be saved.
    file_prefix (str): The prefix for the filename.
    """
    import os

    # Check existing files to determine the next file number
    existing_files = [f for f in os.listdir() if f.startswith(file_prefix)]
    next_file_number = len(existing_files) + 1
    file_name = f"{file_prefix}{next_file_number}.txt"

    # Write to file
    with open(file_name, "w") as file:
        file.write(output_text)

    return file_name

# Sample input
sample_input = """
 [
[
    "sample text here! :D"
]
]
"""

# Clean the text
cleaned_text = clean_text(sample_input)

# Save the cleaned text to a file
saved_file_name = save_output(cleaned_text)
print(f"Output saved in file: {saved_file_name}")
