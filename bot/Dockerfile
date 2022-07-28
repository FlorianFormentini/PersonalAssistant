FROM ubuntu:latest

ADD . /app/

WORKDIR /app

USER root

RUN pip install -r actions/requirements-actions.txt

USER 1001

CMD ["rasa" "--help"]