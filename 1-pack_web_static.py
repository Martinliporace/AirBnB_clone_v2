#!/usr/bin/python3
"""1. Compress before sending"""

from fabric.api import local
from datetime import datetime
from os import path


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
