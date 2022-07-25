## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "1ApWapzMBu8EbHuK1e6Y7Eunq8Io3DC3CCas7Ekir8qcRnsaSTayr3QMIvLEGRbyXHtgqIKH3eim6UluM3mdr7t76tvL88riT1k-wuGfbX-baIfOHoMm-oegp4gfzrfyeSBAM_1a-Xod1j9l2F1hLORyCiXQ0Jj0wopJoinWzcdTENFvR3YrUaUBfI_W2pFgz15zZ8fS4cWllFXXg_U89kpQ8VikJeYMoB6l9DVZKq7F17xlj04UeVaGKKkK4SyTr3FEMNNBGwKUCXj1LB0TLPE2AcF1C-1PLEBxf01GSudsDXxQfAa3kbLg6fxL1gkQMvISSTv9lH_kIx7TuD7C9ImRA5ywXJa0=")
BOT_TOKEN = getenv("BOT_TOKEN", "1752238114:AAFQhfdbNbSdAYLiRtJUzLAOzFuu9-HU7s4")
BOT_NAME = getenv("BOT_NAME", "Dowz")
API_ID = int(getenv("API_ID", "6060654"))
API_HASH = getenv("API_HASH", "b106c2148b2d3bd246f789a1e17c2d91")
OWNER_NAME = getenv("OWNER_NAME", "Dowz")
OWNER_USERNAME = getenv("OWNER_USERNAME", "DowzS")
ALIVE_NAME = getenv("ALIVE_NAME", "Dowz")
BOT_USERNAME = getenv("BOT_USERNAME", "Dowz_ghbot")
OWNER_ID = getenv("OWNER_ID", "2117814704")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "DozwS")
GROUP_SUPPORT = getenv("wofkq", "wofkq")
UPDATES_CHANNEL = getenv("wofkc", "wofkc")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2117814704").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/e22e5d1f0ccd57fa5f677.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
