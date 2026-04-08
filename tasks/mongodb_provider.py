from pathlib import Path

import common
import settings

PROVIDER_DIR = settings.MAIN_DIR / 'mongodb-provider'


class MongodbProvider(object):
    """A set of services provider functions to mongodb-provider."""

    def create_dot_env(self) -> Path:
        """Create the .env file in the mongodb-provider directory."""
        return common.env_file(env_path=PROVIDER_DIR)