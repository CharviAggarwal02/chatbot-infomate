// Toggle between light and dark mode
document.getElementById('modeToggle').addEventListener('change', function () {
    document.body.classList.toggle('dark-mode');
});

document.getElementById('sendButton').addEventListener('click', sendMessage);
document.getElementById('userInput').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

function sendMessage() {
    const userInput = document.getElementById('userInput').value;
    if (userInput.trim() === '') return;

    displayMessage(userInput, 'userMessage');

    fetch('http://127.0.0.1:5000/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        displayMessage(data.response, 'botMessage');
    })
    .catch(error => {
        console.error('Error:', error);
        displayMessage("Sorry, I couldn't connect to the server.", 'botMessage');
    });

    document.getElementById('userInput').value = '';
}

function displayMessage(text, className) {
    const chatMessages = document.getElementById('chatMessages');
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${className}`;
    messageDiv.textContent = text;
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}
