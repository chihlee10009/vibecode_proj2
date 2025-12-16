import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

app = Flask(__name__)
CORS(app)

# Configure Gemini API
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("Warning: GEMINI_API_KEY not found in environment variables.")

genai.configure(api_key=api_key)

# Generation config
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 50,
}

model = genai.GenerativeModel(model_name="gemini-2.5-flash", generation_config=generation_config)

@app.route('/api/greet', methods=['POST'])
def greet():
    try:
        data = request.get_json()
        message = data.get('message', '')

        if not message:
            return jsonify({'error': 'Message is required'}), 400

        prompt = (
            f"You are a witty, friendly, and cool AI assistant. "
            f"A user has just said this to you: \"{message}\". "
            f"Generate a short, unique, and fun greeting reply (max 15 words). "
            f"Make it vary each time and be creative. Don't just say \"Hello\"."
        )

        response = model.generate_content(prompt)
        reply = response.text.strip()

        return jsonify({'reply': reply})

    except Exception as e:
        print(f"Error generating greeting: {e}")
        return jsonify({'reply': "I'm having a bit of a brain freeze, but hello anyway! 🧊"}), 500

if __name__ == '__main__':
    app.run(port=5001, debug=True)
