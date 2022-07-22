from ssl import OP_NO_RENEGOTIATION
from GetClients import client_list
from dotenv import find_dotenv, load_dotenv
from GetActions import action_list
from os import environ as env
import json
from pathlib import Path

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)
AUTH0_DOMAIN = env.get("AUTH0_DOMAIN")
AUTH0_API_IDENTIFIER = env.get("API_IDENTIFIER")
AUTH0_CLIENT_ID = env.get("CLIENT_ID")
AUTH0_CLIENT_SECRET= env.get("CLIENT_SECRET")

def get_client_names():
    list = client_list()
    length = len(list)   
    client_names = []
    # Iterating the list to get the client names
    # print("list - ", list)
    for i in range(length):
        client_names.append(list[i]["name"])
        client_names.append(list[i]["client_id"])
    client_id_list = tuple(client_names)
        # print("client_names: ", list[i]["name"])
        # client_names.append(list[i]["name"])
        
    # print("client_id_list - ", client_id_list)

    return(client_id_list)


def get_action_list():
    list_dict = action_list()
    list_of_actions = []
    # print("list_dict - ", type(list_dict), list_dict)
    length = len(list_dict["actions"])
    # Iterating the list to get the actions
    for i in range(length):
        action = {}
        action["Action Name"] = list_dict["actions"][i]["name"]
        action["code"] = list_dict["actions"][i]["code"]
        list_of_actions.append(action)
        
    # print("list_of_actions - ", list_of_actions)
    return(list_of_actions)
   
                
# get_client_names()
# get_action_list()