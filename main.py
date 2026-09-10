"""
SOBUJ99 SIGNAL BOT - Main Entry Point
Quotex LIVE / Non-OTC Market 5-Minute Trading Signal Bot
Powered by Twelve Data API with Strict 80% Technical Score Threshold
"""

import sys
import logging
import asyncio
import config

TELEGRAM_BOT_TOKEN = config.TELEGRAM_BOT_TOKEN
TWELVE_DATA_API_KEY = config.TWELVE_DATA_API_KEY
from pair_mapping import get_all_live_pairs
from telegram_bot import setup_telegram_bot
from scheduler import SignalScheduler

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger("SOBUJ99-BOT")

async def main():
    if not TELEGRAM_BOT_TOKEN or not TWELVE_DATA_API_KEY:
        logger.error("Missing TELEGRAM_BOT_TOKEN or TWELVE_DATA_API_KEY. Exiting.")
        sys.exit(1)

    logger.info("Initializing Telegram Bot Application...")
    app = setup_telegram_bot(TELEGRAM_BOT_TOKEN)

    logger.info("Starting Signal Scheduler...")
    scheduler = SignalScheduler(bot_app=app)
    scheduler_task = asyncio.create_task(scheduler.run_loop())

    logger.info("Starting Telegram Bot Polling loop...")
    async with app:
        await app.start()
        await app.updater.start_polling(drop_pending_updates=True)
        logger.info("SOBUJ99 SIGNAL BOT is LIVE!")
        try:
            await asyncio.Event().wait()
        finally:
            scheduler.stop()
            scheduler_task.cancel()
            await app.updater.stop()
            await app.stop()

if __name__ == "__main__":
    asyncio.run(main())
