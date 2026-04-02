# 📊 Monitoring Provider (Grafana Stack)

A full observability stack using **Loki** for log aggregation, **Promtail** for log shipping, and **Grafana** for visualization.

## ⚙️ Configuration

- **Grafana Web UI:** [http://localhost:3000](http://localhost:3000)
- **Loki API Port:** `3100`
- **Promtail Port:** `9080`

### 🛠 Services

- **Grafana:** Visualization and dashboards. Access it with anonymous admin access enabled by default.
  - Config: `./grafana/datasource.yaml`
  - Data: `./grafana/.data`
- **Loki:** Log aggregation system.
  - Data: `./loki/.data`
- **Promtail:** Scrapes logs from `/var/log/` (mapped to `./promtail/app-logs/`) and pushes to Loki.
  - Config: `./promtail/config.yaml`
  - Logs: `./promtail/app-logs/`

### 🔑 Environment variables (.env)

Managed by the `.env` file in `./grafana/`.

| Variable | Description | Default |
|----------|-------------|---------|
| `GF_PATHS_PROVISIONING` | Path to Grafana provisioning files | `/etc/grafana/provisioning` |
| `GF_AUTH_ANONYMOUS_ORG_ROLE` | Role for anonymous users | `Admin` |
| `GF_AUTH_ANONYMOUS_ENABLED` | Enable anonymous access | `true` |

---

> [!WARNING]
> **GrowthBook** and **Grafana Stack** share the same default ports (3000/3100). If you need to run both simultaneously, you must change the port mappings in `compose.override.yml`.
