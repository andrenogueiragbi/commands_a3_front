import requests
import json


def searchTypeCommands():
    url = "http://localhost:5000/v1/type"

    payload = {
 
    }
    headers = {"Content-Type": "application/json"}

    response = requests.request("GET", url, json=payload, headers=headers)

    
    return response.json()

