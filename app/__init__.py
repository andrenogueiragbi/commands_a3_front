from flask import Flask
import os
from datetime import timedelta
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


app =  Flask(__name__)
app.config.from_object('config')

app.secret_key = os.urandom(12).hex()
app.permanent_session_lifetime = timedelta(days=2)

