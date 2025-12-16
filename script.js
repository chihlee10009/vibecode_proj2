document.addEventListener('DOMContentLoaded', () => {
    const input = document.getElementById('greetingInput');
    const outputContainer = document.getElementById('outputContainer');
    const outputText = document.getElementById('greetingOutput');

    input.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
            const text = input.value.trim();
            if (text) {
                fetchGreeting(text);
            }
        }
    });

    async function fetchGreeting(message) {
        // Show loading state
        showThinking();
        
        try {
            const response = await fetch('http://localhost:5001/api/greet', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message })
            });
            
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            
            const data = await response.json();
            showGreeting(data.reply);
        } catch (error) {
            console.error('Error:', error);
            showGreeting("Oops! I couldn't reach the server. Is it running? 🔌");
        }
    }

    function showThinking() {
        if (outputContainer.classList.contains('active')) hideGreeting();
        // Optional: Add a thinking visual if desired, for now just wait
        // or we could show a "Thinking..." text
        document.querySelector('.globe-1').style.filter = 'blur(40px) brightness(1.5)';
    }

    function showGreeting(message) {
        outputText.textContent = message;
        outputContainer.classList.remove('hidden');
        outputContainer.classList.add('active');
        
        // Add a subtle bloom effect to the globe when greeting appears
        document.querySelector('.globe-1').style.filter = 'blur(60px) brightness(1.2)';
    }

    function hideGreeting() {
        outputContainer.classList.add('hidden');
        outputContainer.classList.remove('active');
        
        // Reset globe
        document.querySelector('.globe-1').style.filter = 'blur(80px)';
    }
});
