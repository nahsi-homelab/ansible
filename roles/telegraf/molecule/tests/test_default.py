import testinfra.utils.ansible_runner
import pytest
import os
import json

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
        os.environ["MOLECULE_INVENTORY_FILE"]).get_hosts("all")


def test_user_exist(host):
    assert host.user("telegraf").exists


def test_telegraf_running_and_enabled(host):
    service = host.service("telegraf")
    assert service.is_running
    assert service.is_enabled


@pytest.mark.parametrize("dirs", [
    "/opt/telegraf",
    "/opt/telegraf/conf.d",
])
def test_telegraf_directories(host, dirs):
    d = host.file(dirs)
    assert d.is_directory
    assert d.exists


@pytest.mark.parametrize("files", [
    "/opt/telegraf/telegraf.conf",
    "/opt/telegraf/conf.d/system.conf",
    "/opt/telegraf/conf.d/health.conf",
])
def test_files_present(host, files):
    f = host.file(files)
    assert f.exists
    assert f.is_file


@pytest.mark.parametrize("files", [
    "/opt/telegraf/conf.d/test.conf",
])
def test_files_absent(host, files):
    f = host.file(files)
    assert not f.exists


def test_telegraf_prometheus_listening(host):
    s = host.socket("tcp://0.0.0.0:9271")
    assert s.is_listening
