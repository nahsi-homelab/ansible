# telegraf

>This role installs and configures telegraf.

## Role Variables

| variable                | description                                    |
|-------------------------|------------------------------------------------|
| `telegraf_version`      | telegaf version to use                         |
| `telegraf_checksum`     | telegaf checksum archive (see github releases) |
| `telegraf_download_url` | where to look for binaries and such            |
| `telegraf_config`       | main telegraf configuration                    |
| `telegraf_service`      | telegraf unit file                             |
| `telegraf_configs`      | map of telegraf "plugins" configs              |
| `telegraf_scripts`      | map of scripts                                 |
| `telegraf_dirs_overlay` | map of directories to create                   |

See [defaults/](defaults/) for details and examples.

## Tags
* `configs` - manage config files
* `scripts` - manage exec scripts

## External Resources
- https://github.com/influxdata/telegraf

## Author
* **Anatoly Laskaris** - [nahsi](https://github.com/nahsi)
