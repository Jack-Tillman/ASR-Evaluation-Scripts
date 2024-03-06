import werpy
import pandas as pd

#read file content
def read_file(filepath):
    with open(filepath, 'r') as file:
        return file.read().strip()  # Removes any leading/trailing whitespace

#write output to a file
def write_output(filepath, content):
    with open(filepath, 'w') as file:
        file.write(content)
        
#'hyp_path' and 'ref_path' are the file paths to hypothesis and reference transcriptions
hyp_path = '110753-AWS-transcript-normalized-unpunctxt' 
ref_path = 'Tillman,Matt-D110753-normalized.txt' 

# Load the contents of the files into variables
hyp = read_file(hyp_path)
ref = read_file(ref_path)

summary = werpy.summary(ref, hyp)
df = pd.DataFrame(summary)
# Output file path
output_path = 'output/110753-output.txt'  

# Save the WER result to a file
write_output(output_path, f"{df.to_string()}")
print(df.to_string())


