from pathlib import Path

from docker import from_env
from docker.models.containers import Container
from dotenv import unset_key, set_key, dotenv_values

import settings

docker_client = from_env()


def env_file(env_path: Path) -> Path:
    """Create a .env file in the given directory, else
    if already exists return it, else
    if exists .env.example create a copy of it."""
    example_file_path = env_path / ".env.example"
    env_file_path = env_path / ".env"

    if env_file_path.exists():
        return env_file_path

    if example_file_path.exists():
        example_vars = dotenv_values(example_file_path)

        if len(example_vars.keys()) == 0:
            print(f"Created empty {env_file_path}")
            return env_file_path

        for key, value in example_vars.items():
            set_key(env_file_path, key, str(value or ""))

        print(f"Created {env_file_path} from example")
    else:
        print(f"Created empty {env_file_path}")
        env_file_path.touch()

    return env_file_path


def set_env_var(env_path: Path, key: str, value: str | int | bool) -> tuple[bool | None, str, str]:
    """Create an env variable in the given .env directory.
    If the .env does not exist, create a new one."""
    return set_key(env_file(env_path), key, str(value))


def remove_env_var(env_path: Path, key: str) -> tuple[bool | None, str]:
    """Remove an env variable from the given .env directory."""
    return unset_key(env_path, key)


def list_up_providers() -> list[Container]:
    """List the active providers from docker."""
    containers: list[Container] = docker_client.containers.list(filters={"label": "project=lit-4d"})
    return containers


class CommonProviderFunctions(object):
    """Common functions for all providers."""
    PROVIDER_DIR: Path = None
    PROVIDER_IMAGE_VERSION_LABEL: str = None

    def dot_env(self, create: bool = None) -> None:
        """
        Configurations about .env in the provider path.
            :arg create: Create a new .env file if it does not exist.
        """
        if self.PROVIDER_DIR is None:
            raise Exception("PROVIDER_DIR is not defined.")

        if create is not None and create == True:
            env_file(env_path=self.PROVIDER_DIR)
            print(f"{self.PROVIDER_DIR}/.env created.")
            return

    def config(self, image_version: str = None):
        """
        Configure provider settings.
            :arg image_version: The version of the provider image to use.
        """
        if self.PROVIDER_IMAGE_VERSION_LABEL is None:
            raise Exception("PROVIDER_IMAGE_VERSION_LABEL is not defined.")

        if image_version is not None:
            set_env_var(
                env_path=settings.MAIN_DIR,
                key=self.PROVIDER_IMAGE_VERSION_LABEL,
                value=image_version
            )
            print(f"{self.PROVIDER_IMAGE_VERSION_LABEL} set to {image_version}.")
