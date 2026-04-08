# DEPRECATED: This module is deprecated and will be removed in a future release.
# Use the `tasks` package instead: python -m tasks
import warnings
from common.env import create_env as _create_env

def create_env() -> None:
    warnings.warn(
        "scripts.email_provider.create_env is deprecated. Use the `tasks` package instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    _create_env(provider_dir="email-provider")
