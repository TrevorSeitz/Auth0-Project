from os import environ as env
from GetClients import client_list
from dotenv import find_dotenv, load_dotenv
from GetActions import action_list

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
    for i in range(length):
        client_names.append(list[i]["name"])
        client_names.append(list[i]["client_id"])
    client_id_list = tuple(client_names)
    return(client_id_list)

def get_action_list():
    list_dict = action_list()
    list_of_actions = []
    length = len(list_dict["actions"])
    # Iterating the list to get the actions
    for i in range(length):
        action = {}
        action["Action Name"] = list_dict["actions"][i]["name"] + " - Trigger: " + list_dict["actions"][i]["supported_triggers"][0]["id"] 
        action["code"] = list_dict["actions"][i]["code"]
        list_of_actions.append(action)
    return(list_of_actions)