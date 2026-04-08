import common
import settings


class SqldbProviderFunctions(common.CommonProviderFunctions):
    """A set of services provider functions to sqldb-provider."""
    PROVIDER_DIR = settings.MAIN_DIR / 'sqldb-provider'
    PROVIDER_IMAGE_VERSION_LABEL = "SQLDB_PROVIDER_IMAGE_VERSION"


functions = SqldbProviderFunctions()
