# Bootstrap
## Steps
0. Add host to inventory with all required variables
1. Boot into installation media ([hrmpf](https://github.com/leahneukirchen/hrmpf))
2. Prepare disks (see below)
4. Make sure Gentoo rootfs is mounted to `install_prefix` (defaults to `/mnt/gentoo`)
5. Run bootstrap playbook:
```
ansible-playbook stage3.yml -k -e "target=<target> root_password=<pass>"
```
6. Run bootstrap playbook:
```
ansible-playbook bootstrap.yml -k -e "target=<target>"
```

## Prepare disks
### ZFS
- https://blog.victormendonca.com/2020/11/03/zfs-for-dummies
- https://arstechnica.com/information-technology/2020/05/zfs-101-understanding-zfs-storage-and-performance

```sh
zpool create -o ashift=13 \
    -O xattr=sa \
    -O relatime=on \
    -O acltype=posix \
    -O mountpoint=none \
    -O normalization=formD \
    -O compression=zstd \
    -O dnodesize=auto \
    -R /mnt/gentoo \
    main /dev/disk/by-id/id
```

[zstd compression](https://github.com/openzfs/zfs/pull/10278)

#### Example dataset layout
```
NAME                      USED  AVAIL     REFER  MOUNTPOINT
main                      164G   735G       96K  none
main/containers          3.66G   735G       96K  none
main/system              15.6G   735G       96K  none
main/system/gentoo       11.3G   735G     11.3G  /
main/system/swap         4.25G   735G     3.69G  -
main/users                145G   735G       96K  none
main/users/nahsi          145G   735G       96K  none
main/users/nahsi/home    63.5G   735G     63.5G  /home/nahsi
```

#### Set default bootfs
```
zpool set bootfs=main/system/gentoo main
zfs set canmount=noauto main/system/gentoo
```

#### Set kernel CMD
```
zfs set org.zfsbootmenu:commandline="ro quiet loglevel=0" main/system/gentoo
```

#### Encrypted home
```
zfs create -o encryption=on -o keyformat=passphrase main/users/nahsi/home
```

#### ZFS dataset as swap

[ZFS swap](https://github.com/zfsonlinux/pkg-zfs/wiki/HOWTO-use-a-zvol-as-a-swap-device)
```
zfs create -V 4G -b $(getconf PAGESIZE) -o compression=zle \
      -o logbias=throughput -o sync=standard \
      -o primarycache=metadata -o secondarycache=none \
      main/system/swap
```

### UEFI
- `gdisk /path/to/disk`
- Last sector: +512M
- HEX: EF00

```sh
mkfs.vfat -F 32 /dev/disk/by-partlabel/EFI
```

### Legacy GPT
#### Install syslinux bootloader
```
dd bs=440 count=1 conv=notrunc if=/usr/share/syslinux/gptmbr.bin of=/path/to//boot/disk
```

#### Partition disk
- `gdisk /path/to/disk`
- Last sector: +512M

#### Format partition to ext4
```
mkfs.ext4 /path/to/boot/partition
```

#### Install extlinux
```
mkdir /mnt/gentoo/boot/syslinux
mount /path/to/partition /mnt/gentoo/boot/syslinux
extlinux --install /mnt/gentoo/boot/syslinux
```

### Set boot attribute
```
sgdisk /path/to/boot/disk --attributes=1:set:2
```
