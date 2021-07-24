#!/usr/bin/env python

"""
1a. As you have done in previous classes, 
create a Python file named "my_devices.py". 
In this file, define the connection information for: 
'cisco3', 'arista1', 'arista2', and 'srx2'. 
This file should contain all the necessary information 
to create a Netmiko connection. Use getpass() for the password handling. 
Use a global_delay_factor of 4 for both the arista1 device and the arista2 device. 
This Python module should be used to store 
the connection information for all of the exercises in this lesson.

1b. Create a Python script that executes "show version" 
on each of the network devices defined in my_devices.py. 
This script should execute serially i.e. one SSH connection after the other. 
Record the total execution time for the script. 
Print the "show version" output and the total execution time to standard output. 
As part of this exercise, you should create a function 
that both establishes a Netmiko connection and that executes a single show command 
that you pass in as argument. 
This function's arguments should be the Netmiko device dictionary 
and the "show-command" argument. 
The function should return the result from the show command.
"""

from netmiko import ConnectHandler
from my_devices import devices
from datetime import datetime
import time


def netmiko_show_ver(device, command):
    with ConnectHandler(**device) as net_connect:
        output = net_connect.send_command(command)
    return output


show_command = "show version"


if __name__=="__main__":

    start_time = datetime.now()
    t0 = time.time()

    for device in devices:
        result = netmiko_show_ver(device, show_command)
        print("#" * 80)
        print(f"OUTPUT ----------> {device['host']}")
        print("#" * 80)
        print(result)

    end_time = datetime.now()
    t1 = time.time()

    print("#" * 80)
    print("SCRIPT FINISHED EXECUTION")
    print("#" * 80)
    print(f"Execution time: {end_time - start_time}")
    print(f"Execution time: {t1 - t0:.2f}")
    print("#" * 80)
