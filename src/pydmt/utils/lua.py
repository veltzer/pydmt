"""
lua.py

Load "config/*.lua" files and expose them like python modules.

The config files used to be python modules loaded via importlib. They are now
lua data files. Every call site kept its "getattr(mod, name)" shape, so the
object returned here mimics just enough of a module: attribute access, and
"hasattr" working for absent keys.

Lua globals are upper case by convention (NAME, KEYWORDS, ...) while the old
python attributes were lower case (name, keywords, ...). Lookup is therefore
case insensitive, which lets the call sites keep asking for "name".
"""

import os.path
from typing import Any

# lupa exposes LuaRuntime through a module level __getattr__ that points at the
# bundled lua version (lupa.lua54, lupa.lua55, ...), so it cannot be imported
# by name. Going through the package attribute works for any bundled version.
import lupa


CONFIG_FOLDER = "config"


def lua_to_python(value: Any) -> Any:
    """
    Recursively convert a lua value into its python equivalent.

    Lua has a single table type, so a table is a list if its keys are exactly
    1..n and a dict otherwise. An empty table becomes an empty list, which
    matches how the config files use them.
    """
    if not hasattr(value, "values"):
        return value
    keys = list(value.keys())
    if keys == list(range(1, len(keys) + 1)):
        return [lua_to_python(x) for x in value.values()]
    return {k: lua_to_python(value[k]) for k in keys}


class LuaConfig:
    """ A loaded lua config file, accessed like a module """
    def __init__(self, values: dict[str, Any]):
        # keyed by lower case name so that "name" finds the lua global "NAME"
        self._values = {k.lower(): v for k, v in values.items()}

    def __getattr__(self, name: str) -> Any:
        try:
            return self._values[name.lower()]
        except KeyError:
            raise AttributeError(name) from None


def config_path(name: str) -> str:
    """ return the path of a config file by its short name ("project") """
    return os.path.join(CONFIG_FOLDER, f"{name}.lua")


def config_exists(name: str) -> bool:
    """ return whether a config file exists """
    return os.path.isfile(config_path(name))


def load_config(name: str) -> LuaConfig:
    """
    Load "config/[name].lua" and return it as a module like object.

    Raises FileNotFoundError if the file does not exist, mirroring the
    ModuleNotFoundError that importlib used to raise.
    """
    path = config_path(name)
    if not os.path.isfile(path):
        raise FileNotFoundError(path)
    runtime = lupa.LuaRuntime()
    with open(path, encoding="utf-8") as stream:
        runtime.execute(stream.read())
    globals_table = runtime.globals()
    values = {}
    for key in globals_table.keys():
        # skip the lua standard library, we only want what the file declared
        if key in _LUA_BUILTINS:
            continue
        values[key] = lua_to_python(globals_table[key])
    return LuaConfig(values)


_LUA_BUILTINS = frozenset({
    "_G", "_VERSION", "assert", "collectgarbage", "coroutine", "debug", "dofile",
    "error", "getmetatable", "io", "ipairs", "load", "loadfile", "math", "next",
    "os", "package", "pairs", "pcall", "print", "python", "rawequal", "rawget",
    "rawlen", "rawset", "require", "select", "setmetatable", "string", "table",
    "tonumber", "tostring", "type", "utf8", "xpcall",
})
