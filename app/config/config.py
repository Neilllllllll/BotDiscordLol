import os
from dotenv import load_dotenv

load_dotenv()

CHANNEL_ID = int(os.getenv('DISCORD_CHANNEL_ID'))
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN", "your-default-token-here")

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "botdb")
DB_USER = os.getenv("DB_USER", "user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_PORT = int(os.getenv("DB_PORT", 5432))
