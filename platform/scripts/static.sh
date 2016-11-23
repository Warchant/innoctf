#!/bin/sh
echo "Deploying static files"
mkdir -p ${VAGRANT_PATH}/problem_static
sudo cp -r ${VAGRANT_PATH}/problem_static /srv/http/ctf/problem-static
