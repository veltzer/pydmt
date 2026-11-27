"""
copy.py
"""


from typing import TYPE_CHECKING

from pydmt.api.builder import Builder, Node, SourceFile, TargetFile
from pydmt.utils.digest import sha1_file
from pydmt.utils.filesystem import copy_mkdir

if TYPE_CHECKING:
    from collections.abc import Generator


class BuilderCopy(Builder):
    def __init__(self,
                 source: str,
                 target: str,
                 ):
        self.source = source
        self.sources: list[Node] = [SourceFile(self.source)]
        self.target = target
        self.targets: list[Node] = [TargetFile(self.target)]

    def get_sources(self) -> list[Node]:
        return self.sources

    def get_targets(self) -> list[Node]:
        return self.targets

    def build(self):
        copy_mkdir(self.source, self.target)

    def yield_results(self) -> Generator[tuple[str, str]]:
        yield sha1_file(self.target), self.target
