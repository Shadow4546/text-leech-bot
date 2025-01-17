import os

API_ID    = os.environ.get("API_ID", "2857756")
API_HASH  = os.environ.get("API_HASH", "efelkg45957f6e16708")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8Ajl4tg4") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
