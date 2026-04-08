import common
import settings


class FeatureFlagProviderFunctions(common.CommonProviderFunctions):
    """A set of services provider functions to feature-flag-provider."""
    PROVIDER_DIR = settings.MAIN_DIR / 'feature-flag-provider'
    PROVIDER_IMAGE_VERSION_LABEL = "FEATURE_FLAG_PROVIDER_IMAGE_VERSION"


functions = FeatureFlagProviderFunctions()
