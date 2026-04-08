# 🔐 OAuth2 Provider (Keycloak)

**Keycloak** is an open-source identity and access management solution. This project includes a pre-configured realm and
integration with SNS/SQS for event-driven architectures.

## ⚙️ Configuration

- **Admin Console:** [http://localhost:8180/admin](http://localhost:8180/admin)
- **Port:** `8180`
- **Management Port:** `9101`
- **Docker Network Host:** `oauth-provider`

### 📂 Volumes and Files

- `./providers`: Custom Keycloak providers (JAR files).
- `./helms`: Realm configuration files for import (e.g., `my-app.realm.json`).

> [!tip]
> Recommended see this [keycloak-json-schema](https://github.com/jirutka/keycloak-json-schema) to better understand the
> structure of the JSON healm files.

### 🔑 Environment variables (.env)

The configuration is managed by the `.env` file in this directory.

| Variable                       | Description                    | Default                                                    |
|--------------------------------|--------------------------------|------------------------------------------------------------|
| `KC_BOOTSTRAP_ADMIN_USERNAME`  | Keycloak admin username        | `admin@oauth-provider.com`                                 |
| `KC_BOOTSTRAP_ADMIN_PASSWORD`  | Keycloak admin password        | `changeit`                                                 |
| `KC_DB`                        | Database vendor                | `postgres`                                                 |
| `KC_DB_NAME`                   | Database name                  | `keycloak_db`                                              |
| `KC_DB_URL`                    | JDBC database URL              | `jdbc:postgresql://sqldb-provider:5432/keycloak_db`        |
| `KC_HTTP_PORT`                 | Main HTTP port                 | `8180`                                                     |
| `KC_SNS_EVENT_TOPIC_ARN`       | SNS topic ARN for events       | `arn:aws:sns:sa-east-1:000000000000:keycloak-events`       |
| `KC_SNS_ADMIN_EVENT_TOPIC_ARN` | SNS topic ARN for admin events | `arn:aws:sns:sa-east-1:000000000000:keycloak-admin-events` |

---

## 🛠 Usage

### Get Token Example

```bash
curl --location 'http://localhost:8180/realms/my-app/protocol/openid-connect/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'client_id=my-app-client' \
--data-urlencode 'client_secret=...my-app realm > clients > my-app-client > secrets...' \
--data-urlencode 'grant_type=password' \
--data-urlencode 'username=user@my-app.com' \
--data-urlencode 'password=changeit'
```

---

> [!TIP]
> Custom configs can be added to `./helms/my-app.realm.json`. You can
> also [import/export realms](https://www.keycloak.org/server/importExport#_importing_a_realm_from_a_file) as needed.
