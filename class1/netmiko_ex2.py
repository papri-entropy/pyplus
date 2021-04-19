#!/usr/bin/env python

"""
2. Add a second NX-OS device to your first exercise. 
Make sure you are using dictionaries to represent the two NX-OS devices.
Additionally, use a for-loop to accomplish the Netmiko connection creation. 
Once again print the prompt back from the devices that you connected to.
"""

from pprint import pprint
from netmiko import ConnectHandler
from getpass import getpass
import os

password = os.getenv("PYPLUS_PASS") if os.getenv("PYPLUS_PASS") else getpass()

nxos1 = {
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_nxos"
}

nxos2 = {
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_nxos"
}

for device in (nxos1, nxos2):
    print(device)

for device in (nxos1, nxos2):
    net_connect = ConnectHandler(**device)

    print("*" * 80)
    print(net_connect.find_prompt())
    print("*" * 80)
