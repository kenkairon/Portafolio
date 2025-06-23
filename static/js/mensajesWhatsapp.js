const toggleBtn = document.getElementById('chat-toggle-btn');
const widget = document.getElementById('whatsapp-widget');
const closeBtn = document.getElementById('whatsapp-close');
const form = document.getElementById('whatsapp-form');
const input = document.getElementById('whatsapp-input');
const messages = document.getElementById('whatsapp-messages');

toggleBtn.addEventListener('click', () => {
    console.log("Clic detectado");
    widget.style.display = 'flex';
    toggleBtn.style.display = 'none';

    if (!document.querySelector('.message.bot')) {
        addMessage("Hola 👋, ¿En qué puedo ayudarte?", 'bot');
    }
});

closeBtn.addEventListener('click', () => {
    widget.style.display = 'none';
    toggleBtn.style.display = 'flex';
});

form.addEventListener('submit', (e) => {
    e.preventDefault();
    const text = input.value.trim();
    if (text) {
        addMessage(text, 'user');
        input.value = '';
        const encodedMsg = encodeURIComponent(text);
        window.open(`https://wa.me/56979347247?text=${encodedMsg}`, '_blank');
    }
});

function addMessage(text, sender) {
    const msg = document.createElement('div');
    msg.classList.add('message', sender);
    msg.textContent = text;
    messages.appendChild(msg);
    messages.scrollTop = messages.scrollHeight;
}