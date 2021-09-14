import config.project

package_name = config.project.project_name

console_scripts = [
    "pydmt=pydmt.main:main",
]

setup_requires = [
]

test_requires = [
    'pylint',
    'pytest',
    'pytest-cov',
    'pyflakes',
    'flake8',
]

install_requires = [
    'pyfakeuse',
    'pylogconf',
    'pytconf',
    'mako',
    'Sphinx',
    'pyyaml',
    'jsonschema',
]

dev_requires = [
    'pypitools',
    'pydmt',
    'pyclassifiers',
    'pymakehelper',
]

python_requires = ">=3.7"

extras_require = {
}

test_os = "[ubuntu-18.04, ubuntu-20.04]"
test_python = "[3.7, 3.8, 3.9]"
test_container = "[ 'ubuntu:18.04', 'ubuntu:20.04' ]"
