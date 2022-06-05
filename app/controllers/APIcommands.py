import requests
import json

#urlservidor = 'http://127.0.0.1:5001'
urlservidor ='https://a3-commands-api.herokuapp.com'


def searchCommandSpecific(type, token):
    url = f"{urlservidor}/v1/commands/search/{type}"

    payload = {}
    headers = {"Content-Type": "application/json",
               "Authorization": f"Bearer {token}"
               }

    response = requests.request("GET", url, json=payload, headers=headers)

    return response.json()


def saveCommand(type_id, title, description, commands, tags, creator, token):
    url = f"{urlservidor}/v1/commands"

    payload = {
        "title": title,
        "description": description,
        "commands": commands,
        "tags": tags,
        "creator": creator,
        "type_id": type_id

    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }

    response = requests.request("POST", url, headers=headers, json=payload)

    return response.json()


def deleteCommand(id, token):
    url = f"{urlservidor}/v1/commands/{id}"

    payload = {

    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }

    response = requests.request("DELETE", url, headers=headers, json=payload)

    return response.json()


def updateCommand(idCommands, type_id, title, description, commands, tags, creator, token):
    url = f"{urlservidor}/v1/commands/{idCommands}"

    payload = {
        "title": title,
        "description": description,
        "commands": commands,
        "tags": tags,
        "creator": creator,
        "type_id": type_id

    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }

    response = requests.request("PUT", url, headers=headers, json=payload)

    return response.json()
