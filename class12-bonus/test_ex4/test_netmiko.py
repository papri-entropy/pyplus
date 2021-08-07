#!/usr/bin/env python

from getpass import getpass
from netmiko import ConnectHandler

def netmiko_conn():
    net_connect = ConnectHandler(
        host = "arista1.lasthop.io",
        device_type = "arista_eos", 
        username = "pyclass",
        password = getpass(),
    )
    return net_connect

def test_find_prompt():
    net_connect = netmiko_conn()
    assert "arista1" in net_connect.find_prompt()

def test_show_version():
    net_connect = netmiko_conn()
    output = net_connect.send_command("show version")
    assert "4.20.10M" in output
