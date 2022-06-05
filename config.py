import os
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())



SECRET_KEY = os.urandom(24)
# this is important or wont work
#app.config['SESSION_COOKIE_NAME'] = "my_session"