import aws_services_provider
import email_provider
import feature_flag_provider
import mongodb_provider
import monitoring_provider
import oauth_provider
import root_functions
import sqldb_provider


class CLI(object):
    """Common CLI for all providers functions."""

    def __init__(self):
        self.aws_services = aws_services_provider.functions
        self.email = email_provider.functions
        self.feature_flag = feature_flag_provider.functions
        self.mongodb = mongodb_provider.functions
        self.monitoring = monitoring_provider.functions
        self.oauth = oauth_provider.functions
        self.sqldb = sqldb_provider.functions
        self._root = root_functions.functions

    def init(self):
        """Start the scripts to initialize the providers configs."""

        self._root.create_compose_dot_env()
        self._root.create_default_providers_dot_env()
        self._root.define_default_providers_image_versions()

    def list_up_providers(self):
        """List all providers."""
        return self._root.list_up_providers()


cli = CLI()
