import os

# BUG FIX: int("") and int("-") both crash with ValueError.
# Changed defaults to "0" so the app starts even without env vars set.

API_ID = int(os.environ.get("API_ID", "30978477"))
API_HASH = os.environ.get("API_HASH", "4d908be0390fb1f4fd079506af5b1971")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8925022436:AAEtRsK96KpD8BNwzJfA8krDi9vbWfXxVU0")

OWNER_ID = int(os.environ.get("OWNER_ID", "5575032909"))

# SUDO_USERS: space-separated list of user IDs e.g. "123456 789012"
_sudo_raw = os.environ.get("SUDO_USERS", "5575032909").strip()
SUDO_USERS = list(map(int, _sudo_raw.split())) if _sudo_raw else []

MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://abcdef95108_db_user:lzSM3yBBKPsrgYUQ@cluster0.r2pwqnt.mongodb.net/?appName=Cluster0")

# BUG FIX: int("-") crashes. Default to 0 if not set.
_channel_raw = os.environ.get("CHANNEL_ID", "0").strip()
CHANNEL_ID = int(_channel_raw) if _channel_raw else 0

PREMIUM_LOGS = os.environ.get("PREMIUM_LOGS", "")
