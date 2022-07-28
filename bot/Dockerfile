FROM ubuntu:22.04

ADD . /app/

WORKDIR /app

ENTRYPOINT []

USER root

RUN apt-get update && apt-get install -y python3 python3-pip && python3 -m pip install --no-cache --upgrade pip

RUN python3 -m pip install -r requirements-bot.txt --no-cache

USER 1001

CMD ["rasa" "--help"]