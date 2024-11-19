#!/bin/sh
awslocal sns create-topic --name keycloak-events --region sa-east-1 --output table | cat
echo "\n"
awslocal sqs create-queue --queue-name keycloak-events-sqs --region sa-east-1 --output table | cat
echo "\n"
awslocal sns subscribe --topic-arn arn:aws:sns:sa-east-1:000000000000:keycloak-events --region sa-east-1 --protocol sqs --notification-endpoint arn:aws:sqs:sa-east-1:000000000000:keycloak-events-sqs --output table | cat
echo "\n"

awslocal sns create-topic --name keycloak-admin-events --region sa-east-1 --output table | cat
echo "\n"
awslocal sqs create-queue --queue-name keycloak-admin-events-sqs --region sa-east-1 --output table | cat
echo "\n"
awslocal sns subscribe --topic-arn arn:aws:sns:sa-east-1:000000000000:keycloak-admin-events --region sa-east-1 --protocol sqs --notification-endpoint arn:aws:sqs:sa-east-1:000000000000:keycloak-admin-events-sqs --output table | cat
echo "\n"