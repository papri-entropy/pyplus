#!/usr/bin/env python

"""
3. For one of the Cisco IOS devices, use Netmiko and the send_command() method 
to retrieve 'show version'. Save this output to a file in the current working directory.
"""

from pprint import pprint
from netmiko import ConnectHandler
from getpass import getpass
import os

password = os.getenv("PYPLUS_PASS") if os.getenv("PYPLUS_PASS") else getpass()

cisco3 = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_nxos",
    "session_log": "session_log"
}

net_connect = ConnectHandler(**cisco3)

output = net_connect.send_command("show version")

with open("cisco3_version", "w") as f:
    f.write(output)

print("*" * 80)
print(output)
print("*" * 80)
