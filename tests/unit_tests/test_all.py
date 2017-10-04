import unittest

import pydmt.core.pydmt


class TestAll(unittest.TestCase):

    def testCreateObject(self):
        pydmt.core.pydmt.PyDMT()

    def testCreateBuild(self):
        p = pydmt.core.pydmt.PyDMT()
        p.build()
