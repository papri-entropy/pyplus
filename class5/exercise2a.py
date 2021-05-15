#!/usr/bin/env python

"""
2a. Use Python and Jinja2 to generate the below NX-OS interface configuration. 
You should use an external template file and a Jinja2 environment to accomplish this. 
The interface, ip_address, and netmask should all be variables in the Jinja2 template.
 

nxos1
interface Ethernet1/1
  ip address 10.1.100.1/24

nxos2
interface Ethernet1/1
  ip address 10.1.100.2/24
"""

from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('./templates')

devices = {
        "nxos_devices": {
        "nxos1": {
        "INTF": "Ethernet1/1",
        "IP_ADDRESS": "10.1.100.1",
        "NETMASK": 24
            }
        ,
        "nxos2": {
        "INTF": "Ethernet1/1",
        "IP_ADDRESS": "10.1.100.2",
        "NETMASK": 24
            }
        }
    }
    
template_file = 'nxos_intf.j2'
template = env.get_template(template_file)
output = template.render(**devices)

print(output)
