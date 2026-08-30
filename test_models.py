from google import genai
from ai_assistant.config import get_gemini_api_key

client = genai.Client(api_key=get_gemini_api_key())

for model in client.models.list():
    print(model.name)