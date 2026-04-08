import common
import settings

PROVIDER_DIR = settings.MAIN_DIR / 'sqldb-provider'


class SqldbProvider(object):
    """A set of services provider functions to sqldb-provider."""

    def dot_env(self, create: bool = None) -> None:
        """
        Configurations about .env in the sqldb-provider.
        """
        if create is not None and create == True:
            common.env_file(env_path=PROVIDER_DIR)
            print(f"{PROVIDER_DIR}/.env created.")
            return
