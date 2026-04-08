# DEPRECATED: This module is deprecated and will be removed in a future release.
# Use the `tasks` package instead: python -m tasks
from collections.abc import Callable
from .create_env import create_env
from .change_version import change_version

FUNCTIONS: dict[str, Callable[..., None]] = {
    "create_env": create_env,
    "change_version": change_version,
}
