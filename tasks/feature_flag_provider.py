from pathlib import Path

import common
import settings

PROVIDER_DIR = settings.MAIN_DIR / 'feature-flag-provider'


class FeatureFlagProvider(object):
    """A set of services provider functions to feature-flag-provider."""

    def create_dot_env(self) -> Path:
        """Create the .env file in the feature-flag-provider directory."""
        return common.env_file(env_path=PROVIDER_DIR)
