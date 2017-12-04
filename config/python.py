import config.project

package_name = config.project.project_name

console_scripts = [
    'pydmt_build=pydmt.scripts.build:main',
]

setup_requires = [
]

install_requires = [
    # core
    'click',  # for command line parsing
    'pyfakeuse',  # for ignoring arguments to functions
    'pylogconf',  # for configuring logging
    # plugins
    'mako',  # for template handling
    'Sphinx',  # for the sphinx builder
]

dev_requires = [
    'pypitools',  # for upload and registration
    'pydmt',  # for building
    'pyclassifiers',  # for specifying classifications
]

python_requires = ">=3"
