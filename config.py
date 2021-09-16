import os

from os import getenv
from dotenv import load_dotenv

load_dotenv()
admins = {}
ADMIN = int(os.getenv('ADMIN'))
CHANNEL = int(os.getenv('CHANNEL'))
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_USERNAME = os.getenv("BOT_USERNAME", "VcVideoRobot")
ASSISTANT_NAME = os.getenv("ASSISTANT_NAME")
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP")
UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL")
SOURCE_CODE = os.getenv("SOURCE_CODE")
BOT_TOKEN = os.getenv("BOT_TOKEN")
SESSION_NAME = os.getenv("SESSION_NAME")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
