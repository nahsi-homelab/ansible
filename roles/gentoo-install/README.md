# gentoo-install

## Description
Prepare Gentoo stage3.

Does roughly the following:
- Get latest autobuilt stage3
- Unpack stage3 with correct permissions
- Prepare chroot (mount virtual filesystems, copy `resolv.conf` etc)
- Install gentoolkit - `portage` module dependency

## Requirements
- Ansible version >= 2.9

## Role Variables
| Name | Default value | Description |
| ---- | ------------- | ----------- |
| `arch` | | HW architecture: amd64, arm64 etc |
| `install_prefix` | `/mnt/gentoo` | where to unpack stage3 |

## Preparation
1. Boot into installation media
2. [Configure network](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Networking) if necessary
3. Format disks and mount Gentoo rootfs to `install_prefix` (defaults to `/mnt/gentoo`)
see [Configure disks](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Disks)

## Examples
```yaml
- name: Install stage3 gentoo
  hosts: some-livecd
  roles:
    - gentoo-install
```

## Testing
Tests are automated with

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
