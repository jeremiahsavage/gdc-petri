FROM ubuntu:xenial-20161010

MAINTAINER Jeremiah H. Savage <jeremiahsavage@gmail.com>

RUN apt-get update \
    && apt-get install -y \
       python-pip \
    && apt-get clean \
    && pip install \
       SNAKES==0.9.25 \
       sqlalchemy==1.1.7                
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*