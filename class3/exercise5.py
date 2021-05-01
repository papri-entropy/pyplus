#!/usr/bin/env python

"""
5. In your lab environment, there is a file located at ~/.netmiko.yml. 
This file contains all of the devices used in the lab. 
Create a Python program that processes this YAML file and then uses Netmiko to connect to the Cisco3 router. 
Print out the router prompt from this device.

Note, the device dictionaries in the .netmiko.yml file use key-value pairs designed to work directly with Netmiko. 
The .netmiko.yml also contains group definitions for: cisco, arista, juniper, and nxos groups. 
These group definitions are lists of devices. Once again, don't check the .netmiko.yml into GitHub.
"""

import os
import yaml
from netmiko import ConnectHandler
from pprint import pprint

file_dir = os.environ['HOME']
file_name = ".netmiko.yml"
filename = file_dir + "/" + file_name

"""
alternatively:

home_dir = os.path.expanduser("~")
filename = os.path.join(home_dir, ".netmiko.yml")

print(home_dir)
print(filename)
"""

with open(filename) as f:
    data = yaml.load(f)

#pprint(data)

cisco3 = data['cisco3']

print(cisco3)

net_connect = ConnectHandler(**cisco3)

output = net_connect.find_prompt()

print(output)
