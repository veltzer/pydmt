import setuptools

setuptools.setup(
    name='pydmt',
    version='0.0.4',
    description='pydmt is a tool for constructing software',
    long_description='pydmt is a tool for constructing software',
    url='https://github.com/veltzer/pydmt',
    download_url='https://github.com/veltzer/pydmt',
    author='Mark Veltzer',
    author_email='mark.veltzer@gmail.com',
    maintainer='Mark Veltzer',
    maintainer_email='mark.veltzer@gmail.com',
    license='MIT',
    platforms=['python3'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
    ],
    keywords='pydmt cons scons software construction make maven mvn',
    packages=setuptools.find_packages(),
    install_requires=[
        'mako',  # for template handling
        'click',  # for command line parsing
        'pyfakeuse',  # for ignoring arguments to functions
    ],
    entry_points={
        'console_scripts': [
        ],
    },
)
