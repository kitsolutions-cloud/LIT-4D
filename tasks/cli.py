from aws_services_provider import AwsServicesProvider
from email_provider import EmailProvider
from feature_flag_provider import FeatureFlagProvider
from mongodb_provider import MongodbProvider
from monitoring_provider import MonitoringProvider
from oauth_provider import OauthProvider
from root_functions import RootFunctions
from sqldb_provider import SqldbProvider


class CLI(object):
    """Common CLI for all providers functions."""

    def __init__(self):
        self.aws_services_provider = AwsServicesProvider()
        self.email_provider = EmailProvider()
        self.feature_flag_provider = FeatureFlagProvider()
        self.mongodb_provider = MongodbProvider()
        self.monitoring_provider = MonitoringProvider()
        self.oauth_provider = OauthProvider()
        self.sqldb_provider = SqldbProvider()
        self.root = RootFunctions()

    def init(self):
        """Start the scripts to initialize the providers configs."""
        self.aws_services_provider.dot_env(create=True)
        self.email_provider.dot_env(create=True)
        self.feature_flag_provider.dot_env()
        self.mongodb_provider.dot_env()
        self.monitoring_provider.create_dot_env()
        self.oauth_provider.dot_env()
        self.sqldb_provider.dot_env()

        self.root.create_dot_env_compose()
        self.root.define_default_provider_versions()
