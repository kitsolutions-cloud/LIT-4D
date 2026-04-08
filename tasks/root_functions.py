from pathlib import Path

import common
import settings


class RootFunctions(object):
    """Common functions for all providers or root management project directory."""

    def create_dot_env_compose(self) -> Path:
        """Create the .env file in the root directory to docker compose ARGS."""
        return common.env_file(env_path=settings.MAIN_DIR)

    def define_default_provider_versions(self):
        """Define the provider image versions."""
        common.cli.oauth_provider.set_provider_version("latest")
