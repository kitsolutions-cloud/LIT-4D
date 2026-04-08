from pathlib import Path

import common
import settings

PROVIDER_DIR = settings.MAIN_DIR / 'oauth-provider'


class OauthProvider(object):
    """A set of services provider functions to oauth-provider."""

    def create_dot_env(self) -> Path:
        """Create the .env file in the oauth-provider directory."""
        return common.env_file(env_path=PROVIDER_DIR)

    def set_provider_version(self, version: str):
        """Set the provider version located in the root .env file as OAUTH_PROVIDER_IMAGE_VERSION."""
        common.set_env_var(
            env_path=settings.MAIN_DIR,
            key="OAUTH_PROVIDER_IMAGE_VERSION",
            value=version
        )
