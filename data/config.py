import os
from dotenv import load_dotenv
load_dotenv()
BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
ADMINS = [
    609248670
]
ip = os.getenv("ip")
aiogram_redis = {
    'host': ip
}
redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}
banned_users = [123456, 5678889]
PROVIDER_TOKEN = os.getenv("PROVIDER_TOKEN")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")
