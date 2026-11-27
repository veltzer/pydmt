"""
copy.py
"""

import shutil

from pydmt.api.one_source_one_target import OneSourceOneTarget


class Copy(OneSourceOneTarget):
    def build(self) -> None:
        shutil.copy(self.source, self.target)
