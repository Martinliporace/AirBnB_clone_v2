#!/usr/bin/python3
"""2. Deploy archive!"""

from fabric.api import local, env, run, put
from datetime import datetime
from os import path

env.hosts = ['54.147.142.107', '34.235.143.218']
env.user = "ubuntu"

def do_pack():
    """script that generates a .tgz archive from the contents
    of the web_static folder of your AirBnB Clone repo"""

    local("mkdir -p versions")
    date_time = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_" + date_time + ".tgz"

    try:
        local("tar -cvzf " + file_name + " web_static")
        return (file_name)
    except:
        return (None)

def do_deploy(archive_path):
    """ todos aprontandose para irse de joda y
    yo aca como un pelotudo, lpqlp"""

    if path.exists(archive_path):
        try:
            name = archive_path.replace('versions/', '').split('.')
            file_name = "/data/web_static/releases/" + name[0] + "/"
            put(archive_path, "/tmp/")
            run("mkdir -p " + file_name)
            run("tar -xzf /tmp/" + archive_path.split("/")[1] + " -C " + file_name)
            run("rm /tmp/" + archive_path.split("/")[1])
            run("mv " + file_name + "web_static/* " + file_name)
            run("rm -rf " + file_name + "web_static")
            run("rm -rf /data/web_static/current")
            run("ln -s " + file_name + " /data/web_static/current")
            print("OK")
            return True
        except:
            return False
    else:
        return False
