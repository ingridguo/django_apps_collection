
# django_apps_collection

Start Django with youtube [Python Django Crash Course](https://www.youtube.com/watch?v=D6esTdOLXh4),
which helps to setup environment with the following requirements:

1. Python 3.6.5
2. Django 2.0.6
3. XAMPP

## create a django project

   In a virtual environment, enter: django-admin startproject django_apps_collection

   (py1) D:\Projects>django-admin startproject django_apps_collections

### create a django app

- run web server

    (py1) D:\Projects\django_apps_collections>python manage.py runserver

### migrate default security data

  This requires a new mysql creation, and modify settings.py

    (py1) D:\Projects\django_apps_collections>python manage.py migrate

### create a super user for localhost:8000/admin (default)

    (py1) D:\Projects\django_apps_collections>python manage.py createsuperuser
     Username (leave blank to use 'iguo'): iguo
     Email address: iguo201xxxx@gmail.com
     Password:
     Password (again):
     Superuser created successfully.

### create an app under project

    (py1) D:\Projects\django_apps_collections>python manage.py startapp posts

### create a data model, and make migrations

    (py1) D:\Projects\django_apps_collections>python manage.py makemigrations posts
    (py1) D:\Projects\django_apps_collections>python manage.py migrate

All the apps will use the above command.
