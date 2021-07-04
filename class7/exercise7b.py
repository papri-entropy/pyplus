#!/usr/bin/env python

"""
7b. Run the following two show commands on the nxos1 device 
using a single method and passing in a list of commands: 
"show system uptime" and "show system resources". 
Print the XML output from these two commands.
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

cmds = [
    "show system uptime",
    "show system resources"
    ]
output = device.show_list(cmds)

for show_cmd in output:
    print(etree.tostring(show_cmd).decode()) 
    input("Hit enter to see the next output: ")


