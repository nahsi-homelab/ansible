# gentoo-kernel

## Description
Configure and install custom Gentoo
[distribution Kernel](https://wiki.gentoo.org/wiki/Project:Distribution_Kernel)

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

## Credits
To [Jakub Jirutka](https://github.com/jirutka) for `eselect` Ansible
[module](https://github.com/gentoo-ansible/role-base/blob/master/library/eselect]).

## Author
Anatoly Laskaris
