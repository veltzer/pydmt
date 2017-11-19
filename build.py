#!/usr/bin/env python

from pydmt.builders.sphinx import Sphinx
from pydmt.core.pydmt import PyDMT
from pydmt.features.templating import Templating
import pylogconf

import config

pylogconf.setup()
pydmt = PyDMT()
f = Templating(config=config)
f.setup(pydmt)
b = Sphinx(package_name=config.project_name)
pydmt.add_builder(b)
pydmt.build_all()
