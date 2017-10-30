from typing import List

import os

import sys

from pydmt.api.builder import Builder
from pydmt.core.utils import sha1_file, get_modules_list, makedirs_for_file
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


class Mako(Builder):
<<<<<<< HEAD
    def __init__(self, definitions_folder: str, source: str, target: str):
        self.definitions_folder = definitions_folder
=======
    def __init__(self, source, target):
        super().__init__()
>>>>>>> 6736e4221c483118bc851261c6c411797b6b2465
        self.source = source
        self.target = target

    def get_signature(self) -> str:
        return sha1_file(self.source)

    def build(self):
        d = load_and_populate(self.definitions_folder)
        process(
            d,
            input_file=self.source,
            output_file=self.target,
        )

    def get_targets(self) -> List[str]:
        return [self.target]

    def get_targets_post_build(self) -> List[str]:
        return []


override_var_name = 'TEMPLAR_OVERRIDE'


def load_and_populate(folder: str):
    d = D()
    for m in get_modules_list(folder):
        m.populate(d)

    # environment override
    if override_var_name in os.environ:
        values = os.environ[override_var_name].split(';')
        for value in values:
            k, v = value.strip().split('=')
            d[k] = v

    return d


def process(d, input_file, output_file, input_encoding=sys.getdefaultencoding(),
            output_encoding=sys.getdefaultencoding()):
    lookup = mako.lookup.TemplateLookup(
        directories=['.'],
        input_encoding=input_encoding,
        output_encoding=output_encoding,
    )
    template = mako.template.Template(
        filename=input_file,
        lookup=lookup,
        input_encoding=input_encoding,
        output_encoding=output_encoding,
    )
    makedirs_for_file(output_file)
    f = open(output_file, 'wb')
    f.write(template.render(tdefs=d))
    f.close()


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
