from pathlib import Path

import common
import settings

PROVIDER_DIR = settings.MAIN_DIR / 'monitoring-provider'


class _MonitoringProviderAlloy(object):
    """The available functions to alloy service."""

    def create_dot_env(self) -> Path:
        """Create the .env file in the monitoring-provider/alloy directory."""
        return common.env_file(env_path=PROVIDER_DIR / 'alloy')


class _MonitoringProviderGrafana(object):
    """The available functions to alloy service."""

    def create_dot_env(self) -> Path:
        """Create the .env file in the monitoring-provider/grafana directory."""
        return common.env_file(env_path=PROVIDER_DIR / 'grafana')


class _MonitoringProviderLoki(object):
    """The available functions to alloy service."""

    def create_dot_env(self) -> Path:
        """Create the .env file in the monitoring-provider/loki directory."""
        return common.env_file(env_path=PROVIDER_DIR / 'loki')


class MonitoringProvider(object):
    """A set of services provider functions to monitoring-provider."""

    def __init__(self):
        self.alloy = _MonitoringProviderAlloy()
        self.grafana = _MonitoringProviderGrafana()
        self.loki = _MonitoringProviderLoki()

    def create_dot_env(self):
        self.alloy.create_dot_env()
        self.grafana.create_dot_env()
        self.loki.create_dot_env()
