#!/usr/bin/python3
"""4. Keep it clean!"""

from fabric.api import local, env, run, put
from datetime import datetime
from os import path
import os
import time
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
    except Exception:
        return (None)


def do_deploy(archive_path):
    """ todos aprontandose para irse de joda y
    yo aca como un pelotudo, lpqlp"""

    if path.exists(archive_path):
        try:
            name = archive_path.replace('versions/', '').split('.')
            file_name = "/data/web_static/releases/" + name[0] + "/"
            file_name_f = archive_path.split("/")[1]
            put(archive_path, "/tmp/")
            run("mkdir -p " + file_name)
            run("tar -xzf /tmp/" + file_name_f + " -C " + file_name)
            run("rm /tmp/" + archive_path.split("/")[1])
            run("mv " + file_name + "web_static/* " + file_name)
            run("rm -rf " + file_name + "web_static")
            run("rm -rf /data/web_static/current")
            run("ln -s " + file_name + " /data/web_static/current")
            print("OK")
            return True
        except Exception:
            return False
    else:
        return False


def deploy():
    """creates and distributes an archive to your web servers,
    using the function deploy"""
    path = do_pack()
    if path is None:
        return False
    dep = do_deploy(path)
    return dep


def do_clean(number=0):
    """deletes out-of-date archives"""
    if int(number) == 0 or int(number) == 1:
        local("ls -tu versions > out_of_date.txt")
        total = os.listdir("versions")
        local("tail -n +2 out_of_date.txt > to_del.txt")
        local("for line in $(cat to_del.txt); do rm -rf versions/$line ;done")

        run("ls -tu /data/web_static/releases > out_of_date.txt")
        total = os.listdir("/data/web_static/releases")
        run("tail -n +2 out_of_date.txt > to_del.txt")
        run("for line in $(cat to_del.txt);do rm -rf /data/web_static/\
            releases/$line ;done")

        local("rm out_of_date.txt to_del.txt")
        run("rm out_of_date.txt to_del.txt")
    else:
        number = int(number)+1
        local("ls -tu versions > out_of_date.txt")
        total = os.listdir("versions")
        local("tail -n +{} out_of_date.txt > to_del.txt".format(number)
        local("for line in $(cat to_del.txt); do rm -rf versions/$line ;done")

        run("ls -tu /data/web_static/releases > out_of_date.txt")
        total = os.listdir("/data/web_static/releases")
        run("tail -n -+{} out_of_date.txt > to_del.txt".format(number)
        run("for line in $(cat to_del.txt); do rm -rf /data/web_static/\
            releases/$line ;done")

        local("rm out_of_date.txt to_del.txt")
        run("rm out_of_date.txt to_del.txt")
