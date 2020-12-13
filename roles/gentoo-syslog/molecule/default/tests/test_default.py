import testinfra.utils.ansible_runner
import pytest
import os
import json

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
        os.environ["MOLECULE_INVENTORY_FILE"]).get_hosts("all")


def test_logrotate_configured(host):
    f = host.file("/etc/logrotate.d/syslog-ng")
    assert f.exists
    assert f.contains("/var/log/test.log")
    assert f.contains("size 1K")

def test_syslog_configured(host):
    f = host.file("/etc/syslog-ng/syslog-ng.conf")
    assert f.exists
    assert f.contains("/var/log/test.log")

    cmd = host.run("syslog-ng")
    assert cmd.succeeded

    host.run("logger 'molecule test'")
    log = host.file("/var/log/test.log")
    assert log.exists
    assert log.contains("molecule test")
