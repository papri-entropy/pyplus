#!/usr/bin/env python

"""
4. Note, this exercise might be fairly challenging. 
Construct a new YAML file that contains the four Arista switches. 
This YAML file should contain all of the connection information 
need to create a pyeapi connection using the connect method. 
Using this inventory information and pyeapi, 
create a Python script that configures the following on the four Arista switches: 

interface {{ intf_name }}
   ip address {{ intf_ip }}/{{ intf_mask }}

The {{ intf_name }} should be a Loopback interface between 1 and 99 (for example Loopback99).

The {{ intf_ip }} should be an address from the 172.31.X.X address space. The {{ intf_mask }} should be either a /24 or a /30.

Each Arista switch should have a unique loopback number, and a unique interface IP address.

You should use Jinja2 templating to generate the configuration for each Arista switch.

The data for {{ intf_name }} and for {{ intf_ip }} should be stored in your YAML file 
and should be associated with each individual Arista device. 
For example, here is what 'arista4' might look like in the YAML file:

arista4:
  transport: https
  host: arista4.lasthop.io
  username: pyclass
  port: 443
  data:
    intf_name: Loopback99
    intf_ip: 172.31.1.13
    intf_mask: 30

Use pyeapi to push this configuration to the four Arista switches. 
Use pyeapi and "show ip interface brief" to display the IP address table after the configuration changes have been made.
"""

from pprint import pprint
from my_funcs import read_yaml, arp_output
import pyeapi
import json
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from pprint import pprint

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('.')


data = read_yaml("arista_hosts.yaml")

for k in data:
    intf_vars = dict()
    intf_vars["intf_name"] = data[k]["data"]["intf_name"]
    intf_vars["intf_ip"] = data[k]["data"]["intf_ip"]
    intf_vars["intf_mask"] = data[k]["data"]["intf_mask"]

    template_file = "arista_intf.j2"
    template = env.get_template(template_file)
    intf_config = template.render(**intf_vars) 
    intf_config = intf_config.splitlines()
    pprint(intf_config)

    connection = pyeapi.client.connect(**data[k])
    device = pyeapi.client.Node(connection)
    config_output = device.config(intf_config)
    print(config_output)

    intf_output = device.enable("show ip interface brief")
    pprint(intf_output[0]["result"]["output"])


