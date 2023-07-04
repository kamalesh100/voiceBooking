import os
import re
from flask import Flask, request, jsonify
import spacy

app = Flask(__name__)

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

@app.route('/predict', methods=['POST'])
def predict():
    # Get the JSON data from the request
    data = request.get_json(force=True)

    # Get the text from the JSON data
    text = data.get('text', '')

    # Process the text
    doc = nlp(text)

    # Extract the entities and put them in a list of dictionaries
    entities = [{"label": ent.label_, "text": ent.text} for ent in doc.ents]

    # Return the entities as JSON
    return jsonify(entities)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
