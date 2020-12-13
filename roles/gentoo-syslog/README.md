# Ansible Role: gentoo-syslog

## Description

Install and configure syslog-ng and logrotate on Gentoo host. Configure log rotation of syslog-ng logs.

## Requirements

- Ansible version >= 2.9

## Role Variables

All variables are stored in [defaults/main.yml](defaults/main.yml) with comments.

### User variables
`syslog_sources`, `syslog_destinations`, `syslog_filters` and `syslog_logs` can be defined in group_vars or host_vars and will be combined with default variables

### Autoconfigured log rotation
For every syslog file destination log rotation would be configured automatically with default logrotate options.

To use custom logrotate options add `logrotate` to syslog destination:
```yaml
syslog_destinations:
  test:
    - driver: file
      params: '"/var/log/test.log"'
      logrotate:
        - size 1K
```

### Starting services
`chroot: true` needs to be set when installing syslog-ng in chroot environment (when installing Gentoo for example).

When set to `true` starting and restarting services would be skipped.

## Examples

### Playbook
```yaml
- hosts: ubuntu-livecd
  vars:
    chroot: true
    syslog_destinations:
      install:
        - driver: file
          params: '"/var/log/install.log"'
          logrotate:
            - size 1K
            - compress
  roles:
    - gentoo-install
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
Tests are automated with

- [tox](https://tox.readthedocs.io/en/latest/)
- [Molecule](http://molecule.readthedocs.org/en/latest/)
- [testinfra](https://testinfra.readthedocs.io/en/latest/index.html)

Since I don't host my own container registry at this moment you have to build container with Gentoo locally. See more at this [README](../../dockerfiles/)

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
