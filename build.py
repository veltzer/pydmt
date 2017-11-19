#!/usr/bin/env python

import pylogconf

# noinspection PyUnresolvedReferences
import config
# noinspection PyUnresolvedReferences
import config.python
# noinspection PyUnresolvedReferences
import config.personal
# noinspection PyUnresolvedReferences
import config.project

import pydmt.version
from pydmt.builders.sphinx import Sphinx
from pydmt.core.pydmt import PyDMT
from pydmt.features.templating import Templating

pylogconf.setup()
p = PyDMT()
f = Templating(data={
    "config": config,
    "version": pydmt.version,
})
f.setup(p)
b = Sphinx(package_name=config.python.project_name)
p.add_builder(b)
p.build_all()

__all__ = [config, config.python, config.personal]
