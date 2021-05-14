# gentoo-syslog

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

## Author
Anatoly Laskaris
