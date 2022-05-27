import requests
import json



def makelogin(email,password):
    url = "http://localhost:5000/v1/users/login"

    payload = {
        "email": email,
        "password": password
    }
    headers = {"Content-Type": "application/json"}

    response = requests.request("POST", url, json=payload, headers=headers)
    
    return response.json()
    