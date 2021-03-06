# pull official base image
FROM python:3.9.5-slim-buster

# set work directory
WORKDIR /code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /code/
COPY manage.py /code/
RUN pip install -r requirements.txt

# copy project
COPY . /code