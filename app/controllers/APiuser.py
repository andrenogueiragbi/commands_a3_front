import requests
import json

urlservidor = 'http://127.0.0.1:5001'
#urlservidor ='https://a3-commands-api.herokuapp.com'


def searchUser(token):
    url = f"{urlservidor}/v1/users"

    payload = {}
    headers = {"Content-Type": "application/json",
               "Authorization": f"Bearer {token}"
               }

    response = requests.request("GET", url, json=payload, headers=headers)

    return response.json()

def searchUserId(id,token):
    url = f"{urlservidor}/v1/users/{id}"

    payload = {}
    headers = {"Content-Type": "application/json",
               "Authorization": f"Bearer {token}"
               }

    response = requests.request("GET", url, json=payload, headers=headers)

    return response.json()

def saveNewUser(name,email,password,level,company,token):
    url = f"{urlservidor}/v1/users"

    payload = {
        "name": name,
        "email": email,
        "password": password,
        "level": level,
        "company": company,  

    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }

    response = requests.request("POST", url, headers=headers, json=payload)

    return response.json()



def deleteUser(id, token):
    url = f"{urlservidor}/v1/users/{id}"

    payload = {

    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }

    response = requests.request("DELETE", url, headers=headers, json=payload)

    return response.json()


def updateUser(idUser, name,email,password,level,company,token):
    url = f"{urlservidor}/v1/users/{idUser}"

    payload = {
        "name": name,
        "email": email,
        "password": password if password != "" else False,
        "level": level,
        "company": company,

    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }

    response = requests.request("PUT", url, headers=headers, json=payload)

    return response.json()
