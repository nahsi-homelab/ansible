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
6. Run base playbook:
```
ansible-playbook base.yml -k -e "target=<target>"
```

## Prepare disks
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
    main /dev/disk/by-id/id
```

#### Example dataset layout
```
NAME                      USED  AVAIL     REFER  MOUNTPOINT
main                      164G   735G       96K  none
main/containers          3.66G   735G       96K  none
main/system              15.6G   735G       96K  none
main/system/gentoo       11.3G   735G     11.3G  /
main/system/swap         4.25G   735G     3.69G  -
main/user                 145G   735G       96K  none
main/user/nahsi           145G   735G       96K  none
main/user/nahsi/home     63.5G   735G     63.5G  /home/nahsi
```

```
zpool set bootfs=main/system/gentoo main
zfs set canmount=noauto main/system/gentoo
```

### UEFI
- `gdisk /path/to/disk`
- Last sector: +512M
- HEX: EF00

```sh
mkfs.vfat -F 32 /dev/disk/by-partlabel/EFI
```

### Legacy GPT
#### Partition disk
```
gdisk /path/to/disk
Command (? for help): x

Expert command (? for help): a
Partition number (1-3): 1
Known attributes are:
0: system partition
1: hide from EFI
2: legacy BIOS bootable
60: read-only
62: hidden
63: do not automount

Attribute value is 0000000000000000. Set fields are:
  No fields set

Toggle which attribute field (0-63, 64 or <Enter> to exit): 2
Have enabled the 'legacy BIOS bootable' attribute.
Attribute value is 0000000000000004. Set fields are:
2 (legacy BIOS bootable)

Toggle which attribute field (0-63, 64 or <Enter> to exit):

Expert command (? for help): w
```

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

#### Install syslinux MBR data
```
dd bs=440 count=1 conv=notrunc if=/usr/lib/syslinux/gptmbr.bin of=/path/to/disk
```
