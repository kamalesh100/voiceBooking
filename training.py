import os
import spacy
from spacy.util import minibatch, compounding
from spacy.training import Example
import random
import importlib.util

# Define the directory for the training data and the models
file_path = "training_data/data.py"
MODELS_DIR = "models"

# Create a blank 'en' model
nlp = spacy.blank("en")
# Create a new entity recognizer and add it to the pipeline
ner = nlp.create_pipe("ner")
nlp.add_pipe("ner")
# Add the new label to the entity recognizer
ner.add_label("Origin")
ner.add_label("Destination")
ner.add_label("Date")
ner.add_label("Passenger")


# Start the training
nlp.begin_training()

# Load this chunk of training data
spec = importlib.util.spec_from_file_location("module.name", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
TRAIN_DATA = module.TRAIN_DATA

# Train for 10 iterations
for itn in range(10):
    random.shuffle(TRAIN_DATA)
    losses = {}

    # Batch the examples and iterate over them
    for batch in minibatch(TRAIN_DATA, size=compounding(4.0, 32.0, 1.001)):
        for text, annotations in batch:
            # Create an Example object
            doc = nlp.make_doc(text)
            example = Example.from_dict(doc, annotations)

            # Update the model
            nlp.update([example], drop=0.1, losses=losses)

    print(f"Model {itn+1}, Losses: {losses}")

# Create a new directory for this model if it doesn't exist
model_dir = f"{MODELS_DIR}/model"
os.makedirs(model_dir, exist_ok=True)
# Save the model
nlp.to_disk(model_dir)
