import os

from pydmt.api.feature import Feature
from pydmt.builders.mako import Mako
from pydmt.core.pydmt import PyDMT


class Templating(Feature):
    def setup(self, pydmt: PyDMT) -> None:
        for root, directories, files in os.walk("templates"):
            for file in files:
                source = os.path.join(root, file)
                target_base, ext = os.path.splitext(source)
                if ext == '.mako':
                    target = os.sep.join(target_base.split(os.sep)[1:])
                    builder = Mako(
                        definitions_folders=['definitions', os.path.expanduser("~/.config/pydmt")],
                        source=source,
                        target=target,
                    )
                    pydmt.add_builder(builder)
