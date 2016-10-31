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
rm /etc/nginx/sites-enabled/default
service nginx restart
