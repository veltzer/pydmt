import os
from typing import Tuple, Iterable, List

from pydmt.core.utils import copy_mkdir, makedirs_for_file


class Cache:
    def __init__(self):
        self.folder = ".pydmt"

    def get_list_by_signature(self, signature: str):
        full_path = os.path.join(self.folder, "lists", signature[:2], signature[2:])
        if os.path.isfile(full_path):
            return full_path
        else:
            return None

    def get_object_by_signature(self, signature: str):
        full_path = os.path.join(self.folder, "objects", signature[:2], signature[2:])
        if os.path.isfile(full_path):
            return full_path
        else:
            return None

    def save_list_by_signature(self, signature: str, content: str):
        full_path = os.path.join(self.folder, "lists", signature[:2], signature[2:])
        makedirs_for_file(full_path)
        with open(full_path, "wt") as file_handle:
            file_handle.write(content)

    def save_object_by_signature(self, signature: str, file_name: str):
        full_path = os.path.join(self.folder, "objects", signature[:2], signature[2:])
        copy_mkdir(file_name, full_path)

    @staticmethod
    def iterate_objects(file_name: str) -> Iterable[Tuple[str, str]]:
        with open(file_name) as file_handle:
            for line in file_handle:
                yield tuple(line.split(" "))

    @staticmethod
    def save_objects(file_name: str, object_tuples: List[Tuple[str, str]]) -> None:
        with open(file_name, "w") as file_handle:
            for object_tuple in object_tuples:
                file_handle.write(" ".join(object_tuple))
