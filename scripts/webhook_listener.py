#!/usr/bin/python3.4
from flask import Flask
import os
app = Flask(__name__)

# this should be run only in host OS
@app.route("/secret/4e6b950c05715b915d74cd2e93553ae3")
def pull():
    res = os.system("cd /home/bogdan/tools/picoCTF-Platform-2; git pull origin master")
    if res == 0:
        return "success"
    else:
        return "fail"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=12399)
