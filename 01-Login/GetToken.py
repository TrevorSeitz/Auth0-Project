import http.client
import json

from os import environ as env
from urllib.parse import urlencode
from dotenv import load_dotenv, find_dotenv
from flask import Flask, request, redirect, render_template, session, url_for

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)
AUTH0_API_IDENTIFIER = env.get("API_IDENTIFIER")
AUTH0_DOMAIN = env.get("AUTH0_DOMAIN")
AUTH0_CLIENT_ID = env.get("CLIENT_ID")
AUTH0_CLIENT_SECRET= env.get("CLIENT_SECRET")

# def get_token(AUTH0_DOMAIN, AUTH0_CLIENT_ID, AUTH0_CLIENT_SECRET, AUTH0_API_IDENTIFIER):
def get_token():
    conn = http.client.HTTPSConnection((AUTH0_DOMAIN))
    payload = { 
            "client_id": AUTH0_CLIENT_ID,
            "client_secret": AUTH0_CLIENT_SECRET,
            "audience": AUTH0_API_IDENTIFIER,
            "grant_type": "client_credentials" 
            }
    headers = { 'content-type': "application/x-www-form-urlencoded" }

    conn.request("POST", "/oauth/token", urlencode(payload), headers)
    # THIS returns a jwt token - res
    res = conn.getresponse()
    data = res.read() 
    tokendetails_json = data.decode('utf8').replace("'", '"') # convert to json
    message = json.loads(tokendetails_json) 
    token = message['access_token'] # get the token

    # print("token - ", token)
    # session["auth_token"] = token
    
    app = Flask(__name__)
    app.token = token
    return token

# get_token(AUTH0_DOMAIN, AUTH0_CLIENT_ID, AUTH0_CLIENT_SECRET, AUTH0_API_IDENTIFIER)
get_token()
