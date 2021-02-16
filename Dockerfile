# syntax = docker/dockerfile:experimental
FROM python:latest as builder

WORKDIR /root

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY account ./account
COPY TaskManager ./TaskManager
COPY manage.py ./manage.py

RUN python manage.py makemigrations account
RUN python manage.py migrate

ENV DJANGO_SUPERUSER_USERNAME=admin
ARG DJANGO_SUPERUSER_PASSWORD=admin
ARG DJANGO_SUPERUSER_EMAIL=admin@example.com
RUN python manage.py createsuperuser --noinput
