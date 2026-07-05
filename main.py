#  MIT License — original by Dan <https://github.com/delivrance>

import os
import asyncio
import importlib
import logging
from pyrogram import Client, idle
from logging.handlers import RotatingFileHandler
from config import API_ID, API_HASH, BOT_TOKEN, OWNER_ID, SUDO_USERS, MONGO_URL, CHANNEL_ID, PREMIUM_LOGS
from Extractor.modules import ALL_MODULES
from web import web_app
import threading

LOGGER = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler("log.txt", maxBytes=5000000, backupCount=10),
        logging.StreamHandler(),
    ],
)


async def sumit_boot():
    for all_module in ALL_MODULES:
        importlib.import_module("Extractor.modules." + all_module)

    LOGGER.info("» ʙᴏᴛ ᴅᴇᴘʟᴏʏ sᴜᴄᴄᴇssғᴜʟʟʏ 🚀🎉")
    await idle()
    LOGGER.info("» ɢᴏᴏᴅ ʙʏᴇ ! sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ.")


def run_web():
    port = int(os.environ.get("PORT", 8080))
    web_app.run(host="0.0.0.0", port=port)


if __name__ == "__main__":
    # BUG FIX: asyncio.get_event_loop() is deprecated in Python 3.10+.
    # Replaced with asyncio.run() for the bot, web server runs in a daemon thread.
    web_thread = threading.Thread(target=run_web, daemon=True)
    web_thread.start()
    asyncio.run(sumit_boot())
