import pyclassifiers.values
import pydmt.helpers.general
import pydmt.helpers.signature

project_github_username = "veltzer"
project_name = "pydmt"
github_repo_name = project_name
project_website = f"https://{project_github_username}.github.io/{project_name}"
project_website_source = f"https://github.com/{project_github_username}/{project_name}"
project_website_git = f"git://github.com/{project_github_username}/{project_name}.git"
project_website_download_ppa = "https://launchpanet/~mark-veltzer/+archive/ubuntu/ppa"
project_website_download_src = project_website_source
project_description_short = "python dependency management tool"
project_description_long = """TBD"""
# keywords to put on html pages or for search, dont put the name of the project or my details
# as they will be added automatically...
project_keywords = [
    "pydmt",
    "cons",
    "scons",
    "software construction",
    "make",
    "cmake",
    "maven",
    "mvn",
]
project_license = "MIT"
project_year_started = 2017
project_platforms = [
    "python3",
]
project_classifiers = [
    pyclassifiers.values.DevelopmentStatus__4_Beta,
    pyclassifiers.values.Environment__Console,
    pyclassifiers.values.OperatingSystem__OSIndependent,
    pyclassifiers.values.ProgrammingLanguage__Python,
    pyclassifiers.values.ProgrammingLanguage__Python__3,
    pyclassifiers.values.ProgrammingLanguage__Python__3__Only,
    pyclassifiers.values.ProgrammingLanguage__Python__39,
    pyclassifiers.values.Topic__Utilities,
    pyclassifiers.values.License__OSIApproved__MITLicense,
]
project_data_files = []

project_copyright_years_long = pydmt.helpers.signature.get_copyright_years_long(project_year_started)
