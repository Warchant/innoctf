#!/bin/bash

# run this script on clean system to install all dependencies for picoctf platform
# NOTE: in /ctf must be repo https://github.com/warchant/innoctf
apt-get update
apt-get install -y \
    python3-pip \
    nginx unzip \
    mongodb \
    gunicorn \
    git \
    libzmq-dev \
    nodejs-legacy \
    npm \
    libclosure-compiler-java \
    ruby-dev \
    dos2unix \
    tmux \
    openjdk-7-jdk

npm install -g coffee-script react-tools jsxhint
pip3 install -r /ctf/api/requirements.txt
gem install jekyll -v 2.5.3

# create server folder
mkdir -p /srv/http/ctf
mkdir -p /srv/certs
cp -R /ctf/config/https/ /srv/
chown -R www-data:www-data /srv/http

# setup nginx
cp /ctf/config/https/* /srv/certs
cp /ctf/config/tuning/* /etc/nginx
rm /etc/nginx/sites-enabled/default
nginx -s reload
