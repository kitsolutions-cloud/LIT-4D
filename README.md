# LFIS4D

Local Foundation Integration Services 4 Devs

The OpenSource toolkit that every developer needs to build the integration between local projects and external providers during in development staging.

## Main functionality / Problem to solve

Solve a problem that everyone must face to start configurations within the service provider they want to use. Go through a step-by-step configuration, confirmation, validation and billing process... to finally check how the customer will receive the welcome email (SMT relays for example) from your application.

## Prerequisites

- [Docker 🐋👍🏼](https://docs.docker.com/engine/install/)

## Services & providers

### 📨 Mailing Provider with [maildev](https://github.com/maildev/maildev?tab=readme-ov-file)

Accessible on ports 1025 & [1080](http://localhost:1080)

SMTP connection for configure client

```dotenv
host=localhost
port=1025
sender|user=mail.sender@test.com
password=changeit
SSL=false
TLS=false
```

Web client

```dotenv
webclient=http://localhost:1080
user=mail.admin@test.com
password=changeit
```

> [!NOTE]
>
> edit ./mailing_provider/.env for change the default vars, as you prefer
---

### 🔐 OAuth2 provider with [keycloak](https://github.com/keycloak/keycloak?tab=readme-ov-file#open-source-identity-and-access-management)

```dotenv
```

> [!NOTE]
>
> edit ./oauth_provider/.env for change the default vars, as you prefer
---

### 📦 SQL database provider with [postgres](https://github.com/docker-library/docs/blob/master/postgres/README.md)

```dotenv
host=localhost
port=5432
user=postgres
password=d59b44d359cbd2e55cb76f2381a4b4a45560a8df
default_db=lfis4d
```

> [!NOTE]
>
> edit ./sqldb_provider/.env for change the default vars, as you prefer
>
> For development porpuoses, access [localhost:5433](http://localhost:5433) to access chat2db with default credentials below login form.
---

## Initial setup

Only setup the declaration of environment variables inside of .[provider].env services files

Run `docker compose up -d` and check the ports available

## Future plans

### Services to add

☝🏼 Reverse proxy with [traefik](https://github.com/traefik/traefik?tab=readme-ov-file#documentation)

☝🏼 Storage service (like s3) with [minio](https://min.io/docs/minio/container/index.html#quickstart-for-containers)

☝🏼 And much more... 👀

### Automations

💡 Create unique .env file based on their providers (idea)
💡 Script for create databases at runtime
💡 Script for creating custom healms

### And going on 🚀

Enjoy ;)
