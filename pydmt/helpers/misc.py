def get_version_str():
    import config.version
    return ".".join(str(x) for x in config.version.tup)
