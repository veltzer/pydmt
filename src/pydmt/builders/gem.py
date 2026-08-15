"""
This module installs gem modules
"""


import os

from pydmt.api.one_source_one_target import OneSourceOneTarget
from pydmt.utils.filesystem import mkdir_touch, unlink_files
from pydmt.utils.subprocess import check_call


class Installer(OneSourceOneTarget):
    def build(self) -> None:
        unlink_files([self.target])
        os.environ["GEM_HOME"] = "gems"
        args = [
            "bundle",
            "install",
        ]
        check_call(args)
        mkdir_touch(self.target)
