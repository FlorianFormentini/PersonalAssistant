FROM python:3.9.13

ADD . /app/

WORKDIR /app

ENTRYPOINT []

USER root

RUN pip install -r requirements-bot.txt --no-cache

USER 1001

CMD ["rasa", "--help"]