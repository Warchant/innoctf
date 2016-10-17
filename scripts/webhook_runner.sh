#!/bin/bash
tmux kill-session -t webhook
tmux new -s webhook -d python3 webhook_listener.py
