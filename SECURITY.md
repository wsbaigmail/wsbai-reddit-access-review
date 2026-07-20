# Security

- OAuth credentials are stored outside the repository in an encrypted local or cloud secret store.
- Secrets are never committed, logged, emailed, or included in screenshots.
- The connector uses least-privilege read-only access.
- Network requests are logged with credential redaction.
- Dataset fingerprints and provenance manifests detect unauthorized changes.
- The service fails closed when approval, credentials, rate-limit state, or source integrity is uncertain.
- Production deployment will use per-environment credentials, audit logs, backups, and key rotation.
