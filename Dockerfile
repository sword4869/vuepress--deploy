# syntax=docker/dockerfile:1
FROM node:16

COPY entrypoint.sh ./entrypoint.sh
COPY translator-v1.py ./translator-v1.py
COPY translator-v2.py ./translator-v2.py

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/entrypoint.sh"]