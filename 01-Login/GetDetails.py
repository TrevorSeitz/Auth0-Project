from GetClients import client_list
# from typing_extensions import Self
from GetActions import action_list
from os import environ as env
import json
from pathlib import Path

client_id=env.get("AUTH0_CLIENT_ID"),
client_secret=env.get("AUTH0_CLIENT_SECRET"),
path = env.get("AUTH0_DOMAIN")
manage_secret = env.get("AUTH0_MANAGE_SECRET")


def get_client_names():
    list = client_list(client_id, client_secret, path, manage_secret)
    length = len(list)   
    client_names = []
    # Iterating the list to get the client names
    for i in range(length):
        client_names.append(list[i]["name"])
    # print("client names - ", client_names)
    return(client_names)


def get_action_list():
    listDir = action_list(client_id, client_secret, path, manage_secret)
    list_of_actions = []
    print("listDir - ", type(listDir))
    length = len(listDir["actions"])
    # Iterating the list to get the actions
    for i in listDir["actions"]:
        action = {}
        loc = listDir["actions"].index(i)
        action["Action Name"] = listDir["actions"][loc]["name"]
        action["code"] = listDir["actions"][loc]["code"]
        print("Action Name - ", action["Action Name"])
        list_of_actions.append(action)
        # print("\n", "\n", "list_of_actions - ", loc + 1, ":  ", list_of_actions)
        return(list_of_actions)
            
# get_client_names()
# get_action_list()