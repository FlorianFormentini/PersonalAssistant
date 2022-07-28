FROM ubuntu:22.04

ADD . /app/

WORKDIR /app

ENTRYPOINT []

USER root

RUN apt-get update && apt-get install software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
# Install py39 from deadsnakes repository
RUN apt-get update && apt-get install -y python3.9 python3-pip
# Install rasa
RUN python3.9 -m pip install --no-cache --upgrade pip
RUN python3.9 -m pip install -r requirements-bot.txt --no-cache

USER 1001

CMD ["rasa" "--help"]