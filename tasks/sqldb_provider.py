from pathlib import Path

import common
import settings

PROVIDER_DIR = settings.MAIN_DIR / 'sqldb-provider'


class SqldbProvider(object):
    """A set of services provider functions to sqldb-provider."""

    def create_dot_env(self) -> Path:
        """Create the .env file in the sqldb-provider directory."""
        return common.env_file(env_path=PROVIDER_DIR)
