#!/usr/bin/env bash

efi_dir="/boot/efi/"

die() {
    echo "$@" >&2
    exit 1
}

mkdir -p "$efi_dir" \
    || die "Failed to create $efi_dir"
{ mountpoint -q "$efi_dir" || mount "$efi_dir"; } \
    || die "Failed to mount $efi_dir"

rsync -Lav -q --exclude="*.old" --include="vmlinuz*" --include="initramfs*" --exclude="*" /boot/ "${efi_dir}/EFI/Gentoo/"
    || die "Failed to rsync initramfs"

umount "$efi_dir" \
    || echo "Failed to unmount $efi_dir"
