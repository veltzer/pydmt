from typing import List, Dict

import shutil

from pydmt.api.builder import Builder
from pydmt.core.cache import Cache
from pydmt.core.utils import sha1_file


class PyDMT:
    def __init__(self):
        self.builders = []  # type: List[Builder]
        self.target_to_builder = {}  # type: Dict[str, Builder]
        self.cache = Cache()

    def build_by_builder(self, b: Builder) -> None:
        target_signature = b.get_signature()
        blob_name = self.cache.get_list_by_signature(target_signature)
        if blob_name:
            for object_name, ref in Cache.iterate_objects(blob_name):
                shutil.copy(ref, object_name)
        else:
            b.build()
            # first lets build a list of what was constructed
            targets = b.get_targets()
            if targets is None:
                targets = b.get_targets_post_build()
            content = ""
            for target in targets:
                signature = sha1_file(target)
                content += target + " " + signature
                self.cache.save_object_by_signature(signature, target)

            self.cache.save_list_by_signature(target_signature, content)

    def build_by_target(self, target: str) -> None:
        print("building [{}]".format(target))
        b = self.target_to_builder[target]
        self.build_by_builder(b)

    def build_by_targets(self, targets: List[str]) -> None:
        print("building [{}]".format(targets))
        for target in targets:
            self.build_by_target(target)

    def addBuilder(self, b: Builder) -> None:
        self.builders.append(b)
        targets = b.get_targets()
        if targets:
            for target in targets:
                self.target_to_builder[target] = b
