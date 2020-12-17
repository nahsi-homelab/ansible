import testinfra.utils.ansible_runner
import pytest
import os
import json

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
        os.environ["MOLECULE_INVENTORY_FILE"]).get_hosts("all")


def test_gentoo_repository_configured(host):
    f = host.file("/mnt/gentoo/etc/portage/repos.conf/gentoo.conf")
    assert f.exists
    assert f.contains("[gentoo]")

def test_gentoo_stage3_unpacked(host):
    d = host.file("/mnt/gentoo/lib")
    assert d.exists
