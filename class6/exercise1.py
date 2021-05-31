#!/usr/bin/env python

"""
1. Using the pyeapi library, connect to arista3.lasthop.io and execute 'show ip arp'. 
From this ARP table data, print out a mapping of all of the IP addresses 
and their corresponding MAC addresses.
"""

import pyeapi
import json
from pprint import pprint
from getpass import getpass

connection = pyeapi.client.connect(
    transport="https",
    host="arista3.lasthop.io",
    username="pyclass",
    password=getpass(),
    port="443",
    )

arista3 = pyeapi.client.Node(connection)
output = arista3.enable("show ip arp")

arp_dict = dict()

for arp_entry in output[0]["result"]["ipV4Neighbors"]:
    ip = arp_entry["address"]
    mac = arp_entry["hwAddress"]
    arp_dict[ip] = mac
    print(f"{ip:^15} {'--->':^15} {mac:^15}")

print(json.dumps(arp_dict, indent=4))
