import setuptools

import sys
if not sys.version_info[0] == 3:
    sys.exit("Sorry, only python version 3 is supported")

setuptools.setup(
    name='pydmt',
    version='0.0.1',
    description='pydmt is a tool for constructing software',
    long_description='pydmt is a tool for constructing software',
    url='https://veltzer.github.io/pydmt',
    author='Mark Veltzer',
    author_email='mark.veltzer@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
    ],
    keywords='pydmt cons scons software construction make maven mvn',
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
        ],
    },
)
