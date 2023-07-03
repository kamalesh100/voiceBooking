import spacy
from spacy.training import Example

# Load the trained model
nlp = spacy.load("model_10k")

# Test data: Replace with your own data.
# TEST_DATA = [
# ("I'd like to travel from Leeds to Oxford with 4 friends on August 12th.", {'entities': [(24, 29, 'Origin'), (33, 39, 'Destination'), (45, 46, 'Passenger'), (58, 69, 'Date')]}), ('Please book a trip from Leeds to Cambridge for 6 passengers on July 16.', {'entities': [(24, 29, 'Origin'), (33, 42, 'Destination'), (47, 48, 'Passenger'), (63, 70, 'Date')]}),
# ]
from dataset import TRAIN_DATA

examples = []
for text, annots in TRAIN_DATA:
    doc = nlp.make_doc(text)
    example = Example.from_dict(doc, annots)
    examples.append(example)

scores = nlp.evaluate(examples)

# The scores object includes several metrics. Print them all.
print("Precision", scores["ents_p"])
print("Recall", scores["ents_r"])
print("F-score", scores["ents_f"])
print("Per-Entity", scores["ents_per_type"])
