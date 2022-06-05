import requests
import json

#urlservidor ='http://127.0.0.1:5001'
urlservidor ='https://a3-commands-api.herokuapp.com'


def makeRegister(name,email,password,coupon,company):
    url = f"{urlservidor}/v1/users/coupon"

    payload = {
        "name": name,
        "email": email,
        "password": password,
        "coupon":coupon,
        "company":company
    }
    headers = {"Content-Type": "application/json"}

    response = requests.request("POST", url, json=payload, headers=headers)
    
    return response.json()
    