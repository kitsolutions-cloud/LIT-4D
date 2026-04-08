from pathlib import Path

from docker.models.containers import Container

import aws_services_provider
import common
import email_provider
import feature_flag_provider
import mongodb_provider
import monitoring_provider
import oauth_provider
import settings
import sqldb_provider


class RootFunctions(object):
    """Common functions for all providers or root management project directory."""

    def create_compose_dot_env(self) -> Path:
        """Create the .env file in the root directory to docker compose ARGS."""
        return common.dot_env_file(env_path=settings.MAIN_DIR)

    def create_default_providers_dot_env(self):
        """Create the providers .env files."""
        aws_services_provider.functions.dot_env(create=True)
        email_provider.functions.dot_env(create=True)
        feature_flag_provider.functions.dot_env(create=True)
        mongodb_provider.functions.dot_env(create=True)
        monitoring_provider.functions.dot_env(create=True)
        oauth_provider.functions.dot_env(create=True)
        sqldb_provider.functions.dot_env(create=True)

    def define_default_providers_image_versions(self):
        """Define the providers image versions to latest."""
        aws_services_provider.functions.config(image_version="latest")
        email_provider.functions.config(image_version="latest")
        feature_flag_provider.functions.config(image_version="latest")
        mongodb_provider.functions.config(image_version="latest")
        monitoring_provider.functions.config(image_version="latest")
        oauth_provider.functions.config(image_version="latest")
        sqldb_provider.functions.config(image_version="latest")

    def list_up_providers(self) -> list[Container]:
        """List all providers."""
        return common.list_up_providers()


functions = RootFunctions()
