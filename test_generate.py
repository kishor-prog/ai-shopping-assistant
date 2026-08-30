from google import genai
from ai_assistant.config import get_gemini_api_key, MODEL_NAME

client = genai.Client(api_key=get_gemini_api_key())

response = client.models.generate_content(
    model=MODEL_NAME,
    contents="Say hello in one sentence."
)

print(response.text)