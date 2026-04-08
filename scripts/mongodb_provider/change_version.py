# DEPRECATED: This module is deprecated and will be removed in a future release.
# Use the `tasks` package instead: python -m tasks
import warnings
import re
from pathlib import Path

def change_version(version: str = "latest"):
    """
    Updates MONGODB_PROVIDER_IMAGE_VERSION in the root .env file.

    .. deprecated::
        Use `tasks` package instead: python -m tasks
    """
    warnings.warn(
        "scripts.mongodb_provider.change_version is deprecated. Use the `tasks` package instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    env_file = Path(".env")

    if not env_file.exists():
        print(f"Error: {env_file} does not exist.")
        return

    content = env_file.read_text()
    updated = re.sub(
        r"^(MONGODB_PROVIDER_IMAGE_VERSION=).*",
        rf"\g<1>{version}",
        content,
        flags=re.MULTILINE
    )
    env_file.write_text(updated)
    print(f"Successfully updated MONGODB_PROVIDER_IMAGE_VERSION to '{version}' in {env_file}")
