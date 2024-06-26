import os

from pydmt.api.feature import Feature
from pydmt.builders.make import BuilderMake
from pydmt.core.pydmt import PyDMT


class FeatureMake(Feature):
    def setup(self, pydmt: PyDMT) -> None:
        if not os.path.isfile("Makefile"):
            return
        pydmt.add_builder(BuilderMake(
            source="Makefile",
            target="out/make.stamp",
        ))
