# Key Vault Operations for AI Apps

Topic: Azure Key Vault
Tags: key-vault, secrets, azure, identity

## Key points
- Use managed identity; rotate secrets without redeploying app code.
- Separate vaults or RBAC scopes per environment (dev/stage/prod).
- Soft-delete + purge protection for production vaults.
- Compare vault configs across envs (tags, access policies/RBAC, network rules).
- Agents that "manage secrets" must never echo secret values — only names/versions/metadata.

## Clip notes
Reel covered: ops checklist before giving an agent Key Vault list/get permissions.
