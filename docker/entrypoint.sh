#!/bin/sh

python manage.py makemigrations account --noinput
python manage.py migrate --noinput
python manage.py createsuperuser --noinput
python manage.py runserver 0.0.0.0:80