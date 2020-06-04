import config.project
import pydmt.endpoints.main

package_name = config.project.project_name

console_scripts = [
    'pydmt=' + pydmt.endpoints.main.__name__ + ":" + pydmt.endpoints.main.main.__name__,
]

setup_requires = [
]

test_requires = [
    'pylint',  # to check for lint errors
    'pytest',  # for testing
    'pyflakes',  # for testing
]

install_requires = [
    # core
    'pyfakeuse',  # for ignoring arguments to functions
    'pylogconf',  # for configuring logging
    'pytconf',  # for handling command line arguments
    # plugins
    'mako',  # for template handling
    'Sphinx',  # for the sphinx builder
]

dev_requires = [
    'pypitools',  # for upload and registration
    'pydmt',  # for building
    'pyclassifiers',  # for specifying classifications
]

python_requires = ">=3.5"

extras_require={
#    ':python_version == "2.7"': ['futures'],  # for python2.7 backport of concurrent.futures
}
