import hashlib
import os
import pkgutil
import shutil
from typing import Generator

from api.builder import Populator


def hex_digest(filename: str, algorithm_name: str) -> str:
    block_size = 65536
    hash_object = hashlib.new(algorithm_name)
    with open(filename, 'rb') as file_handle:
        buf = file_handle.read(block_size)
        while len(buf) > 0:
            hash_object.update(buf)
            buf = file_handle.read(block_size)
    return hash_object.hexdigest()


def sha1_file(filename: str) -> str:
    return hex_digest(filename, "sha1")


def makedirs_for_file(filename: str):
    folder = os.path.dirname(filename)
    os.makedirs(folder)


def copy_mkdir(source: str, destination: str):
    makedirs_for_file(destination)
    shutil.copy(source, destination)


def get_modules_list(folder: str) -> Generator[Populator, None, None]:
    for (module_loader, name, is_package) in pkgutil.iter_modules(path=[folder]):
        if is_package:
            continue
        ml = module_loader.find_module(name)
        m = ml.load_module()
        yield m
