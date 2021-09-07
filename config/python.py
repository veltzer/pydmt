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
]

dev_requires = [
    'pypitools',
    'pydmt',
    'pyclassifiers',
    'pymakehelper',
]

python_requires = ">=3.6"

extras_require = {
}
test_os = "[ubuntu-16.04, ubuntu-18.04, ubuntu-20.04]"
test_python = "[3.6, 3.7, 3.8]"
test_container = "[ 'ubuntu:18.04', 'ubuntu:20.04' ]"
