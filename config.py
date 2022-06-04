import os
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())

SECRET_KEY=os.environ.get('SECRETKEY')
SECRET_KEY=12332154
