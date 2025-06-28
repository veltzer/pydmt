""" python deps for this project """

console_scripts: list[str] = [
    "pydmt=pydmt.main:main",
]
config_requires: list[str] = [
    "pyclassifiers",
]
install_requires: list[str] = [
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
build_requires: list[str] = [
    "pymakehelper",
    "pydmt",
]
test_requires: list[str] = [
    "pylint",
    "pytest",
    "pytest-cov",
    "mypy",
    # types
    "types-PyYAML",
    "types-jsonschema",
]
requires = config_requires + install_requires + build_requires + test_requires
