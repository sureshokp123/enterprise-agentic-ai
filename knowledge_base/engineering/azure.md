# Azure Deployment Guidelines

## Services Used

Azure OpenAI

Azure App Service

Azure Container Registry

Azure Storage

Azure Key Vault

Azure PostgreSQL

---

## Deployment Process

Developer

↓

GitHub

↓

GitHub Actions

↓

Azure Container Registry

↓

Azure App Service

---

## Secrets

Store secrets inside Azure Key Vault.

Never commit API keys to GitHub.

---

## Monitoring

Enable:

Application Insights

Log Analytics

Azure Monitor

---

## Scaling

App Service supports automatic scaling.

Scaling rules should be configured for CPU and memory usage.

---

## Security

Use Managed Identity whenever possible.

Enable HTTPS only.

---

## Backups

Enable scheduled backups for production applications.