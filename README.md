# Auth0 Python Web App

## General info
This project is a first pass at the requested app for Charlie T. Customer.

## Technologies
Project is created with:
* Python - flask.
* Auth0 login and Management API.
* created using the Auth0 Python Quickstart example.


## Setup
To run this project, you must first grant the client access to Management API.  To do this, you will need to go to your manage.auth0.com Dashboard, click on "Applications", then "APIs", and finally "Auth0 Management API".Once there, you will need to go to the "Machine to Machine Applications" tab and ensure your application is authorized.  Then, click on the deopdown arrow to the right of the authorization switch and enable the permissions to "read:clients" and "read:actions".

Once the client is authorized, download or clone this repo and run it in the terminal (or Shell) at the 01-Login/ level of the directory it is in.  run it by typing:  python3 server.py.

* The credentials examples are in the .env.example file.  You should add your credentials to the file or request the test client information, and then save the file as simply .env.

## Required Features

* The app will use the Auth0 Management API to get the Clients and Actions.
* The app will prompt the user to log in using the Auth0 Authentication process.
* The app is only accessible to the Client’s users with the “Admin” role assigned using Auth0 Authorization Core.  
* Upon launch, the app will execute a search that will gather all client apps and actions, then create a list of those applications, the actions that apply to each application and the triggers assigned to the action.
* The app can be dynamically updated with a refresh button.

## Please dirrect questions and comments to trevinla@gmail.com