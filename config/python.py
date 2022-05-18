import pyclassifiers.values
import config.project

package_name = config.project.name

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
    "gitpython",
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

python_requires = ">=3.6"

platforms = [
    "python3",
]
classifiers = [
    pyclassifiers.values.DevelopmentStatus__4_Beta,
    pyclassifiers.values.Environment__Console,
    pyclassifiers.values.OperatingSystem__OSIndependent,
    pyclassifiers.values.ProgrammingLanguage__Python,
    pyclassifiers.values.ProgrammingLanguage__Python__3,
    pyclassifiers.values.ProgrammingLanguage__Python__3__Only,
    pyclassifiers.values.ProgrammingLanguage__Python__39,
    pyclassifiers.values.Topic__Utilities,
    pyclassifiers.values.License__OSIApproved__MITLicense,
]
