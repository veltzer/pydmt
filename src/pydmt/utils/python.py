"""
python.y
"""

import glob
import os
import pprint
from typing import TYPE_CHECKING, Any

from pydmt.utils.lua import load_config

if TYPE_CHECKING:
    from collections.abc import Callable


def hlp_source_under(folder: str) -> str:
    """
    this function finds all the python packages under a folder and
    write the "packages" and "package_dir" entries for a python setup.py
    script
    """
    # walk the folder and find the __init__.py entries for packages.
    packages = []
    package_dir = {}
    for root, _, files in os.walk(folder):
        for file in files:
            if file != "__init__.py":
                continue
            full = os.path.dirname(os.path.join(root, file))
            relative = os.path.relpath(full, folder)
            packages.append(relative)
            package_dir[relative] = full
    # we use pprint because we want the order to always remain the same
    return f"packages={sorted(packages)},\npackage_dir={pprint.pformat(package_dir)}"


def hlp_files_under(destination_folder: str, pat: str) -> str:
    file_list = [x for x in glob.glob(pat) if os.path.isfile(x)]
    return f"(\'{destination_folder}\', {file_list})"


def make_hlp_project_keywords(d: Any) -> Callable[[], str]:
    def hlp_project_keywords() -> str:
        return f"{d.project_keywords.split()}"

    return hlp_project_keywords


def make_hlp_project_platforms(d: Any) -> Callable[[], str]:
    def hlp_project_platforms() -> str:
        return f"{d.project_platforms.split()}"

    return hlp_project_platforms


def make_hlp_project_classifiers(d: Any) -> Callable[[], str]:
    def hlp_project_classifiers() -> str:
        classifiers = d.project_classifiers.split("\n")
        classifiers = [x.strip()[1:-1] for x in classifiers]
        return f"{classifiers}"

    return hlp_project_classifiers


def make_hlp_wrap(level: int):
    def hlp_wrap(t: str) -> str:
        return t.replace("\n", "\n" + "\t" * level)

    return hlp_wrap


def collect_reqs(*, add_dev: bool = False) -> list[str]:
    try:
        reqs: list[str] = []
        mod = load_config("python")
        if hasattr(mod, "requires"):
            reqs += mod.requires
        if add_dev and hasattr(mod, "dev_requires"):
            reqs += mod.dev_requires
    except FileNotFoundError:
        return []
    else:
        return reqs


def collect_bootstrap_reqs() -> list[str]:
    try:
        mod = load_config("bootstrap")
        if hasattr(mod, "requires"):
            return list(mod.requires)
    except FileNotFoundError:
        return []
    else:
        return []


def get_install_args() -> list[str]:
    return [
        "python",
        "-m",
        "pip",
        "install",
    ]
