from dotenv import load_dotenv
from pathlib import Path
import os
from google import genai

env_path = Path(__file__).parent / "ai_assistant" / ".env"
load_dotenv(env_path)

print(os.getenv("GEMINI_API_KEY"))

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Hello"
)

print(response.text)