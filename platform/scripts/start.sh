#/bin/bash
echo "[+] Running start.sh"

# Start the server
echo "Restarting the server"
sudo service nginx restart

echo "Generating web with Jekyll"
cd ${VAGRANT_PATH}/web
sudo jekyll build --watch &

# Transpile the CoffeeScript files
echo "Transpiling Coffeescript"
coffee -w -c -o ${VAGRANT_PATH}/web/js/ ${VAGRANT_PATH}/web/coffee/ &

# Clear the cache
echo "Clearing the API cache"
${VAGRANT_PATH}/api/api_manager.py database clear cache

#Start picoCTF API
echo "Starting the InnoCTF API"
tmux kill-session -t picoapi 2> /dev/null
#tmux new-session -s picoapi -d "cd ${VAGRANT_PATH}/api && python3 run.py"
tmux new-session -s picoapi -d "cd ${VAGRANT_PATH}/api && bash gunicorn_start.sh"
#cd ${VAGRANT_PATH}/api && python3 run.py &
#cd ${VAGRANT_PATH}/api && bash gunicorn_start.sh &

#Start scoreboard
echo "Starting scoreboard session"
#tmux kill-session -t scoreboard 2> /dev/null
#tmux new-session -s scoreboard -d "cd ${VAGRANT_PATH}/api/; python3 daemon_manager.py -i 300 cache_stats"
cd ${VAGRANT_PATH}/api/; python3 daemon_manager.py -i 300 cache_stats
