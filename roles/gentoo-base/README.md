# Ansible Role: gentoo-base

## Description

Configure basic Gentoo. Install packages, configure portage etc.

## Requirements

- Ansible version >= 2.9

## Role Variables

For examples see comments in <defaults>.

| Name | Default value | Description |
| ---- | ------------- | ----------- |
| `base_portage_jobs` | hosts cores * threads | used in `MAKEOPTS` and emerge opts |
| `base_portage_la` | jobs * 0.9 | load average, used in `MAKEOPTS` and emerge opts |
| `base_portage_mirrors` | `["https://distfiles.gentoo.org"]` | |
| `base_portage_features` | `[]` | |
| `base_portage_use` | `[]` | |
| `base_portage_package_use` | `[]` | |
| `base_portage_makeconf_default` | see <defaults/portage.yml> | used to construct `/etc/portage/make.conf` |
| `base_portage_makeconf` | `{}` | host/group vars, will be merged with `base_portage_makeconf_default` |
|||
| `base_distccd` | | distccd config, see <defaults/distcc.yml> |
| `base_distccd_allow` | host ipv4 subnet | list of ips/subnets allowed to connect to distccd |
|||
| `base_filesystems` | `[]` | filesystem to mount and add to fstab, see <defaults/system.yml> |
| `base_timezone` | "Europe/Moscow" | |
| `base_env` | `{}` | variables to set with eselect |
| `base_packages_default` | see <defaults/system.yml> | list of packages to install |
| `base_packages` | `[]` | list of packages to install, will be added to `base_packages_default` |
| `base_servies` | `[]` | list of services to enable, see <defaults/system.yml> |
| `base_openrc_default` | see <defaults/system.yml> | used to construct `/etc/rc.conf` |
| `base_openrc` | `{}` | host/group vars, will be merged with `base_openrc_default` |
| `base_hwclock_default` | see <defaults/system.yml> | used to construct `/etc/conf.d/hwclock` |
| `base_nwclock` | `{}` | host/group vars, will be merged with `base_hwclock_default` |
| `base_network` | see <defaults/system.yml> |
| `base_network_interfaces` | `[]` | list of network interfaces to enable |
|||
| `base_sshd_allow_groups` | `[ "wheel" ]` | only allow users from groups to connect |
| `base_sshd_allow_users` | `[]` | only allow users to connect |
| `base_sshd_host_keys` | `[ "/etc/ssh/ssh_host_rsa_key", "/etc/ssh/ssh_host_ed25519_key" ]` | enabled cryptosystems |
| `base_sshd` | see <defaults/system.yml> | sshd config |
| `chroot` | `false` | whether system this host is running again is in chroot - if `true` some services will not be restarted |
| `users` | `{}` | map of users, see below |

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

## Examples
```yaml
- name: Install Gentoo
  hosts: all
  roles:
    - gentoo-base
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

## Credits
To [Jakub Jirutka](https://github.com/jirutka) for `eselect` Ansible [module](https://github.com/gentoo-ansible/role-base/blob/master/library/eselect]).

## Author
Anatoly Laskaris
