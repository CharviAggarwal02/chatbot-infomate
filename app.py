import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

with open("college_data.json") as f:
    data = json.load(f)

@app.route('/chat', methods=['POST'])
def chat():
    message = request.json['message'].lower()

    for item in data:
        if item["text"].lower() == message:
            return jsonify({"response": item["response"]})

    return jsonify({"response": "Sorry, I don't have information about that."})

@app.route('/ping')
def ping():
    return jsonify({"response": "Server is running"})
