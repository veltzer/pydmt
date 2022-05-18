<%!
    import pydmt.helpers.misc
    import pydmt.helpers.signature
    import config.project
    import config.python
    import user.personal
    import glob
    import yaml
    import os
%># *${config.project.name}* project by ${user.personal.fullname}

description: ${config.project.description_short}

project website: ${config.project.website}

author: ${user.personal.fullname}

version: ${pydmt.helpers.misc.get_version_str()}

![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)
![License](https://img.shields.io/github/license/veltzer/pytconf)

${"##"} build status

<%
	action_files = glob.glob('.github/workflows/*.yml')
	for action_file in action_files:
		with open(action_file, 'r') as stream:
			action_name=yaml.safe_load(stream)["name"]
			context.write(f"![{action_name}](https://github.com/{config.project.github_username}/{config.project.name}/workflows/{action_name}/badge.svg)")
%>

${"##"} pypi stats

![PyPI - Status](https://img.shields.io/pypi/status/${config.python.package_name})
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/${config.python.package_name})
![PyPI - License](https://img.shields.io/pypi/l/${config.python.package_name})
![PyPI - Package Name](https://img.shields.io/pypi/v/${config.python.package_name})
![PyPI - Format](https://img.shields.io/pypi/format/${config.python.package_name})

${"##"} download stats

![PyPI - Downloads](https://img.shields.io/pypi/dd/${config.python.package_name})
![PyPI - Downloads](https://img.shields.io/pypi/dw/${config.python.package_name})
![PyPI - Downloads](https://img.shields.io/pypi/dm/${config.python.package_name})
<%doc>
![Downloads](https://pepy.tech/badge/${config.python.package_name})
![Downloads](https://pepy.tech/badge/${config.python.package_name}/week)
![Downloads](https://pepy.tech/badge/${config.python.package_name}/month)
</%doc>
% if hasattr(config.project, "codacy_id"):
${"##"} codacy stuff 

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/${config.project.codacy_id})](https://www.codacy.com/app/jarrekk/imgkit?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=${config.project.github_username}/${config.python.package_name}&amp;utm_campaign=Badge_Grade)
% endif

% if os.path.isfile("../snipplets/main.md.mako"):
<%include file="../snipplets/main.md.mako" />
% endif

${"##"} contact me
[mailto](mailto:${user.personal.email})
![gitter](https://img.shields.io/gitter/room/veltzer/mark.veltzer)
![discord](https://img.shields.io/discord/719336281624281119)
![discord](https://img.shields.io/discord/719336282194444302)

${user.personal.fullname}, Copyright © ${pydmt.helpers.signature.get_copyright_years_long()}
