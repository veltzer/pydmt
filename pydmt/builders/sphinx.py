"""
This is the module which is in charge of running sphinx to generate
automatic documentation.

TODO
maybe call sphinx programatically and this way we would not have
to set the PYTHONPATH and get better integration with sphinx?
"""


import os
import shutil
from typing import List

from pydmt.api.builder import Builder
from pydmt.utils.filesystem import files_under_folder, unlink_files, copy_mkdir
from pydmt.utils.digest import sha1_files_folders
import subprocess


"""
This is review of how to build a sphinx documentation:
- if you want documentation for the code you need to run "sphinx-apidoc"
- it will generate files that describe every sub package in your package.
- after this you run "sphinx-build"
- "sphinx-quickstart" is not needed unless you are starting a new project. 
"""


class Sphinx(Builder):
    def get_sources(self) -> List[str]:
        return self._get_source_folder_source_files()

    def __init__(self,
                 package_name: str,
                 source_folder: str = "sphinx",
                 target_folder: str = "docs"):
        super().__init__()
        self.package_name = package_name
        self.source_folder = source_folder
        self.target_folder = target_folder

    def get_signature(self) -> str:
        if os.path.isfile(self.package_name+".py"):
            files = [self.package_name+".py"]
            files.extend(self._get_source_folder_source_files())
            return sha1_files_folders(
                files=files,
                folders=[
                    os.path.join(self.source_folder, "static"),
                    os.path.join(self.source_folder, "copy"),
                ],
            )
        if os.path.isdir(self.package_name):
            files = self._get_source_folder_source_files()
            files.extend(files_under_folder(self.package_name, suffix=".py"))
            files.extend(files_under_folder(os.path.join(self.source_folder, "static")))
            files.extend(files_under_folder(os.path.join(self.source_folder, "copy")))
            return sha1_files_folders(files=files)
        raise ValueError("Sphinx cannot find source code")

    def _get_source_folder_targets(self) -> List[str]:
        return [
            os.path.join(self.source_folder, "modules.rst"),
            os.path.join(self.source_folder, "{}.rst".format(self.package_name)),
            # We need to add the list of all output files of running sphinx-apidoc
            # os.path.join(self.source_folder, "{}.endpoints.rst".format(self.package_name)),
        ]

    def _get_source_folder_source_files(self) -> List[str]:
        return [
            os.path.join(self.source_folder, "index.rst"),
            os.path.join(self.source_folder, "conf.py"),
        ]

    def build(self) -> None:
        unlink_files(self._get_source_folder_targets(), only_if_exist=True)
        args = [
            "sphinx-apidoc",
            "-q",  # quiet
            "-f",
            "-o",
            self.source_folder,
        ]
        # single file module vs package
        if os.path.isfile(self.package_name+'.py'):
            args.append(self.package_name+'.py')
        else:
            args.append(self.package_name)
        subprocess.check_call(args)
        if os.path.isdir(self.target_folder):
            shutil.rmtree(self.target_folder, ignore_errors=False)
            os.environ["PYTHONPATH"] = "."
            subprocess.check_call([
                "sphinx-build",
                # don't use a saved environment, always read all files
                # "-E",
                # Do not emit colored output(default: auto - detect)
                "--no-color",
                # turn warnings into errors
                "-W",
                # no output on stdout, just warnings on stderr
                "-q",
                self.source_folder,
                self.target_folder,
            ])
        for filename in files_under_folder(os.path.join(self.source_folder, "copy")):
            basename = os.path.basename(filename)
            copy_mkdir(filename, os.path.join(self.target_folder, basename))

    def get_targets_post_build(self) -> List[str]:
        return_list = self._get_source_folder_targets()
        return_list.extend(files_under_folder(self.target_folder))
        return return_list
