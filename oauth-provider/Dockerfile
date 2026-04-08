ARG PROVIDER_VERSION
FROM quay.io/keycloak/keycloak:${PROVIDER_VERSION} AS builder

ENV KC_DB=postgres
ENV KC_METRICS_ENABLED=true
ENV KC_HEALTH_ENABLED=true

WORKDIR /opt/keycloak

ADD --chown=keycloak:keycloak --chmod=744 https://github.com/moparisthebest/static-curl/releases/download/v8.17.0/curl-amd64 ./static-curl

RUN mv static-curl /opt/keycloak/bin/static-curl

RUN /opt/keycloak/bin/kc.sh build

FROM quay.io/keycloak/keycloak:${PROVIDER_VERSION}

COPY --from=builder /opt/keycloak/ /opt/keycloak/

ENTRYPOINT ["/opt/keycloak/bin/kc.sh"]
