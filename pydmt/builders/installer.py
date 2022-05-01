"""
This is a module that will install OS packages for you.
"""


from typing import List, Generator, Tuple
import subprocess

from pydmt.api.builder import Builder, Node, SourceFile, TargetFile
from pydmt.utils.filesystem import unlink_files
from pydmt.utils.digest import sha1_file

RESULT = "deps.stamp"


class Installer(Builder):
    """
    This is review of how to build a sphinx documentation:
    - if you want documentation for the code you need to run "sphinx-apidoc"
    - it will generate files that describe every sub package in your package.
    - after this you run "sphinx-build"
    - "sphinx-quickstart" is not needed unless you are starting a new project.
    """
    def get_sources(self) -> List[Node]:
        file_list = [
            SourceFile("config/deps.py"),
        ]
        return file_list

    def get_targets(self) -> List[Node]:
        return [TargetFile(RESULT)]

    def __init__(self, packages: List[str]):
        super().__init__()
        self.packages = packages

    def build(self) -> None:
        unlink_files(RESULT)
        args = [
            'sudo',
            'apt-get',
            'install',
        ]
        args.extend(self.packages)
        subprocess.check_call(args)

    def yield_results(self) -> Generator[Tuple[str, str], None, None]:
        yield sha1_file(RESULT), RESULT
