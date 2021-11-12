# consul

>This role installs and configures [Consul](https://www.consul.io).

## Role Variables

| variable              | description                                  |
|-----------------------|----------------------------------------------|
| `consul_version`      | consul version to use                        |
| `consul_config`       | main consul configuration                    |
| `consul_service`      | consul unitfile                              |
| `consul_services`     | map of services to register via json         |
| `consul_configs`      | map of consul override configs               |
| `consul_scripts`      | map of scripts                               |
| `consul_dirs`         | map of dirs to create combined with defaults |
| `consul_user`         | user to own consul files                     |
| `consul_group`        | group to own consul files                    |

See [defaults/](defaults/) for details and examples.

## Tags
* `config` - update consul unitfile and main config
* `services` - sync consul services
* `scripts` - sync consul scripts

## External Resources
- https://www.consul.io/docs/install/ports.html
- https://www.consul.io/docs/agent/options
- https://learn.hashicorp.com/tutorials/consul/dns-forwarding#dnsmasq-setup

## Author
* **Anatoly Laskaris** - [nahsi](https://github.com/nahsi)
