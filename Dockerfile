# syntax = docker/dockerfile:experimental
FROM python:latest

WORKDIR /root

ENV DJANGO_SUPERUSER_USERNAME=admin
ARG DJANGO_SUPERUSER_PASSWORD=admin
ARG DJANGO_SUPERUSER_EMAIL=admin@example.com

COPY requirements.txt ./requirements.txt
COPY account ./account
COPY TaskManager ./TaskManager
COPY manage.py ./manage.py
COPY docker/entrypoint.sh ./entrypoint.sh

RUN pip install -r requirements.txt
