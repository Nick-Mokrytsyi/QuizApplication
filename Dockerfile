FROM python:3.10.10-slim

RUN apt update && \
    apt-get install -y python3-dev libpq-dev gcc curl && \
    apt-get install -y mc vim


ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /opt/src
WORKDIR /opt/src

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    rm -f requirements.txt

COPY src .
#COPY .env_prod ../.env


EXPOSE 1488

#CMD python manage.py runserver 0.0.0.0:1488
