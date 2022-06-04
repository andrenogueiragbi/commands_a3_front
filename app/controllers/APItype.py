import requests
import json


def searchTypeCommands():
    url = "https://a3-commands-api.herokuapp.com/v1/type"

    payload = {
 
    }
    headers = {"Content-Type": "application/json"}

    response = requests.request("GET", url, json=payload, headers=headers)

    
    return response.json()

