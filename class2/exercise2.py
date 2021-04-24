#!/usr/bin/env python

"""
2. Create a Netmiko connection to the 'nxos2' device using a global_delay_factor of 2. 
Execute 'show lldp neighbors detail' and print the returned output to standard output. 
Execute 'show lldp neighbors detail' a second time using send_command() with a delay_factor of 8. 
Print the output of this command to standard output. 
Use the Python datetime library to record the execution time of both of these commands. 
Print these execution times to standard output.
"""

from pprint import pprint
from netmiko import ConnectHandler
from getpass import getpass
import os
import datetime

password = os.getenv("PYPLUS_PASS") if os.getenv("PYPLUS_PASS") else getpass()

nxos2 = {
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_nxos",
    "global_delay_factor": 2,
    "session_log": "session_log"
}

net_connect = ConnectHandler(**nxos2)

command = "show lldp neighbors detail"

start_time_global_delay_factor_2 = datetime.datetime.now()
output = net_connect.send_command(command)
end_time_global_delay_factor_2 = datetime.datetime.now()
print(output)

start_time_delay_factor_8 = datetime.datetime.now()
output = net_connect.send_command(command, delay_factor=8)
end_time_delay_factor_8 = datetime.datetime.now()
print(output)

print("*" * 80)
print(f"Script start time: { start_time_global_delay_factor_2 }")
print(f"Script end time: { end_time_global_delay_factor_2 }")
print(f"Script execution time based on GLOBA_DELAY_FACTOR of 2: { end_time_global_delay_factor_2 - start_time_global_delay_factor_2 }")
print("*" * 80)
print(f"Script start time: { start_time_delay_factor_8 }")
print(f"Script end time: { end_time_delay_factor_8 }")
print(f"Script execution time based on command DELAY_FACTOR of 8: { end_time_delay_factor_8 - start_time_delay_factor_8 }")
print("*" * 80)
