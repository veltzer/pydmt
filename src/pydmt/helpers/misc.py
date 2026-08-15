"""
misc.py
"""

from pydmt.utils.lua import load_config


def get_version_str():
    tup = getattr(load_config("version"), "tup")
    return ".".join(str(x) for x in tup)
