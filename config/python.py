# deb section
deb_package = True
deb_section = 'python'
deb_priority = 'optional'
deb_architecture = 'all'
deb_package_name = 'pyscrapers'
# to which series to publish the package?
deb_series = [
    'artful',
    'zesty',
    'xenial',
    'trusty',
]
deb_depends = '${misc:Depends}, ${python3:Depends}, python3-mako'
deb_builddepends = 'python3, python3-setuptools, debhelper, dh-python'
deb_standards_version = '3.9.8'
deb_x_python_version = '>= 3.4'
deb_x_python3_version = '>= 3.4'
deb_urgency = 'low'
# archive of package
deb_repo = '~/packages'
# where to put packages that are built?
deb_out_folder = 'out'
# build_all = build.all
# where to build source packages?
# build_source = build.source
# where to build source packages?
# build_gbp = build.gbp

# python section
entry_points = {
    'console_scripts': [
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
