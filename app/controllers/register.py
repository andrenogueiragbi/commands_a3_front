import requests
import json



def makeRegister(name,email,password,coupon,company):
    url = "https://a3-commands-api.herokuapp.com/v1/users/coupon"

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
    