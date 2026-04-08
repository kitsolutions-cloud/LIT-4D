import common
import settings


class OauthProviderFunctions(common.CommonProviderFunctions):
    """A set of services provider functions to oauth-provider."""
    PROVIDER_DIR = settings.MAIN_DIR / 'oauth-provider'
    PROVIDER_IMAGE_VERSION_LABEL = "OAUTH_PROVIDER_IMAGE_VERSION"


functions = OauthProviderFunctions()
