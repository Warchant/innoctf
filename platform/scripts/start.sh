#/bin/bash
# Transpile the CoffeeScript files
echo "Transpiling Coffeescript"
coffee -c -o ${VAGRANT_PATH}/web/js/ ${VAGRANT_PATH}/web/coffee/

# Shutdown the server
echo "Shutting down nginx"
sudo service nginx stop

# Clean out the old files
echo "Cleaning up old files"
sudo rm -rf /srv/http/ctf/*

echo "Generating web with Jekyll"
cd ${VAGRANT_PATH}/web
sudo jekyll build

echo "Copying files to server"
mkdir -p ${VAGRANT_PATH}/problem_static
sudo cp -r ${VAGRANT_PATH}/problem_static /srv/http/ctf/problem-static

# Make sure everything is in UNIX format.
sudo dos2unix -q /srv/http/ctf/*.html

# Start the server
echo "Restarting the server"
sudo service nginx start

# Clear the cache
echo "Clearing the API cache"
${VAGRANT_PATH}/api/api_manager.py database clear cache

#Start picoCTF API
echo "Starting the InnoCTF API"
#tmux kill-session -t picoapi 2> /dev/null
#tmux new-session -s picoapi -d "cd ${VAGRANT_PATH}/api && python3 run.py"
#cd ${VAGRANT_PATH}/api && python3 run.py &
cd ${VAGRANT_PATH}/api && bash gunicorn_start.sh &

#Start scoreboard
echo "Starting scoreboard session"
#tmux kill-session -t scoreboard 2> /dev/null
#tmux new-session -s scoreboard -d "cd ${VAGRANT_PATH}/api/; python3 daemon_manager.py -i 300 cache_stats"
cd ${VAGRANT_PATH}/api/; python3 daemon_manager.py -i 300 cache_stats
