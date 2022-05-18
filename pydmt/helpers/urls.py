import pydmt.helpers.project
import user.personal

def get_website():
    name = pydmt.helpers.project.get_project_name()
website = f"https://{github_username}.github.io/{name}"
website_source = f"https://github.com/{github_username}/{name}"
website_git = f"git://github.com/{github_username}/{name}.git"
website_download_ppa = "https://launchpanet/~{launchpad_username}/+archive/ubuntu/ppa"
website_download_src = website_source
