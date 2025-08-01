"""
mako.py
"""

import sys
import os
import os.path
from collections.abc import Generator

import mako
import mako.exceptions
import mako.lookup
import mako.template

from pydmt.api.builder import Builder, Node, SourceFile, TargetFile, SourceFolder
from pydmt.utils.filesystem import makedirs_for_file
from pydmt.utils.digest import sha1_file

FOLDER_CONFIG = "config"
FOLDER_SNIPPLETS = "snipplets"


class BuilderMako(Builder):
    # pylint: disable=too-many-positional-arguments
    def __init__(self,
                 source: str,
                 target: str,
                 data: dict[str, object] | None,
                 config_files: list[str],
                 snipplet_files: list[str],
                 ):
        # super().__init__()
        self.source = source
        self.target = target
        self.data = data
        self.config_files: list[str] = config_files
        self.snipplet_files: list[str] = snipplet_files
        self.sources: list[Node] = [SourceFile(self.source)]
        if os.path.isdir(FOLDER_CONFIG):
            self.sources.append(SourceFolder(FOLDER_CONFIG))
        if os.path.isdir(FOLDER_SNIPPLETS):
            self.sources.append(SourceFolder(FOLDER_SNIPPLETS))
        self.targets: list[Node] = [TargetFile(self.target)]

    def get_sources(self) -> list[Node]:
        return self.sources

    def get_targets(self) -> list[Node]:
        return self.targets

    def build(self):
        lookup = mako.lookup.TemplateLookup(
            directories=['.'],
        )
        template = mako.template.Template(
            filename=self.source,
            lookup=lookup,
        )
        makedirs_for_file(self.target)
        if self.data is None:
            output = template.render()
        else:
            output = template.render(**self.data)
        with open(self.target, "w") as file_handle:
            file_handle.write(output)

    def yield_results(self) -> Generator[tuple[str, str], None, None]:
        yield sha1_file(self.target), self.target


def print_full_exception():
    print("printing full exception")
    traceback = mako.exceptions.RichTraceback()
    for (filename, line_number, function_name, line) in traceback.traceback:
        print(f"File {filename}, line {line_number}, in {function_name}")
        print(line)
    print(f"{traceback.error.__class__.__name__}: {traceback.error}")


def print_exception(e, input_file):
    found = False
    traceback = mako.exceptions.RichTraceback()
    for (filename, line_number, function_name, line) in traceback.traceback:
        if filename == input_file:
            print(f"{sys.argv[0]}: error {e} in {filename}, line {line_number} function {function_name}")
            print(f"{line}")
            found = True
    if not found:
        for (filename, line_number, function_name, line) in traceback.traceback:
            print(f"File {filename}, line {line_number}, in {function_name}")
            print(line)
        print(f"{traceback.error.__class__.__name__}: {traceback.error}")
