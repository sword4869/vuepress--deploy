# syntax=docker/dockerfile:1
FROM node:16

RUN apt update && apt install python3

COPY entrypoint.sh /entrypoint.sh
COPY translator.py /translator.py

RUN python /translator.py $INFO_REPOSITORY
# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/entrypoint.sh"]