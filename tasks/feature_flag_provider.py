import common
import settings

PROVIDER_DIR = settings.MAIN_DIR / 'feature-flag-provider'


class FeatureFlagProvider(object):
    """A set of services provider functions to feature-flag-provider."""

    def dot_env(self, create: bool = None) -> None:
        """
        Configurations about .env in the feature-flag-provider.
            :arg create: Create a new .env file if it does not exist.
        """
        if create is not None and create == True:
            common.env_file(env_path=PROVIDER_DIR)
            print(f"{PROVIDER_DIR}/.env created.")
            return
