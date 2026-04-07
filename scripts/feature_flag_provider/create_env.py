from common.env import create_env as _create_env


def create_env() -> None:
    _create_env(provider_dir="feature-flag-provider")
