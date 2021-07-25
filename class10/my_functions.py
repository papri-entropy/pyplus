#!/usr/bin/env python

from netmiko import ConnectHandler

def ssh_command(device, command):
    with ConnectHandler(**device) as net_connect:
        output = net_connect.send_command(command)
    print("#" * 80)
    print(f"OUTPUT ----------> {device['host']}")
    print("#" * 80)
    print(output)
 

def ssh_command2(device, command):
    with ConnectHandler(**device) as net_connect:
        output = net_connect.send_command(command)

    return output
 
def ssh_command3(device):
    with ConnectHandler(**device) as net_connect:
        if device['host'] == "srx2.lasthop.io":
            output = net_connect.send_command("show arp")
        else:
            output = net_connect.send_command("show ip arp")

    return output
