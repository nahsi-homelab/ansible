# HashiCorp Vault

## Description
Installs and configures HashiCorp [Vault](https://www.vaultproject.io).

### Role Variables
See [defaults/main.yml](defaults/main.yml) for details and examples.

| name | type | description |
| ---- | ---- | ----------- |
| vault_config| map | vault confgiration |
| vault_dirs | map | vault directories to create |
| vault_dir | string | main vault dir, used in `vault_dirs` |
| vault_version | string | |

### External Resources
- https://www.vaultproject.io/docs/configuration

### Author
Anatoly Laskaris
