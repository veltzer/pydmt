from pydmt.api.feature import Feature
from pydmt.builders.apt import BuilderApt
from pydmt.core.pydmt import PyDMT
from pydmt.helpers.attrs import get_packages


class FeatureApt(Feature):
    def __init__(
        self,
    ):
        self.packages = get_packages()

    def setup(self, pydmt: PyDMT) -> None:
        if self.packages is not None:
            pydmt.add_builder(BuilderApt(
                source="config/deps.py",
                target="out/deps.stamp",
                packages=self.packages
            ))
