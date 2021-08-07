# vault

>This role installs and configures [Vault](https://www.vaultproject.io).

## Role Variables

| variable              | description                                         |
|-----------------------|-----------------------------------------------------|
| `vault_version`      | vault version to use                               |
| `vault_config`       | main vault configuration                           |
| `vault_service`      | vault unitfile                                     |
| `vault_configs`      | map of vault override configs                      |
| `vault_dirs_overlay` | map of directories to create combined with defaults |

See [defaults/](defaults/) for details and examples.

## Tags
* `configuration` - update Vault unitfile and main config
* `configs` - sync Vault configs

## Author
* **Anatoly Laskaris** - [nahsi](https://github.com/nahsi)
