# LIT-4D

## Local Integration Tools 4 Devs

The OpenSource toolkit that every developer needs to build the integration between local projects and external providers during in development staging.

## Main functionality / Problem to solve

Solve a problem that everyone must face to start configurations within the service provider they want to use. Go through a step-by-step configuration, confirmation, validation and billing process... to finally check how the customer will receive the welcome email (SMT relays for example) from your application.

## Prerequisites

- [Docker 🐋👍🏼](https://docs.docker.com/engine/install/)

## Services & providers

### 📨 E-mail Provider with [maildev](https://github.com/maildev/maildev?tab=readme-ov-file)

```dotenv
host=localhost # or `email-provider` if you are connecting throught docker network
port=1025
sender|user=sender@email-provider.com
password=changeit
SSL=false
TLS=false

# Web client
webclient=http://localhost:1080
user=admin@email-provider.com
password=changeit
```

> [!NOTE]
>
> edit ./email-provider/.env for change or add more vars, as you prefer

---

### 🔐 OAuth2 provider with [keycloak](https://github.com/keycloak/keycloak?tab=readme-ov-file#open-source-identity-and-access-management)

```dotenv
# Keycloak Admin
helm_hostname=http://localhost:8180
admin_helm=http://localhost:8180/admin
admin_username=admin@oauth-provider.com
admin_password=changeit

# MyApp
default_roles=APP_USER,APP_MANAGER,APP_ADMIN,APP_OWNER
default_users=user@myapp.com,staff.user@myapp.com,manager.user@myapp.com,admin.user@myapp.com,owner.user@myapp.com
defailt_passwords=changeit # must be confirm account to activate them

# Account profile
myapp_account_profile=http://localhost:8180/realms/pyapp/account
```

Example to get token from client myapp realm client

```bash
curl --location 'http://localhost:8180/realms/myapp/protocol/openid-connect/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'client_id=myapp-client' \
--data-urlencode 'client_secret=...myapp realm > clients > myapp-client > secrets...' \
--data-urlencode 'grant_type=password' \
--data-urlencode 'username=user@myapp.com' \
--data-urlencode 'password=changeit'
```

> [!NOTE]
>
> Edit ./oauth-provider/.env for change the default vars, as you prefer
>
> Change the ./oauth-provider/helms/myapp.realm.json to add your custom configs for your necessities or create another one based on it.

---

### 📦 SQL database provider with [postgres](https://github.com/docker-library/docs/blob/master/postgres/README.md)

```dotenv
host=localhost # or `sqldb-provider` if you are connecting throught docker network
port=5432
user=postgres
password=Po$tgre5
default_db=myapp_db
```

> [!NOTE]
>
> edit ./sqldb-provider/.env for change the default vars, as you prefer
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
