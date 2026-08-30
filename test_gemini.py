from google import genai
from ai_assistant.config import get_gemini_api_key, MODEL_NAME

api_key = get_gemini_api_key()
print(f"API Key loaded (length: {len(api_key)})")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model=MODEL_NAME,
    contents="Hello",
)

print(response.text)