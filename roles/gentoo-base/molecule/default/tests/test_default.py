import testinfra.utils.ansible_runner
import pytest
import os
import json

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
        os.environ["MOLECULE_INVENTORY_FILE"]).get_hosts("all")


def test_user_exist(host):
    assert host.user("test") exists
