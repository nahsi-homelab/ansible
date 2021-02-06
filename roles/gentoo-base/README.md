# gentoo-base

## Description

Configure Gentoo. Install packages, configure portage, sshd, network etc.

## Requirements

- Ansible version >= 2.9

## Role Variables

For examples see comments in [defaults](defaults).

| Name | Default value | Description |
| ---- | ------------- | ----------- |
| `chroot` | `false` | if `true` some services will not be restarted |
| `users` | `{}` | map of users to create, see [below](#Examples) |
|||
| `base_portage_jobs` | hosts cores * threads | used in `MAKEOPTS` and emerge opts |
| `base_portage_la` | jobs * 0.9 | load average, used in `MAKEOPTS` and emerge opts |
| `base_portage_mirrors` | `["https://distfiles.gentoo.org"]` | |
| `base_portage_features` | `[]` | |
| `base_portage_use` | `[]` | |
| `base_portage_package_use` | `[]` | |
| `base_portage_makeconf_default` | see [defaults/portage.yml](defaults/portage.yml) | used to create `/etc/portage/make.conf` |
| `base_portage_makeconf` | `{}` | host/group vars, will be merged with `base_portage_makeconf_default` |
|||
| `base_filesystems` | `[]` | filesystem to mount and add to fstab, see [defaults/system.yml](defaults/system.yml) |
| `base_timezone` | `"Europe/Moscow"` | |
| `base_consolefont` | `"ter-16b"` | one of `/usr/share/consolefonts` |
| `base_env` | `{}` | variables to set with eselect, see [defaults/system.yml](defaults/system.yml) |
|||
| `base_packages_default` | see [defaults/system.yml](defaults/system.yml) | list of packages to install |
| `base_packages` | `[]` | list of packages to install, will be added to `base_packages_default` |
| `base_services_default` | see [defaults/system.yml](defaults/system.yml) | list of services to enable |
| `base_services` | `[]` | list of services to enable, will be added to `base_services_default` |
|||
| `base_openrc_default` | see [defaults/system.yml](defaults/system.yml) | used to create `/etc/rc.conf` |
| `base_openrc` | `{}` | host/group vars, will be merged with `base_openrc_default` |
|||
| `base_hwclock_default` | see [defaults/system.yml](defaults/system.yml) | used to create `/etc/conf.d/hwclock` |
| `base_nwclock` | `{}` | host/group vars, will be merged with `base_hwclock_default` |
|||
| `base_network` | see [defaults/system.yml](defaults/system.yml) | netifrc configuration |
| `base_network_interfaces` | `[]` | list of network interfaces to enable |
| `base_dns` | see [defaults/system.yml](defaults/system.yml) | used to create `/etc/resolvconf.conf` |
|||
| `base_sshd` | see [defaults/system.yml](defaults/system.yml) | sshd config |
| `base_sshd_listen_address` | `{{ ansible_default_ipv4.address }}` | sshd listen address |
| `base_sshd_allow_groups` | `[ "wheel" ]` | only allow users from groups to connect |
| `base_sshd_allow_users` | `[]` | only allow users to connect |
| `base_sshd_host_keys` | `[ "/etc/ssh/ssh_host_rsa_key", "/etc/ssh/ssh_host_ed25519_key" ]` | enabled cryptosystems |
|||
| `base_distccd` | see [defaults/distcc.yml](defaults/distcc.yml) | distccd config |
| `base_distccd_allow` | `["{{ ansible_default_ipv4.network }}"]` | list of IPs/subnets allowed to connect to distccd |
|||
| `base_podman_policy` | see [defaults/containers.yml](defaults/containers.yml) | podman policy settings |
| `base_podman_registries` | see [defaults/containers.yml](defaults/containers.yml) | podman registries |

## Examples

### Users
```yaml
users:
  - name: test
    groups:
      - wheel
      - portage
    ssh_keys:
      - key: <ssh_public_key>
        comment: "test"
```

### Playbook
```yaml
- name: Install Gentoo
  hosts: all
  roles:
    - gentoo-base
```

## Credits
To [Jakub Jirutka](https://github.com/jirutka) for `eselect` Ansible [module](https://github.com/gentoo-ansible/role-base/blob/master/library/eselect]).

## Author
Anatoly Laskaris
