from pydmt.api.feature import Feature
from pydmt.builders.installer import Installer
from pydmt.core.pydmt import PyDMT


class Packages(Feature):
    def __init__(
        self,
    ):
        # pylint: disable=import-outside-toplevel
        try:
            import config.deps
            self.packages = config.deps.packages
        except ModuleNotFoundError:
            pass

    def setup(self, pydmt: PyDMT) -> None:
        pydmt.add_builder(Installer(packages=self.packages))
