import argparse
import importlib
import sys
import os
from collections.abc import Callable

# Add the scripts directory to sys.path to allow imports from it
scripts_dir = os.path.dirname(os.path.abspath(__file__))
if scripts_dir not in sys.path:
    sys.path.insert(0, scripts_dir)

_PROVIDER_MODULES = [
    "aws_services_provider",
    "email_provider",
    "feature_flag_provider",
    "mongodb_provider",
    "monitoring_provider_grafana",
    "monitoring_provider_loki",
    "monitoring_provider_alloy",
    "oauth_provider",
    "sqldb_provider",
]

PROVIDERS: dict[str, dict[str, Callable[..., None]]] = {
    name: importlib.import_module(name).FUNCTIONS
    for name in _PROVIDER_MODULES
}


def main() -> None:
    """
    Main script for automating provider-related tasks.
    Example usage: python scripts/automations.py -p sqldb_provider -f create_env
    """
    parser = argparse.ArgumentParser(
        description="Automations main script to execute provider functions.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
  python scripts/automations.py -p aws_services_provider -f create_env
  python scripts/automations.py --provider sqldb-provider --function create_env
  python scripts/automations.py -f create_env
  python scripts/automations.py -p sqldb_provider -f change_version -v 15
  python scripts/automations.py -f change_version -v latest
"""
    )

    parser.add_argument(
        "-p", "--provider",
        required=False,
        help="The name of the provider script (e.g., aws_services_provider or aws-services-provider)."
    )
    parser.add_argument(
        "-f", "--function",
        required=True,
        help="The name of the function to execute from the provider script (e.g., create_env)."
    )
    parser.add_argument(
        "-v", "--version",
        required=False,
        help="The image version to set (used by change_version, e.g., latest, 16, 26.0.5)."
    )

    args = parser.parse_args()

    function_name: str = args.function

    if args.provider:
        # Normalize provider name (replace '-' with '_')
        provider_name: str = args.provider.replace("-", "_")

        if provider_name not in PROVIDERS:
            print(f"Error: Provider '{provider_name}' is not allowed or not implemented.")
            sys.exit(1)

        if function_name not in PROVIDERS[provider_name]:
            print(f"Error: Function '{function_name}' not found for provider '{provider_name}'.")
            sys.exit(1)

        try:
            func = PROVIDERS[provider_name][function_name]
            print(f"Running '{function_name}' for provider '{provider_name}'...")
            if args.version is not None:
                func(version=args.version)
            else:
                func()
        except Exception as e:
            print(f"An unexpected error occurred for provider '{provider_name}': {e}")
    else:
        found_at_least_one = False
        for provider_name, functions in PROVIDERS.items():
            if function_name in functions:
                found_at_least_one = True
                try:
                    print(f"Running '{function_name}' for provider '{provider_name}'...")
                    if args.version is not None:
                        functions[function_name](version=args.version)
                    else:
                        functions[function_name]()
                except Exception as e:
                    print(f"An unexpected error occurred for provider '{provider_name}': {e}")

        if not found_at_least_one:
            print(f"Error: Function '{function_name}' not found in any provider.")
            sys.exit(1)


if __name__ == "__main__":
    main()
