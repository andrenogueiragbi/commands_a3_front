import requests
import json

#urlservidor = 'http://127.0.0.1:5001'
urlservidor ='https://a3-commands-api.herokuapp.com'


def searchTypeCommands(token):
    url = f"{urlservidor}/v1/type"

    payload = {}
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.request("GET", url, json=payload, headers=headers)

    return response.json()
