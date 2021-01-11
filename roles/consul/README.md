# consul

## Description
Install and configure [Consul](https://www.consul.io).

### Role Variables
See [defaults/main.yml](defaults/main.yml) for details and examples.

| name | type | description |
| ---- | ---- | ----------- |
| consul_config| map | consul confgiration |
| consul_bootstrap_config | bootstrap parameters |
| consul_dirs | map | consul directories to create |
| consul_version | string | |
| consul_datacenter | string | |

`consul_config` and `consul_dirs` are two level variables, i.e. there are:

* `consul_config_base` - variable with default Consul configuration parameters
* `consul_config_overlay` - empty variable with parameters to be defined in Ansible inventory
* `consul_config` - variable containing all above variables merged in order

`consul_config` can be specified at any level (group_vars or host_vars) to
override defailt configuration parameters instead of merging.

### External Resources
- https://www.consul.io/docs/install/ports.html
- https://www.consul.io/docs/agent/options

### Author
Anatoly Laskaris
