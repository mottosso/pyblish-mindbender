"""Public API

Anything that is not defined here is **internal** and
unreliable for external use.

Motivation for api.py:
    Storing the API in a module, as opposed to in __init__.py, enables
    use of it internally.

    For example, from `pipeline.py`:
        >> from . import api
        >> api.do_this()

    The important bit is avoiding circular dependencies, where api.py
    is calling upon a module which in turn calls upon api.py.

"""

import logging

from . import schema

from .pipeline import (
    install,
    uninstall,

    ls,
    search,

    Loader,
    discover_loaders,

    register_root,
    register_data,
    register_host,
    register_format,
    register_family,
    register_loaders_path,
    register_plugins,

    registered_host,
    registered_families,
    registered_loaders_paths,
    registered_formats,
    registered_data,
    registered_root,

    deregister_plugins,
    deregister_family,
    deregister_data,
    deregister_loaders_path,

    any_representation,

    fixture,
)

from .lib import (
    format_staging_dir,
    format_shared_dir,
    format_version,

    time,

    find_latest_version,
    parse_version,
)

logging.basicConfig()

__all__ = [
    "install",
    "uninstall",

    "schema",

    "ls",
    "search",

    "Loader",
    "discover_loaders",

    "register_host",
    "register_data",
    "register_format",
    "register_family",
    "register_loaders_path",
    "register_plugins",
    "register_root",

    "registered_root",
    "registered_loaders_paths",
    "registered_host",
    "registered_families",
    "registered_formats",
    "registered_data",

    "deregister_plugins",
    "deregister_family",
    "deregister_data",
    "deregister_loaders_path",

    "format_staging_dir",
    "format_shared_dir",
    "format_version",

    "find_latest_version",
    "parse_version",

    "time",

    "any_representation",

    "fixture",
]
