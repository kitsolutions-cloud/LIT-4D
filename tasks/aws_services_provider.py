from pathlib import Path

import common
import settings

PROVIDER_DIR = settings.MAIN_DIR / 'aws-services-provider'


class AwsServicesProvider(object):
    """A set of services provider functions to aws-services-provider."""

    def create_dot_env(self) -> Path:
        """Create the .env file in the aws-services-provider directory."""
        return common.env_file(env_path=PROVIDER_DIR)
