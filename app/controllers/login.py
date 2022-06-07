import requests
import json

urlservidor = 'http://127.0.0.1:5001'
#urlservidor ='https://a3-commands-api.herokuapp.com'


def makelogin(email, password):
    url = f"{urlservidor}/v1/users/login"

    payload = {
        "email": email,
        "password": password
    }
    headers = {"Content-Type": "application/json"}

    response = requests.request("POST", url, json=payload, headers=headers)

    return response.json()
