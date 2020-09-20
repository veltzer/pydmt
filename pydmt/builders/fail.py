from typing import List

from pydmt.api.builder import Builder, Source, SourceFile


class Fail(Builder):

    def __init__(self, source: str, target: str):
        super().__init__()
        self.sources = [SourceFile(filename=source)]
        self.targets = [target]

    def get_sources(self) -> List[Source]:
        return self.sources

    def get_targets(self) -> List[str]:
        return self.targets

    def build(self):
        raise ValueError("fail")
