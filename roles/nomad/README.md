# HashiCorp Nomad

## Description
Installs and configures HashiCorp [Nomad](https://www.nomadproject.io/).

## Role Variables
See [defaults/main.yml](defaults/main.yml) for details and examples.

| name | type | description |
| ---- | ---- | ----------- |
| nomad_config| map | nomad confgiration |
| nomad_dirs | map | nomad directories to create |
| nomad_dir | string | main nomad dir, used in `nomad_dirs` |
| nomad_version | string | |

## Examples
Deploy Nomad server with Vault integration:
```ssh
export token="$(vault token create -policy nomad-server -period 72h -orphan -field token)"
ansible-playbook site.yml -e "target=nomad-server role=nomad nomad_token=$token"
```

### External Resources
- https://www.nomadproject.io/docs/configuration

### Author
Anatoly Laskaris
