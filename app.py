import json
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from flask import Flask, request, jsonify
from flask_cors import CORS

# Initialize Flask app and enable CORS
app = Flask(__name__)
CORS(app)

# Initialize ChatterBot with ListTrainer for custom training
chatbot = ChatBot('InfoMate')
trainer = ListTrainer(chatbot)

# Load custom data from JSON file and train the chatbot
with open('college_data.json', 'r') as file:
    data = json.load(file)
    for item in data:
        # Train the chatbot with questions and responses from JSON
        trainer.train([item['text'], item['response']])

# Define route for chatbot communication
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    
    # Get a response from ChatterBot
    bot_response = chatbot.get_response(user_message)
    
    # Return response as JSON
    return jsonify({"response": str(bot_response)})

# Endpoint for server testing
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"response": "Server is running"})

if __name__ == '__main__':
    app.run(debug=True)
