import http.client
import json
from os import environ as env
from urllib.parse import quote_plus, urlencode

from authlib.integrations.flask_client import OAuth
from dotenv import find_dotenv, load_dotenv
from flask import Flask, redirect, render_template, session, url_for

client_id=env.get("AUTH0_CLIENT_ID"),
client_secret=env.get("AUTH0_CLIENT_SECRET"),
# client_id = 'xxxxxxxxxxxxxxxxxxxx'
# client_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
path = env.get("AUTH0_DOMAIN")
manage_secret = env.get("AUTH0_MANAGE_SECRET")

# GET THE ACCESS TOKEN using the client_id and client_secret
# conn = http.client.HTTPSConnection(env.get("AUTH0_CLIENT_SECRET"))
conn = http.client.HTTPSConnection("auth0-project.us.auth0.com")
# payload = "{\"client_id\":\""+client_id+"\",\"client_secret\":\""+client_secret+"\",\"audience\":\"auth0-project.us.auth0.com/api/v2/\",\"grant_type\":\"client_credentials\"}"
payload = "{\"client_id\":\"{client_id}\",\"client_secret\":\"{client_secret}\",\"audience\":\"https:\"({path} + /api/v2/)\",\"grant_type\":\"client_credentials\"}"
headers = { 'content-type': "application/json" }
conn.request("POST", "/oauth/token", payload, headers)
res = conn.getresponse()
data = res.read()
tokendetails_json = data.decode('utf8').replace("'", '"')
# Load the JSON to a Python list & dump it back out as formatted JSON
# tokendetails = json.loads(tokendetails_json)
# print("token details", tokendetails)

#NOW GET THE USERS AND TOTAL
# conn = http.client.HTTPSConnection({path})
conn = http.client.HTTPSConnection("auth0-project.us.auth0.com")
# payload = "{\"client_id\":\""+client_id+"\",\"client_secret\":\""+client_secret+"\",\"audience\":\"https:\""+path+" + /api/v2/\",\"grant_type\":\"client_credentials\"}"
payload = "{\"client_id\":\"{client_id}\",\"client_secret\":\"{client_secret}\",\"audience\":\"https:\"({path} + /api/v2/)\",\"grant_type\":\"client_credentials\"}"
# headers = { 'content-type': "application/json","Authorization": "Bearer "+tokendetails['access_token'] }
headers = { 'content-type': "application/json","Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlNaY01kRTlrYkxTcFhPaGpabnM2QiJ9.eyJpc3MiOiJodHRwczovL2F1dGgwLXByb2plY3QudXMuYXV0aDAuY29tLyIsInN1YiI6IjRhbGNWQVhhRWh4MnB1VUtnNms2eU42RmxoUmZmMVdQQGNsaWVudHMiLCJhdWQiOiJodHRwczovL2F1dGgwLXByb2plY3QudXMuYXV0aDAuY29tL2FwaS92Mi8iLCJpYXQiOjE2NTgxNTU0ODksImV4cCI6MTY1ODI0MTg4OSwiYXpwIjoiNGFsY1ZBWGFFaHgycHVVS2c2azZ5TjZGbGhSZmYxV1AiLCJzY29wZSI6InJlYWQ6Y2xpZW50X2dyYW50cyBjcmVhdGU6Y2xpZW50X2dyYW50cyBkZWxldGU6Y2xpZW50X2dyYW50cyB1cGRhdGU6Y2xpZW50X2dyYW50cyByZWFkOnVzZXJzIHVwZGF0ZTp1c2VycyBkZWxldGU6dXNlcnMgY3JlYXRlOnVzZXJzIHJlYWQ6dXNlcnNfYXBwX21ldGFkYXRhIHVwZGF0ZTp1c2Vyc19hcHBfbWV0YWRhdGEgZGVsZXRlOnVzZXJzX2FwcF9tZXRhZGF0YSBjcmVhdGU6dXNlcnNfYXBwX21ldGFkYXRhIHJlYWQ6dXNlcl9jdXN0b21fYmxvY2tzIGNyZWF0ZTp1c2VyX2N1c3RvbV9ibG9ja3MgZGVsZXRlOnVzZXJfY3VzdG9tX2Jsb2NrcyBjcmVhdGU6dXNlcl90aWNrZXRzIHJlYWQ6Y2xpZW50cyB1cGRhdGU6Y2xpZW50cyBkZWxldGU6Y2xpZW50cyBjcmVhdGU6Y2xpZW50cyByZWFkOmNsaWVudF9rZXlzIHVwZGF0ZTpjbGllbnRfa2V5cyBkZWxldGU6Y2xpZW50X2tleXMgY3JlYXRlOmNsaWVudF9rZXlzIHJlYWQ6Y29ubmVjdGlvbnMgdXBkYXRlOmNvbm5lY3Rpb25zIGRlbGV0ZTpjb25uZWN0aW9ucyBjcmVhdGU6Y29ubmVjdGlvbnMgcmVhZDpyZXNvdXJjZV9zZXJ2ZXJzIHVwZGF0ZTpyZXNvdXJjZV9zZXJ2ZXJzIGRlbGV0ZTpyZXNvdXJjZV9zZXJ2ZXJzIGNyZWF0ZTpyZXNvdXJjZV9zZXJ2ZXJzIHJlYWQ6ZGV2aWNlX2NyZWRlbnRpYWxzIHVwZGF0ZTpkZXZpY2VfY3JlZGVudGlhbHMgZGVsZXRlOmRldmljZV9jcmVkZW50aWFscyBjcmVhdGU6ZGV2aWNlX2NyZWRlbnRpYWxzIHJlYWQ6cnVsZXMgdXBkYXRlOnJ1bGVzIGRlbGV0ZTpydWxlcyBjcmVhdGU6cnVsZXMgcmVhZDpydWxlc19jb25maWdzIHVwZGF0ZTpydWxlc19jb25maWdzIGRlbGV0ZTpydWxlc19jb25maWdzIHJlYWQ6aG9va3MgdXBkYXRlOmhvb2tzIGRlbGV0ZTpob29rcyBjcmVhdGU6aG9va3MgcmVhZDphY3Rpb25zIHVwZGF0ZTphY3Rpb25zIGRlbGV0ZTphY3Rpb25zIGNyZWF0ZTphY3Rpb25zIHJlYWQ6ZW1haWxfcHJvdmlkZXIgdXBkYXRlOmVtYWlsX3Byb3ZpZGVyIGRlbGV0ZTplbWFpbF9wcm92aWRlciBjcmVhdGU6ZW1haWxfcHJvdmlkZXIgYmxhY2tsaXN0OnRva2VucyByZWFkOnN0YXRzIHJlYWQ6aW5zaWdodHMgcmVhZDp0ZW5hbnRfc2V0dGluZ3MgdXBkYXRlOnRlbmFudF9zZXR0aW5ncyByZWFkOmxvZ3MgcmVhZDpsb2dzX3VzZXJzIHJlYWQ6c2hpZWxkcyBjcmVhdGU6c2hpZWxkcyB1cGRhdGU6c2hpZWxkcyBkZWxldGU6c2hpZWxkcyByZWFkOmFub21hbHlfYmxvY2tzIGRlbGV0ZTphbm9tYWx5X2Jsb2NrcyB1cGRhdGU6dHJpZ2dlcnMgcmVhZDp0cmlnZ2VycyByZWFkOmdyYW50cyBkZWxldGU6Z3JhbnRzIHJlYWQ6Z3VhcmRpYW5fZmFjdG9ycyB1cGRhdGU6Z3VhcmRpYW5fZmFjdG9ycyByZWFkOmd1YXJkaWFuX2Vucm9sbG1lbnRzIGRlbGV0ZTpndWFyZGlhbl9lbnJvbGxtZW50cyBjcmVhdGU6Z3VhcmRpYW5fZW5yb2xsbWVudF90aWNrZXRzIHJlYWQ6dXNlcl9pZHBfdG9rZW5zIGNyZWF0ZTpwYXNzd29yZHNfY2hlY2tpbmdfam9iIGRlbGV0ZTpwYXNzd29yZHNfY2hlY2tpbmdfam9iIHJlYWQ6Y3VzdG9tX2RvbWFpbnMgZGVsZXRlOmN1c3RvbV9kb21haW5zIGNyZWF0ZTpjdXN0b21fZG9tYWlucyB1cGRhdGU6Y3VzdG9tX2RvbWFpbnMgcmVhZDplbWFpbF90ZW1wbGF0ZXMgY3JlYXRlOmVtYWlsX3RlbXBsYXRlcyB1cGRhdGU6ZW1haWxfdGVtcGxhdGVzIHJlYWQ6bWZhX3BvbGljaWVzIHVwZGF0ZTptZmFfcG9saWNpZXMgcmVhZDpyb2xlcyBjcmVhdGU6cm9sZXMgZGVsZXRlOnJvbGVzIHVwZGF0ZTpyb2xlcyByZWFkOnByb21wdHMgdXBkYXRlOnByb21wdHMgcmVhZDpicmFuZGluZyB1cGRhdGU6YnJhbmRpbmcgZGVsZXRlOmJyYW5kaW5nIHJlYWQ6bG9nX3N0cmVhbXMgY3JlYXRlOmxvZ19zdHJlYW1zIGRlbGV0ZTpsb2dfc3RyZWFtcyB1cGRhdGU6bG9nX3N0cmVhbXMgY3JlYXRlOnNpZ25pbmdfa2V5cyByZWFkOnNpZ25pbmdfa2V5cyB1cGRhdGU6c2lnbmluZ19rZXlzIHJlYWQ6bGltaXRzIHVwZGF0ZTpsaW1pdHMgY3JlYXRlOnJvbGVfbWVtYmVycyByZWFkOnJvbGVfbWVtYmVycyBkZWxldGU6cm9sZV9tZW1iZXJzIHJlYWQ6ZW50aXRsZW1lbnRzIHJlYWQ6YXR0YWNrX3Byb3RlY3Rpb24gdXBkYXRlOmF0dGFja19wcm90ZWN0aW9uIHJlYWQ6b3JnYW5pemF0aW9uc19zdW1tYXJ5IHJlYWQ6b3JnYW5pemF0aW9ucyB1cGRhdGU6b3JnYW5pemF0aW9ucyBjcmVhdGU6b3JnYW5pemF0aW9ucyBkZWxldGU6b3JnYW5pemF0aW9ucyBjcmVhdGU6b3JnYW5pemF0aW9uX21lbWJlcnMgcmVhZDpvcmdhbml6YXRpb25fbWVtYmVycyBkZWxldGU6b3JnYW5pemF0aW9uX21lbWJlcnMgY3JlYXRlOm9yZ2FuaXphdGlvbl9jb25uZWN0aW9ucyByZWFkOm9yZ2FuaXphdGlvbl9jb25uZWN0aW9ucyB1cGRhdGU6b3JnYW5pemF0aW9uX2Nvbm5lY3Rpb25zIGRlbGV0ZTpvcmdhbml6YXRpb25fY29ubmVjdGlvbnMgY3JlYXRlOm9yZ2FuaXphdGlvbl9tZW1iZXJfcm9sZXMgcmVhZDpvcmdhbml6YXRpb25fbWVtYmVyX3JvbGVzIGRlbGV0ZTpvcmdhbml6YXRpb25fbWVtYmVyX3JvbGVzIGNyZWF0ZTpvcmdhbml6YXRpb25faW52aXRhdGlvbnMgcmVhZDpvcmdhbml6YXRpb25faW52aXRhdGlvbnMgZGVsZXRlOm9yZ2FuaXphdGlvbl9pbnZpdGF0aW9ucyIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyJ9.tqzMadMDqX21AB1jZ4TF0OXXakUm2EY4QH4DVIGo5McY1d6w91bOgITgBIXIpOWTKOOoBNoNQddlHkMenNnfIrhIv24AePOY2C5PHR_j4PYzA4Ud_jYfG-Zl8opYMVDx371nSzt68G8_kxHHbTe9mXpR7tNcCJ7sTozqmzJER8POkZ5jwFiDNfEENsAfYRa6t7tJbPTWi-28pyOG0M2tuOPp8rvbbeUZjyVcSjD6tgbwLphupJi_07eE_0tdMV-e_8Arm_CMTalh5IN40C4lTea_F-Ca1og5dTFEK5PQ4xu2u0s9mt6ZJ9eJoX1w7FgV1-lggPP2Zy-k9bxsbD1W5w"  }

conn.request("GET", "/api/v2/clients?include_totals=true", payload, headers)
res = conn.getresponse()
data = res.read()
result_data_json = data.decode('utf8').replace("'", '"')

# Load the JSON to a Python list & dump it back out as formatted JSON
result_data = json.loads(result_data_json)
client_list = result_data["clients"]
# print(result_data)                  # Json list of all users
# print(result_data['total'])         # Just the count of total users
# print(client_list)         # client list