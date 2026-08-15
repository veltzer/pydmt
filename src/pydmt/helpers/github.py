"""
github.py
"""

from pydmt.utils.lua import load_config, config_exists


def get_workflows_platforms():
    if not config_exists("github"):
        return None
    mod = load_config("github")
    if hasattr(mod, "workflows_platforms"):
        return getattr(mod, "workflows_platforms")
    return None
