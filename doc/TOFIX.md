# TOFIX

Findings from a code scan on 2026-10-04.

## High

- `src/pydmt/features/apt.py:23` - the feature only registers when `config/deps.py` exists (and uses it as the builder source at line 26), but the packages are read from `config/deps.lua` (`helpers/attrs.py:27` via `utils/lua.py`); after the config move to Lua the apt feature never runs. Gate on and depend on `config/deps.lua`.
- `src/pydmt/features/reqs.py:11` - same stale gate: `FeatureReqs` (and `FeatureVenv`, `features/venv.py:16,21`) require `config/python.py`, while `BuilderReqs`/`BuilderVenv` read requirements from `config/python.lua`/`config/bootstrap.lua` (`utils/python.py:71,83`). Switch the source file to the `.lua` files (and drop the unused `SOURCE_FILE` in `builders/venv.py:15`).
- `src/pydmt/helpers/urls.py:40` - `get_website_ppa()` reads the GitHub username instead of `get_launchpad_username()`, and the URL at line 43 is misspelled (`launchpanet` instead of `launchpad.net`); fix both.

## Medium

- `src/pydmt/helpers/python.py:25` - `{main.__name__, }` formats a tuple, so `make_console_script` returns `pkg=module:('main',)` (verified) instead of `pkg=module:main`; drop the trailing comma.
- `src/pydmt/builders/sphinx.py:39` - the signature walks `self.package_name` at the repo root, but sources live in `src/<package>` (line 74), so changes to the Python code never invalidate the cached docs; walk `os.path.join("src", self.package_name)`. Lines 77-80 also append the package name as a trailing `sphinx-apidoc` argument, which apidoc treats as an exclude pattern - a leftover from the pre-`src/` layout; remove it.
- `src/pydmt/builders/apt.py:35` - `apt-get remove` is run without `--yes`, so it stops at the confirmation prompt (or aborts without a tty) even though `DEBIAN_FRONTEND=noninteractive` is set; add `--yes` as the update/install calls do.
- `src/pydmt/core/pydmt.py:152` - `clean_all` calls `target.remove()` for every target, and `File.remove`/`Folder.remove` (`api/builder.py:116,160`) raise when the target was never built, so `pydmt clean` aborts on the first missing target; ignore missing files/folders.
- `src/pydmt/helpers/urls.py:36` - returns a `git://github.com/...` URL; GitHub turned off the unauthenticated git protocol in 2022, so this URL no longer works. Use `https://github.com/<user>/<name>.git`.
- `src/pydmt/helpers/apt.py:12` - runs `lsb_release` and `dpkg-architecture` (shell pipeline, line 14) at import time, so merely importing `pydmt.helpers.apt` (or `helpers.composites`) fails on any non-Debian host or container without those tools; compute the values lazily in functions.
- `src/pydmt/main.py:14` - `ConfigApt`, `ConfigSubprocess` and `ConfigImport` are not listed in any endpoint's `configs=`, so `apt_quiet`, `print_command`, `quiet` and the `import_*` switches cannot be set from the command line (verified with `pydmt help build`), while `ConfigOutput.verbose`/`print_not` are exposed but never read anywhere. Register the used configs and delete the unused ones.
- `src/pydmt/builders/venv.py:51` - runs the `virtualenv` executable, which is not a declared dependency in `pyproject.toml:39-50`; use `python -m venv` or add `virtualenv` to the dependencies.
- `rsconstruct.toml:53` - `dep_inputs = ["src/pydmt/*.py"]` only covers the top-level modules, but the docs autodoc the subpackages too (`sphinx/pydmt.api.rst`, `pydmt.builders.rst`, ...); use `src/pydmt/**/*.py` so a change in a subpackage rebuilds the docs.

## Low

- `src/pydmt/configs.py:86` - `logging.WARNING` is listed twice, and `FATAL`/`CRITICAL` (lines 88-89) are the same level, so `pydmt help build` shows `WARNING,WARNING` and `CRITICAL,CRITICAL`; dedupe the choice list.
- `src/pydmt/features/yaml.py:29` - the stamp path joins `target_base` and `source + ".stamp"`, producing `out/yaml/x/yaml/x.yaml.stamp`; use one of them.
- `src/pydmt/utils/python.py:12` - `hlp_source_under`, `hlp_files_under` and the `make_hlp_*` helpers duplicate `helpers/python.py:132-182` and are referenced nowhere; delete the copies. `core/graph.py:6` (empty `Graph`), `utils/php.py`, `utils/importlib.py` and `utils/subprocess.py:21` (`check_call_ve_env`) are also unreferenced.
- `src/pydmt/helpers/deb_python_package.py:15` - targets long-EOL Ubuntu series (trusty, xenial, bionic, cosmic, disco), Standards-Version 3.9.8 and Python `>= 3.4`; update or delete the module.
- `src/pydmt/core/pydmt.py:103` - `# pylint: disable=broad-except` (also `builders/mako.py:24`) are leftovers: pylint is not run by the build; remove them.
- `tests/unit_tests/test_all.py:49` - `test04Incremental` is a copy of `test03SimpleCopy` and never runs a second build, so incremental rebuild (cache hit / `nop`) is untested; build twice and assert `get_nop() == 1`.
- `pyproject.toml:101` - the mypy override lists the project's own package `pydmt.*` under `ignore_missing_imports`; remove that entry.
