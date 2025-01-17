import os

API_ID    = os.environ.get("API_ID", "28935416")
API_HASH  = os.environ.get("API_HASH", "e18c05697d95edfe39d8957f6e110308")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8105056819:AAEbNiQAAijX_bElj5V5zEEAjl_mSQd4tg4") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
