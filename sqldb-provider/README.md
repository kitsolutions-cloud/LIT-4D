# 📦 SQL Database Provider (PostgreSQL)

**PostgreSQL** is the primary relational database. This service also includes **Adminer** as a web-based database
management tool.

## ⚙️ Configuration

- **Postgres Port:** `5432`
- **Adminer (Web UI):** [http://localhost:5433](http://localhost:5433)
- **Docker Network Host:** `sqldb-provider`

### 🔑 Environment variables (.env)

The configuration is managed by the `.env` file in this directory.

| Variable            | Description                     | Default     |
|---------------------|---------------------------------|-------------|
| `POSTGRES_DB`       | Name of the primary database    | `my-app_db` |
| `POSTGRES_USER`     | Database administrator username | `postgres`  |
| `POSTGRES_PASSWORD` | Database administrator password | `P@stgre5`  |
| `POSTGRES_PORT`     | PostgreSQL internal port        | `5432`      |

### 📂 Initial Data

- `init.sql`: SQL scripts that run on the first startup to initialize the database (e.g., creating the `keycloak_db`).

---

> [!TIP]
> **Adminer** is pre-configured with the `pepa-linha-dark` design. Access it to manage your databases through a
> user-friendly interface.
