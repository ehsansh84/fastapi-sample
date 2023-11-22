#FROM ubuntu:latest
FROM python:3.10
RUN pip install pytest
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt
COPY . /app/
CMD python /app/main.py
