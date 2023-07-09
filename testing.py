import spacy
import importlib.util
import json

nlp = spacy.load("models/model")

# Define the directory for the testing data and the files
file_path = "testing_data/data.py"

# List to hold the results
results = []

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
        result["entities"].append(
            {
                "label": ent.label_,
                "value": ent.text,
                "start": ent.start_char,
                "end": ent.end_char,
            }
        )
    # Add the dictionary to the results list
    results.append(result)

# Write the results to the file
with open("testingResult.py", "w") as f:
    f.write(json.dumps(results, indent=2))
