FROM rasa/rasa-sdk:3.2.0

WORKDIR /app

COPY . /app/actions

USER root
RUN pip install -r actions/requirements-actions.txt

USER 1001
