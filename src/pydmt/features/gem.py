"""
gem.py
"""

import os.path
from typing import TYPE_CHECKING

from pydmt.api.feature import Feature
from pydmt.builders.gem import Installer

if TYPE_CHECKING:
    from pydmt.core.pydmt import PyDMT


class FeatureGem(Feature):
    def setup(self, pydmt: PyDMT) -> None:
        if not os.path.isfile("Gemfile"):
            return
        pydmt.add_builder(Installer(
            source="Gemfile",
            target="out/gem.stamp",
        ))
