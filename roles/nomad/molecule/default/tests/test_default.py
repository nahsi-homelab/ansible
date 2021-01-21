import testinfra.utils.ansible_runner
import pytest
import os
import json


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
        os.environ["MOLECULE_INVENTORY_FILE"]).get_hosts("all")


@pytest.mark.parametrize("dirs", [
    "/opt/nomad",
    "/opt/nomad/data"
])
def test_directories(host, dirs):
    d = host.file(dirs)
    assert d.is_directory
    assert d.exists


@pytest.mark.parametrize("files", [
    "/opt/nomad/conf.d/nomad.json"
])
def test_files(host, files):
    f = host.file(files)
    assert f.exists
    assert f.is_file


def test_user(host):
    assert host.group("nomad").exists
    assert host.user("nomad").exists


def test_service_is_running(host):
    service = host.service("nomad")

    assert service.is_running
    assert service.is_enabled


def test_server_sockets(host):
    http = host.socket("tcp://127.0.0.1:4646")

    assert http.is_listening
