import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_dependencies(host):
    aptitude = host.package('aptitude')
    assert aptitude.is_installed

    gnupg2 = host.package('gnupg2')
    assert gnupg2.is_installed

    apt_transport_https = host.package('apt-transport-https')
    assert apt_transport_https.is_installed


def test_repo_exist(host):
    f = host.file('/etc/apt/sources.list.d/downloads_plex_tv_repo_deb.list')

    assert f.exists
    assert f.contains("deb https://downloads.plex.tv/repo/deb public main")


def test_plex_installed(host):
    plex = host.package('plexmediaserver')

    assert plex.is_installed


def test_plex_svc_exist(host):
    f = host.file('/lib/systemd/system/plexmediaserver.service')

    assert f.exists
