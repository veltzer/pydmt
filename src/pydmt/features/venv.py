"""
venv.py
"""

import os
from typing import TYPE_CHECKING

from pydmt.api.feature import Feature
from pydmt.builders.venv import BuilderVenv

if TYPE_CHECKING:
    from pydmt.core.pydmt import PyDMT


class FeatureVenv(Feature):
    def setup(self, pydmt: PyDMT) -> None:
        if "GITHUB_WORKFLOW" in os.environ:
            return
        if not os.path.isfile("config/python.py"):
            return
        if not os.path.isfile(".pydmt.venv"):
            return
        pydmt.add_builder(BuilderVenv(
            source="config/python.py",
            target="out/venv.stamp",
        ))
