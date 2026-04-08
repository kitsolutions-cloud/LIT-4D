import common
import settings


class SqldbProviderFunctions(common.CommonProviderFunctions):
    """A set of functions to sqldb-provider."""
    _PROVIDER_DIR = settings.MAIN_DIR / 'sqldb-provider'
    _PROVIDER_IMAGE_VERSION_LABEL = "SQLDB_PROVIDER_IMAGE_VERSION"


functions = SqldbProviderFunctions()
