import importlib.util
import json

# Define the directory for the training data and the files
file_path = "training_data/data.py"

# Prepare the final output
output = []

# Load this chunk of training data
spec = importlib.util.spec_from_file_location("module.name", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
TRAIN_DATA = module.TRAIN_DATA

for item in TRAIN_DATA:
    entities = item[1]["entities"]
    entity_dict = {"text": item[0]}
    for start, end, label in entities:
        value = item[0][start:end]
        entity_dict[label] = value
    output.append(entity_dict)

# Store the result in a Python file
with open("verifyDatasetResult.py", "w") as f:
    f.write("output = ")
    f.write(json.dumps(output, indent=2))
print("Check 'verifyDatasetResult.py' for data verification.")
