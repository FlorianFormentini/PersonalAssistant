FROM ubuntu:latest

ADD . /app/

WORKDIR /app

USER root

RUN pip install -r bot/requirements-bot.txt

USER 1001

CMD ["rasa" "--help"]