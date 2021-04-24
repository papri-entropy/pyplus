#!/usr/bin/env python

"""
 1. Use the extended 'ping' command and Netmiko on the 'cisco4' router. This should prompt you for additional information as follows:

cisco4#ping
Protocol [ip]: 
Target IP address: 8.8.8.8
Repeat count [5]: 
Datagram size [100]: 
Timeout in seconds [2]: 
Extended commands [n]: 
Sweep range of sizes [n]: 
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 8.8.8.8, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/4 ms

a. Use send_command_timing() to handle the additional prompting from this 'ping' command. Specify a target IP address of '8.8.8.8'

b. Use send_command() and the expect_string argument to handle the additional prompting. Once again specify a target IP address of '8.8.8.8'.
"""

from pprint import pprint
from netmiko import ConnectHandler
from getpass import getpass
import os

password = os.getenv("PYPLUS_PASS") if os.getenv("PYPLUS_PASS") else getpass()

cisco4 = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_ios",
    "session_log": "session_log"
}

net_connect = ConnectHandler(**cisco4)

print("*" * 80)
print("PING using send_command_timing: ")
print("*" * 80)

output = net_connect.send_command_timing("ping",
    strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("\n",
    strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("8.8.8.8",
    strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("10",
    strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("\n",
    strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("\n",
    strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("\n",
    strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing("\n",
    strip_prompt=False, strip_command=False)

print(output)


print("*" * 80)
print("PING using send_command: ")
print("*" * 80)

output = net_connect.send_command("ping", expect_string=r"Protocol",
    strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r"Target IP address",
    strip_prompt=False, strip_command=False)
output += net_connect.send_command("8.8.8.8", expect_string=r"Repeat count",
    strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r"Datagram size",
    strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r"Timeout in seconds",
    strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r"Extended commands",
    strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r"Sweep range of sizes",
    strip_prompt=False, strip_command=False)
output += net_connect.send_command("\n", expect_string=r"#",
    strip_prompt=False, strip_command=False)

print(output)

net_connect.disconnect()
