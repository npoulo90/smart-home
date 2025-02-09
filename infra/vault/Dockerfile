# Use the official Vault image
FROM hashicorp/vault

# Copy the configuration file
COPY config/vault.hcl /vault/config/vault.hcl

# Set the command to run Vault
CMD ["server", "-dev"]
