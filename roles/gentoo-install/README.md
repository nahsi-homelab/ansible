# gentoo-install

## Description
Prepare Gentoo stage3.

Does roughly the following:
- Get latest autobuilt stage3
- Unpack stage3 with correct permissions
- Prepare chroot (mount virtual filesystems, copy `resolv.conf` etc)
- Install gentoolkit - `portage` module dependency

## Preparation
1. Boot into installation media
2. [Configure network](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Networking) if necessary
3. Format disks and mount Gentoo rootfs to `install_prefix` (defaults to `/mnt/gentoo`)
see [Configure disks](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Disks)

## Author
Anatoly Laskaris
