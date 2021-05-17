#!/usr/bin/env python

"""
4. Expand on exercise3 except use a for-loop to configure five VRFs. 
Each VRF should have a unique name and a unique route distinguisher. 
Each VRF should once again have the IPv4 and the IPv6 address families 
controlled by a conditional-variable passed into the template.

Note, you will want to pass in a list or dictionary of VRFs that you loop over in your Jinja2 template.
"""

from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from pprint import pprint

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('./templates')

vrfs = {"vrfs": [
	{"name": "blue",
        "rd": "100:1",
        "ipv4_enabled": True,
        "ipv6_enabled": True},
	{"name": "green",
        "rd": "100:2",
        "ipv4_enabled": True,
        "ipv6_enabled": True},
	{"name": "red",
        "rd": "100:3",
        "ipv4_enabled": True,
        "ipv6_enabled": True},
	{"name": "yellow",
        "rd": "100:4",
        "ipv4_enabled": True,
        "ipv6_enabled": True},
	{"name": "black",
        "rd": "100:5",
        "ipv4_enabled": True,
        "ipv6_enabled": True}]}

template_file = 'vrf.j2'
template = env.get_template(template_file)
output = template.render(**vrfs)

print(output)

