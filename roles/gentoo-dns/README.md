# gentoo-dns

## Description

Install and configure DNSCrypt and Unbound.

## Requirements

- Ansible version >= 2.9

## Role Variables

### DNSCrypt

See [defaults/main/dnscrypt.yml](defaults/main/dnscrypt.yml) for details and examples.

| Name | Type | Description |
| ---- | ---- | ----------- |
| dns_dnscrypt_listen | list | listen addresses |
| dns_dnscrypt_options | map | |
| dns_dnscrypt_servers | list | upstream DNS servers |
| dns_dnscrypt_routes | list | servers with relays |
| dns_dnscrypt_sources | map | |
| dns_dnscrypt_static | map | |
| dns_dnscrypt_blacklist | map | |
| dns_dnscrypt_ip_blacklist | map | |
| dns_dnscrypt_whitelist | map | |

### Unbound

See [defaults/main/dnscrypt.yml](defaults/main/dnscrypt.yml) for details and examples.

| Name | Type | Description |
| ---- | ---- | ----------- |
| dns_unbound_server_default | map | default configuration |
| dns_unbound_server | map | will be merged with `dns_unbound_server_default` |

## Examples

### Playbook
```yaml
- hosts: all
  roles:
    - gentoo-dns
```

## Tests

- [Molecule](http://molecule.readthedocs.org/en/latest/)
- [testinfra](https://testinfra.readthedocs.io/en/latest/index.html)

To run tests:
```sh
molecule test
```

## Author
Anatoly Laskaris
