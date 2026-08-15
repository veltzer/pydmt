"""
attrs.py
"""

from pydmt.utils.lua import config_exists, load_config


def _get(config_name: str, attr: str):
    """ return an attribute of a config file, or None if either is missing """
    if not config_exists(config_name):
        return None
    mod = load_config(config_name)
    if not hasattr(mod, attr):
        return None
    return getattr(mod, attr)


def get_github_username():
    return _get("personal", "github_username")


def get_launchpad_username():
    return _get("personal", "launchpad_username")


def get_packages():
    return _get("deps", "packages")


def get_packages_remove():
    return _get("deps", "packages_remove")
