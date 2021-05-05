#!/usr/bin/env python

"""
6. Use Netmiko to retrieve 'show run' from the Cisco4 device. 
Feed this configuration into CiscoConfParse.

Use CiscoConfParse to find all of the interfaces on Cisco4 that have an IP address. 
Print out the interface name and IP address for each interface. 
Your solution should work if there is more than one IP address configured on Cisco4. 
For example, if you configure a loopback interface on Cisco4 with an IP address, 
then your solution should continue to work. 
The output from this program should look similar to the following:

$ python confparse_ex6.py 

Interface Line: interface GigabitEthernet0/0/0
IP Address Line:  ip address 10.220.88.23 255.255.255.0
"""

from pprint import pprint
import os
import re
from getpass import getpass
from netmiko import ConnectHandler
from ciscoconfparse import CiscoConfParse

password = os.environ["PYPLUS_PASS"] if os.environ["PYPLUS_PASS"] else getpass()

cisco4 = {
    'host': 'cisco4.lasthop.io',
    'username': 'pyclass',
    'password': password,
    'device_type': 'cisco_ios'
}

net_connect = ConnectHandler(**cisco4)

sh_run = net_connect.send_command("show running-config")

with open("cisco4_sh_run.txt", "w") as f:
    f.write(sh_run)

sh_run_parsed = CiscoConfParse("cisco4_sh_run.txt")

match = intfs_with_ip = sh_run_parsed.find_objects_w_child(parentspec=r"^interface", childspec=r"^\s+ip address")

#print(match)

for line in match:
    intf = line.parent.text
    print(f"Interface Line: {intf}")
    #ip = line.parent.re_search_children(r"ip address")[0]
    ip_addr = line.children[0].text
    print(f"IP Address Line: {ip_addr}")
    print('#' * 80)



