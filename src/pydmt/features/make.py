"""
make.py
"""

import os
from typing import TYPE_CHECKING

from pydmt.api.feature import Feature
from pydmt.builders.make import BuilderMake

if TYPE_CHECKING:
    from pydmt.core.pydmt import PyDMT

SOURCE_FILE = "Makefile"


class FeatureMake(Feature):
    def setup(self, pydmt: PyDMT) -> None:
        if not os.path.isfile(SOURCE_FILE):
            return
        pydmt.add_builder(BuilderMake(
            source=SOURCE_FILE,
            target="out/make.stamp",
        ))
