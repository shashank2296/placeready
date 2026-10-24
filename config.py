import os
from dotenv import load_dotenv

load_dotenv()  # reads .env
JWT_SECRET = os.getenv("JWT_SECRET", "dev-secret-change-me")
MODEL = os.getenv("CLAUDE_MODEL", "claude-sonnet-5-5")
