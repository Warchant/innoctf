#!/bin/sh
WORKERS=4
gunicorn -b 0.0.0.0:8000 -w $WORKERS 'api.app:config_app()'
