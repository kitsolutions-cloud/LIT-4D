import common
import settings


class _MonitoringProviderAlloyFunctions(common.CommonProviderFunctions):
    """The available functions to alloy service."""
    _PROVIDER_DIR = settings.MAIN_DIR / 'monitoring-provider/alloy'
    _PROVIDER_IMAGE_VERSION_LABEL = "MONITORING_PROVIDER_ALLOY_IMAGE_VERSION"


class _MonitoringProviderGrafanaFunctions(common.CommonProviderFunctions):
    """The available functions to grafana service."""
    _PROVIDER_DIR = settings.MAIN_DIR / 'monitoring-provider/grafana'
    _PROVIDER_IMAGE_VERSION_LABEL = "MONITORING_PROVIDER_GRAFANA_IMAGE_VERSION"


class _MonitoringProviderLokiFunctions(common.CommonProviderFunctions):
    """The available functions to loki service."""
    _PROVIDER_DIR = settings.MAIN_DIR / 'monitoring-provider/loki'
    _PROVIDER_IMAGE_VERSION_LABEL = "MONITORING_PROVIDER_LOKI_IMAGE_VERSION"


class MonitoringProvider(common.CommonProviderFunctions):
    """A set of functions to monitoring-provider."""

    def __init__(self):
        self.alloy = _MonitoringProviderAlloyFunctions()
        self.grafana = _MonitoringProviderGrafanaFunctions()
        self.loki = _MonitoringProviderLokiFunctions()

    def dot_env(self, **kwargs):
        """Delegates .env configuration to all monitoring sub-services (alloy, grafana, loki)."""
        self.alloy.dot_env(**kwargs)
        self.grafana.dot_env(**kwargs)
        self.loki.dot_env(**kwargs)

    def config(self, **kwargs):
        """Delegates image version configuration to all monitoring sub-services (alloy, grafana, loki)."""
        self.alloy.config(**kwargs)
        self.grafana.config(**kwargs)
        self.loki.config(**kwargs)


functions = MonitoringProvider()
