import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load FAQ data
with open('college_data.json', 'r') as file:
    data = json.load(file)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '').lower().strip()

    for item in data:
        if item['text'].lower() == user_message:
            return jsonify({"response": item['response']})

    return jsonify({
        "response": "Sorry, I don't have information about that. Please contact the administration."
    })

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"response": "Server is running"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
