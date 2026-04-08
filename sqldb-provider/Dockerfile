ARG PROVIDER_VERSION
FROM postgres:${PROVIDER_VERSION}
# SETUP

RUN apt-get update && apt-get install -y postgresql-17-documentdb

COPY init.sql /docker-entrypoint-initdb.d/
