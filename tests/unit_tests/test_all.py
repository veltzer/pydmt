import unittest

import shutil

import pydmt.core.pydmt
from pydmt.builders.copy import Copy
from pydmt.core.tempdir import tempdir


class TestAll(unittest.TestCase):

    def testCreateObject(self):
        pydmt.core.pydmt.PyDMT()

    def testCreateBuild(self):
        p = pydmt.core.pydmt.PyDMT()
        p.build_by_targets([])

    def testCheckSimpleCopy(self):
        with tempdir():
            shutil.copy("/etc/passwd", "passwd")
            p = pydmt.core.pydmt.PyDMT()
            b = Copy("passwd", "copy_of_passwd")
            p.addBuilder(b)
            p.build_by_builder(b)


