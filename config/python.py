from typing import List


console_scripts: List[str] = [
    "pydmt=pydmt.main:main",
]
config_requires: List[str] = [
    "pyclassifiers",
]
dev_requires: List[str] = [
    "pypitools",
]
make_requires: List[str] = [
    "pymakehelper",
    "pydmt",
    "pyclassifiers",
    "types-jsonschema",
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
test_requires: List[str] = [
    "pylint",
    "pytest",
    "pytest-cov",
    "pyflakes",
    "flake8",
    "mypy",
    "types-PyYAML",
]
requires = config_requires + install_requires + make_requires + test_requires
