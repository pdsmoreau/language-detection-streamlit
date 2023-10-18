FROM python:3.10.0-slim-buster

WORKDIR /usr/app/src

ARG LANG='en_us.UTF.8'

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY / ./

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt


CMD ["streamlit","run","app.py"]