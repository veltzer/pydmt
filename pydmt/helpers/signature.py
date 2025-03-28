"""
signature.py
"""

import datetime
import time

import git


def get_project_year_started(repo=".") -> int:
    repo = git.Repo(repo)
    commits = list(repo.iter_commits())
    last_commit = commits[-1]
    t = time.gmtime(last_commit.authored_date)
    return t.tm_year


def get_copyright_years_long(repo="."):
    project_year_started = get_project_year_started(repo=repo)
    general_current_year = datetime.datetime.now().year
    return ", ".join(map(str, range(int(project_year_started), general_current_year + 1)))


def get_copyright_years_short(repo="."):
    project_year_started = get_project_year_started(repo=repo)
    general_current_year = datetime.datetime.now().year
    if general_current_year == project_year_started:
        return general_current_year
    return f"{project_year_started} - {general_current_year}"
