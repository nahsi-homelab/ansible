# Ansible Role: gentoo-syslog

## Description

Install and configure syslog-ng and logrotate on Gentoo host.
Configure log rotation of syslog-ng logs.

### Automatic log rotation
For every syslog file destination log rotation would be configured
automatically with default logrotate options.

To use custom logrotate options add `logrotate` to syslog destination:
```yaml
syslog_destinations:
  test:
    - driver: file
      params: '"/var/log/test.log"'
      logrotate:
        - size 1K
```

## Requirements

- Ansible version >= 2.9

## Role Variables

All variables are stored in [defaults/main.yml](defaults/main.yml) with comments.
## Examples

### Playbook
```yaml
- hosts: all
  roles:
    - gentoo-syslog
```

### Inventory

Utilizing all variables:
```yaml
syslog_sources:
  my_app:
    - driver: file
      params: '"/opt/my_app/log"'

syslog_filters:
  filter: 'message("hey");'

syslog_destinations:
  my_logs:
    - driver: file
      params: '"/var/log/my_logs.log"'
      logrotate:
        - rotate 3
        - size 1K
        - compress

syslog_logs:
  - sources: [ 'my_app' ]
    filters: [ 'my_filter' ]
    destinations: [ 'my_logs' ]
```

Sending logs to promtail running on localhost:
```yaml
syslog_destinations:
  promtail:
    - driver: syslog
      params: '"localhost" transport("tcp") port(1514)'

syslog_logs:
  - sources: [ 'src' ]
    destinations: [ 'promtail' ]
```

## Testing
Tests are WIP.

Since I don't host my own container registry at this moment you have to
[build](../../dockerfiles) container with Gentoo locally before running tests.

Tests will be automated with:

- [tox](https://tox.readthedocs.io/en/latest/)
- [Molecule](http://molecule.readthedocs.org/en/latest/)
- [testinfra](https://testinfra.readthedocs.io/en/latest/index.html)

To install tox run:
```sh
pip install tox
```

To run tests on all ansible versions:
```sh
tox
```

To run a custom molecule command on custom environment:
```sh
tox -e ansible29 -- molecule test -s
```

## Author
Anatoly Laskaris
