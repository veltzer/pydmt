from typing import List


class Builder:
    def build(self) -> None:
        pass

    def signature(self) -> bytes:
        pass


class PyDMT:
    def __init__(self):
        self.builders = []  # type: List[Builder]

    def build(self, node_name: str) -> None:
        print("building [{}]".format(node_name))

    def addBuilder(self, b: Builder) -> None:
        self.builders.append(b)
