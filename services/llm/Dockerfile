FROM python:3.9-slim

WORKDIR /app

COPY ../infra/requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY . /app
