import http.client
import json
from os import environ as env


client_secrets = env.get("AUTH0_CLIENT_SECRET")
conn = http.client.HTTPSConnection("auth0-project.us.auth0.com")

payload = "grant_type=client_credentials&client_id=zd8SShr3UL94mkQHDIulCHJ59Vg1Hvj2&client_secret=JRQ7PIgGI8WgyI_VhrtDaD4SaYg0WdJ_tqNlqW1wsYQc-UQRtYNIYID5K6ddxwBK&audience=https%3A%2F%2Fauth0-project.us.auth0.com%2Fapi%2Fv2%2F"

headers = { 'content-type': "application/x-www-form-urlencoded" }

headers = { 'content-type': "application/x-www-form-urlencoded" }

conn.request("POST", "/auth0-project.us.auth0.com/oauth/token", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))