import common
import settings

PROVIDER_DIR = settings.MAIN_DIR / 'monitoring-provider'


class _MonitoringProviderAlloy(object):
    """The available functions to alloy service."""

    def dot_env(self, create: bool = None) -> None:
        """
        Configurations about .env in the monitoring-provider/alloy.
            :arg create: Create a new .env file if it does not exist.
        """
        if create is not None and create == True:
            common.env_file(env_path=(PROVIDER_DIR / 'alloy'))
            print(f"{PROVIDER_DIR}/.env created.")
            return


class _MonitoringProviderGrafana(object):
    """The available functions to alloy service."""

    def dot_env(self, create: bool = None) -> None:
        """
        Configurations about .env in the monitoring-provider/grafana.
            :arg create: Create a new .env file if it does not exist.
        """
        if create is not None and create == True:
            common.env_file(env_path=(PROVIDER_DIR / 'grafana'))
            print(f"{PROVIDER_DIR}/.env created.")
            return


class _MonitoringProviderLoki(object):
    """The available functions to alloy service."""

    def dot_env(self, create: bool = None) -> None:
        """
        Configurations about .env in the monitoring-provider/loki.
            :arg create: Create a new .env file if it does not exist.
        """
        if create is not None and create == True:
            common.env_file(env_path=(PROVIDER_DIR / 'loki'))
            print(f"{PROVIDER_DIR}/.env created.")
            return


class MonitoringProvider(object):
    """A set of services provider functions to monitoring-provider."""

    def __init__(self):
        self.alloy = _MonitoringProviderAlloy()
        self.grafana = _MonitoringProviderGrafana()
        self.loki = _MonitoringProviderLoki()

    def create_dot_env(self):
        self.alloy.dot_env(create=True)
        self.grafana.dot_env(create=True)
        self.loki.dot_env(create=True)
