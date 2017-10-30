from typing import List, Dict

import shutil

import os

from pydmt.api.builder import Builder
from pydmt.core.cache import Cache
from pydmt.core.utils import sha1_file


class BuildProcessStats:
    def __init__(self):
        self.builder = 0
        self.copy = 0
        self.nop = 0
        self.missing = 0
        self.fail = 0
        self.success = 0

    def add_builder(self):
        self.builder += 1

    def add_copy(self):
        self.copy += 1

    def add_nop(self):
        self.nop += 1

    def add_missing(self):
        self.missing += 1

    def add_fail(self):
        self.fail += 1

    def add_success(self):
        self.success += 1


class PyDMT:
    def __init__(self):
        self.builders = []  # type: List[Builder]
        self.target_to_builder = {}  # type: Dict[str, Builder]
        self.cache = Cache()

    def build_by_builder(self, b: Builder, stats: BuildProcessStats):
        """ run one builder, return statistics about the run """
        target_signature = b.get_signature()
        blob_name = self.cache.get_list_by_signature(target_signature)
        if blob_name:
            for object_name, signature in Cache.iterate_objects(blob_name):
                filename = self.cache.get_object_by_signature(signature)
                if os.path.isfile(object_name):
                    object_name_signature = sha1_file(object_name)
                    if object_name_signature != signature:
                        shutil.copy(filename, object_name)
                        stats.add_copy()
                    else:
                        stats.add_nop()
                else:
                    stats.add_missing()
                    shutil.copy(filename, object_name)
                    stats.add_copy()
        else:
            stats.add_builder()
            # noinspection PyBroadException
            try:
                b.build()
                stats.add_success()
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
            except Exception:
                stats.add_fail()

    def build_by_target(self, target: str, stats: BuildProcessStats) -> None:
        b = self.target_to_builder[target]
        self.build_by_builder(b, stats)

    def build_by_targets(self, targets: List[str], stats: BuildProcessStats) -> None:
        for target in targets:
            self.build_by_target(target, stats)

    def add_builder(self, b: Builder) -> None:
        self.builders.append(b)
        targets = b.get_targets()
        if targets:
            for target in targets:
                self.target_to_builder[target] = b
