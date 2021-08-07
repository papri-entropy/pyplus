#!/usr/bin/env python

import pytest
from getpass import getpass
from netmiko import ConnectHandler

password = getpass()

@pytest.fixture(scope="module")
def netmiko_conn():
    net_connect = ConnectHandler(
        host = "arista1.lasthop.io",
        device_type = "arista_eos", 
        username = "pyclass",
        password = password,
    )
    return net_connect

def test_find_prompt(netmiko_conn):
    assert "arista1" in netmiko_conn.find_prompt()

def test_show_version(netmiko_conn):
    output = netmiko_conn.send_command("show version")
    assert "4.20.10M" in output
