# Vault Agent

## Description
Install and configure Vault Agent.

### Role Variables
See [defaults/main.yml](defaults/main.yml) for details and examples.

| name | type | description |
| ---- | ---- | ----------- |
| vault_agent_config| map | vault-agent confgiration |
| vault_agent_sources | map | template sources configuration |
| vault_agent_dir | string | main vault-agent dir |
| vault_agent_dirs | map | vault-agent directories to create |
| vault_agent_version | string | |

## Examples
```sh
ansible-playbook site.yml -e "target=antiochia role=vault-agent"
```

### Author
Anatoly Laskaris
