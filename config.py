import re
from os import getenv, environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

API_ID = int(environ.get("API_ID", "28542813"))
API_HASH = environ.get("API_HASH", "02ce7c339f7776844ff4ab03da338ccd")
BOT_TOKEN = environ.get("BOT_TOKEN", "6468449640:AAGWY7mbMdkREIJFQrkiD9XtgC6OfrMGv_o")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002015639009"))
ADMINS = int(environ.get("ADMINS", "6064893774"))
DB_URI = environ.get("DB_URI", "mongodb+srv://yashsing2008:12345678yash@cluster0.j8n5cqz.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = environ.get("DB_NAME", "cluster0")
OPENAI_API = environ.get("OPENAI_API", "")
AI = is_enabled((environ.get("AI","True")), False)
