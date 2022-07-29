FROM rasa/rasa-sdk:3.1.2

WORKDIR /app

COPY . /app/actions

USER root

RUN pip install -r actions/requirements-actions.txt --no-cache

USER 1001
