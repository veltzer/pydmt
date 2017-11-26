import pylogconf

from pydmt.builders.sphinx import Sphinx
from pydmt.core.pydmt import PyDMT
from pydmt.features.templating import Templating

import config.project


def main():
    pylogconf.setup()
    p = PyDMT()
    t = Templating()
    t.setup(p)
    p.add_builder(Sphinx(package_name=config.project.project_name))
    p.build_all()


if __name__ == '__main__':
    main()
