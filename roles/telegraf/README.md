# Telegraf

## Description
Installs and configures Telegraf - metrics collection agent.

### Role Variables
See [defaults/main.yml](defaults/main.yml) for details and examples.

| name | type | description |
| ---- | ---- | ----------- |
| telegraf_agent_config | string | agent configuration |
| telegraf_configs | map | plugins configuration |
| telegraf_version | string | |
| telegraf_checksum | string | |

### How to use
1. Install `python3-virtualenv`
2. Create python virtual environment with
```sh
python3 -m virtualenv ~/.homelab/ansible/telegraf
source ~/.homelab/ansible/telegraf/bin/activate
pip install -r requirements.txt
```
3. Run the role

### External Resources
- https://github.com/influxdata/telegraf

### Author
Anatoly Laskaris
