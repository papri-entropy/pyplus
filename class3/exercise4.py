#!/usr/bin/env python

"""
4. You have the following JSON ARP data from an Arista switch:

{
    "dynamicEntries": 2,
    "ipV4Neighbors": [
        {
            "hwAddress": "dc38.e111.97cf",
            "address": "172.17.17.1",
            "interface": "Ethernet45",
            "age": 0
        },
        {
            "hwAddress": "90e2.ba5c.25fd",
            "address": "172.17.16.1",
            "interface": "Ethernet36",
            "age": 0
        }
    ],
    "notLearnedEntries": 0,
    "totalEntries": 2,
    "staticEntries": 0
}


From a file, read this JSON data into your Python program. 
Process this ARP data and return a dictionary where the 
dictionary keys are the IP addresses and the dictionary values are the MAC addresses. 
Print this dictionary to standard output.
"""

import json
from pprint import pprint

with open("arista_arp.json") as f:
    data = json.load(f)

print(json.dumps(data, indent=4))

arp_dict = dict()

for k, v in data.items():
    if k == "ipV4Neighbors":
        for entry in v:
            address = entry["address"]
            mac = entry["hwAddress"]
            arp_dict[address] = mac
            #arp_dict[entry["address"]] = entry["hwAddress"]

print("New ARP dictionary: ")
print(json.dumps(arp_dict, indent=4))
