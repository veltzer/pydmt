from typing import List

import shutil

from pydmt.api.builder import Builder
from pydmt.core.utils import sha1_file


class Mako(Builder):
    def __init__(self, source, target):
        super().__init__()
        self.source = source
        self.target = target

    def get_signature(self) -> str:
        return sha1_file(self.source)

    def build(self):
        shutil.copy(self.source, self.target)

    def get_targets(self) -> List[str]:
        return [self.target]

    def get_targets_post_build(self) -> List[str]:
        return []
