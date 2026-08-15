"""
project.py
"""

from pydmt.utils.lua import load_config


def get_name():
    """ this gives you the name of the project, this must exist """
    return load_config("project").name
