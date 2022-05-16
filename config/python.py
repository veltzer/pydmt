import config.project

package_name = config.project.project_name

console_scripts = [
    "pydmt=pydmt.main:main",
]

dev_requires = [
    "pypitools",
]
config_requires = [
    "pyclassifiers",
]
install_requires = [
    "pyfakeuse",
    "pylogconf",
    "pytconf",
    "mako",
    "Sphinx",
    "pyyaml",
    "jsonschema",
    "venv-run",
]
test_requires = [
    "pylint",
    "pytest",
    "pytest-cov",
    "pyflakes",
    "flake8",
]
make_requires = [
    "pymakehelper",
]

python_requires = ">=3.10"
