FROM python:3.5

RUN apt-get update

RUN pip install --upgrade pip
RUN pip install scrapy boto3

WORKDIR /app
ADD . /app/
