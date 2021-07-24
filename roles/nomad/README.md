# nomad

>This role installs and configures [nomad](https://www.nomadproject.io).

## Role Variables

| variable             | description                                         |
|----------------------|-----------------------------------------------------|
| `nomad_version`      | nomad version to use                                |
| `nomad_config`       | main nomad configuration                            |
| `nomad_service`      | nomad unitfile                                      |
| `nomad_configs`      | map of nomad override configs                       |
| `nomad_dirs_overlay` | map of directories to create combined with defaults |

See [defaults/](defaults/) for details and examples.

## Tags
* `configuration` - update nomad unitfile and config

## Author
* **Anatoly Laskaris** - [nahsi](https://github.com/nahsi)
