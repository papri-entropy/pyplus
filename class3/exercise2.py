#!/usr/bin/env python

"""
2a. Create a list where each of the list elements is a dictionary representing one of the network devices in the lab. 
Do this for at least four of the lab devices. 
The dictionary should have keys corresponding to the device_name, host (i.e. FQDN), username, and password. 
Use a fictional username/password to avoid checking the lab password into GitHub.

2b. Write the data structure you created in part 2a out to a YAML file. Use expanded YAML format. How could you re-use this YAML file later when creating Netmiko connections to devices?
"""

from pprint import pprint
import yaml

pynet_dev = [
	{
'device_name': 'arista1',
'host': 'arista1.lasthop.io',
'username': 'test',
'password': 'testsecret'
	},
	{
'device_name': 'arista2',
'host': 'arista2.lasthop.io',
'username': 'test',
'password': 'testsecret'
	},
	{
'device_name': 'arista3',
'host': 'arista3.lasthop.io',
'username': 'test',
'password': 'testsecret'
	},
	{
'device_name': 'arista4',
'host': 'arista4.lasthop.io',
'username': 'test',
'password': 'testsecret'
	},
	{
'device_name': 'nxos1',
'host': 'nxos1.lasthop.io',
'username': 'test',
'password': 'testsecret'
	},
	{
'device_name': 'nxos2',
'host': 'nxos2.lasthop.io',
'username': 'test',
'password': 'testsecret'
	}
]

filename = "python_to_yaml.yaml"

with open(filename, 'w') as f:
    yaml.dump(pynet_dev, f, default_flow_style=False) 


with open(filename) as f:
    yaml_to_python = yaml.load(f)

pprint(yaml_to_python)



