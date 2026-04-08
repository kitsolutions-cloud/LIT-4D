import common
import settings


class MongodbProviderFunctions(common.CommonProviderFunctions):
    """A set of services provider functions to mongodb-provider."""
    PROVIDER_DIR = settings.MAIN_DIR / 'mongodb-provider'
    PROVIDER_IMAGE_VERSION_LABEL = "MONGODB_PROVIDER_IMAGE_VERSION"


functions = MongodbProviderFunctions()
