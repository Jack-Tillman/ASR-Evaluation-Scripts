import string

def normalize_text_file(input_file_path):
    # Generate the output file name by appending "-normalized" before the file extension
    output_file_path = input_file_path.rsplit('.', 1)[0] + "-normalized." + input_file_path.rsplit('.', 1)[1]
    
    # Read the input file
    with open(input_file_path, 'r') as file:
        content = file.read()
    
    # Normalize the content: convert to lowercase and remove punctuation
    normalized_content = content.lower()
    normalized_content = normalized_content.translate(str.maketrans('', '', string.punctuation))
    
    # Write the normalized content to the output file
    with open(output_file_path, 'w') as file:
        file.write(normalized_content)
    
    print(f"File has been normalized and saved as: {output_file_path}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        input_file_path = sys.argv[1]
        normalize_text_file(input_file_path)
    else:
        print("Please provide the path to the input file as an argument.")

