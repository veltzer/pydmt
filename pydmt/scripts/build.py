import os
import pylogconf
import sys

from pydmt.builders.sphinx import Sphinx
from pydmt.core.pydmt import PyDMT
from pydmt.features.templating import Templating


def main():
    debug = True
    sphinx = False
    add_import_of_cwd = True
    if add_import_of_cwd:
        sys.path.insert(0, os.getcwd())
    pylogconf.setup()
    if debug:
        print("system path is [{}]".format(sys.path))
    p = PyDMT()
    t = Templating()
    t.setup(p)
    if sphinx:
        import config.project
        p.add_builder(Sphinx(package_name=config.project.project_name))
    p.build_all()


if __name__ == '__main__':
    main()
