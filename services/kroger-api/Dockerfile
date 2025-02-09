FROM python:3.9-slim

WORKDIR /app

COPY ../infra/central_requirements.txt /app/central_requirements.txt
RUN pip install -r /app/central_requirements.txt

COPY . /app
