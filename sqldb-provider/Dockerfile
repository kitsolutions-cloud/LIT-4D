ARG PROVIDER_VERSION
FROM postgres:${PROVIDER_VERSION}
# SETUP

COPY init.sql /docker-entrypoint-initdb.d/
