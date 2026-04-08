import common
import settings


class OauthProviderFunctions(common.CommonProviderFunctions):
    """A set of functions to oauth-provider."""
    _PROVIDER_DIR = settings.MAIN_DIR / 'oauth-provider'
    _PROVIDER_IMAGE_VERSION_LABEL = "OAUTH_PROVIDER_IMAGE_VERSION"


functions = OauthProviderFunctions()
