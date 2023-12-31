# Python-Django-Multi_Format_Data_Processor
#### This project is running with Django web server.
#### Now you can use this to parse .pdf to .txt or .doc

<br>

## Requirements
1. Please use ```pip install Django``` in cmd to install Django framework.
2. Please use pip install to install all libs in the requirements.txt.
3. If encountered migrations/migrate related problem, please use following lines in cmd under root dir to repair
   ```cmd
   python manage.py makemigrations
   python manage.pt migrate
   ```


## How to run
* Open cmd and cd to the root dir of the Django project, run ```python manage.py runserver``` to start the server at local. 
* Use browser to open 127.0.0.1:8000
* To manipulate user database, please go to ```127.0.0.1:8000/admin``` with superuser account.

## Authentication
* I've added a superuser:
  ```
  username: admin
  password: 12345678
  ```
* For pdf_reader, I created an account:
  ```
  username: admin
  password: 12345678
  ```
* No session or token authentication for other apps.
