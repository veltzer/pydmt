import config.project

package_name = config.project.project_name

console_scripts = [
    "pydmt.main:main",
]

setup_requires = [
]

test_requires = [
    'pylint',
    'pytest',
    'pyflakes',
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
]

python_requires = ">=3.6"

extras_require = {
}
