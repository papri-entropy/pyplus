#!/usr/bin/env python

"""
6a. Create an nxapi_plumbing "Device" object for nxos1. 
The api_format should be "jsonrpc" and the transport should be "https" (port 8443). 
Use getpass() to capture the device's password. 
Send the "show interface Ethernet1/1" command to the device, 
parse the output, and print out the following information:

Interface: Ethernet1/1; State: up; MTU: 1500
"""

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from pprint import pprint
from getpass import getpass
from nxapi_plumbing import Device

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

password = getpass()

nxos1 = {
    "api_format": "jsonrpc",
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": password,
    "transport": "https",
    "port": 8443,
    "verify": False
    }

device = Device(**nxos1)

output = device.show("show interface Ethernet1/1")

interface = output['TABLE_interface']['ROW_interface']['interface']
state = output['TABLE_interface']['ROW_interface']['state']
mtu = output['TABLE_interface']['ROW_interface']['eth_mtu']

print()
print(f"Interface: {interface}; State: {state}; MTU: {mtu}")
print()


     
