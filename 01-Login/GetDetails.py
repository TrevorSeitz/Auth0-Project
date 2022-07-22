from ssl import OP_NO_RENEGOTIATION
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
    # print("list - ", list)
    for i in range(length):
        client_names.append(list[i]["name"])
        client_names.append(list[i]["client_id"])
    client_id_list = tuple(client_names)
    return(client_id_list)


def get_action_list():
    list_dict = action_list(client_id, client_secret, path, manage_secret)
    list_of_actions = []
    length = len(list_dict["actions"])
    # Iterating the list to get the actions
    for i in range(length):
        action = {}
        action["Action Name"] = list_dict["actions"][i]["name"]
        action["code"] = list_dict["actions"][i]["code"]
        list_of_actions.append(action)
    
    return(list_of_actions)
   
                
# get_client_names()
# get_action_list()