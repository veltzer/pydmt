-- python deps for this project

dofile("config/shared.lua")

-- append every element of "src" onto "dst"
local function extend(dst, src)
    for _, value in ipairs(src) do
        table.insert(dst, value)
    end
    return dst
end

INSTALL_REQUIRES = {
    "pyfakeuse",
    "pylogconf",
    "pytconf",
    "mako",
    "sphinx",
    "pyyaml",
    "jsonschema",
    "venv-run",
    "gitpython",
    "lupa",
}
BUILD_REQUIRES = PBUILD
TEST_REQUIRES = PTEST
TYPES_REQUIRES = {
    "types-PyYAML",
    "types-jsonschema",
}

REQUIRES = {}
extend(REQUIRES, INSTALL_REQUIRES)
extend(REQUIRES, BUILD_REQUIRES)
extend(REQUIRES, TEST_REQUIRES)
extend(REQUIRES, TYPES_REQUIRES)

SCRIPTS = {
    pydmt = "pydmt.main:main",
}
