FROM python:3.9.2-slim-buster

RUN apt update \
    && pip3 install --upgrade pip

WORKDIR /opt/app

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY main.py main.py
ENTRYPOINT python3 main.py