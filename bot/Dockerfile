FROM rasa/rasa:3.1.6
# FROM python:3.9.13

ADD . /app/

WORKDIR /app


# ENTRYPOINT []
# USER root
# RUN pip install --upgrade pip 
# RUN pip install -r requirements-bot.txt --no-cache

USER 1001

CMD ["run", "--enable-api", "--cors='*'"]