from pathlib import Path
import os
import warnings

from dotenv import load_dotenv

# Search for .env in project root and ai_assistant directory
CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parent

# Load root .env first, then local if present
if (PROJECT_ROOT / ".env").exists():
    load_dotenv(PROJECT_ROOT / ".env")
elif (CURRENT_DIR / ".env").exists():
    load_dotenv(CURRENT_DIR / ".env")
else:
    load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configurable Gemini Model
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")


def get_gemini_api_key() -> str:
    key = os.getenv("GEMINI_API_KEY") or GEMINI_API_KEY
    if not key:
        raise ValueError(
            "GEMINI_API_KEY is not set. Please add it to your .env file or environment variables."
        )
    return key