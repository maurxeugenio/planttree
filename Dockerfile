FROM python:3.8.3-alpine as base

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1


RUN apk update && apk add libffi-dev libpq tzdata python3 && python -m pip install --upgrade pip 

RUN apk add --virtual .build-deps gcc python3-dev musl-dev postgresql-dev build-base \
    jpeg-dev zlib-dev

# Install pip requirements
ADD requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
ENV HOME=/app

ENV LD_PRELOAD=/lib/libssl.so.1.1
