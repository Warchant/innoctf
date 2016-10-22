#!/bin/bash

# Updates
apt-get -y update
apt-get -y upgrade

# CTF-Platform Dependencies
apt-get -y install python3-pip
apt-get -y install nginx
apt-get -y install unzip
apt-get -y install mongodb
apt-get -y install gunicorn
apt-get -y install git
apt-get -y install libzmq-dev
apt-get -y install nodejs-legacy
apt-get -y install npm
apt-get -y install libclosure-compiler-java
apt-get -y install ruby-dev
apt-get -y install dos2unix
apt-get -y install tmux
apt-get -y install openjdk-7-jdk

npm install -g coffee-script
npm install -g react-tools
npm install -g jsxhint

if [ -d /home/vagrant ]; then
    export VAGRANT_PATH=/home/vagrant
else
    export VAGRANT_PATH=$(cd $(dirname $0)/..; pwd)
fi

pip3 install -r ${VAGRANT_PATH}/api/requirements.txt

# Jekyll
gem install jekyll -v 2.5.3

# Configure Environment
echo "PATH=$PATH:${VAGRANT_PATH}/scripts" >> /etc/profile
echo "export VAGRANT_PATH=${VAGRANT_PATH}" >> /etc/profile

pip3 install -r ${VAGRANT_PATH}/api/requirements.txt

# Jekyll
gem install jekyll -v 2.5.3

# Configure Nginx
mkdir -p /srv/http/ctf
cp ${VAGRANT_PATH}/config/https /srv/https
cp ${VAGRANT_PATH}/config/development.nginx /etc/nginx/sites-enabled/innoctf.nginx
rm /etc/nginx/sites-enabled/default
service nginx restart

# add ssh keys
keyfile="/home/vagrant/.ssh/authorized_keys"
mkdir -p "/home/vagrant/.ssh"
echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCu9pXtWcLUTBw4sgcE0O4zIuEP8j88fj1aB3IWYlI7cAMLYsBPLhDlSOyutFxtw6ht2zWU0n8GAKxwwtc/wYRc38wsnwFIK3EuCM/p6JOE3GPG51NyCmO3vcN12ONiwhknUVCpFl+QDUzRwyzEHkr10VTbY/1fcIYxrKBrV5xxazzHd4/PrRfpDCiuwnaAaZps7xgJm66tb5ZgvKA5XPlpKG178RY5Y42DDMCi8NVxRIzVQ0pkhvk2wWtlM0e5Rm8aN3/0uCqtl0YdopeNWe6rz6GGIO64fCcNLHvqfms6GJs93hM5fPDZWiIbWpcYwosU6NtSzHAoEIN+erOhuDQ7 rodionov12@menad" >> $keyfile
echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCtDz+DdVwJTy327Hqlc1oQCOqB4j1uH8tqhfufJqhZKNSmiHp1VXpEoX8R8Z3EY0Zwdzr0vWI7SjA3CN97hyMWlkhAYAw2rfhmExu/Hnd9KSv92wFCMeGVz+4B6chLgxmYjWfOHzQXb5lAjbtRw3Thtqt/62QLOFWmv5AsV2qbLqqQcxXgONNEJum0BXUQV5QdL+dddDMicIKuk9NjiWMX7hbl2oxM3jvMygD8W5rcb7taekrhow9K20+23T4dj9mzZShER9xihmx4jp3cqyL3g0CADr3bwimrmgIQM3YSINnQ+5aiBCy2xRNPCC2upi9RZolYwuVgAF+xu9qw9ZaJ" >> $keyfile
echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAgEAhbmgPUFnPyf9/QCvpTYrsxH0lHggVgIN/rpT4hCbJHd8fgpx5qnj8zdi9of4jw6+szAQ5URHZZPB67ZES92q4eWjRtCs7yWlcrOAlqLP8phVcKEtlNYSKTk4uyTKwSprPFZdjdDDWhpqw4v6NT9/pkgGwOr4aVgh1Vm1h3sOu8I+nF8kIbk6oGOccpINq9932T7Ydo1h5reyRmPdeKsRbIa0y0UrMNbDof0iLqi2L2dvjPZEAWNS8giJqrOcD7AsPiho4EJ8ulwaiK/EJ6BufioTq1GmNAWy0VcxGx7fN2xSovozlTr0D3eRntKQZ50t4gxxJ70twSrA5cQhLdMo4FCLqbuLhoRJmVn6VpTLat8suR9H1ruF+Yb1qBVix5Cetn7cC1DaVVA2qakBkrIdK7b7i7WYBoXxS+HA3Jdpa83fFf0Xve0swoFq5p65j0rhz16+0Z3LNYtUaPdlcU29fA/OWpXuE8BuACOyeMqpPD/ghajBzLR44p56UapngQI2wda95ktAfZSXV5wEsQPm/M20W15iuAbJ6HuYVUVsH3luFfQCc9wbXNjvWTQ3UEiL4taTf/46/ZY/TmkoudbNlfF/b3TTwR6Q9J0mNT1ieVi9+u1mUW83578PN1qpsIxe5zABUxf/oqs+8kJtFrjiFJ4C/DkZKUn9e+26hEuLA5c= rsa-key-20160818" >> $keyfile
echo "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAvs+EAhDxMZL5Jh7mq7MjL0PfB2U8zH6cxTiv8iLa/ywPMzyWnkqd3qFsunxLvzbI9Q/n4syJKNS+8kCTfK+o79WF/iwPJbBQqI3Pxgos0EOTj4GcF2NmkvzqsasrBxgnNPv9HUTJmeK4rOv8615h99/18hcc0IGoL08ey86v0pWK8n+Jms3eF9ez8hIwUD6oeix7bNdJjR/X4qoHJTxpr353XuBuRDbf0w19Pw21hP4xqkCU1efteh+QahCUVnvIlOZnACf1Hu6W22F+K8UR1O5i7yQYQpOstK+vRWNtEuyd0ezeKA/b98OerX7zMo61scW6rf/YQ7iNjpgcCMcSuw== mail@kitsu.me" >> $keyfile
echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDHrDjw1kqLNMEIgMmFEZt/YBu/eROzbPs9etfPqRtIcUFlMbO+uWVRXJ0HX1quDT23hjyhZMAK9tG/jePdmac7OlrxEkINGltFMT4Eoj2RjUflpHsgbeem6SqrusgIzCn9/2zN1fqA3Pl7DPBCix/7/anUn7NbbAUTzKOnrJ+9gpDKXjInehu5YU2Z/NyCLUHD9d3C9++BMt5YtaPWYCXiPpPE1AJsZStnvo4TeFrUAlnhg9PjtvGV5P+ibPYibj5XA8oodAd4cy4Cximq3iouOIdq2bEQQOKwOIbdgAInyUUKo3miZHIzyzsNraCKq5cMVuai61VipqioWAINPWbN bogdan@st1.os3.su" >> $keyfile


# install mongoclient
cd ${VAGRANT_PATH}
curl https://install.meteor.com/ | sh
wget https://github.com/rsercano/mongoclient/archive/master.zip
unzip master.zip
rm master.zip
cd ${VAGRANT_PATH}/mongoclient-master; meteor npm install
