"""
test_all.py
"""

import os
import shutil
import unittest
from typing import override

from pydmt.api.copy import Copy
from pydmt.api.fail import Fail
from pydmt.core.pydmt import BuildProcessStats, PyDMT
from pydmt.core.tempdir import tempdir


class TestAll(unittest.TestCase):

    @classmethod
    @override
    def setUpClass(cls) -> None:
        pass

    def test00_create_pydmt(self) -> None:
        PyDMT()

    def test01_null_build(self) -> None:
        p = PyDMT()
        p.build_all()

    def test02_return_type(self) -> None:
        p = PyDMT()
        stats = p.build_all()
        assert isinstance(stats, BuildProcessStats), "must be BuildProcessStats"

    @staticmethod
    def get_std_test() -> BuildProcessStats:
        shutil.copy("/etc/passwd", "passwd")
        p = PyDMT()
        b = Copy("passwd", "copy_of_passwd")
        p.add_builder(b)
        return p.build_all()

    def test03_simple_copy(self) -> None:
        with tempdir():
            stats = self.get_std_test()
            assert stats.get_builder_ok() == 1
            assert stats.get_copy_missing() == 0

    def test04_incremental(self) -> None:
        with tempdir():
            stats = self.get_std_test()
            assert stats.get_builder_ok() == 1
            assert stats.get_copy_missing() == 0
            assert stats.get_nop() == 0

    def test05_copy_after_remove(self) -> None:
        with tempdir():
            shutil.copy("/etc/passwd", "passwd")
            p = PyDMT()
            b = Copy("passwd", "copy_of_passwd")
            p.add_builder(b)
            p.build_all()
            os.unlink("copy_of_passwd")
            stats = p.build_all()
            assert stats.get_builder_ok() == 0
            assert stats.get_builder_fail() == 0
            assert stats.get_nop() == 0
            assert stats.get_copy_missing() == 1

    def test06_fail(self) -> None:
        with tempdir():
            shutil.copy("/etc/passwd", "passwd")
            p = PyDMT()
            b = Fail("passwd", "copy_of_passwd")
            p.add_builder(b)
            stats = p.build_all()
            assert stats.get_builder_ok() == 0
            assert stats.get_builder_fail() == 1
            assert stats.get_copy_missing() == 0
            assert stats.get_nop() == 0
