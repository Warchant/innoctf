#!/bin/bash

# Updates
apt-get -y update 
apt-get -y upgrade

# CTF-Platform Dependencies
apt-get -y install python3-pip
apt-get -y install nginx
apt-get -y install mongodb
apt-get -y install gunicorn
apt-get -y install git
apt-get -y install libzmq-dev
apt-get -y install nodejs-legacy
apt-get -y install npm
apt-get -y install libclosure-compiler-java
apt-get -y install shellinabox

npm install -g coffee-script
npm install -g react-tools
npm install -g jsxhint

pip3 install Flask
pip3 install py3k-bcrypt
pip3 install pymongo
pip3 install pyzmq

# Configure Environment
echo "PATH=$PATH:/home/vagrant/scripts" >> /etc/profile

# Configure shellinabox
id -u box &> /dev/null
if [[ $? != 0 ]]; then
  echo "Creating box test user"
  useradd -m box -p $(echo "box" | openssl passwd -1 -stdin)
fi;

#kill the auto starting one?
killall shellinaboxd &> /dev/null

shellinaboxd -b -p 1337 -u vagrant --static-file=ShellInABox.js:/home/vagrant/minigames/shellinabox/ShellInABox.hax.js 

# Configure Nginx
cp /vagrant/config/ctf.nginx /etc/nginx/sites-enabled/ctf
rm /etc/nginx/sites-enabled/default
mkdir -p /srv/http/ctf
service nginx restart
