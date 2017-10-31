import unittest

import shutil

import os

from pydmt.builders.fail import Fail
from pydmt.core.pydmt import PyDMT, BuildProcessStats
from pydmt.builders.copy import Copy
from pydmt.core.tempdir import tempdir


class TestAll(unittest.TestCase):

    def testCreatePyDMT(self):
        PyDMT()

    def testNullBuild(self):
        p = PyDMT()
        p.build_all()

    def testReturnType(self):
        p = PyDMT()
        stats = p.build_all()
        self.assertIsInstance(stats, BuildProcessStats, "must be BuildProcessStats")

    def testSimpleCopy(self):
        with tempdir():
            shutil.copy("/etc/passwd", "passwd")
            p = PyDMT()
            b = Copy("passwd", "copy_of_passwd")
            p.add_builder(b)
            stats = p.build_all()
            self.assertEqual(stats.builder, 1)
            self.assertEqual(stats.copy, 0)

    def testIncremental(self):
        with tempdir():
            shutil.copy("/etc/passwd", "passwd")
            p = PyDMT()
            b = Copy("passwd", "copy_of_passwd")
            p.add_builder(b)
            stats = p.build_all()
            self.assertEqual(stats.builder, 1)
            self.assertEqual(stats.copy, 0)
            self.assertEqual(stats.nop, 0)

    def testCopyAfterRemove(self):
        with tempdir():
            shutil.copy("/etc/passwd", "passwd")
            p = PyDMT()
            b = Copy("passwd", "copy_of_passwd")
            p.add_builder(b)
            p.build_all()
            os.unlink("copy_of_passwd")
            stats = p.build_all()
            self.assertEqual(stats.builder, 0)
            self.assertEqual(stats.copy, 1)
            self.assertEqual(stats.nop, 0)
            self.assertEqual(stats.missing, 1)

    def testFail(self):
        with tempdir():
            shutil.copy("/etc/passwd", "passwd")
            p = PyDMT()
            b = Fail("passwd", "copy_of_passwd")
            p.add_builder(b)
            stats = p.build_all()
            self.assertEqual(stats.builder, 1)
            self.assertEqual(stats.copy, 0)
            self.assertEqual(stats.fail, 1)
            self.assertEqual(stats.nop, 0)
            self.assertEqual(stats.missing, 0)
