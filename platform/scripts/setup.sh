#!/bin/bash
echo "[+] Running setup.sh"
# create server folder
mkdir -p /srv/http/ctf
mkdir -p /srv/certs
chown -R www-data:www-data /srv/http

# setup nginx
mkdir -p /var/log/nginx
mkdir -p /var/log/mongodb
cp ${VAGRANT_PATH}/config/certs/* /srv/certs
cp ${VAGRANT_PATH}/config/nginx/* /etc/nginx
cp ${VAGRANT_PATH}/config/innoctf.com.nginx /etc/nginx/sites-enabled/innoctf.com.nginx
rm /etc/nginx/sites-enabled/default 2>/dev/null
service nginx restart

echo "Copying files to server"
#sudo cp -r ${VAGRANT_PATH}/web/* /srv/http/ctf/
mkdir -p ${VAGRANT_PATH}/problem_static
sudo cp -r ${VAGRANT_PATH}/problem_static /srv/http/ctf/problem-static

# Make sure everything is in UNIX format.
sudo dos2unix -q /srv/http/ctf/*.html

# Clear the cache
echo "Clearing the API cache"
${VAGRANT_PATH}/api/api_manager.py database clear cache
