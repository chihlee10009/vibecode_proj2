document.addEventListener('DOMContentLoaded', () => {
    const input = document.getElementById('greetingInput');
    const outputContainer = document.getElementById('outputContainer');
    const outputText = document.getElementById('greetingOutput');

    input.addEventListener('input', (e) => {
        const text = e.target.value.trim().toLowerCase();
        
        if (text === 'hi' || text === 'hello' || text === 'hey') {
            showGreeting("Hello there! 👋");
        } else if (text === '') {
            hideGreeting();
        } else {
            // Optional: You could show a default state or clear it
            // For now, let's only verify on specific greetings or clear on empty
            hideGreeting();
        }
    });

    function showGreeting(message) {
        // If already showing same message, ignore
        if (outputContainer.classList.contains('active') && outputText.textContent === message) return;

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
