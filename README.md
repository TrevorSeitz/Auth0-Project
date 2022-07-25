# Auth0 Python Web App

## General info
This project is a first pass at the requested app for Charlie T. Customer.

## Technologies
Project is created with:
* Python - flask.
* Auth0 login and Management API.
* created using the Auth0 Python Quickstart example.


## Setup
To run this project, download or clone this repo and run it in Python3.
/usr/local/bin/python3 (or where ever Python3 is stored) **repo location**/Auth0-Project/01-Login/server.py.

* The credentials examples are in the .env.example file.  You should add your own or request the test client information.

## Required Features

* The app will use the Auth0 Management API to get the Clients and Actions.
* The app will prompt the user to log in using the Auth0 Authentication process.
* The app is only accessible to the Client’s users with the “Admin” role assigned using Auth0 Authorization Core.  
* Upon launch, the app will execute a search that will gather all client apps and actions, then create a list of those applications, the actions that apply to each application and the triggers assigned to the action.
* The app can be dynamically updated with a refresh button.

## Please dirrect questions and comments to trevinla@gmail.com