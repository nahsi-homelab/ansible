# HashiCorp Nomad

## Description
Installs and configures HashiCorp [Nomad](https://www.nomadproject.io/).

## Requirements
```sh
pip install hvac ansible-modules-hashivault
```

## Role Variables
See [defaults/main.yml](defaults/main.yml) for details and examples.

| name | type | description |
| ---- | ---- | ----------- |
| `nomad_config` | map | Nomad server confgiration |
| `nomad_client_config` | map | Nomad client confgiration |
| `nomad_vault_config` | map | Nomad Vault integration confgiration |
| `nomad_vault_init` | bool | when set to true will create/update Vault token |
| `nomad_dirs` | map | Nomad directories to create |
| `nomad_dir` | string | main Nomad dir, used in `nomad_dirs` |
| `nomad_version` | string | |
| `nomad_podman_version` | string | podman plugin version |

## Examples
Deploy Nomad server with Vault integration:
```ssh
ansible-playbook site.yml -e "target=nomad-server role=nomad nomad_vault_init=true"
```

### External Resources
- https://www.nomadproject.io/docs/configuration

### Author
Anatoly Laskaris
