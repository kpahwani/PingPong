# PingPong
Ping Pong autonomous game with user and admin view

Setup
    Create a ython virtual enviorment
    Install Django
    Import the PIngPong project
    Create database using magae.py task:
      -manage.py makemigrations
      -manage.py migrate
    Start serve yo host the application on browser:
      -manage.py runserver
    
Deployment:
    Before deployment don't forget to set the DEBUG flag to False in settings.py

Project technology specifications:
    Django - The web framework
    Python - Language
    Databases - sqlite
    Templates - DjangoTemplates
    RestAPI - Rest api framework

Start project:
    Enter [http://127.0.0.1:8000/home/] in browser this will take you to the home page

Project Structure:
    PingPong Project:
      Contains project setting and url mapings.    
    Players:
      Application to manage players information 
    Refree Application:
      Application to validate/conduct the championship and present the results.

REST API calls:
    http://127.0.0.1:8000/referee/activate_users/ <br>
    http://127.0.0.1:8000/referee/all_players/
    http://127.0.0.1:8000/referee/start_game/
    http://127.0.0.1:8000/referee/get_results/

Function call:
    The CURD oerations for player application are managed using function call.
    
Authors
    Kaushal Pahwani
    
