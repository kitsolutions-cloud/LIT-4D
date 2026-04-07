import argparse
import sys
import os

# Add the scripts directory to sys.path to allow imports from it
scripts_dir = os.path.dirname(os.path.abspath(__file__))
if scripts_dir not in sys.path:
    sys.path.insert(0, scripts_dir)

# Import all provider modules
import aws_services_provider.create_env as aws_services_provider_create_env
import aws_services_provider.change_version as aws_services_provider_change_version
import email_provider.create_env as email_provider_create_env
import email_provider.change_version as email_provider_change_version
import feature_flag_provider.create_env as feature_flag_provider_create_env
import feature_flag_provider.change_version as feature_flag_provider_change_version
import mongodb_provider.create_env as mongodb_provider_create_env
import mongodb_provider.change_version as mongodb_provider_change_version
import monitoring_provider_grafana.create_env as monitoring_provider_grafana_create_env
import monitoring_provider_grafana.change_version as monitoring_provider_grafana_change_version
import monitoring_provider_loki.create_env as monitoring_provider_loki_create_env
import monitoring_provider_loki.change_version as monitoring_provider_loki_change_version
import monitoring_provider_alloy.create_env as monitoring_provider_alloy_create_env
import monitoring_provider_alloy.change_version as monitoring_provider_alloy_change_version
import oauth_provider.create_env as oauth_provider_create_env
import oauth_provider.change_version as oauth_provider_change_version
import sqldb_provider.create_env as sqldb_provider_create_env
import sqldb_provider.change_version as sqldb_provider_change_version

# Fixed function mapping for providers
PROVIDERS = {
    "aws_services_provider": {
        "create_env": aws_services_provider_create_env.create_env,
        "change_version": aws_services_provider_change_version.change_version,
    },
    "email_provider": {
        "create_env": email_provider_create_env.create_env,
        "change_version": email_provider_change_version.change_version,
    },
    "feature_flag_provider": {
        "create_env": feature_flag_provider_create_env.create_env,
        "change_version": feature_flag_provider_change_version.change_version,
    },
    "mongodb_provider": {
        "create_env": mongodb_provider_create_env.create_env,
        "change_version": mongodb_provider_change_version.change_version,
    },
    "monitoring_provider_grafana": {
        "create_env": monitoring_provider_grafana_create_env.create_env,
        "change_version": monitoring_provider_grafana_change_version.change_version,
    },
    "monitoring_provider_loki": {
        "create_env": monitoring_provider_loki_create_env.create_env,
        "change_version": monitoring_provider_loki_change_version.change_version,
    },
    "monitoring_provider_alloy": {
        "create_env": monitoring_provider_alloy_create_env.create_env,
        "change_version": monitoring_provider_alloy_change_version.change_version,
    },
    "oauth_provider": {
        "create_env": oauth_provider_create_env.create_env,
        "change_version": oauth_provider_change_version.change_version,
    },
    "sqldb_provider": {
        "create_env": sqldb_provider_create_env.create_env,
        "change_version": sqldb_provider_change_version.change_version,
    },
}

def main():
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

    function_name = args.function
    
    if args.provider:
        # Normalize provider name (replace '-' with '_')
        provider_name = args.provider.replace("-", "_")

        # Validate provider name exists in the allowed list
        if provider_name not in PROVIDERS:
            print(f"Error: Provider '{provider_name}' is not allowed or not implemented.")
            sys.exit(1)

        # Validate function name exists for the provider
        if function_name not in PROVIDERS[provider_name]:
            print(f"Error: Function '{function_name}' not found for provider '{provider_name}'.")
            sys.exit(1)

        try:
            # Call the fixed function directly from the mapping
            func = PROVIDERS[provider_name][function_name]
            print(f"Running '{function_name}' for provider '{provider_name}'...")
            if args.version is not None:
                func(args.version)
            else:
                func()
        except Exception as e:
            print(f"An unexpected error occurred for provider '{provider_name}': {e}")
    else:
        # Run for all providers that have the function
        found_at_least_one = False
        for provider_name, functions in PROVIDERS.items():
            if function_name in functions:
                found_at_least_one = True
                try:
                    print(f"Running '{function_name}' for provider '{provider_name}'...")
                    if args.version is not None:
                        functions[function_name](args.version)
                    else:
                        functions[function_name]()
                except Exception as e:
                    print(f"An unexpected error occurred for provider '{provider_name}': {e}")
        
        if not found_at_least_one:
            print(f"Error: Function '{function_name}' not found in any provider.")
            sys.exit(1)

if __name__ == "__main__":
    main()
