import os
import re
from flask import Flask, request, jsonify
import spacy

app = Flask(__name__)

nlp = spacy.load(f"models/model")


@app.route("/predict", methods=["POST"])
def predict():
    # Get the JSON data from the request
    data = request.get_json(force=True)

    # Get the text from the JSON data
    text = data.get("text", "")

    # Process the text
    doc = nlp(text)

    # Extract the entities and put them in a list of dictionaries
    entities = [{"label": ent.label_, "text": ent.text} for ent in doc.ents]

    # Return the entities as JSON
    return jsonify(entities)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
