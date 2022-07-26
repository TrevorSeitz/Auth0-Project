import json
import http.client
import requests 

from os import environ as env
from urllib.parse import quote_plus, urlencode
from authlib.integrations.flask_client import OAuth
from dotenv import find_dotenv, load_dotenv
from flask import Flask, request, redirect, render_template, session, url_for
from CombineLists import main_list

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)
    
app = Flask(__name__)
app.secret_key = env.get("CLIENT_SECRET")

oauth = OAuth(app)

oauth.register(
    "auth0",
    client_id=env.get("CLIENT_ID"),
    client_secret=env.get("CLIENT_SECRET"),
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f'https://{env.get("AUTH0_DOMAIN")}/.well-known/openid-configuration'
)

@app.route("/login")
def login():
    return oauth.auth0.authorize_redirect(
        redirect_uri=url_for("callback", _external=True)
    )

@app.route("/callback", methods=["GET", "POST"])
def callback():
    token = oauth.auth0.authorize_access_token()
    session["user"] = token
    user = session["user"]
    if user["userinfo"]["https://my-app.example.com/roles"]: 
        for i in user["userinfo"]["https://my-app.example.com/roles"]:
            print("Role = ", i)
            if i == 'Admin':
                return redirect("/")
    return redirect("/logout")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(
        "https://" + env.get("AUTH0_DOMAIN")
        + "/v2/logout?"
        + urlencode(
            {
                "returnTo": url_for("home", _external=True),
                "client_id": env.get("CLIENT_ID"),
            },
            quote_via=quote_plus,
        )
    )

@app.route("/")
def home():
    return render_template(
        "home.html",
        session=session.get("user"),
        client_list=main_list(),
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=env.get("PORT", 3000))