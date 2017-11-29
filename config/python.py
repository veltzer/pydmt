entry_points = {
    'console_scripts': [
        'pydmt_build=pydmt.scripts.build:main',
    ],
}
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
]
