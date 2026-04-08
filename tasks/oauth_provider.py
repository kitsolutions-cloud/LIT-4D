import common
import settings

PROVIDER_DIR = settings.MAIN_DIR / 'oauth-provider'


class OauthProvider(object):
    """A set of services provider functions to oauth-provider."""

    def dot_env(self, create: bool = None) -> None:
        """
        Configurations about .env in the oauth-provider.
            :arg create: Create a new .env file if it does not exist.
        """
        if create is not None and create == True:
            common.env_file(env_path=PROVIDER_DIR)

    def config(self, version: str = None):
        """
        Configure provider settings.
            :arg version: The version of the provider image to use.
        """
        if version is not None:
            common.set_env_var(
                env_path=settings.MAIN_DIR,
                key="OAUTH_PROVIDER_IMAGE_VERSION",
                value=version
            )
