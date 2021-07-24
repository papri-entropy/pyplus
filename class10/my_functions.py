#!/usr/bin/env python

from netmiko import ConnectHandler

def ssh_command(device, command):
    with ConnectHandler(**device) as net_connect:
        output = net_connect.send_command(command)
    print("#" * 80)
    print(f"OUTPUT ----------> {device['host']}")
    print("#" * 80)
    print(output)
 

