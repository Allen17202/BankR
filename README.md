# BankR
Banking System built with Django and Python
# App Features
  - Display Account Balance and Number.
  - Support  Account Types (e.x. Checking Account, Savings Account)
  - Transaction report
  - See balance after every transaction in the Transaction Report

# Prerequistes
Be sure you have the following installed on your development machine:
  -	Python3
  -	Ubuntu Command Line
  -	Git
  -	pip
  -	Virtualenv 

# Requirements
-	asgiref==3.3.1
-	Django==3.1.3
-	psycopg2-binary==2.8.6
-	pytz==2020.4
-	sqlparse==0.4.12.8.1

# Project Install
To setup a local development environment:
Create a virtual environment in which to install Python pip packages.Used On Ubuntu

```bash
pip3 install virtualenv	   # Save it next to project folder
virtualenv venv            # create a virtualenv, venv can be whatever name you want
source venv/bin/activate   # activate the Python virtualenv, can be deactivated with cmd deactivate
```
Clone GitHub Project,
```bash
git clone https://github.com/Allen17202/BankR.git #make sure you are in the python virtual envirnonment
cd BankR
```
Install development dependencies,
```bash
pip install -r requirements.txt
```
Migrate Database,
```python
python manage.py makemigrations
python manage.py migrate
```
Run the web application locally,
```python
python manage.py runserver # 127.0.0.1:8000 
```
Create Superuser,
```python
python manage.py createsuperuser  #input ideal username and password
```

