#!/usr/bin/env python

"""
5. On both the NXOS1 and NXOS2 switches configure five VLANs including VLAN names (just pick 5 VLAN numbers between 100 - 999). 
Use Netmiko's send_config_from_file() method to accomplish this. 
Also use Netmiko's save_config() method to save the changes to the startup-config.
"""

from pprint import pprint
from netmiko import ConnectHandler
from getpass import getpass
import os
from datetime import datetime

password = os.getenv("PYPLUS_PASS") if os.getenv("PYPLUS_PASS") else getpass()

nxos1 = {
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_nxos",
    "session_log": "session_log"
}

nxos2 = {
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_nxos",
    "session_log": "session_log"
}

for device in (nxos1, nxos2):
    net_connect = ConnectHandler(**device)
    send_config = net_connect.send_config_from_file("nxos_vlans.txt")	
    print(send_config)
    save_config = net_connect.save_config()
    print(save_config)
    net_connect.disconnect()






