import os
from dotenv import load_dotenv

load_dotenv()

# Configuration for Discord Bot
CHANNEL_ID = int(os.getenv('DISCORD_CHANNEL_ID', 123456789012345678))
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN", "your-default-token-here")

# Configuration for Database
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "botdb")
DB_USER = os.getenv("DB_USER", "user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_PORT = int(os.getenv("DB_PORT", 5432))

# Configuration for Riot API
RIOT_API_KEY = os.getenv("RIOT_API_KEY", "your-default-riot-api-key-here")
