import requests
import json


def makelogin(email,password):
    url = "https://a3-commands-api.herokuapp.com/v1/users/login"

    payload = {
        "email": email,
        "password": password
    }
    headers = {"Content-Type": "application/json"}

    response = requests.request("POST", url, json=payload, headers=headers)
    
    return response.json()
    