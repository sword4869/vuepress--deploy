# syntax=docker/dockerfile:1
FROM node:16

WORKDIR /app
COPY entrypoint.sh /entrypoint.sh

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/entrypoint.sh"]