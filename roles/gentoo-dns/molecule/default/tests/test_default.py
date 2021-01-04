import testinfra.utils.ansible_runner
import pytest
import os
import json

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
        os.environ["MOLECULE_INVENTORY_FILE"]).get_hosts("all")


@pytest.mark.parametrize("dirs", [
    "/etc/dnscrypt-proxy/",
    "/etc/unbound/",
    "/etc/unbound/conf.d"
])
def test_directories(host, dirs):
    d = host.file(dirs)
    assert d.is_directory
    assert d.exists


def test_unbound_configured(host):
    f = host.file("/etc/unbound/unbound.conf")
    assert f.exists
    assert f.contains("include: /etc/unbound/conf.d/interfaces.conf")

    f = host.file("/etc/unbound/conf.d/interfaces.conf")
    assert f.exists
    assert f.contains("interface: 0.0.0.0@53")


def test_dnscrypt_configured(host):
    f = host.file("/etc/dnscrypt-proxy/dnscrypt-proxy.toml")
    assert f.exists
    assert f.contains("require_nolog = true")


@pytest.mark.parametrize("service", [
    "unbound",
    "dnscrypt-proxy"
    ])
def test_services(host, service):
    service = host.service(service)

    assert service.is_running
    assert service.is_enabled


@pytest.mark.parametrize("port", [
    "53",
    "5053"
    ])
def test_sockets(host, port):
    s = host.socket("tcp://0.0.0.0:{}".format(port))
    assert s.is_listening
