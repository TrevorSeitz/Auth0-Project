import http.client
import json

from os import environ as env
from urllib.parse import urlencode
from GetToken import get_token
from dotenv import find_dotenv, load_dotenv


ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)
AUTH0_DOMAIN = env.get("AUTH0_DOMAIN")
AUTH0_API_IDENTIFIER = env.get("API_IDENTIFIER")
AUTH0_CLIENT_ID = env.get("CLIENT_ID")
AUTH0_CLIENT_SECRET= env.get("CLIENT_SECRET")

def client_list():
    token = "Bearer " + get_token()
    
    conn = http.client.HTTPSConnection((AUTH0_DOMAIN))
    payload = { 
            "client_id": AUTH0_CLIENT_ID,
            "client_secret": AUTH0_CLIENT_SECRET,
            "audience": AUTH0_API_IDENTIFIER,
            "grant_type": "client_credentials" 
            }
    headers = { 'content-type': "application/json","authorization": token }

    conn.request("GET", "/api/v2/clients", urlencode(payload), headers)
    res = conn.getresponse()
    data = res.read()
    result_data_json = data.decode('utf8').replace("'", '"')

    # Load the JSON to a Python list & dump it back out as formatted JSON
    result_data = json.loads(result_data_json)
    client_list = result_data
    
    # print("client_list - ", client_list)
    return client_list

# client_list(AUTH0_CLIENT_ID, AUTH0_CLIENT_SECRET, AUTH0_API_IDENTIFIER, AUTH0_DOMAIN)
client_list()