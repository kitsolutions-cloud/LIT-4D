from pathlib import Path

from docker import from_env
from docker.models.containers import Container
from dotenv import unset_key, set_key, dotenv_values

from cli import CLI

docker_client = from_env()
cli = CLI()


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
