import os

import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(os.environ["MOLECULE_INVENTORY_FILE"]).get_hosts("all")

@pytest.mark.parametrize(
    "directory",
    [
        "/opt/geth/data",
        "/opt/geth/config",
        "/opt/geth/logs"
    ]
)
def test_directories(host, directory):
    d = host.file(directory)
    assert d.exists
    assert d.is_directory
    assert d.user == "geth"
    assert d.group == "geth"

@pytest.mark.parametrize(
    "file",
    [
        "/usr/local/bin/geth",
        "/lib/systemd/system/geth.service",
        "/opt/geth/config/config.toml"
    ],
)
def test_files(host, file):
    f = host.file(file)
    assert f.exists
    assert f.is_file


@pytest.mark.parametrize("service", ["geth"])
def test_service(host, service):
    s = host.service(service)
    assert s.is_running
    assert s.is_enabled
