# 📨 E-mail Provider (MailDev)

**MailDev** is an SMTP server and Web interface to view emails sent during development. It captures all emails and displays them in a web UI, preventing them from being sent to real addresses.

## ⚙️ Configuration

- **Web Client (UI):** [http://localhost:1080](http://localhost:1080)
- **SMTP Server:** `localhost:1025`
- **Docker Network Host:** `email-provider`

### 🔑 Environment variables (.env)

The configuration is managed by the `.env` file in this directory.

| Variable | Description | Default |
|----------|-------------|---------|
| `MAILDEV_WEB_USER` | Username for the Web UI | `admin@email-provider.com` |
| `MAILDEV_WEB_PASS` | Password for the Web UI | `changeit` |
| `MAILDEV_INCOMING_USER` | SMTP authentication username | `sender@email-provider.com` |
| `MAILDEV_INCOMING_PASS` | SMTP authentication password | `changeit` |

---

> [!NOTE]
> You can edit `.env` to change credentials or add more variables.
