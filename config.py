import os

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
TWELVE_DATA_API_KEY = os.getenv("TWELVE_DATA_API_KEY")
MARKET_TYPE = os.getenv("MARKET_TYPE", "forex")
TIMEFRAME = os.getenv("TIMEFRAME", "1day")
TIMEZONE = os.getenv("TIMEZONE", "Asia/Dhaka")
