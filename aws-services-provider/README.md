# ☁️ AWS Services Provider (LocalStack)

**LocalStack** provides a fully functional local AWS cloud stack. It is pre-configured to support SNS and SQS, including specific topics for Keycloak events.

## ⚙️ Configuration

- **Edge Port:** `4566`
- **Docker Network Host:** `aws-services-provider`
- **Default Region:** `sa-east-1`

### 🔑 Environment variables (.env)

The configuration is managed by the `.env` file in this directory.

| Variable | Description | Default |
|----------|-------------|---------|
| `SERVICES` | List of AWS services to enable | `sns,sqs` |
| `AWS_DEFAULT_REGION` | Default AWS region | `sa-east-1` |
| `AWS_ACCESS_KEY_ID` | Mocked access key ID | `access-key` |
| `AWS_SECRET_ACCESS_KEY` | Mocked secret access key | `secret-access-key` |

---

## 🛠 Setup

### 1. Resource Initialization

Initial resources (topics/queues) are created via the scripts in the `./ready.d/` directory.

Ensure the scripts have executable permissions:

```bash
chmod +x ./aws-services-provider/ready.d/*
```

---

> [!TIP]
> Use the [AWS CLI](https://aws.amazon.com/cli/) or [LocalStack's CLI](https://github.com/localstack/localstack-cli) to interact with the services locally:
> `aws --endpoint-url=http://localhost:4566 sns list-topics`
