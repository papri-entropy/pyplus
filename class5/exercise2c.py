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

from netmiko import ConnectHandler
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from vars import my_devices
import time

nxos1_config = my_devices.devices["nxos_devices"]["nxos1"]["config"]
nxos2_config = my_devices.devices["nxos_devices"]["nxos2"]["config"]

nxos1_conn = my_devices.devices["nxos_devices"]["nxos1"]["connection"]
nxos2_conn = my_devices.devices["nxos_devices"]["nxos2"]["connection"]

nxos1 = {"config": nxos1_config, "conn": nxos1_conn}
nxos2 = {"config": nxos2_config, "conn": nxos2_conn}

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('./templates')
    
template_file = 'nxos_netmiko.j2'

def nxos_config():
    for device in (nxos1, nxos2):
        template = env.get_template(template_file)
        config_output = template.render(**device["config"])
        config = config_output.splitlines()
        print(config_output)
        net_connect = ConnectHandler(**device["conn"])
        print(net_connect.find_prompt())
        net_connect.send_config_set(config)


def ping_check():
    for device in (nxos1, nxos2):
        net_connect = ConnectHandler(**device["conn"])
        print(net_connect.find_prompt())
        intf = device["config"]["INTF"]
        arp_output = net_connect.send_command(f"show ip arp { intf }", use_textfsm=True)
        neigh_addr = arp_output[0]['address']
        ping_output = net_connect.send_command(f"ping { neigh_addr }")
        print(ping_output)
        if "5 packets transmitted, 5 packets received, 0.00% packet loss" in ping_output:
    	    print("PING was 100% success")
        else:
    	    print("PING failed or experienced packet loss") 

def bgp_check():
    for device in (nxos1, nxos2):
        net_connect = ConnectHandler(**device["conn"])
        print(net_connect.find_prompt())
        bgp_neigh = device["config"]["PEER_IP"]
        show_bgp_output = net_connect.send_command(f"show ip bgp neighbors { bgp_neigh }", use_textfsm=True)
        bgp_state = show_bgp_output[0]['bgp_state']
        if bgp_state == 'Established':
    	    print("BGP Established")
        else:
    	    print("BGP NOT Established, please t-shoot") 

nxos_config()
time.sleep(15)
ping_check()
bgp_check()



