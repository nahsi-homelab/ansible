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

### Author
Anatoly Laskaris
