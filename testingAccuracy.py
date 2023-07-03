import os
import re
import spacy
from spacy.training.example import offsets_to_biluo_tags
import importlib.util

def sort_model_dirs(dir_name):
    match = re.search(r'model_(\d+)', dir_name)
    if match is not None:
        return int(match.group(1))
    else:
        return 0

model_dirs = os.listdir("models")
model_dirs.sort(key=sort_model_dirs)
latest_model_dir = model_dirs[-1]
nlp = spacy.load(f"models/{latest_model_dir}")

# Load the testing data
spec = importlib.util.spec_from_file_location("module.name", "testing_data/data_1m_10.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
TEST_DATA = module.TEST_DATA

correct_predictions = 0
total_predictions = 0

# Iterate over the testing data
for text, annotations in TEST_DATA:
    doc = nlp(text)
    true_entities = annotations['entities']

    # Convert the entities to the BILOU tagging scheme
    true_biluo = offsets_to_biluo_tags(doc, true_entities)
    pred_biluo = [token.ent_iob_ + '-' + token.ent_type_ if token.ent_iob_ != 'O' else 'O' for token in doc]

    # Compare the predicted entities with the true entities
    for true, pred in zip(true_biluo, pred_biluo):
        if true == pred:
            correct_predictions += 1
        total_predictions += 1

# Calculate the accuracy
accuracy = correct_predictions / total_predictions
print('Testing accuracy:', accuracy)