#!/bin/bash

echo "[+] Running deploy"

echo "Deploying static files"
mkdir -p ${VAGRANT_PATH}/problem_static
sudo cp -r ${VAGRANT_PATH}/problem_static /srv/http/ctf/problem-static

echo "Deploying problems"
cd ${VAGRANT_PATH}/api
python3 api_manager.py problems load ../problems/ graders/ ../problem_static

echo "Deploying achievements"
cd ${VAGRANT_PATH}/api
python3 api_manager.py -v achievements load achievements/*.json
