"""
sphinx.py
"""

import os
from typing import TYPE_CHECKING

from pydmt.api.feature import Feature
from pydmt.builders.sphinx import BuilderSphinx

if TYPE_CHECKING:
    from pydmt.core.pydmt import PyDMT

SPHINX_FOLDER = "sphinx"


class FeatureSphinx(Feature):
    def setup(self, pydmt: PyDMT) -> None:
        if not os.path.isdir(SPHINX_FOLDER):
            return
        pydmt.add_builder(BuilderSphinx())
