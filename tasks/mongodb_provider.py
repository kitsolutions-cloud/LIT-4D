from pathlib import Path

import common
import settings

PROVIDER_DIR = settings.MAIN_DIR / 'mongodb-provider'


class MongodbProvider(object):
    """A set of services provider functions to mongodb-provider."""

    def dot_env(self, create: bool = None) -> None:
        """
        Configurations about .env in the mongodb-provider.
            :arg create: Create a new .env file if it does not exist.
        """
        if create is not None and create == True:
            common.env_file(env_path=PROVIDER_DIR)
            print(f"{PROVIDER_DIR}/.env created.")
            return