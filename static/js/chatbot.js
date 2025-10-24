const chatButton = document.getElementById('chat-button');
const chatBox = document.getElementById('chat-box');
const chatMessages = document.getElementById('chat-messages');
const chatInput = document.getElementById('chat-input');
const sendBtn = document.getElementById('send-btn');

// Mostrar/ocultar chat
chatButton.addEventListener('click', () => {
    chatBox.style.display = chatBox.style.display === 'flex' ? 'none' : 'flex';
});

// Enviar mensaje
function sendMessage() {
    const message = chatInput.value.trim();
    if (!message) return;
    chatMessages.innerHTML += `<div style="text-align: right; color: #007bff;"><b>Tú:</b> ${message}</div>`;
    chatInput.value = "";

    fetch("/send_message", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: new URLSearchParams({ message })
    })
        .then(res => res.json())
        .then(data => {
            chatMessages.innerHTML += `<div><b>Bot:</b> ${data.response}</div>`;
            chatMessages.scrollTop = chatMessages.scrollHeight;
        });
}

sendBtn.addEventListener('click', sendMessage);
chatInput.addEventListener('keypress', e => {
    if (e.key === "Enter") sendMessage();
});
