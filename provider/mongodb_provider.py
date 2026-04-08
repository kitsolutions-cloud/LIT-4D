import common
import settings


class MongodbProviderFunctions(common.CommonProviderFunctions):
    """A set of functions to mongodb-provider."""
    _PROVIDER_DIR = settings.MAIN_DIR / 'mongodb-provider'
    _PROVIDER_IMAGE_VERSION_LABEL = "MONGODB_PROVIDER_IMAGE_VERSION"


functions = MongodbProviderFunctions()
