from typing import List
from pyfakeuse.pyfakeuse import fake_use


class Builder:
    def build(self) -> None:
        pass

    def signature(self) -> bytes:
        pass


class PyDMT:
    def __init__(self):
        self.builders = []  # type: List[Builder]

    def build_by_names(self, node_names: List[str]) -> None:
        fake_use(self)
        print("building [{}]".format(node_names))

    def addBuilder(self, b: Builder) -> None:
        self.builders.append(b)
