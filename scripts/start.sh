#!/bin/bash
MONGODB_CLIENT=true
SCOREBOARD=true
DEVPLOY=true

if [ MONGODB_CLIENT ]; then
	cd ${VAGRANT_PATH}/mongoclient-master/ && 
	tmux new -s mclient -d "sudo meteor --port 3000"
	echo "[+] mclient has started"
fi

if [ DEVPLOY ]; then
	cd ${VAGRANT_PATH}/scripts/ &&
	tmux new -s devploy -d devploy
	echo "[+] devploy has started"
fi

if [ SCOREBOARD ]; then
	cd ${VAGRANT_PATH}/api/ && 
	tmux new -s scoreboard -d "sudo python3 daemon_manager.py -i 300 cache_stats"
	echo "[+] scoreboard has started"
fi
