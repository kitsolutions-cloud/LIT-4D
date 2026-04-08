import common
import settings


class EmailProviderFunctions(common.CommonProviderFunctions):
    """A set of functions to email-provider."""
    _PROVIDER_DIR = settings.MAIN_DIR / 'email-provider'
    _PROVIDER_IMAGE_VERSION_LABEL = "EMAIL_PROVIDER_IMAGE_VERSION"


functions = EmailProviderFunctions()
