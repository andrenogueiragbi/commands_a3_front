import requests
import json



def searchType(type='outros'):
    url = f"http://localhost:5000/v1/commands/search/{type}"

    payload = {

    }
    headers = {"Content-Type": "application/json"}

    response = requests.request("GET", url, headers=headers)
    
    return response.json()
    