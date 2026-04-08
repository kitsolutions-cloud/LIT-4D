import common
import settings


class EmailProviderFunctions(common.CommonProviderFunctions):
    """A set of services provider functions to email-provider."""
    PROVIDER_DIR = settings.MAIN_DIR / 'email-provider'
    PROVIDER_IMAGE_VERSION_LABEL = "EMAIL_PROVIDER_IMAGE_VERSION"


functions = EmailProviderFunctions()
