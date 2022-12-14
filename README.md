# Personal Assistant

- **Made with:** [Rasa v3.1.6](https://rasa.com/docs/rasa/) / [Rasa SDK v3.1.2](https://rasa.com/docs/action-server/)
- **Tracker DB:** [MongoDB Atlas Cluster](https://www.mongodb.com/atlas/database)

It was intended to be deployed on a personal home server but it has a too old CPU that doesn't support AVX (which is needed by Tensorflow). I tried differents solutions but I keep getting the same error after the `rasa run` command: `The TensorFlow library was compiled to use AVX instructions, but these aren't available on your machine.`


---
## Features
The main purpose of this bot is to interact with a HomeAssitant Supervised installation hosted on a [CSL mini PC](https://www.csl-computer.com/mini-pcs) under Ubuntu.

**Conversations:** [*Work in Progress*]
- Self-presentation
- Joking about a potential destruction of mankind
- Talking about its tremendous admiration for its creator
- Counting the number of bong hits smoked per day
- Interact with a HomeAssitant system
- Extend Google assistant ?
- Google Calendar event reminder ?

---
## Local use
**A `.env` file must be added to handle ALL credentials and secret vars.** The `docker-compose.yml` file is able to read it when creating images (It is therefore possible to use the `${VAR}` syntax in the compose file without defining environment variables beforehand).  
The same `.env` file is then injected in the 2 images when building them to access channels and tracker db credentials or others needed env vars.

Needed env vars:
- `RASA_VERSION`
- `RASA_SDK_VERSION`
- `SANIC_WORKERS`
- `RASA_TELEMETRY_ENABLED`
- `JWT_SECRET` and/or `AUTH_TOKEN`
- `DB_URI`
- `DB_USER`
- `DB_PWD`
- `HOST_ACTIONS`

To start the bot and its action server (with the api enabled and token/jwt set):
```sh
docker compose up [-d]
```

Then its possible to speak with it on it's REST channel with POST request: 
```sh
curl -XPOST http://localhost:5005/webhooks/rest/webhook \
  -H "Content-type: application/json" \
  -d '{"sender": "test", "message": "hello"}'
```

To quickly start the bot in the console and facilitate debugging two python scripts have been made in the `script` folder.  
It's also possible to use the rasa CLI normaly but only from the `bot` folder.

The `docker-compose.prod.yml` file is used to pull the 2 docker images created during CICD onto my personal server. 


### SpeechToText / TextToSpeech script
The [`tests_STT_TTS.py`](scripts/tests_STT_TTS.py) script is a simple local voice interface to talk with the chatbot.  
If the bot is started on localhost:5005, just run the script in an other terminal.


---
## CI/CD

### Rasa Server
The files needed to build the chatbot's server image have been gathered in the `bot` folder with an appropriate `Dockerfile`.
If something has been modified in this folder after a `push`, a new model is trained and a docker image is build then sent to [DockerHub](https://hub.docker.com).  

### Action Server
If python code has been modified in the `app/actions/` folder after a `push`, the code is verified (lint + types) with commands defined in the [`Makefile`](Makefile). Then the action server docker image is also build and sent to DockerHub.

---
## ???? Ressources

- [Tuto](https://linuxhandbook.com/nginx-reverse-proxy-docker/) to manually setup Nginx with auto SSL an geneneration using Docker
  - An easiest alternative with a great GUI: [Nginx Proxy Manager](https://nginxproxymanager.com/)