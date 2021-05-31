#!/usr/bin/env python

"""
2a. Define an Arista device in an external YAML file (use arista4.lasthop.io for the device). 
In your YAML file, make sure the key names exactly match the names required for use with pyeapi and the connect() method. 
In other words, you should be able to execute 'connect(**device_dict)' where device_dict was retrieved from your YAML file. 
Do not store the lab password in this YAML file, instead set the password using getpass() in your Python program. 
Using this Arista device information stored in a YAML file, repeat the 'show ip arp' retrieval using pyeapi. 
Once again, from this ARP table data, print out a mapping of all of the IP addresses and their corresponding MAC addresses.
"""

import pyeapi
import json
import yaml
from pprint import pprint
from getpass import getpass

password = getpass()

with open("inventory.yaml") as f:
    data = yaml.load(f)

for k in data:
    data[k]["password"] = password

for k in data:
    if k == "arista4":
        connection = pyeapi.client.connect(**data[k])

device = pyeapi.client.Node(connection)

output = device.enable("show ip arp")

arp_dict = dict()

for arp_entry in output[0]["result"]["ipV4Neighbors"]:
    ip = arp_entry["address"]
    mac = arp_entry["hwAddress"]
    arp_dict[ip] = mac
    print(f"{ip:^15} {'--->':^15} {mac:^15}")

print(json.dumps(arp_dict, indent=4))
