from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

with open('college_data.json', 'r') as file:
    data = json.load(file)

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/styles.css')
def css():
    return send_from_directory('.', 'styles.css')

@app.route('/script.js')
def js():
    return send_from_directory('.', 'script.js')

@app.route('/ping')
def ping():
    return jsonify({"response": "Server is running"})

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '').lower().strip()

    for item in data:
        if item['text'].lower() == user_message:
            return jsonify({"response": item['response']})

    return jsonify({
        "response": "Sorry, I don't have information about that."
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
