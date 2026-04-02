# LIT-4D (Local Integration Tools 4 Devs)

The OpenSource toolkit that every developer needs to build the integration between local projects and external providers during in development staging.

## Main functionality / Problem to solve

LIT-4D simplifies the process of setting up local versions of common cloud and infrastructure services. Instead of going through complex configuration, confirmation, validation, and billing processes with real cloud providers, you can use these local tools to test your integrations immediately.

For example, you can:
- Check how customers will receive welcome emails using a local SMTP relay (MailDev).
- Manage identities and permissions locally (Keycloak).
- Emulate AWS services like SNS and SQS (LocalStack).
- Manage feature flags without an external account (GrowthBook).
- Monitor logs and metrics with a full observability stack (Grafana, Loki, Promtail).

---

## Prerequisites

- [Docker 🐋👍🏼](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)

---

## Services & Providers

Detailed configuration for each provider can be found in their respective directories.

- [📨 E-mail Provider (MailDev)](./email-provider/README.md)
- [🔐 OAuth2 Provider (Keycloak)](./oauth-provider/README.md)
- [📦 SQL Database Provider (PostgreSQL & Adminer)](./sqldb-provider/README.md)
- [🍃 NoSQL Database Provider (MongoDB)](./mongodb-provider/README.md)
- [☁️ AWS Services Provider (LocalStack)](./aws-services-provider/README.md)
- [🚩 Feature Flag Provider (GrowthBook)](./feature-flag-provider/README.md)
- [📊 Monitoring Provider (Grafana Stack)](./monitoring-provider/README.md)

---

## Initial Setup

1. Configure environment variables in the respective provider directories (e.g., `./email-provider/.env`) if needed.
2. Build and start the services:
   ```bash
   docker compose up -d
   ```
3. Verify the ports are available and services are running.

---

## Future plans

### Services to add
- [ ] ☝🏼 Reverse proxy with [traefik](https://github.com/traefik/traefik?tab=readme-ov-file#documentation)
- [ ] ☝🏼 Storage service (like s3) with [minio](https://min.io/docs/minio/container/index.html#quickstart-for-containers)
- [ ] ☝🏼 And much more... 👀

### Automations
- [ ] 💡 Create unique .env file based on their providers
- [ ] 💡 Script for create databases at runtime
- [ ] 💡 Script for creating custom helms

---

### And going on 🚀

Enjoy ;)
