#!/usr/bin/env python

"""
1. Create a Python program that uses Jinja2 to generate the below BGP configuration. 
Your template should be directly embedded inside of your program as a string and 
should use for the following variables: local_as, peer1_ip, peer1_as, peer2_ip, peer2_as.

router bgp 10
  neighbor 10.1.20.2 remote-as 20
    update-source loopback99
    ebgp-multihop 2
    address-family ipv4 unicast
  neighbor 10.1.30.2 remote-as 30
    address-family ipv4 unicast
"""

from jinja2 import Template
from pprint import pprint

bgp_template = """
router bgp {{ local_as }}
  neighbor {{ peer1_ip }} remote-as {{ peer1_as }}
    update-source loopback99
    ebgp-multihop 2
    address-family ipv4 unicast
  neighbor {{ peer2_ip }} remote-as {{ peer2_as }}
    address-family ipv4 unicast
"""

bgp_vars = {
    "local_as": 10,
    "peer1_ip": "10.1.20.1",
    "peer1_as": 20,
    "peer2_ip": "10.1.30.2",
    "peer2_as": 30
}

template = Template(bgp_template)
bgp_config = template.render(**bgp_vars)

print(bgp_config)
