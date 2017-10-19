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
        p.build_by_targets([], BuildProcessStats())

    def testSimpleCopy(self):
        with tempdir():
            shutil.copy("/etc/passwd", "passwd")
            p = PyDMT()
            b = Copy("passwd", "copy_of_passwd")
            p.addBuilder(b)
            stats = BuildProcessStats()
            p.build_by_builder(b, stats)
            self.assertEqual(stats.builder, 1)
            self.assertEqual(stats.copy, 0)

    def testIncremental(self):
        with tempdir():
            shutil.copy("/etc/passwd", "passwd")
            p = PyDMT()
            b = Copy("passwd", "copy_of_passwd")
            p.addBuilder(b)
            p.build_by_builder(b, BuildProcessStats())
            stats = BuildProcessStats()
            p.build_by_builder(b, stats)
            self.assertEqual(stats.builder, 0)
            self.assertEqual(stats.copy, 0)
            self.assertEqual(stats.nop, 1)

    def testCopyAfterRemove(self):
        with tempdir():
            shutil.copy("/etc/passwd", "passwd")
            p = PyDMT()
            b = Copy("passwd", "copy_of_passwd")
            p.addBuilder(b)
            p.build_by_builder(b, BuildProcessStats())
            stats = BuildProcessStats()
            os.unlink("copy_of_passwd")
            p.build_by_builder(b, stats)
            self.assertEqual(stats.builder, 0)
            self.assertEqual(stats.copy, 1)
            self.assertEqual(stats.nop, 0)
            self.assertEqual(stats.missing, 1)

    def testFail(self):
        with tempdir():
            shutil.copy("/etc/passwd", "passwd")
            p = PyDMT()
            b = Fail("passwd", "copy_of_passwd")
            p.addBuilder(b)
            stats = BuildProcessStats()
            p.build_by_builder(b, stats)
            self.assertEqual(stats.builder, 1)
            self.assertEqual(stats.copy, 0)
            self.assertEqual(stats.fail, 1)
            self.assertEqual(stats.nop, 0)
            self.assertEqual(stats.missing, 0)
