# import http.client
# import json
# from os import environ as env


# client_secrets = env.get("AUTH0_CLIENT_SECRET")
# conn = http.client.HTTPSConnection("auth0-project.us.auth0.com")

# payload = "grant_type=client_credentials&client_id=zd8SShr3UL94mkQHDIulCHJ59Vg1Hvj2&client_secret=JRQ7PIgGI8WgyI_VhrtDaD4SaYg0WdJ_tqNlqW1wsYQc-UQRtYNIYID5K6ddxwBK&audience=https%3A%2F%2Fauth0-project.us.auth0.com%2Fapi%2Fv2%2F"

# headers = { 'content-type': "application/x-www-form-urlencoded" }

# headers = { 'content-type': "application/x-www-form-urlencoded" }

# conn.request("POST", "/auth0-project.us.auth0.com/oauth/token", payload, headers)

# res = conn.getresponse()
# data = res.read()

# print(data.decode("utf-8"))

import http.client
import json
from os import environ as env

from urllib.parse import urlencode, quote_plus

from dotenv import load_dotenv, find_dotenv
from flask import Flask, request, jsonify, _request_ctx_stack, Response
from flask_cors import cross_origin
from jose import jwt

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)
AUTH0_DOMAIN = env.get("AUTH0_DOMAIN")
AUTH0_API_IDENTIFIER = env.get("API_IDENTIFIER")
AUTH0_CLIENT_ID = env.get("CLIENT_ID")
AUTH0_CLIENT_SECRET= env.get("CLIENT_SECRET")
AUTH0_OTHER_IDENTIFIER= env.get("OTHER_IDENTIFIER")
ALGORITHMS = ["RS256"]
APP = Flask(__name__)

print("==========================================================")

conn = http.client.HTTPSConnection((AUTH0_DOMAIN))
# conn = http.client.HTTPSConnection("")

# payload = "grant_type=client_credentials&client_id=MY_CLIENT_ID%7D&client_secret=MY_CLIENT_SECRET&audience=MY_API_IDENTIFIER"
# payload = "grant_type=client_credentials&client_id=%24%7BMY_CLIENT_ID%7D&client_secret=MY_CLIENT_SECRET&audience=MY_API_IDENTIFIER"
payload = { 
        "client_id": AUTH0_CLIENT_ID,
        "client_secret": AUTH0_CLIENT_SECRET,
        "audience": AUTH0_API_IDENTIFIER,
        "grant_type": "client_credentials" 
        }
        
print("payload: ", payload)

new_payload = urlencode(payload)

print("new_payload: ", new_payload)

headers = { 'content-type': "application/json"}

conn.request("POST", "/oauth/token", new_payload, headers)
# THIS returns a jwt token - res
res = conn.getresponse()
print("res: ", res)
data = res.read()
message = json.loads(data.decode("utf-8"))
token = message['access_token']
print("res: ", res)
print("message: ", message)

print("token ", token)

# print(CLIENT_SECRET)