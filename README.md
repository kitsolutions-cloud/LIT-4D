# LFIS4D

Local Foundation Integration Services 4 Devs

The OpenSource toolkit that every developer needs to build the integration between local projects and external providers during in development staging.

## Main functionality / Problem to solve

Solve a problem that everyone must face to start configurations within the service provider they want to use. Go through a step-by-step configuration, confirmation, validation and billing process... to finally check how the customer will receive the welcome email (SMT relays for example) from your application.

## Prerequisites

- [Docker 🐋👍🏼](https://docs.docker.com/engine/install/)

## Supported services & providers

- [x] 📧 Mailing Provider with [maildev](https://github.com/maildev/maildev?tab=readme-ov-file)

## Initial setup

Only setup the declaration of environment variables inside of *.env services files, if don't, they wont to wake up

```dotenv
# .env
MAILING_PROVIDER_ENABLE=true
# and goes on...
```
Run `docker compose up -d` and check the ports available

## Future plans

### Services to add

- OAuth2 provider with [keycloak](https://github.com/keycloak/keycloak?tab=readme-ov-file)
- SQL database provider with [postgres](https://github.com/docker-library/docs/blob/master/postgres/README.md)
- Storage service (like s3) with [minio](https://min.io/docs/minio/container/index.html#quickstart-for-containers)
- And much more... 👀

### Creating .sh scripts for automation

- Automation for create .env files based prompting and customizing then with prompt commands

### And going on 🚀

Enjoy ;)
