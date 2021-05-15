#!/usr/bin/env python

"""
2b. Expand your Jinja2 template such that both the following interface and BGP configurations are generated for nxos1 and nxos2. 
The interface name, IP address, netmask, local_as, and peer_ip should all be variables in the template. 
This is iBGP so the remote_as will be the same as the local_as.

nxos1

interface Ethernet1/1
  ip address 10.1.100.1/24

router bgp 22
  neighbor 10.1.100.2 remote-as 22
    address-family ipv4 unicast


nxos2

interface Ethernet1/1
  ip address 10.1.100.2/24

router bgp 22
  neighbor 10.1.100.1 remote-as 22
    address-family ipv4 unicast
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
        "NETMASK": 24,
        "LOCAL_AS": 22,
        "PEER_IP": "10.1.100.2"
            }
        ,
        "nxos2": {
        "INTF": "Ethernet1/1",
        "IP_ADDRESS": "10.1.100.2",
        "NETMASK": 24,
        "LOCAL_AS": 22,
        "PEER_IP": "10.1.100.1"
            }
        }
    }
    
template_file = 'nxos_intf_bgp.j2'
template = env.get_template(template_file)
output = template.render(**devices)


print(output)
