import testinfra.utils.ansible_runner
import pytest
import os
import json


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
        os.environ["MOLECULE_INVENTORY_FILE"]).get_hosts("all")


@pytest.mark.parametrize("dirs", [
    "/opt/vault-agent",
    "/opt/vault-agent/source.d",
])
def test_directories(host, dirs):
    d = host.file(dirs)
    assert d.is_directory
    assert d.exists

@pytest.mark.parametrize("files", [
    "/opt/vault-agent/vault-agent.json"
])
def test_files(host, files):
    f = host.file(files)

    assert f.exists
    assert f.is_file


def test_user(host):
    assert host.group("vault-agent").exists
    assert host.user("vault-agent").exists


def test_service_is_running(host):
    service = host.service("vault-agent")

    assert service.is_running
    assert service.is_enabled
