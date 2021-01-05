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

    s = host.socket("tcp://0.0.0.0:53")
    assert s.is_listening


def test_dnscrypt_configured(host):
    f = host.file("/etc/dnscrypt-proxy/dnscrypt-proxy.toml")
    assert f.exists
    assert f.contains("require_nolog = true")

    s = host.socket("tcp://127.0.0.1:5053")
    assert s.is_listening


@pytest.mark.parametrize("service", [
    "unbound",
    "dnscrypt-proxy"
    ])
def test_services(host, service):
    service = host.service(service)

    assert service.is_running
    assert service.is_enabled


def test_dns(host):
    google = host.addr("google.com")

    assert google.is_resolvable
