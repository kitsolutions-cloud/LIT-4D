# 🚩 Feature Flag Provider (GrowthBook)

**GrowthBook** is an open-source platform for feature flags and A/B testing. It uses MongoDB to store its configurations.

## ⚙️ Configuration

- **Web UI:** [http://localhost:3000](http://localhost:3000)
- **API Port:** `3100`
- **Docker Network Host:** `feature-flag-provider`

### 🔑 Environment variables (.env)

The configuration is managed by the `.env` file in this directory.

| Variable | Description | Default |
|----------|-------------|---------|
| `MONGODB_URI` | Connection string for MongoDB | `mongodb://root:change1t@mongodb-provider:27017/growthbook?authSource=admin` |

---

> [!WARNING]
> **GrowthBook** and **Grafana Stack** share the same default ports (3000/3100). If you need to run both simultaneously, you must change the port mappings in `compose.override.yml`.
