# 🍃 NoSQL Database Provider (MongoDB)

**MongoDB** is used as the NoSQL database, primarily for the GrowthBook feature flag service in this setup.

## ⚙️ Configuration

- **Port:** `27017`
- **Docker Network Host:** `mongodb-provider`

### 🔑 Environment variables (.env)

The configuration is managed by the `.env` file in this directory.

| Variable                     | Description                 | Default    |
|------------------------------|-----------------------------|------------|
| `MONGO_INITDB_ROOT_USERNAME` | Root administrator username | `root`     |
| `MONGO_INITDB_ROOT_PASSWORD` | Root administrator password | `change1t` |

---

> [!NOTE]
> MongoDB data is persisted in the `./.data/db` directory.
