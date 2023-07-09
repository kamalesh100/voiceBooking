import os
import re
import spacy
from spacy.training.example import offsets_to_biluo_tags
import importlib.util

nlp = spacy.load("models/model")

# Load the testing data
spec = importlib.util.spec_from_file_location("module.name", "training_data/data.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
TRAIN_DATA = module.TRAIN_DATA

correct_predictions = 0
total_predictions = 0

# Iterate over the testing data
for text, annotations in TRAIN_DATA:
    doc = nlp(text)
    true_entities = annotations["entities"]

    # Convert the entities to the BILOU tagging scheme
    true_biluo = offsets_to_biluo_tags(doc, true_entities)
    pred_biluo = [
        token.ent_iob_ + "-" + token.ent_type_ if token.ent_iob_ != "O" else "O"
        for token in doc
    ]

    # Compare the predicted entities with the true entities
    for true, pred in zip(true_biluo, pred_biluo):
        if true == pred:
            correct_predictions += 1
        total_predictions += 1

# Calculate the accuracy
accuracy = correct_predictions / total_predictions
print("Training accuracy:", accuracy)
