# gentoo-dns

## Description

Install and configure dnscrypt and Unbound.

## Requirements

- Ansible version >= 2.9

## Role Variables

All variables are stored in [defaults/main.yml](defaults/main.yml) with comments.

## Examples

### Playbook
```yaml
- hosts: all
  roles:
    - gentoo-dns
```

## Author
Anatoly Laskaris
