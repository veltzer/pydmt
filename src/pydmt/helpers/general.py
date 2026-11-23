"""
general.py
"""

import datetime as dt
import os
import socket

current_folder = os.path.basename(os.getcwd())
current_year = dt.datetime.now().astimezone().year
homedir = os.path.expanduser("~")
hostname = socket.gethostname()
