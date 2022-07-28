FROM ubuntu:latest

ADD . /app/

WORKDIR /app
ENTRYPOINT []

USER root



RUN apt-get update && apt-get install -y python3 python3-pip && python3 -m pip install --no-cache --upgrade pip

RUN pip install -r bot/requirements-bot.txt --no-cache

USER 1001

CMD ["rasa" "--help"]