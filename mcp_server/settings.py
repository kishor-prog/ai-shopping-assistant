import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env from project root if available
ROOT_DIR = Path(__file__).resolve().parent.parent
load_dotenv(ROOT_DIR / ".env")


class MCPSettings:
    BACKEND_URL: str = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")
    REQUEST_TIMEOUT: float = float(os.getenv("MCP_REQUEST_TIMEOUT", "10.0"))


settings = MCPSettings()
