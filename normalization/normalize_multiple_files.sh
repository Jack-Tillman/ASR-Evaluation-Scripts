#!/bin/bash

# Check if the normalize_text_file.py script exists in the current directory
if [ ! -f "./normalize_text_file.py" ]; then
    echo "The normalize_text_file.py script is not found in the current directory."
    exit 1
fi

# Loop through the first 20 .txt files in the current directory and normalize them
count=0
for file in *.txt; do
    if [ "$count" -lt 20 ]; then
        python3 normalize_text_file.py "$file"
        ((count++))
    else
        break
    fi
done

echo "Normalization complete for $count files."
