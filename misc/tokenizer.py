import nltk
from nltk.tokenize import word_tokenize
import string

def tokenize_text_file(input_file_path):
    # Generate the output file name by appending "-tokenized" before the file extension
    output_file_path = input_file_path.rsplit('.', 1)[0] + "-tokenized." + input_file_path.rsplit('.', 1)[1]
    
    # Read the input file
    with open(input_file_path, 'r') as file:
        content = file.read()
    
    # Normalize the content: convert to lowercase and remove punctuation
    tokenized_content = word_tokenize(content)
    
    # Write the normalized content to the output file
    with open(output_file_path, 'w') as file:
        file.write(str(tokenized_content))
    
    print(f"File has been tokenized and saved as: {output_file_path}")

# Example usage
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        input_file_path = sys.argv[1]
        tokenize_text_file(input_file_path)
    else:
        print("Please provide the path to the input file as an argument.")
