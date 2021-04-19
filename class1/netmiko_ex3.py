#!/usr/bin/env python

"""
 1. In the lab environment use Netmiko to connect to one of the Cisco NX-OS devices. 
You can find the IP addresses and username/passwords of the Cisco devices in the 
'Lab Environment' email or alternatively in the ~/.netmiko.yml file. 
Simply print the router prompt back from this device to verify you are connecting to the device properly.
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
