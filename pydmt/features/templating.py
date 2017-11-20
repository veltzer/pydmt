import os

from pydmt.api.feature import Feature
from pydmt.builders.mako import Mako
from pydmt.core.pydmt import PyDMT


class Templating(Feature):
    def __init__(self, data=None):
        self.data = data

    def setup(self, pydmt: PyDMT) -> None:
        for root, directories, filenames in os.walk("templates"):
            for filename in filenames:
                source = os.path.join(root, filename)
                target_base, ext = os.path.splitext(source)
                if ext == '.mako':
                    target = os.sep.join(target_base.split(os.sep)[1:])
                    builder = Mako(
                        source=source,
                        target=target,
                        data=self.data,
                    )
                    pydmt.add_builder(builder)
