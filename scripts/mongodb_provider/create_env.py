import shutil
from pathlib import Path

def create_env():
    """
    Creates a .env file based on .env.example for the mongodb-provider.
    """
    provider_dir = Path("mongodb-provider")
    example_file = provider_dir / ".env.example"
    env_file = provider_dir / ".env"
    
    if example_file.exists():
        shutil.copyfile(example_file, env_file)
        print(f"Successfully created {env_file}")
    else:
        print(f"Error: {example_file} does not exist.")
