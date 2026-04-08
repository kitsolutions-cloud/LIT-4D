from pathlib import Path

import common
import settings

PROVIDER_DIR = settings.MAIN_DIR / 'email-provider'


class EmailProvider(object):
    """A set of services provider functions to email-provider."""

    def create_dot_env(self) -> Path:
        """Create the .env file in the email-provider directory."""
        return common.env_file(env_path=PROVIDER_DIR)
