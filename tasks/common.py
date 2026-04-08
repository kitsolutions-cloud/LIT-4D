from pathlib import Path

from dotenv import unset_key, set_key, dotenv_values

from cli import CLI


def env_file(env_path: Path) -> Path:
    """Create a .env file in the given directory, else
    if already exists return it, else
    if exists .env.example create a copy of it."""
    example_file = env_path / ".env.example"
    env_file = env_path / ".env"

    if env_file.exists():
        return env_file

    if example_file.exists():
        example_vars = dotenv_values(example_file)

        if len(example_vars.keys()) == 0:
            print(f"Created empty {env_file}")
            return env_file

        for key, value in example_vars.items():
            set_key(env_file, key, value or "")

        print(f"Created {env_file} from example")
    else:
        print(f"Created empty {env_file}")
        env_file.touch()

    return env_file


def set_env_var(env_path: Path, key: str, value: str) -> tuple[bool | None, str, str]:
    """Create an env variable in the given .env directory.
    If the .env does not exist, create a new one."""
    return set_key(env_file(env_path), key, value)


def remove_env_var(env_path: Path, key: str) -> tuple[bool | None, str]:
    """Remove an env variable from the given .env directory."""
    return unset_key(env_path, key)


cli = CLI()
