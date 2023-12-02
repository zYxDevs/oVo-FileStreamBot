# This file is a part of oVo-FileStreamBot

from os import environ
from dotenv import load_dotenv

load_dotenv()




class Var(object):
    MULTI_CLIENT = False
    API_ID = int(environ.get("API_ID"))
    API_HASH = str(environ.get("API_HASH"))
    BOT_TOKEN = str(environ.get("BOT_TOKEN"))
    SLEEP_THRESHOLD = int(environ.get("SLEEP_THRESHOLD", "60"))  # 1 minute
    WORKERS = int(environ.get("WORKERS", "6"))  # 6 workers = 6 commands at once
    BIN_CHANNEL = int(
        environ.get("BIN_CHANNEL", None)
    )  # you NEED to use a CHANNEL when you're using MULTI_CLIENT
    PORT = int(environ.get("PORT", 8080))
    BIND_ADDRESS = str(environ.get("WEB_SERVER_BIND_ADDRESS", "0.0.0.0"))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    HAS_SSL = environ.get("HAS_SSL", False)
    HAS_SSL = str(HAS_SSL).lower() == "true"
    NO_PORT = environ.get("NO_PORT", False)
    NO_PORT = str(NO_PORT).lower() == "true"
    if "DYNO" in environ:
        ON_HEROKU = True
        APP_NAME = str(environ.get("APP_NAME"))
    else:
        ON_HEROKU = False
    FQDN = (
        str(environ.get("FQDN", BIND_ADDRESS))
        if not ON_HEROKU or environ.get("FQDN")
        else f"{APP_NAME}.herokuapp.com"
    )
    if ON_HEROKU:
        URL = f"https://{FQDN}/"
    else:
        URL = f'http{"s" if HAS_SSL else ""}://{FQDN}{"" if NO_PORT else f":{PORT}"}/'

    UPDATES_CHANNEL = "HxBots"
    OWNER_ID = int(environ.get('OWNER_ID', '754495556'))

    BANNED_CHANNELS = list(
        {
            int(x)
            for x in str(
                environ.get("BANNED_CHANNELS", "-1001296894100")
            ).split()
        }
    )
    BANNED_USERS = list(
        {
            int(x)
            for x in str(
                environ.get("BANNED_USERS", "5275470552 5287015877")
            ).split()
        }
    )
