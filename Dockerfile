FROM python:3.10-alpine

WORKDIR /restaurants
COPY requirements.txt /restaurants/
RUN pip install -r requirements.txt
COPY . /restaurants/
