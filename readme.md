# Project Name: Corporate Asset Tracker

## Project Goals:
1. The application might be used by several companies
2. Each company might add all or some of its employees
3. Each company and its staff might delegate one or more devices to employees for a certain period of time
4. Each company should be able to see when a Device was checked out and returned
5. Each device should have a log of what condition it was handed out and returned

## Steps to run the project in your machine
1. git clone https://github.com/sanowar-dwn/asset_tracker.git
2. pip install -r requirements.txt
3. py manage.py makemigrations
4. py manage.py migrate
5. py manage.py createsuperuser
6. py manage.py runserver

## Interacting with the app
1. http://127.0.0.1:8000/admin/ - SuperAdmin Dashboard
2. http://127.0.0.1:8000/swagger/ - API Documentation
