ARG PROVIDER_VERSION=latest
FROM grafana/alloy:${PROVIDER_VERSION}

RUN apt-get update && apt-get install -y curl

RUN rm -rf /var/lib/apt/lists/*