import common
import settings


class FeatureFlagProviderFunctions(common.CommonProviderFunctions):
    """A set of functions to feature-flag-provider."""
    _PROVIDER_DIR = settings.MAIN_DIR / 'feature-flag-provider'
    _PROVIDER_IMAGE_VERSION_LABEL = "FEATURE_FLAG_PROVIDER_IMAGE_VERSION"


functions = FeatureFlagProviderFunctions()
