import os
import re
import spacy

# Function to sort model directories by the integer in their names
def sort_model_dirs(dir_name):
    match = re.search(r'model_(\d+)', dir_name)
    if match is not None:
        return int(match.group(1))
    else:
        return 0  # Default to 0 if no match

# Get the list of model directories
model_dirs = os.listdir("models")

# Sort the model directories
model_dirs.sort(key=sort_model_dirs)

# Get the directory of the latest model
latest_model_dir = model_dirs[-1]

# Load the latest model
nlp = spacy.load(f"models/{latest_model_dir}")

# Test text
test_text = "Book tickets to london from leeds on 23rd June for 2 people."

# Process the text
doc = nlp(test_text)

# Print the entities
for ent in doc.ents:
    print(ent.label_, ": ", ent.text, "[", ent.start_char, ",", ent.end_char, "]")
