#!/usr/bin/env python

"""
4. Use Netmiko and the send_config_set() method to configure the following on the Cisco3 router.

ip name-server 1.1.1.1
ip name-server 1.0.0.1
ip domain-lookup

Experiment with fast_cli=True to see how long the script takes to execute (with and without this option enabled).

Verify DNS lookups on the router are now working by executing 'ping google.com'. Verify from this that you receive a ping response back.
"""

from pprint import pprint
from netmiko import ConnectHandler
from getpass import getpass
import os
from datetime import datetime

password = os.getenv("PYPLUS_PASS") if os.getenv("PYPLUS_PASS") else getpass()

cisco3 = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_ios",
    "session_log": "session_log"
}

net_connect = ConnectHandler(**cisco3)

config_cmds = [
                "ip name-server 1.1.1.1",
                "ip name-server 1.0.0.1",
                "ip domain-lookup"
            ]

start_time_no_fastcli = datetime.now()

config_push = net_connect.send_config_set(config_cmds)

ping_output = net_connect.send_command("ping google.com")

end_time_no_fastcli = datetime.now()

print("*" * 80)
print(config_push)
print("*" * 80)

print("*" * 80)
print(ping_output)
print("*" * 80)

if "!!!!!" in ping_output:
    print("PING was 100% success")
else:
    print("PING experienced packet loss")

print(f"Total execution time fast_cli disabled: { end_time_no_fastcli - start_time_no_fastcli }")

cisco3 = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_ios",
    "session_log": "session_log",
    "fast_cli": True
}

net_connect = ConnectHandler(**cisco3)

start_time_fastcli = datetime.now()

config_push = net_connect.send_config_set(config_cmds)

ping_output = net_connect.send_command("ping google.com")

end_time_fastcli = datetime.now()

print("*" * 80)
print(config_push)
print("*" * 80)

print("*" * 80)
print(ping_output)
print("*" * 80)

if "!!!!!" in ping_output:
    print("PING was 100% success")
else:
    print("PING experienced packet loss")

print(f"Total execution time fast_cli enabled: { end_time_fastcli - start_time_fastcli }")

