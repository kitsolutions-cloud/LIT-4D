import fire

from aws_services_provider import AwsServicesProvider
from email_provider import EmailProvider
from feature_flag_provider import FeatureFlagProvider
from mongodb_provider import MongodbProvider
from monitoring_provider import MonitoringProvider
from oauth_provider import OauthProvider
from sqldb_provider import SqldbProvider


class CLI(object):
    def __init__(self):
        self.aws_services_provider = AwsServicesProvider()
        self.email_provider = EmailProvider()
        self.feature_flag_provider = FeatureFlagProvider()
        self.mongodb_provider = MongodbProvider()
        self.monitoring_provider = MonitoringProvider()
        self.oauth_provider = OauthProvider()
        self.sqldb_provider = SqldbProvider()


if __name__ == "__main__":
    fire.Fire(CLI)
