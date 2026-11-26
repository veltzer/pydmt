"""
one_source_one_target.py
"""


from typing import TYPE_CHECKING

from pydmt.api.builder import Builder, Node, SourceFile, TargetFile
from pydmt.utils.digest import sha1_file

if TYPE_CHECKING:
    from collections.abc import Generator, Sequence


class OneSourceOneTarget(Builder):
    """
    This is a builder which has one source file and one target file
    """

    def __init__(self, source: str, target: str):
        # super().__init__()
        self.source = source
        self.target = target
        self.sources: Sequence[Node] = [SourceFile(filename=source)]
        self.targets: Sequence[Node] = [TargetFile(filename=target)]

    def get_sources(self) -> Sequence[Node]:
        return self.sources

    def get_targets(self) -> Sequence[Node]:
        return self.targets

    def yield_results(self) -> Generator[tuple[str, str]]:
        yield sha1_file(self.target), self.target
