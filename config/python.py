""" python depedencies for this project """
from typing import List


console_scripts: List[str] = [
    "pydmt=pydmt.main:main",
]
dev_requires: List[str] = [
    "pypitools",
    "black",
]
config_requires: List[str] = [
    "pyclassifiers",
]
install_requires: List[str] = [
    "pyfakeuse",
    "pylogconf",
    "pytconf",
    "mako",
    "sphinx",
    "pyyaml",
    "jsonschema",
    "venv-run",
    "gitpython",
]
build_requires: List[str] = [
    "pymakehelper",
    "pydmt",
]
test_requires: List[str] = [
    "pylint",
    "pytest",
    "pytest-cov",
    "pyflakes",
    "flake8",
    "mypy",
    # types
    "types-PyYAML",
    "types-jsonschema",
]
requires = config_requires + install_requires + build_requires + test_requires
