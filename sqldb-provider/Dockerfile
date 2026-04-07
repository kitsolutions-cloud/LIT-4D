ARG PROVIDER_VERSION=latest
FROM postgres:${PROVIDER_VERSION}
# SETUP

COPY init.sql /docker-entrypoint-initdb.d/
