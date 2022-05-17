<%!
    import pydmt.helpers.misc
    import config.python
    import user.personal
    import config.project
    import config.version
    import pydmt.helpers.python
%>import setuptools


def get_readme():
    with open('README.rst') as f:
        return f.read()


setuptools.setup(
    # the first three fields are a must according to the documentation
    name="${config.project.name}",
    version="${pydmt.helpers.misc.get_version_str()}",
    packages=${pydmt.helpers.python.array_indented(1, pydmt.helpers.python.find_packages(config.python.package_name))},
    # from here all is optional
    description="${config.project.description_short}",
    long_description=get_readme(),
    long_description_content_type="text/x-rst",
    author="${user.personal.personal_fullname}",
    author_email="${user.personal.personal_email}",
    maintainer="${user.personal.personal_fullname}",
    maintainer_email="${user.personal.personal_email}",
    keywords=${pydmt.helpers.python.array_indented(1, config.project.keywords)},
    url="${config.project.website}",
    download_url="${config.project.website_download_src}",
    license="${config.project.license_type}",
    platforms=${pydmt.helpers.python.array_indented(1, config.python.platforms)},
% if hasattr(config.python, "install_requires"):
    install_requires=${pydmt.helpers.python.array_indented(1, config.python.install_requires)},
% endif
% if hasattr(config.python, "extras_requires"):
    extras_require=${pydmt.helpers.python.dict_indented(1, config.python.extras_require)},
% endif
    classifiers=${pydmt.helpers.python.array_indented(1, config.python.classifiers)},
% if hasattr(config.python, "data_files"):
    data_files=${pydmt.helpers.python.array_indented(1, config.project.data_files)},
% endif
% if hasattr(config.python, "console_scripts"):
    entry_points={"console_scripts": ${pydmt.helpers.python.array_indented(1, config.python.console_scripts)}},
% endif
% if hasattr(config.python, "python_requires"):
    python_requires="${config.python.python_requires}",
% endif
)
