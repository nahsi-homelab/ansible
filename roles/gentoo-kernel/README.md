# gentoo-kernel

## Description
Configure and install custom Gentoo
[distribution Kernel](https://wiki.gentoo.org/wiki/Project:Distribution_Kernel),
[rEFInd](https://rodsbooks.com/refind/configfile.html) and optionally
[ZFSBootMenu](https://zfsbootmenu.org).

### Managing kernel configurations
#### .config
There is a minimal kernel configuration file (`.config`) for each `arch` with
sane defaults, but with platform specific options disabled (i.e. no support
for AMD or Intel CPUs by default, no video drivers etc).

Minimal configuration is copied by Ansible to `/etc/portage/savedcofigs`
and used instead of default config supplied by Gentoo when `savedconfig`
useflag enabled for `sys-kernel/getnoo-kernel`.

#### Kconfig
Platform specific options are managed by custom
[Kconfig](https://www.kernel.org/doc/html/latest/kbuild/kconfig.html) file
located at `/etc/kernel/Kconfig`.

This file is sourced in Linux main Kconfig file using this
[patch](files/custom-kconfig.patch).

Custom Kconfig in turn sources other Kconfig [files](files/kconfig.d/) in
`/etc/kernel/kconfig.d/` managed with `kernel_kconfigs` variable.

## Requirements
- Ansible version >= 2.9

## Role Variables
| Name | Default value | Description |
| ---- | ------------- | ----------- |
| `arch` | | HW architecture: amd64, arm64 etc |
| `kernel_version` | `""` |  |
| `kernel_firmware` | `[]` | list of firmware, used in `linux-firmware` savedconfig and in `CONFIG_EXTRA_FIRMWARE=` |
| `kernel_kconfigs` | `[]` | see [files/kconfig.d](files/kconfig.d) |
| `kernel_postinst` | `[]` | scripts to run after kernel install, see [files/postinst.d](files/postinst.d) |
| `kernel_zfs_on_root` | `false` | flag to trigger zfsbootmenu install |
| `kernel_boot_device` | `""` | path to boot device, example `/dev/disk/by-partlabel/EFI` |
| `kernel_refind_default` | see [defaults/main.yml](defaults/main.yml) | used to construct `/boot/efi/EFI/refind/refind.conf` |
| `kernel_refind` | `{}` | refind config, will be merged with `kernel_refind_default` |
| `kernel_refind_menu` | `[]` | see [defaults/main.yml](defaults/main.yml) |

## Examples
```yaml
- name: Configure Gentoo kernel
  hosts: all
  roles:
    - gentoo-kernel
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

## Credits
To [Jakub Jirutka](https://github.com/jirutka) for `eselect` Ansible
[module](https://github.com/gentoo-ansible/role-base/blob/master/library/eselect]).

## Author
Anatoly Laskaris
