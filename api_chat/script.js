document.getElementById('msger-inputarea').addEventListener('submit', function(event) {
    event.preventDefault();
    sendMessage();
});

//   lorsque la page est chargée, affiche un message de bienvenue en envoyant un message à l'API sur /greet
document.addEventListener('DOMContentLoaded', function() {
    fetch('http://localhost:5000/greet')
    .then(response => response.json())
    .then(data => {
        console.log(data);
        appendMessage('BOT', 'left-msg', data.greeting, new Date());
    })
    .catch(error => console.error('Error:', error));
});

function sendMessage() {
    const userInput = document.getElementById('user-input');
    const chatBox = document.getElementById('chat-box');
    const text = userInput.value.trim();
    
    if (text === '') return;
    
    // efface le champ de saisie
    userInput.value = '';
    
    // ajoute un message utilisateur
    appendMessage('You', 'right-msg', text, new Date());
    
    // envoie des messages à l'API et affiche la réponse
    fetch('http://localhost:5000/echo', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({ text: text }),
})
.then(response => response.json())
.then(data => {
    appendMessage('BOT', 'left-msg', data.echo, new Date());
})
.catch(error => console.error('Error:', error));
}

function appendMessage(name, side, text, time) {
    const chatBox = document.getElementById('chat-box');
    const msgHTML = `
    <div class="msg ${side}"> 
    <div class="msg-bubble">
    <div class="msg-info">
    <div class="msg-info-name">${name}</div>
    <div class="msg-info-time">${formatTime(time)}</div>
    </div>
    <div class="msg-text">${text}</div>
    </div>
    </div>
    `;
    chatBox.innerHTML += msgHTML;
    chatBox.scrollTop = chatBox.scrollHeight;
}

function formatTime(date) {
    return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
}


