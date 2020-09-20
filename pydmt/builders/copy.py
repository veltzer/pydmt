from typing import List

import shutil

from pydmt.api.builder import Builder, SourceFile, Source


class Copy(Builder):

    def __init__(self, source: str, target: str):
        super().__init__()
        self.source = source
        self.target = target
        self.sources = [SourceFile(filename=source)]
        self.targets = [target]

    def get_sources(self) -> List[Source]:
        return self.sources

    def get_targets(self) -> List[str]:
        return self.targets

    def build(self):
        shutil.copy(self.source, self.target)

