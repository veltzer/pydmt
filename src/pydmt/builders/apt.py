"""
This is a module that will install OS packages for you.
"""


import os

from pydmt.api.one_source_one_target import OneSourceOneTarget
from pydmt.configs import ConfigApt, ConfigSudo
from pydmt.utils.filesystem import mkdir_touch, unlink_files
from pydmt.utils.subprocess import check_call


class BuilderApt(OneSourceOneTarget):
    def __init__(self, source: str, target: str, packages: list[str], packages_remove: list[str]):
        super().__init__(source, target)
        self.packages = packages
        self.packages_remove = packages_remove

    def build(self) -> None:
        unlink_files([self.target])
        if not self.packages:
            mkdir_touch(self.target)
            return
        os.environ["DEBIAN_FRONTEND"] = "noninteractive"
        if self.packages_remove is not None:
            args = []
            if ConfigSudo.sudo:
                args.append("sudo")
            args.extend([
                "apt-get",
            ])
            if ConfigApt.apt_quiet:
                args.append("-q=2")
            args.extend([
                "remove",
            ])
            args.extend(self.packages_remove)
            check_call(args)
        args = []
        if ConfigSudo.sudo:
            args.append("sudo")
        args.extend([
            "apt-get",
        ])
        if ConfigApt.apt_quiet:
            args.append("-q=2")
        args.extend([
            "--yes",
            "update",
        ])
        check_call(args)
        args = []
        if ConfigSudo.sudo:
            args.append("sudo")
        args.extend([
            "apt-get",
        ])
        if ConfigApt.apt_quiet:
            args.append("-q=2")
        args.extend([
            "--yes",
            "install",
        ])
        args.extend(self.packages)
        check_call(args)
        mkdir_touch(self.target)
