# Personal Assistant

- **Made with:** [Rasa v3.2.1](https://rasa.com/docs/rasa/) / [Rasa SDK v3.1.0](https://rasa.com/docs/action-server/)
- **Hosted on:** Personal Server  
- **Tracker DB:** [MongoDB Atlas Cluster](https://www.mongodb.com/atlas/database)


## Features

- Self-presentation
- Joking about a potential destruction of mankind
- Talking about its tremendous admiration for its creator
- Counting the number of bong hits smoked per day
- Interact with a HomeAssitant system
- Extend Google assistant ?
- Google Calendar event reminder ?


## Local use
To start the bot and its action server in *production mode*:
```sh
docker compose up
```
The [`Dockerfile.actions`](Dockerfile.actions) is used to inject dependencies (with [`requirements-actions.txt`](requirements-actions.txt)).


## CI/CD

### Model
If something has been modified in the chatbot data file after a `push`, a new model is trained and a docker image is build using the [`Dockerfile`](Dockerfile) then sent to [DockerHub](https://hub.docker.com)

### Action Server
If python code has been modified in the `app/actions/` folder after a `push`, the code is verified (lint + types) with commands defined in the [`Makefile`](Makefile). Then the action server docker image is also build and sent to DockerHub.


---

## 📚 Sources

- [Rasa Voice Assistant article](https://rasa.com/blog/how-to-build-a-voice-assistant-with-open-source-rasa-and-mozilla-tools/)