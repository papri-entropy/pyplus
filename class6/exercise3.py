#!/usr/bin/env python

"""
3. Using your external YAML file and your function located in my_funcs.py, 
use pyeapi to connect to arista4.lasthop.io and retrieve "show ip route". 
From this routing table data, extract all of the static and connected routes from the default VRF. 
Print these routes to the screen and indicate whether the route is a connected route or a static route. 
In the case of a static route, print the next hop address.
"""

from pprint import pprint
from my_funcs import read_yaml, arp_output
import pyeapi
import json
from pprint import pprint

data = read_yaml("inventory.yaml")

for k in data:
    if k == "arista4":
        connection = pyeapi.client.connect(**data[k])

device = pyeapi.client.Node(connection)

output = device.enable("show ip route")

default_rib = output[0]["result"]["vrfs"]["default"]["routes"]

for route in default_rib:
    if default_rib[route]["routeType"] == "static":
        next_hop = default_rib[route]["vias"][0]["nexthopAddr"]
        print(f"{route} via Next Hop: {next_hop} ======> static route")
    if default_rib[route]["routeType"] == "connected":
        print(f"{route} ======> directly connected")
    

