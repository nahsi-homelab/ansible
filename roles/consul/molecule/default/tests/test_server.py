import testinfra.utils.ansible_runner
import pytest
import os
import json


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
        os.environ["MOLECULE_INVENTORY_FILE"]).get_hosts("consul")


def test_server_sockets(host):
    dns = host.socket("tcp://127.0.0.1:8601")
    assert dns.is_listening

    http = host.socket("tcp://0.0.0.0:8500")
    assert http.is_listening
