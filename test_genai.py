import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
print(f"API Key present: {bool(api_key)}")

client = genai.Client(api_key=api_key)
try:
    print("Testing generate_content with gemini-2.5-flash...")
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Hello",
        config=types.GenerateContentConfig(max_output_tokens=100)
    )
    print(f"Response text: {response.text}")
except Exception as e:
    print(f"Error generating: {e}")
except Exception as e:
    print(f"Error listing models: {e}")
