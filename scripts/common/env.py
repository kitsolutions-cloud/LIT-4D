# DEPRECATED: This module is deprecated and will be removed in a future release.
# Use the `tasks` package instead: python -m tasks
from __future__ import annotations

import warnings
import shutil
from pathlib import Path


def copy_env(src: Path, dest: Path) -> None:
    """Copies src file to dest.

    .. deprecated::
        Use `tasks` package instead: python -m tasks
    """
    warnings.warn(
        "scripts.common.env.copy_env is deprecated. Use the `tasks` package instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    shutil.copyfile(src=src, dst=dest)
    print(f"Successfully copied {src} to {dest}")


def create_env(provider_dir: Path | str) -> None:
    """Creates a .env file from .env.example in the given provider directory.

    .. deprecated::
        Use `tasks` package instead: python -m tasks
    """
    warnings.warn(
        "scripts.common.env.create_env is deprecated. Use the `tasks` package instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    directory = Path(provider_dir)
    example_file = directory / ".env.example"
    env_file = directory / ".env"

    if example_file.exists():
        copy_env(src=example_file, dest=env_file)
    else:
        print(f"Error: {example_file} does not exist.")


def manage_env(provider_dir: Path | str) -> None:
    """Creates .env from .env.example only if .env does not already exist.

    .. deprecated::
        Use `tasks` package instead: python -m tasks
    """
    warnings.warn(
        "scripts.common.env.manage_env is deprecated. Use the `tasks` package instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    directory = Path(provider_dir)
    env_file = directory / ".env"

    if env_file.exists():
        print(f"Skipping: {env_file} already exists.")
    else:
        create_env(provider_dir=directory)
