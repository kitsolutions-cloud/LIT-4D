import common
import settings


class AwsServicesProviderFunctions(common.CommonProviderFunctions):
    """A set of services provider functions to aws-services-provider."""
    PROVIDER_DIR = settings.MAIN_DIR / 'aws-services-provider'
    PROVIDER_IMAGE_VERSION_LABEL = "AWS_SERVICES_PROVIDER_IMAGE_VERSION"


functions = AwsServicesProviderFunctions()
