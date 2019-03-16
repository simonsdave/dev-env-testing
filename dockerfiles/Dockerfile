FROM ubuntu:16.04

LABEL maintainer="Dave Simons"

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -y

RUN apt-get install -y python
RUN apt-get install -y python-dev
RUN apt-get install -y python-pip
RUN pip install --upgrade pip

COPY dev_env_testing.tar.gz /tmp/dev_env_testing.tar.gz
RUN cd /tmp && pip install /tmp/dev_env_testing.tar.gz
RUN rm /tmp/dev_env_testing.tar.gz

ENV DEBIAN_FRONTEND newt
