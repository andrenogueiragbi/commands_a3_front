import requests
import json



def searchCommandSpecific(type='outros'):
    url = f"http://localhost:5000/v1/commands/search/{type}"

    payload = {

    }
    headers = {"Content-Type": "application/json"}

    response = requests.request("GET", url, headers=headers)
    
    return response.json()

def saveCommand(type_id,title,description,commands,tags,creator):
    url = f"http://localhost:5000/v1/commands"

    payload = {
        "title": title,
        "description": description,
        "commands": commands,
        "tags": tags,
        "creator": creator,
        "type_id": type_id

    }
    headers = {"Content-Type": "application/json"}

    response = requests.request("POST", url, headers=headers,json=payload)
    
    return response.json()


def deleteCommand(id):
    url = f"http://localhost:5000/v1/commands/{id}"

    payload = {

    }
    headers = {"Content-Type": "application/json"}

    response = requests.request("DELETE", url, headers=headers,json=payload)

    return response.json()


def updateCommand(idCommands,type_id,title,description,commands,tags,creator):
    url = f"http://localhost:5000/v1/commands/{idCommands}"

    payload = {
        "title": title,
        "description": description,
        "commands": commands,
        "tags": tags,
        "creator": creator,
        "type_id": type_id

    }
    headers = {"Content-Type": "application/json"}

    response = requests.request("PUT", url, headers=headers,json=payload)
    
    return response.json()