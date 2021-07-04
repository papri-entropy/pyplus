#!/usr/bin/env python

"""
7a. Create an nxapi_plumbing "Device" object for nxos1. 
The api_format should be "xml" and the transport should be "https" (port 8443). 
Use getpass() to capture the device's password. 
Send the "show interface Ethernet1/1" command to the device, 
parse the output, and print out the following information:

Interface: Ethernet1/1; State: up; MTU: 1500
"""

import requests
import os
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from lxml import etree
from pprint import pprint
from getpass import getpass
from nxapi_plumbing import Device

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

password = os.getenv("PYPLUS_PASS") if os.getenv("PYPLUS_PASS") else getpass()

nxos1 = {
    "api_format": "xml",
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": password,
    "transport": "https",
    "port": 8443,
    "verify": False
    }

device = Device(**nxos1)

output = device.show("show interface Ethernet1/1")
output = etree.tostring(output).decode()
print(output)

xml_data = etree.fromstring(output)

interface = xml_data.find(".//interface").text
state = xml_data.find(".//state").text
mtu = xml_data.find(".//eth_mtu").text

print()
print(f"Interface: {interface}; State: {state}; MTU: {mtu}")
print()

"""
Alternatively, you can use 'find' directly on returned output xml
but nice to visualize it first, using 'tostring'

output = device.show("show interface Ethernet1/1")

interface = output.find(".//interface").text
state = output.find(".//state").text
mtu = output.find(".//eth_mtu").text
"""
