import sys

import common
import settings


class SqldbProviderFunctions(common.CommonProviderFunctions):
    """A set of functions to sqldb-provider."""
    _PROVIDER_DIR = settings.MAIN_DIR / 'sqldb-provider'
    _PROVIDER_IMAGE_VERSION_LABEL = "SQLDB_PROVIDER_IMAGE_VERSION"
    _PROVIDER_CONTAINER_NAME = "sqldb-provider"

    def install_sql_extension(self, extension_name: str) -> None:
        """Install extensions in the sqldb-provider container."""
        container = self.get_provider_container()

        if container is None:
            print(f"{self._PROVIDER_CONTAINER_NAME} container not available.", file=sys.stderr)
            return

        sql_conf_file_path = self.get_data_folder_path() / 'postgresql.conf'

        print(f"Installing '{extension_name}' extension in {sql_conf_file_path}")


functions = SqldbProviderFunctions()
