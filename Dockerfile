# syntax=docker/dockerfile:1
FROM node:16

COPY entrypoint.sh /entrypoint.sh
COPY translator.py /translator.py

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/entrypoint.sh"]