#!/usr/bin/env python

"""
7c. Using the nxapi_plumbing config_list() method, 
configure two loopbacks on nxos1 including interface descriptions. 
Pick random loopback interface numbers between 100 and 199.
"""

import requests
import os
import random
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

first_loopback = str(random.randint(100,199))
second_loopback = str(random.randint(100,199))

cfg_cmds = [
    f"interface loopback {first_loopback}",
    f"description LOOPBACK {first_loopback}",
    f"interface loopback {second_loopback}",
    f"description LOOPBACK {second_loopback}"
    ]

#print(cfg_cmds)

output = device.config_list(cfg_cmds)

for cfg_cmd in output:
    print(etree.tostring(cfg_cmd).decode())
    input("Hit enter to see the next output: ")



