import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

app = Flask(__name__)
CORS(app)

# Configure Gemini API
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("Warning: GEMINI_API_KEY not found in environment variables.")

client = genai.Client(api_key=api_key)

# Generation config
generation_config = types.GenerateContentConfig(
    temperature=0.9,
    top_p=1,
    top_k=1,
    max_output_tokens=800,  # Increased to prevent premature cuts
)

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

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=generation_config
        )
        
        reply = response.text
        if reply:
             reply = reply.strip()
        else:
             print(f"Warning: Empty response text. Finish reason: {response.candidates[0].finish_reason if response.candidates else 'Unknown'}")
             reply = "Hello! (I'm speechless right now!) 😶"

        return jsonify({'reply': reply})

    except Exception as e:
        print(f"Error generating greeting: {e}")
        return jsonify({'reply': "I'm having a bit of a brain freeze, but hello anyway! 🧊"}), 500

if __name__ == '__main__':
    app.run(port=5002, debug=True)
