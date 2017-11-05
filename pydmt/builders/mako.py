import abc
import pkgutil
from typing import List, Generator

import os

import sys

from pydmt.api.builder import Builder
from pydmt.core.utils import sha1_file, makedirs_for_file
import mako
import mako.exceptions
import mako.template
import mako.lookup


class D(dict):
    """
    class that looks like a dictionary but also like a namespace to allow the end users
    namespace like access (easy) and also non namespace like access.
    """
    def __init__(self):
        super().__init__(self)

    def __getattr__(self, name):
        return self[name]

    def __setattr__(self, name, val):
        self[name] = val


class Populator(metaclass=abc.ABCMeta):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def populate(self):
        """ this method actually does the populating """
        pass


def get_modules_list(folder: str) -> Generator[Populator, None, None]:
    for (module_loader, name, is_package) in pkgutil.iter_modules(path=[folder]):
        if is_package:
            continue
        ml = module_loader.find_module(name)
        m = ml.load_module()
        yield m


class Mako(Builder):
    def __init__(self, definitions_folders: List[str], source: str, target: str):
        super().__init__()
        self.definitions_folders = definitions_folders
        self.source = source  # type: str
        self.target = target  # type: str

    def get_signature(self) -> str:
        # FIXME: this should be the sha1 of the source + all the definition files
        # and even a better correction:
        # sha1 of the source file + the sha1 of all the variables references from within
        # the source file.
        return sha1_file(self.source)

    def build(self):
        d = load_and_populate(self.definitions_folders)
        template = mako.template.Template(filename=self.source)
        makedirs_for_file(self.target)
        with open(self.target, 'w') as file_handle:
            file_handle.write(template.render(tdefs=d))

    def get_targets(self) -> List[str]:
        return [self.target]

    def get_targets_post_build(self) -> List[str]:
        return []


override_var_name = 'TEMPLAR_OVERRIDE'


def load_and_populate(folders: List[str]):
    d = D()
    for folder in folders:
        for m in get_modules_list(folder):
            m.populate(d)

    # environment override
    if override_var_name in os.environ:
        values = os.environ[override_var_name].split(';')
        for value in values:
            k, v = value.strip().split('=')
            d[k] = v

    return d


def print_full_exception():
    print('printing full exception')
    traceback = mako.exceptions.RichTraceback()
    for (filename, line_number, function_name, line) in traceback.traceback:
        print('File {0}, line {1}, in {2}'.format(filename, line_number, function_name))
        print(line)
    print('{0}: {1}'.format(str(traceback.error.__class__.__name__), traceback.error))


def print_exception(e, input_file):
    found = False
    traceback = mako.exceptions.RichTraceback()
    for (filename, line_number, function_name, line) in traceback.traceback:
        if filename == input_file:
            print('{0}: error {1} in {2}, line {3}'.format(sys.argv[0], str(e), filename, line_number, function_name))
            print('{0}'.format(line))
            found = True
    if not found:
        for (filename, line_number, function_name, line) in traceback.traceback:
            print('File {0}, line {1}, in {2}'.format(filename, line_number, function_name))
            print(line)
        print('{0}: {1}'.format(str(traceback.error.__class__.__name__), traceback.error))
