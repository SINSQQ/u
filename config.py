from os import getenv

from dotenv import load_dotenv

load_dotenv()

Bot_id = getenv("ID")
APP_NEAM = getenv("APP")
token = getenv("TK")
sudo_id = getenv("sudo_id")
redis_url = getenv("Redis_url")
