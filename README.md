# fyp_recording_app_backend

## To Start A New Django Development Server:
1. Open an empty project file in Visual Studio Code
2. First, create python virtual environment by following the steps shown on this website: https://sourabhbajaj.com/mac-setup/Python/virtualenv.html
3. Install Django: **pip install Django**
4. Install Django Rest Framework: **pip install djangorestframework**
5. To create a project in Django: **django-admin startproject FYPRecordingApp**
6. Change directories to FYPRecordingApp: **cd FYPRecordingApp**
7. Run the development server: **python manage.py runserver**
8. To create app, write: **python manage.py startapp “appname”**
9. To create Django superuser: **python manage.py createsuperuser**
10. To make a database, create model in the models.py
11. If any changes are made to models, serializers, view, e.t.c, migrate changes into the Django development server by following these two commands: **python manage.py makemigrations** and **python manage.py migrate**
12. To use your external IP addres, first add your IP addres to ALLOWED_HOSTS in settings.py
13. cd into your directory and run the following command to start the development server on your external IP addres: **python manage.py runserver 116.86.130.58:8000** (replace the IP address with your own)
