import setuptools

# until we make printing pretty
# noinspection PyPep8
setuptools.setup(
    name='pydmt',
    version='0.0.41',
    description='python dependency management tool',
    long_description='python dependency management tool',
    author='Mark Veltzer',
    author_email='mark.veltzer@gmail.com',
    maintainer='Mark Veltzer',
    maintainer_email='mark.veltzer@gmail.com',
    keywords=['pydmt', 'cons', 'scons', 'software construction', 'make', 'maven', 'mvn'],
    url='https://veltzer.github.io/pydmt',
    download_url='https://github.com/veltzer/pydmt',
    license='MIT',
    platforms=['python3'],
    packages=setuptools.find_packages(),
    install_requires=['click', 'pyfakeuse', 'pylogconf', 'mako', 'Sphinx'],
    classifiers=['Development Status :: 4 - Beta', 'Environment :: Console', 'Operating System :: OS Independent', 'Programming Language :: Python', 'Programming Language :: Python :: 3', 'Topic :: Utilities'],
    data_files=[],
    entry_points={'console_scripts': ['pydmt_build=pydmt.scripts.build:main']},
)
