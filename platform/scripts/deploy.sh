#!/bin/bash

echo "[+] Running deploy.sh"

# Transpile the CoffeeScript files
echo "Transpiling Coffeescript"
coffee -w -c -o ${VAGRANT_PATH}/web/js/ ${VAGRANT_PATH}/web/coffee/

# Clean out the old files
# echo "Cleaning up old files"
# sudo rm -rf /srv/http/ctf/*

echo "Generating web with Jekyll"
cd ${VAGRANT_PATH}/web
sudo jekyll build --watch

# Make sure everything is in UNIX format.
sudo dos2unix -q /srv/http/ctf/*.html
