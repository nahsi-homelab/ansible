import testinfra.utils.ansible_runner
import pytest
import os
import json


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
        os.environ["MOLECULE_INVENTORY_FILE"]).get_hosts("all")


@pytest.mark.parametrize("dirs", [
    "/opt/consul",
    "/opt/consul/scripts",
    "/opt/consul/data"
])
def test_directories(host, dirs):
    d = host.file(dirs)
    assert d.is_directory
    assert d.exists


@pytest.mark.parametrize("files", [
    "/opt/consul/conf.d/consul.json"
])
def test_files(host, files):
    f = host.file(files)
    assert f.exists
    assert f.is_file


def test_user(host):
    assert host.group("consul").exists
    assert host.user("consul").exists


def test_service_is_running(host):
    service = host.service("consul")

    assert service.is_running
    assert service.is_enabled

def test_consul_working(host):
    cmd = host.run("consul catalog services")

    assert cmd.succeeded
