# consul template

## Description
Install and configure Consul Template.

### Role Variables
See [defaults/main.yml](defaults/main.yml) for details and examples.

| name | type | description |
| ---- | ---- | ----------- |
| consul_template_config| map | consul-template confgiration |
| consul_template_templates | map | template configuration |
| consul_template_dir | string | main consul-template dir |
| consul_template_dirs | map | consul-template directories to create |
| consul_template_version | string | |


## Examples
```sh
export token=$(vault token create -policy consul-template -period="24h" -field=token)
ansible-playbook site.yml -e "target=antiochia role=consul-template __vault_token=$token"
```

`__vault_token` is used in `vault` configuration block:
```yaml
consul_template_config:
  vault:
    address: "http://vault.service.consul:8200"
    token: "{{ __vault_token }}"
    renew_token: true
```

### Author
Anatoly Laskaris
