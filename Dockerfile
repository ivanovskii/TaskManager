# syntax = docker/dockerfile:experimental
FROM python:latest as builder

WORKDIR /root

ENV VIRTUAL_ENV=/root/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY account ./account
COPY TaskManager ./TaskManager
COPY manage.py ./manage.py

RUN python manage.py makemigrations account
RUN python manage.py migrate
ARG DJANGO_SUPERUSER_USERNAME
ARG DJANGO_SUPERUSER_PASSWORD
RUN python manage.py createsuperuser --noinput
