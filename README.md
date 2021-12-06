http://3.87.15.199/messages/
http://3.87.15.199/

Installations:
- pip install django
- pip install djangorestframework

Start:
- django-admin startproject chat_project
- cd chat_project # Enter ur proj dir
- python manage.py startapp chat_app

After:
- Add 'chat_app' and 'rest_framework' into INSTALLED_APPS


python manage.py migrate --run-syncdb
