import os
import re
import spacy
import importlib.util
import json

def sort_model_dirs(dir_name):
    match = re.search(r'model_(\d+)', dir_name)
    if match is not None:
        return int(match.group(1))
    else:
        return 0  # Default to 0 if no match

model_dirs = os.listdir("models")
model_dirs.sort(key=sort_model_dirs)
latest_model_dir = model_dirs[-1]
nlp = spacy.load(f"models/{latest_model_dir}")

# Define the directory for the testing data and the files
TEST_DATA_DIR = "testing_data/"
TEST_DATA_FILES = [f"{TEST_DATA_DIR}data_1m_{i+1}.py" for i in range(10)]

# List to hold the results
results = []

for file_path in TEST_DATA_FILES:
    # Load this chunk of testing data
    spec = importlib.util.spec_from_file_location("module.name", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    TEST_DATA = module.TEST_DATA

    for text, _ in TEST_DATA:
        doc = nlp(text)
        # Dictionary to hold the results for this input
        result = {"input": text, "entities": []}
        # Add the entities to the dictionary
        for ent in doc.ents:
            result["entities"].append({"label": ent.label_, "text": ent.text, "start": ent.start_char, "end": ent.end_char})
        # Add the dictionary to the results list
        results.append(result)

# Write the results to the file
with open('testingResult.py', 'w') as f:
    f.write(json.dumps(results, indent=2))
