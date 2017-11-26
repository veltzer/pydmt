entry_points = {
    'console_scripts': [
        'pydmt=pydmt.scripts.pydmt:main',
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
