"""
github.py
"""

from pydmt.utils.lua import config_exists, load_config


def get_workflows_platforms():
    if not config_exists("github"):
        return None
    mod = load_config("github")
    if hasattr(mod, "workflows_platforms"):
        return mod.workflows_platforms
    return None
