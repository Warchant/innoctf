#!/bin/bash
#cd ${VAGRANT_PATH}/mongoclient-master/ && tmux new -s mclient -d "sudo meteor --port 3000"
#cd ${VAGRANT_PATH}/scripts/ && tmux new -s devploy -d devploy
if [ -z "$VAGRANT_PATH" ]; then
	VAGRANT_PATH=/ctf
fi

service mongodb start
service nginx start
/ctf/scripts/devploy
#cd ${VAGRANT_PATH}/api/ && tmux new -s scoreboard -d "sudo python3 daemon_manager.py -i 300 cache_stats"
python3 ${VAGRANT_PATH}/api/daemon_manager.py -i 300 cache_stats
