#!/usr/bin/python3
"""
Fabric script that generates a tgz archive from the contents of the web_static
folder of the AirBnB Clone repo
"""

from datetime import datetime
from fabric.api import local
from os.path import isdir, join

def do_pack():
    """Generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        versions_dir = "versions"
        if not isdir(versions_dir):
            local("mkdir -p {}".format(versions_dir))
        file_name = join(versions_dir, "web_static_{}.tgz".format(date))
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
