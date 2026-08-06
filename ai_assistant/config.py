from pathlib import Path
import os

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / ".env")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Recommended model
MODEL_NAME = "gemini-flash-lite-latest"

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found")