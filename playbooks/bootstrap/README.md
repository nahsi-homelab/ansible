# Bootstrap
## Steps

0. Add host to inventory with all required variables
1. Boot into installation media ([hrmpf](https://github.com/leahneukirchen/hrmpf))
2. Format disks (see below)
3. Mount Gentoo rootfs to `install_prefix` (defaults to `/mnt/gentoo`)
4. Run bootstrap playbook

## Formating disks
### EFI

- `gdisk /path/to/disk`
- Last sector: +512M
- HEX: EF00

```sh
mkfs.vfat -F 32 /dev/disk/by-partlabel/EFI
```

### ZFS
- https://blog.victormendonca.com/2020/11/03/zfs-for-dummies
- https://arstechnica.com/information-technology/2020/05/zfs-101-understanding-zfs-storage-and-performance

```sh
zpool create -o ashift=12 \
    -O xattr=sa \
    -O relatime=on \
    -O acltype=posix \
    -O canmount=off \
    -O normalization=formD \
    -O compression=zstd-3 \
    -O dnodesize=auto \
    hot /dev/disk/by-id/id
```

### Dataset layout
```
NAME                             USED  AVAIL     REFER  MOUNTPOINT
hot                             2.48M   899G       96K  none
hot/system                      1.05M   899G       96K  none
hot/system/gentoo                120K   899G      120K  /mnt/gentoo
hot/system/opt                    96K   899G       96K  /mnt/gentoo/opt
hot/system/usr                   192K   899G       96K  none
hot/system/usr/local              96K   899G       96K  /mnt/gentoo/usr/local
hot/system/var                   480K   899G       96K  none
hot/system/var/cache             192K   899G       96K  none
hot/system/var/cache/distfiles    96K   899G       96K  /mnt/gentoo/var/cache/distfiles
hot/system/var/db                192K   899G       96K  none
hot/system/var/db/repos           96K   899G       96K  /mnt/gentoo/var/db/repos
hot/user                         288K   899G       96K  none
hot/user/home                    192K   899G       96K  none
hot/user/home/nahsi               96K   899G       96K  /mnt/gentoo/home/nahsi
```

```
zfs set recordsize=16K hot/system/var/cache/distfiles
zfs set recordsize=1K hot/system/var/db/repos
```

```
zpool set bootfs=hot/system/gentoo hot
```
