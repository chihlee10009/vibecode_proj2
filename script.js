document.addEventListener('DOMContentLoaded', () => {
    const input = document.getElementById('greetingInput');
    const chatMessages = document.getElementById('chatMessages');

    input.focus();

    input.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
            const text = input.value.trim();
            if (text) {
                // 1. Add User Message
                addMessage(text, 'user');
                input.value = '';
                
                // 2. Fetch Response
                fetchGreeting(text);
            }
        }
    });

    async function fetchGreeting(message) {
        // Show typing indicator
        const indicatorId = showTypingIndicator();
        scrollToBottom();

        try {
            const response = await fetch('/api/greet', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message })
            });

            // Remove typing indicator
            removeTypingIndicator(indicatorId);
            
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            
            const data = await response.json();
            addMessage(data.reply, 'bot');
        } catch (error) {
            removeTypingIndicator(indicatorId);
            console.error('Error:', error);
            addMessage("Oops! I couldn't reach the server. Is it running? 🔌", 'bot');
        }
        
        scrollToBottom();
    }

    function addMessage(text, sender) {
        const div = document.createElement('div');
        div.classList.add('message', sender);
        div.textContent = text;
        chatMessages.appendChild(div);
        scrollToBottom();
    }

    function showTypingIndicator() {
        const id = 'typing-' + Date.now();
        const div = document.createElement('div');
        div.id = id;
        div.classList.add('typing-indicator', 'bot');
        div.innerHTML = `
            <div class="typing-dot"></div>
            <div class="typing-dot"></div>
            <div class="typing-dot"></div>
        `;
        chatMessages.appendChild(div);
        return id;
    }

    function removeTypingIndicator(id) {
        const indicator = document.getElementById(id);
        if (indicator) {
            indicator.remove();
        }
    }

    function scrollToBottom() {
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
});
