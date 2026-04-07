import re
from pathlib import Path

def change_version(version: str = "26.0.5"):
    """
    Updates OAUTH_PROVIDER_IMAGE_VERSION in the root .env file.
    """
    env_file = Path(".env")

    if not env_file.exists():
        print(f"Error: {env_file} does not exist.")
        return

    content = env_file.read_text()
    updated = re.sub(
        r"^(OAUTH_PROVIDER_IMAGE_VERSION=).*",
        rf"\g<1>{version}",
        content,
        flags=re.MULTILINE
    )
    env_file.write_text(updated)
    print(f"Successfully updated OAUTH_PROVIDER_IMAGE_VERSION to '{version}' in {env_file}")
