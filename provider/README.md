# Provider CLI

CLI tool to manage all local development service providers. Each provider is a Docker-based service managed through environment variables and Docker Compose.

## Invocation

```bash
python -m provider <command> [arguments]
```

---

## Root Commands

### `init`

Initialize all providers after cloning the project. Creates `.env` files for every provider and sets default image versions to `latest`.

```bash
python -m provider init
```

> Run this only once after cloning. It is safe to re-run but will not overwrite existing `.env` values.

---

### `ps`

List all running provider containers with their health status.

```bash
python -m provider ps
```

**Output:** List of `(container_name, health_status)` tuples for containers labeled `project=lit-4d`.

---

## Provider Commands

All providers expose a common set of subcommands. Replace `<provider>` with one of:

| Provider | CLI key |
|---|---|
| AWS Services | `aws_services` |
| Email | `email` |
| Feature Flag | `feature_flag` |
| MongoDB | `mongodb` |
| Monitoring | `monitoring` |
| OAuth | `oauth` |
| SQL Database | `sqldb` |

---

### `<provider> dot_env [--create]`

Manage the `.env` file for a provider.

```bash
# Create the .env file if it does not exist
python -m provider <provider> dot_env --create
```

If a `.env.example` file exists in the provider directory, the new `.env` will be pre-populated with its values.

---

### `<provider> config [--image_version VERSION]`

Set the Docker image version/tag for a provider.

```bash
python -m provider <provider> config --image_version 1.2.3
python -m provider <provider> config --image_version latest
```

This writes the version to the root `.env` file under the provider's image version key (e.g., `SQLDB_PROVIDER_IMAGE_VERSION`).

---

## Provider-Specific Commands

### SQL Database (`sqldb`)

#### `sqldb install_sql_extension EXTENSION_NAME`

Install a PostgreSQL extension inside the running `sqldb-provider` container.

```bash
python -m provider sqldb install_sql_extension pg_trgm
python -m provider sqldb install_sql_extension uuid-ossp
```

The container must be running. If it is not available, an error is printed to stderr.

---

## Monitoring Provider

The monitoring provider manages three sub-services: **Alloy**, **Grafana**, and **Loki**. Each can be configured independently via its sub-namespace.

```bash
# Configure a specific sub-service
python -m provider monitoring alloy config --image_version 1.0.0
python -m provider monitoring grafana dot_env --create
python -m provider monitoring loki config --image_version 3.4.1
```

Top-level `dot_env` and `config` calls on `monitoring` delegate to all three sub-services:

```bash
# Applies to alloy, grafana, and loki simultaneously
python -m provider monitoring dot_env --create
python -m provider monitoring config --image_version latest
```

---

## Examples

```bash
# First-time setup
python -m provider init

# Check what's running
python -m provider ps

# Pin mongodb to a specific version
python -m provider mongodb config --image_version 7.0.5

# Create the oauth .env from its example file
python -m provider oauth dot_env --create

# Install a PostgreSQL extension
python -m provider sqldb install_sql_extension pg_stat_statements

# Set grafana image version independently
python -m provider monitoring grafana config --image_version 11.0.0
```
