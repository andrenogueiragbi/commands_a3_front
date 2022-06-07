import requests
import json

urlservidor ='http://127.0.0.1:5001'
#urlservidor ='https://a3-commands-api.herokuapp.com'


def makeRegister(name,email,password,ticket,company):
    url = f"{urlservidor}/v1/users/ticket/"

    payload = {
        "name": name,
        "email": email,
        "password": password,
        "ticket":ticket,
        "company":company
    }
    headers = {"Content-Type": "application/json"}

    response = requests.request("POST", url, json=payload, headers=headers)
    
    return response.json()
    
def createTicket(email_user,token):
    url = f"{urlservidor}/v1/ticket/"

    headers = {"Content-Type": "application/json",
               "Authorization": f"Bearer {token}"}

    payload = {
        "email_user": email_user,
    }


    response = requests.request("POST", url, json=payload, headers=headers)
    
    return response.json()
    