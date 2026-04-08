# DEPRECATED: This module is deprecated and will be removed in a future release.
# Use the `tasks` package instead: python -m tasks
import warnings
import importlib
import sys
import os

_scripts_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _scripts_dir not in sys.path:
    sys.path.insert(0, _scripts_dir)

_PROVIDER_MODULES = [
    "aws_services_provider",
    "email_provider",
    "feature_flag_provider",
    "mongodb_provider",
    "monitoring_provider_grafana",
    "monitoring_provider_loki",
    "monitoring_provider_alloy",
    "oauth_provider",
    "sqldb_provider",
]


def init() -> None:
    """Initialises all providers by creating their .env and setting version to latest.

    .. deprecated::
        Use `tasks` package instead: python -m tasks
    """
    warnings.warn(
        "scripts.common.init.init is deprecated. Use the `tasks` package instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    for module_name in _PROVIDER_MODULES:
        module = importlib.import_module(module_name)
        print(f"Initialising '{module_name}'...")
        module.FUNCTIONS["create_env"]()
        module.FUNCTIONS["change_version"](version="latest")
