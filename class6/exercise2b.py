#!/usr/bin/env python

"""
2b. Create a Python module named 'my_funcs.py'. In this file create two functions: 
function1 should read the YAML file you created in exercise 2a and return the corresponding data structure; 
function2 should handle the output printing of the ARP entries 
(in other words, create a separate function that handles all printing to standard out of the 'show ip arp' data). 
Create a new Python program based on exercise2a except the YAML file loading 
and the output printing is accomplished using the functions defined in my_funcs.py.
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

output = device.enable("show ip arp")

print(json.dumps(arp_output(output), indent=4))


