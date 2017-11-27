entry_points = {
    'console_scripts': [
        'pydmt_build=pydmt.scripts.build:main',
    ],
}
install_requires = [
    # code requirements
    'click',  # for command line parsing
    'pyfakeuse',  # for ignoring arguments to functions
    'pylogconf',  # for configuring logging
    # builder requirements
    'mako',  # for template handling
    'Sphinx',  # for the sphinx builder
    ]
requirements3 = install_requires 
