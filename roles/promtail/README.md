# promtail

>This role installs and configures promtail.

## Role Variables

| variable                | description                                    |
|-------------------------|------------------------------------------------|
| `promtail_version`      | promtail version to use                        |
| `promtail_download_url` | where to look for binaries                     |
| `promtail_config`       | promtail configuration                         |
| `promtail_dirs_overlay` | map of directories to create                   |

## Tags
* `configs` - manage config files

## External Resources
- https://grafana.com/docs/loki/latest/clients/promtail/

## Author
* **Anatoly Laskaris** - [nahsi](https://github.com/nahsi)
