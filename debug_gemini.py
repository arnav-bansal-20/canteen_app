import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

try:
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment")
    genai.configure(api_key=api_key)
    print("Checking models...")
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"Trying {m.name}...")
            try:
                model = genai.GenerativeModel(m.name)
                response = model.generate_content("Hi")
                print(f"SUCCESS with {m.name}")
                break
            except Exception as e:
                print(f"Failed {m.name}: {e}")
except Exception as e:
    print(f"Global Error: {e}")
